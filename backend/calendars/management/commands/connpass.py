from django.core.management.base import BaseCommand
from calendars.models import Event
import datetime
import requests
import math
from time import sleep

class Command(BaseCommand):
  COUNT = 100
  URL = 'https://connpass.com/api/v1/event/'

  def handle(self, *args, **options):
    params = {'keyword': '人工知能', 'count': 1}
    response = requests.get(self.URL, params=params).json()
    print("検索件数:%s" % response['results_available'])
    events_count = response['results_available']

    params['count'] = self.COUNT
    for start_index in range(1, math.ceil(events_count/self.COUNT)+1):
      sleep(5)
      params['start'] = start_index
      response = requests.get(self.URL, params=params).json()
      for event in response['events']:
        id = event['event_id']
        title = event['title']
        address = event['address']
        place = event['place']
        description = event['description']
        event_url = event['event_url']
        started_at = event['started_at']
        ended_at = event['ended_at']
        limit = event['limit']
        accepted = event['accepted']
        waiting = event['waiting']
        lat = event['lat']
        lon = event['lon']

        started_at = datetime.datetime.strptime(started_at, "%Y-%m-%dT%H:%M:%S%z") if ":" != started_at[-3:-2] else started_at[:-3] + started_at[-2:]
        ended_at = datetime.datetime.strptime(ended_at, "%Y-%m-%dT%H:%M:%S%z") if ":" != ended_at[-3:-2] else ended_at[:-3] + ended_at[-2:]

        Event(id,title, address, place, description, event_url, started_at, ended_at, limit, accepted, waiting, lat, lon).save()

    print("FINISH")
