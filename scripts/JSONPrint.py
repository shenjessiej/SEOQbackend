#7.11.2016 SEO Tool Team
#The purpose of this file is to receive the JSON Response and parse it
#Dependencies:

import json
import requests 
import urllib2

#variables
url = 'http://www.blakenewman.com/'
keywords = ['seo']
depth = 1
ip = "72.14.207.99"

class JSONPrint:
	def makeRequest(self):
		r = requests.post('http://qscraper.7dhub.com/api/seoq-tool/start-job/', #makes request
		                  json =  {'url': url,
		                          'keywords': keywords,
		                          'depth': depth,
		                          'ip': ip})
		data = r.json()
		job_id = data['job_id'] #gets job id

		getRequest = json.load(urllib2.urlopen('http://qscraper.7dhub.com/api/status/' + job_id + '/')) #get status of the job

		while getRequest['status'] != 'finished': #continues to get the status of the job until it is finished
			getRequest = json.load(urllib2.urlopen('http://qscraper.7dhub.com/api/status/' + job_id + '/'))

		getRequest = json.load(urllib2.urlopen('http://qscraper.7dhub.com/api/seoq/' + job_id + '/')) #gets request after the job is finished
		print(getRequest['results']) #displays the results

results = JSONPrint()
results.makeRequest()