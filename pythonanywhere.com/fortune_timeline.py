#!/usr/bin/env python3

# need to update requests on pythonanywhere.com
# open bash console and type following pip install command
# pip3.4 install --upgrade --user requests

from pin import Pin
from timeline import Timeline
import datetime, pytz
import fortune

FORTUNE_FILE='fortunes' #fortunes.py appends .dat
todays_fortune = fortune.get_random_fortune(FORTUNE_FILE)

PRODUCTION_KEY='12345678901212345678901234561234'
timeline = Timeline(PRODUCTION_KEY)
topic = 'fortune'

# Post daily at 6am for the chosen timezone
pst = pytz.timezone('America/Los_Angeles')
time_6am = pst.localize(
    datetime.datetime.now().replace(hour=6, minute=0, second=0)).astimezone(pytz.utc)
time_6am += datetime.timedelta(days=1) # post 1 day ahead (ie. tomorrow)
# convert to zulu time for the timeline api, will show up as 6am for the above timezone
time_zulu = time_6am.isoformat().rsplit(".", 1 )[ 0 ] + 'Z',

# have the pin hold just the date
pin_id = str(time_6am.date())
my_pin = Pin(id=pin_id, time= time_zulu, layout={
    'type': 'genericPin',
    'title': 'Daily Fortune',
    'body': todays_fortune})
result = timeline.send_shared_pin([topic_utc], my_pin)
print("timeline send_shared_pin topic:{} result:{}".format(topic_utc, result))
