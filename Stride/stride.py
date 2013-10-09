from xml.dom import minidom

def createURL(lat,lon,radius):
	requesturl='http://api.stride-project.com/events/feeds/d38a9c31-3156-446e-a89e-79aa3d7357c2/datastreams/1/events'
	requesturl = requesturl + '?near=' + str(lat) + ',' + str(lon) + ',' + str(radius)
	return requesturl

URL = createURL(52.211604,0.09166,10000)
print URL
