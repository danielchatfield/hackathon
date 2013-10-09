import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'libs'))
import requests
import xml.etree.ElementTree as ET

def output_text(msg):
	for char in msg:
		sys.stdout.write ( '%s' % char)
		sys.stdout.flush()
		time.sleep(0.05)
	print ''

def fetchURL(lat,lon,radius):
	payload = {'near': str(lat) + ',' +  str(lon) + ',' +  str(radius)}
	requesturl='http://api.stride-project.com/events/feeds/d38a9c31-3156-446e-a89e-79aa3d7357c2/datastreams/1/events'
	r = requests.get(requesturl, params=payload, auth=('7b399134-f740-4432-9a3e-f6d711473558', ''))
	return r

def parseData(lon, lat, radius):
	data = fetchURL(lon, lat, radius)
	parsedXML = ET.fromstring(data.text)
	events=[]
	for x in range(10):
		try:
			descrip =  parsedXML[x][5][5].text
			urgency = parsedXML[x][5][2].text
			severity = parsedXML[x][5][3].text
			certainty = parsedXML[x][5][4].text
			latlong = parsedXML[x][5][9][0].text
			road = parsedXML[x][5][9][5].text
			direction = parsedXML[x][5][9][4].text
			intersection = parsedXML[x][5][9][1].text
			events.append({'descrip': descrip, 'urgency' : urgency, 'severity': severity, 'certainty':certainty, 'latlong' : latlong, 'road': road, 'direction': direction, 'intersection' : intersection})
		except IndexError:
			pass
		return events

currentEvents = parseData(52.211604, 0.09166, 10000)

for event in currentEvents:
	message = 'There is a ' + event['severity'] + ' problem on the ' + event['road'] +  ' ' + event['direction'] + ' near ' + event['intersection'] + '.\n' + event['descrip']
	output_text(message)
