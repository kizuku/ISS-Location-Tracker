import urllib2
import json
import time
from m2x.client import M2XClient

M2X_API_KEY="13f2e490df1f3dbf56d5afb498cda2f3"

client = M2XClient(key=os.environ[M2X_API_KEY])

device = client.create_device(
    name='ISS-Location-Tracker',
    description='Displays coordinates of ISS location at given timestamp',
    visibility='public'

stream = device.create_stream('ISS Location')

while True:
    req = urllib2.Request("http://api.open-notify.org/iss-now.json")
    response = urllib2.urlopen(req)
    obj = json.loads(response.read())
    print obj['timestamp']
    print obj['iss_position']['latitude'], obj['iss_position']['longitude']
    stream.add_value(obj['timestamp'])
    stream.add_value(obj['iss_position']['latitude'], obj['iss_position']['longitude'])
    time.sleep(20)
