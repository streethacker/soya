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
    StringField,
    FloatField,
)


logger = logging.getLogger(__name__)


def __reconstruct_address_info(*addresses):

    result = []

    for address in addresses:
        result.append({
            'distance': address['distance'],
            'telephone': address['telephone'],
            'name': address['name'],
            'address': address['address'],
            'type': address['type'],
            'location': address['location'],
        })

    return result


@bp.route('/geocoding')
@render_json
@validator({
    'keyword': StringField,
    'cityname': StringField,
})
def geocoding(keyword, cityname):
    kwargs = {
        'keyWord': keyword,
        'cityName': cityname,
    }

    return SoyaToolkit().query('geocoding', **kwargs).result


@bp.route('/geocoding/reverse')
@render_json
@validator({
    'longitude': FloatField,
    'latitude': FloatField,
})
def reverse_geocoding(longitude, latitude):

    kwargs = {
        'location': ','.join([str(longitude), str(latitude)]),
    }

    results = SoyaToolkit().query('reverseGeocoding', **kwargs).result

    return __reconstruct_address_info(*results)
