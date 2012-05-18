import os
import json
import time
import urllib
import urllib2
import calendar
import random
from datetime import datetime, timedelta

API_KEY = open('%s/etc/meetup.key' % os.environ['HOME']).read().strip()
base = 'https://api.meetup.com/'

def main():
    m = Meetup(API_KEY)
    # Find the event
    # after=datetime_to_timestamp(datetime(2012, 5, 10))
    # before=datetime_to_timestamp(datetime(2012, 5, 11))
    after=datetime_to_timestamp(datetime.now().date())
    before=datetime_to_timestamp(datetime.now().date() + timedelta(hours=24))
    events = list(
        m.events_for_group(
            'python-atlanta',
            status='upcoming,past',
            time='%s000,%s000' % (after, before)))
    assert len(events) == 1
    event = events[0]
    print '%s at %s on %s' % (
        event['name'],
        event['venue']['name'],
        time.ctime(event['time']/1000))
    raw_input('Press enter to continue...')
    rsvps = m.member_rsvps(event['id'])
    in_drawing = [ member for member, response in rsvps if response == 'yes' ]
    for member in in_drawing:
        print member['name']
    while True:
        raw_input('And the winner is...')
        winner = random.choice(in_drawing)
        print winner['name']


class Meetup(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, endpoint, **kwargs):
        params = dict(kwargs)
        params.setdefault('key', self.api_key)
        # params.setdefault('page', 1)
        q = urllib.urlencode(params)
        url = base + endpoint + '.json/?' + q
        try:
            fp = urllib2.urlopen(url)
            text = fp.read()
            data = json.loads(text)
        except urllib2.HTTPError, e:
            print 'There was an error', e
            import pdb; pdb.set_trace()
        return data

    def member_rsvps(self, event_id):
        r = self('2/rsvps', event_id=event_id)
        for x in r['results']:
            yield x['member'], x['response']

    def events_for_group(self, group, **kwargs):
        r = self('2/events', group_urlname=group, **kwargs)
        for x in r['results']:
            yield x


def datetime_to_timestamp(dt):
    return calendar.timegm(dt.timetuple())
    
if __name__ == '__main__':
    main()
