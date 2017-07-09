# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .forms import QueryForm

# Create your views here.


try:
	import json
except:
	import simplejson as json

from TwitterAPI import TwitterAPI

import urllib, urllib2
import sys



Access_token='3010305642-GzuRDMZAYkiYsuzdhXnFODenUrGfeBrOeHnag8s'
Access_secret='1YiIfbAhPWTeqBTMimiSxXjoASuXL8WPdPfnCT3DhNIWh'
consumer_key='Cw93BNejI3C8SvfKmR1bkXf0h'
consumer_secret='40hYMYHHZtfi9uxkqOYT0EWfPW3CQi9OAvfY0t5kz1M1ZsyuY9'




def query(request):
	if request.method == "POST":
		form = QueryForm(request.POST)
		if form.is_valid():
			print "printing form here"
			print form
			data = form.cleaned_data
			tag = data['query']

			access_token='3010305642-GzuRDMZAYkiYsuzdhXnFODenUrGfeBrOeHnag8s'
			access_secret='1YiIfbAhPWTeqBTMimiSxXjoASuXL8WPdPfnCT3DhNIWh'
			consumer_key='Cw93BNejI3C8SvfKmR1bkXf0h'
			consumer_secret='40hYMYHHZtfi9uxkqOYT0EWfPW3CQi9OAvfY0t5kz1M1ZsyuY9'

			api = TwitterAPI(consumer_key,consumer_secret,access_token,access_secret)
			r = api.request('search/tweets',{'q':tag,'filter':'images'})
			pic_links = []
			for item in r.get_iterator():
				X = json.loads(json.dumps(item).strip())
				Y = X['entities']
				if 'media' in Y:
					Z = Y['media']
					Z = Z[0]
					if 'media_url_https' in Z:
						link = Z['media_url_https']
						pic_links.append(link)

			return render(request,"twitter_pics/result.html",{'pic_links':pic_links})



	else:
		form = QueryForm()

	return render(request,"twitter_pics/query.html",{'form':form})
	
