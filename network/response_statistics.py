#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Measures REST API response time

"""
import requests
import time
import statistics

# user-defined endpoints
# endpoint = 'https://api.temi.cloud/api/v2/public/bandwidth'
endpoint = 'https://api.temi.cloud/api/v2/public/timestamp'

# endpoint = 'https://api.temicloud.cn/api/v2/public/bandwidth'
# endpoint = 'https://api.temicloud.cn/api/v2/public/timestamp'

response_time_list = []

# repeat request
for i in range(100):

	# start time
	t0 = time.time()

	# send a request
	response = requests.get(endpoint)
	
	# response time
	delta = time.time() - t0

	# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
	if response.status_code == 200:
		print("{:.5f}".format(delta))
		response_time_list.append(delta)
	else:
		print("Error {}".format(response.status_code))

print("--")
print("Endpoint: {}".format(endpoint))
print("Samples: {}".format(len(response_time_list)))
print("Average Time: {:.5f} sec".format(statistics.mean(response_time_list)))
print("Variance: {:.5f}".format(statistics.variance(response_time_list)))
print("Maximum Time: {:.5f} sec".format(max(response_time_list)))
print("Minimum Time: {:.5f} sec".format(min(response_time_list)))
