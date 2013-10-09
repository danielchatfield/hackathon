import frontend.stride
from frontend import app, stride
from flask import request

@app.route('/locationAPI')
def location():
	events = []
	output=''
	payload = [[52.204424, 0.105718], [52.211104,0.106512], [52.212629,0.091792], [52.210854,0.091578]]
	for coords in payload:
		someEvents = frontend.stride.parseData(coords[0], coords[1], 804.7)
		events = events + someEvents
	for event in events:
		 message = '<p>There is a ' + event['severity'] + ' problem on the ' + event['road'] +  ' ' + event['direction'] + ' near ' + event['intersection'] + '</p><p>' + event['descrip'] + '</p>'
		 output = output + message + '<br />'
	return output
@app.route('/test')
def test():
	print location()
	return 'qwerty'
