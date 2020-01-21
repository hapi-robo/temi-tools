#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Convert Dialogflow history to spreadsheet

User must manually copy the history from the browser and save this in a text file.
This reads the textfile, parses the data, and saves it to a spreadsheet.

Example training sample:

USER 
サワディカ
Nov 4, 11:19 PM
AGENT 
No matched intent
Nov 4, 11:19 PM
more_vert

"""
import argparse
import os

from simple_report import SimpleReport

# constants
FIELDS = ["Date", "User", "Agent"]


if __name__ == "__main__":
    # collect arguments
    PARSER = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    PARSER.add_argument("filename", help="History text file")
    ARGS = PARSER.parse_args()

    # generate report
    filename, file_extension = os.path.splitext(ARGS.filename)
    REPORT = SimpleReport(filename, FIELDS)
    
    # step each line of history text file
    with open(ARGS.filename, 'r') as fp:
        num_lines = sum(1 for line in open(ARGS.filename))
        rows = int(num_lines / 7)

        print("Reading {} lines of text.".format(num_lines))
        print("Writing {} rows.".format(rows))

        for row in range(1, rows):
            _ = fp.readline()                   # 'USER'
            utterance = fp.readline().strip()   # utterance
            date = fp.readline().strip()        # date
            _ = fp.readline()                   # 'AGENT'
            intent = fp.readline().strip()      # intent
            date = fp.readline().strip()        # date
            _ = fp.readline()                   # 'more_vert'

            print("[{}] {} {} {}".format(row, date, utterance, intent))

            # add row to report
            REPORT.add("Date", row, date, date)
            REPORT.add("User", row, utterance)
            REPORT.add("Agent", row, intent)

    REPORT.close()
