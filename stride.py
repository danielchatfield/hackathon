import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'libs'))
import requests
import xml.etree.ElementTree as ET

def fetchURL(lat,lon,radius):
	payload = {'near': str(lat) + ',' +  str(lon) + ',' +  str(radius)}
	requesturl='http://api.stride-project.com/events/feeds/d38a9c31-3156-446e-a89e-79aa3d7357c2/datastreams/1/events'
	r = requests.get(requesturl, params=payload, auth=('7b399134-f740-4432-9a3e-f6d711473558', ''))
	return r

data = fetchURL(52.211604,0.09166,1000)
parsedXML = ET.fromstring(data.text)
for child in parsedXML.iter('description'):
	print child.text

