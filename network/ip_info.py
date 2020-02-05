#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Add IP information to Wireshark Endpoint Statistics

Takes as input a Wireshark Endpoint Statistics CSV and appends the IP information
obstained from an IP-look-up service.

usage:
    python add_ip.py <input-csv> <output-csv>

Reference:
    https://www.wireshark.org/docs/wsug_html_chunked/ChStatEndpoints.html
"""
import os
import csv
import argparse
import requests
import time


# constants
BASE_URL = 'http://ip-api.com/json/'
KEY_LIST = ['country', 'city', 'lat', 'lon', 'timezone', 'isp', 'org']
REQ_LIMIT = 30 # [requests/minute]
WAIT_PERIOD = 60 # [sec]

DEVICE_IP = '192.168.137.243'
DEVICE_GATEWAY = '192.168.137.1'


def check_append(lst, data, key):
    if key in data:
        lst.append(data[key])
    else:
        lst.append('')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('input_csv', help='Wireshark endpoint CSV filename (.csv)')
    args = parser.parse_args()
    
    with open(args.input_csv) as csv_read_f:
        # create the csv reader object
        csv_reader = csv.reader(csv_read_f, delimiter=',')

        # open a file for writing
        output_filename = os.path.splitext(args.input_csv)[0] + "_info.csv"
        with open(output_filename, 'w') as csv_write_f:
            # create the csv writer object
            csv_writer = csv.writer(csv_write_f)

            # step through each row of the CSV file 
            req_cnt = 0
            for idx, row in enumerate(csv_reader):

                # ignore header
                if idx < 1:
                    row.extend(KEY_LIST)
                    csv_writer.writerow(row)
                else:
                    ip_addr = row[0]
                    print("{} {}".format(idx, ip_addr))

                    if (ip_addr == DEVICE_IP) or (ip_addr == DEVICE_GATEWAY):
                        print("-- skip")
                    else:
                        if req_cnt >= REQ_LIMIT:
                            print("Waiting 60 seconds for server to receive next batch of requests...")
                            time.sleep(WAIT_PERIOD)
                            req_cnt = 0 # reset counter
                        else:
                            # collect IP address details
                            url = BASE_URL + str(ip_addr)
                            resp = requests.get(url)
                            data = resp.json()
                            req_cnt += 1

                            # append IP address details
                            for key in KEY_LIST:
                                if key in data:
                                    row.append(data[key])
                                else:
                                    row.append('')

                            # write row to new csv file
                            csv_writer.writerow(row)
