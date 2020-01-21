#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summarize all Dialogflow utterances for a single intent into a CSV file

"""
import argparse
import json
import os

from simple_report import SimpleReport

# constants
FIELDS = ["Utterance"]


if __name__ == '__main__':
    # collect arguments
    PARSER = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    PARSER.add_argument("filename", help="Utterance file (.json)")
    ARGS = PARSER.parse_args()

    # generate report
    filename, _ = os.path.splitext(ARGS.filename)
    REPORT = SimpleReport(filename, FIELDS)
    
    with open(ARGS.filename, 'r') as fp:
        training_data = json.load(fp)

        for row, userSays in enumerate(training_data["userSays"]):
            # concatenate string
            utterance = ""
            for data in userSays["data"]:
                utterance += data["text"]
            
            REPORT.add("Utterance", row, utterance)

    REPORT.close()
