# -*- coding: utf-8 -*-

import datetime
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
    BoolField,
    DateField,
    StringField,
)


logger = logging.getLogger(__name__)

# FIXME
# Traffic Event Type

TRAFFIC_CONTROL = 0
TRAFFIC_ACCIDENT = 1
ROAD_CONSTRUCTION = 2
TRAFFIC_CONTROL_UNKNOWN = 3


def __reconstruct_weather_info(*weathers):

    result = []

    begin = datetime.datetime.today()

    for index, weather in enumerate(weathers):
        current_date = begin + datetime.timedelta(days=index)

        result.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'name': weather['weather'],
            'temperature': weather['temperature'],
            'wind': weather['wind'],
            'pm25': None,
        })

    return result


def __reconstruct_traffic_event(start_time, end_time, *events):

    EVENT_TYPE_MAP = {
        TRAFFIC_CONTROL: u'交通管制',
        TRAFFIC_ACCIDENT: u'交通事故',
        ROAD_CONSTRUCTION: u'道路施工',
        TRAFFIC_CONTROL_UNKNOWN: u'暂不清楚',
    }

    result = []

    for event in events:
        event_type = EVENT_TYPE_MAP.get(int(event['type']))

        from_time = datetime.datetime.strptime(
            event['startTime'],
            '%Y/%m/%d/%H/%M/%S'
        )
        to_time = datetime.datetime.strptime(
            event['endTime'],
            '%Y/%m/%d/%H/%M/%S'
        )

        if from_time >= start_time and to_time <= end_time:
            result.append({
                'startTime': from_time.strftime('%Y-%m-%d %H:%M:%S'),
                'endTime': to_time.strftime('%Y-%m-%d %H:%M:%S'),
                'title': event['title'],
                'description': event['description'],
                'location': event['location'],
                'type': event_type,
            })

    return result


@bp.route('/weather')
@render_json
@validator({
    'location': StringField,
    'current_only': BoolField,
    'origin': BoolField,
})
def get_weather(location, current_only=True, origin=False):
    kwargs = {'location': location}
    results = SoyaToolkit().query('weather', **kwargs).\
        jsonify()['results'][0]

    if origin:
        return results

    if current_only:
        weather = __reconstruct_weather_info(results['weather_data'][0])[0]
        weather['pm25'] = results.get('pm25')

        return {
            'city': results['currentCity'],
            'weather_info': weather,
        }

    weathers = __reconstruct_weather_info(*results['weather_data'])
    weathers[0]['pm25'] = results.get('pm25')
    return {
        'city': results['currentCity'],
        'weather_info': weathers,
    }


@bp.route('/traffic')
@render_json
@validator({
    'location': StringField,
    'start_time': DateField,
    'end_time': DateField,
})
def get_traffic(location, start_time=None, end_time=None):
    kwargs = {'location': location}
    results = SoyaToolkit().query('trafficEvent', **kwargs).\
        jsonify()['results']

    results = __reconstruct_traffic_event(start_time, end_time, *results)

    return results
