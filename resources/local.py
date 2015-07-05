# -*- coding: utf-8 -*-
 
import base64,urllib2, json

def url_convert(url):
	url = base64.b64decode(url)
	if base64.b64decode('ZGVzaXN0cmVhbXM=') in url:
		req = urllib2.Request(url)
		a = url.split("=")
		b = urllib2.urlopen(req)
		c  = json.loads(b.read())
		for d in c['channel']:
			if d['id'] == a[-1]:
				url = d['stream_url2']
	return url
