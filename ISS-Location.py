import urllib2
import json
import time

while True:
    req = urllib2.Request("http://api.open-notify.org/iss-now.json")
    response = urllib2.urlopen(req)
    obj = json.loads(response.read())
    print obj['timestamp']
    print obj['iss_position']['latitude'], obj['iss_position']['longitude']
    time.sleep(20)
