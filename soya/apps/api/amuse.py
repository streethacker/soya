# -*- coding: utf-8 -*-

import logging

from soya.core.core import (
    SoyaToolkit,
)

from soya.apps.api import (
    bp,
    render_json,
)

from soya.utils.validate import (
    validator,
    FloatField,
    IntField,
    StringField,
)


logger = logging.getLogger(__name__)


def __reconstruct_movie_info(is_new, is_imax, movie_score, *movies):

    def __apply_filters(movie):
        filters = {
            'is_new': int(is_new) if is_new else None,
            'is_imax': int(is_imax) if is_imax is not None else None,
            'movie_score': float(movie_score) if movie_score else None,
        }

        for key, val in filters.iteritems():
            if val is None:
                continue

            if key == 'is_new':
                if int(movie['is_new']) != val:
                    return False
            if key == 'is_imax':
                if int(movie['is_imax']) != val:
                    return False
            if key == 'movie_score':
                if not movie['movie_score']:
                    continue
                if float(movie['movie_score']) < val:
                    return False

        return True

    result = []

    for movie in movies:
        if not __apply_filters(movie):
            continue

        movie_info = {
            'name': movie['movie_name'],
            'type': movie['movie_type'],
            'release_date': movie['movie_release_date'],
            'nation': movie['movie_nation'],
            'starring': movie['movie_starring'],
            'length': movie['movie_length'],
            'score': movie['movie_score'],
            'director': movie['movie_director'],
            'tags': movie['movie_tags'],
            'message': movie['movie_message'],
        }

        picture = movie.get('movie_big_picture') or movie.get('movie_picture')
        time_table = movie.get('time_table')

        movie_info.update({
            'picture': picture,
            'time_table': time_table,
        })

        result.append(movie_info)

    return result


def __reconstruct_cinema_info(movie_score, *cinemas):

    result = []

    for cinema in cinemas:
        movies = __reconstruct_movie_info(
            None,
            None,
            movie_score,
            *cinema['movies']
        )

        result.append({
            'name': cinema['name'],
            'telephone': cinema['telephone'],
            'location': cinema['location'],
            'address': cinema['address'],
            'rating': cinema['rating'],
            'movies': movies,
        })

    return result


def __reconstruct_movie_on_cinema_info(rating, *movie_on_cinemas):

    result = []

    for movie in movie_on_cinemas:
        if rating is not None and movie['rating'] < rating:
            continue

        result.append({
            'name': movie['name'],
            'telephone': movie['telephone'],
            'location': movie['location'],
            'address': movie['address'],
            'rating': float(movie['rating']),
            'time_table': movie['time_table'],
        })

    return result


@bp.route('/movie/hot')
@render_json
@validator({
    'location': StringField,
    'is_new': IntField,
    'is_imax': IntField,
    'movie_score': FloatField,
})
def get_hot_movie(location, is_new=None, is_imax=None, movie_score=None):
    kwargs = {'location': location, 'qt': 'hot_movie'}

    results = SoyaToolkit().query('movie', **kwargs).result

    return __reconstruct_movie_info(
        is_new,
        is_imax,
        movie_score,
        *results.get('movie')
    )


@bp.route('/search/cinema')
@render_json
@validator({
    'location': StringField,
    'cinema_name': StringField,
    'movie_score': FloatField,
})
def search_cinema(location, cinema_name, movie_score=None):

    kwargs = {
        'location': location,
        'wd': cinema_name,
        'qt': 'search_cinema',
    }

    results = SoyaToolkit().query('movie', **kwargs).result

    return __reconstruct_cinema_info(movie_score, *results)


@bp.route('/search/movie')
@render_json
@validator({
    'location': StringField,
    'movie_name': StringField,
    'rating': FloatField,
    'page_number': IntField,
})
def search_movie(location, movie_name, rating=None, page_number=1):

    kwargs = {
        'location': location,
        'wd': movie_name,
        'pn': page_number,
        'qt': 'search_movie',
    }

    results = SoyaToolkit().query('movie', **kwargs).result

    return __reconstruct_movie_on_cinema_info(rating, *results)
