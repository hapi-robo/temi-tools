#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyze temi call logs

"""
import pandas as pd

FILENAME = 'temi_call_logs_2020_09-10.csv'

BETA_TESTING = [120203007, 119260139, 119260109, 119260114, 119260058, 119452439, 119452389, 119452440, 119462496]
DEMO_ROBOTS = [119260119, 120192907, 120192893, 119260057]

if __name__ == '__main__':
    # Read CSV file into dataframe df
    df = pd.read_csv(FILENAME)

    # Analysis
    unique_ids = df.robotId.unique()
    unique_ids.sort()
    for id in unique_ids:
        logs = df.loc[df['robotId'] == id]

        if id in BETA_TESTING:
            print('{},{},{}'.format(id, logs.size, 'HRST BETA-TESTING'))
        elif id in DEMO_ROBOTS:
            print('{},{},{}'.format(id, logs.size, 'HRST DEMO-ROBOTS'))
        else:
            print('{},{}'.format(id, logs.size))

    cant_join = df.loc[df['Status'] == 'CANT_JOIN']
    poor_connection = df.loc[df['Status'] == 'POOR_CONNECTION']
    timeout = df.loc[df['Status'] == 'TIMEOUT']
    print("Can't Join: {} ({}%)".format(cant_join.size, 100 * cant_join.size / df.size))
    print("Poor Connection: {} ({}%)".format(poor_connection.size, 100 * poor_connection.size / df.size))
    print("Timeout: {} ({}%)".format(timeout.size, 100 * timeout.size / df.size))
