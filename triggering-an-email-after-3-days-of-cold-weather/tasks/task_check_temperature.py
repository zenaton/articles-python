import http
import json

from zenaton.abstracts.task import Task
from zenaton.traits.zenatonable import Zenatonable

from exceptions import AddressNotFound, NotAuthorized, TemperatureNotFound, UnhandledStatusCode


class TaskCheckTemperature(Task, Zenatonable):

    def __init__(self, city):
        self.city = city

    def handle(self):
        OPEN_WEATHER_MAP_API_KEY = '<Enter your Open Weather Map API key here>'

        host = 'api.openweathermap.org'
        path = '/data/2.5/weather?q={}&units=imperial&APPID={}'.format(str(self.city), OPEN_WEATHER_MAP_API_KEY)
        conn = http.client.HTTPConnection(host)
        conn.request('GET', path)
        r = conn.getresponse()
        content = json.loads(r.read().decode('utf-8'))
        conn.close()

        if r.status == 200:
            try:
                temperature = content['main']['temp']
                print('Current temperature in {}: {}°F'.format(self.city, str(temperature)))
                return temperature
            except KeyError:
                raise TemperatureNotFound
        if r.status == 401:
            raise NotAuthorized
        if r.status in [400, 404]:
            raise AddressNotFound
        raise UnhandledStatusCode
