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
            'is_imax': int(is_imax) if str(is_imax) else None,
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
                if float(movie['movie_score']) < val:
                    return False

        return True

    result = []

    for movie in movies:
        if not __apply_filters(movie):
            continue

        result.append({
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
            'picture': movie['movie_big_picture'],
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

    results = SoyaToolkit().query('movie', **kwargs).\
        jsonify()['result']['movie']

    return __reconstruct_movie_info(is_new, is_imax, movie_score, *results)
