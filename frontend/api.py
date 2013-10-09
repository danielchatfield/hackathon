import frontend.stride
from frontend import app, stride
from flask import request
from collections import OrderedDict

@app.route('/locationAPI', methods=['POST'])
def location():
	events = []
	output=''
	payload = request.data
	print payload
	payload = [['52.204424', '0.105718'], ['52.211104','0.106512'], ['52.212629','0.091792'], ['52.210854','0.091578']]
	for coords in payload:
		someEvents = frontend.stride.parseData(float(coords[0]), float(coords[1]), 804.7)
		events = events + someEvents
	seenEvents = set()
	uniqueEvents= []
	for event in events:
		temp = tuple(event.items())
		if temp not in seenEvents:
			seenEvents.add(temp)
			uniqueEvents.append(event)
	for event in uniqueEvents:
		 message = '<p>There is a ' + event['severity'] + ' problem on the ' + event['road'] +  ' ' + event['direction'] + '.'  + '</p><p>' + event['descrip'] + '</p>'
		 output = output + message + '<br />'
	return output

@app.route('/test')
def test():
	print location()
	return 'qwerty'
