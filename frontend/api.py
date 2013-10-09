import frontend.stride
from frontend import app, stride
from flask import request, json
from collections import OrderedDict

@app.route('/locationAPI', methods=['POST'])
def location():
	events = []
	output=''
	payload = request.data
	#print payload
	#payload = [['52.204424', '0.105718'], ['52.211104','0.106512'], ['52.212629','0.091792'], ['52.210854','0.091578']]
	uniqueEvents = LocationWorker(payload)
	output = json.dumps(uniqueEvents)
	return output
def LocationWorker(coordinates):
	events = []
	for coords in coordinates:
		someEvents = frontend.stride.parseData(float(coords[0]), float(coords[1]), 50000)
		events = events + someEvents
	seenEvents = set()
	uniqueEvents= []
	for event in events:
		temp = tuple(event.items())
		if temp not in seenEvents:
			seenEvents.add(temp)
			uniqueEvents.append(event)
	return uniqueEvents

@app.route('/test')
def test():
	#print location()
	return 'qwerty'
