import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'libs'))
import requests
import xml.etree.ElementTree

def createURL(lat,lon,radius):
	payload = {'near': str(lat) + ' ' +  str(lon) + ',' +  str(radius)
	requesturl='http://api.stride-project.com/events/feeds/d38a9c31-3156-446e-a89e-79aa3d7357c2/datastreams/1/events.json'
	requesturl = requesturl + '?near=' + str(lat) + ',' + str(lon) + ',' + str(radius)
	return requesturl

URL = createURL(52.211604,0.09166,1000000)


r = requests.get(URL, auth=('7b399134-f740-4432-9a3e-f6d711473558', ''))

print r.text

