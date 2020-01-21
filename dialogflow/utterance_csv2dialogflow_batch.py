#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Converts a batch of CSV training files to Dialogflow's JSON data format.

This script takes a directory of CSV training files and converts this to
a list of Dialogflow JSON training data. Each CSV file is one intent 
containing any number of training utterances.

Usage:
    ./csv2dialogflow_batch.py training/ agent_en/intents/ agent_jp/intents/

"""
import argparse
import os
import json
import csv

COLUMN = 0 # CSV column with training phrases (first column is 0)


def meta_file(old_json, new_json):
    """Modify Dialogflow JSON meta file

    Args:
        old_json (str): Path to old Dialogflow JSON meta file
        new_json (str): Path to new Dialogflow JSON meta file

    Returns:
        New Dialogflow JSON meta file

    """
    json_file = open(old_json)
    json_data = json.load(json_file)
    
    # add modification
    for id1, responses in enumerate(json_data["responses"]):
        for id2, messages in enumerate(responses["messages"]):
            # print("{}".format(messages["lang"]))
            # print("{}".format(json_data["responses"][id1]["messages"][id2]["lang"]))
            json_data["responses"][id1]["messages"][id2]["lang"] = "ja"

    # write new JSON files
    with open(new_json, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)



def training_file(path_csv, path_json):
    """Convert CSV training file to JSON

    Args:
        path_csv (str): Path for CSV training file
        path_json (str): Path to Dialogflow jSON meta file

    Returns:
        Dialogflow JSON training file

    """
    csv_file = open(path_csv)
    csv_data = csv.reader(csv_file, delimiter=';')

    # skip header
    next(csv_data, None)

    # step through each row of the CSV file
    json_data = [] 
    for row in csv_data:
        # print(row[COLUMN])

        # single utterance
        tmp = False
        sample = {
            "id": "",
            "data": [
                {
                    "text": row[COLUMN],
                    "userDefined": tmp
                }
            ],
            "isTemplate": tmp,
            "count": 0,
            "updated": 0
        }

        # print(sample)
        json_data.append(sample)


    # write new JSON files
    with open(path_json, 'w') as outfile:
        json.dump(json_data, outfile, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path_training', help='Path to CSV training folder')
    parser.add_argument(
        'path_intent_en', help='Path to Dialogflow intent folder (English)')
    parser.add_argument(
        'path_intent_jp', help='Path to Dialogflow intent folder (Japanese)')
    args = parser.parse_args()
    

    # collect all filenames from training folder
    filenames = sorted([f for f in os.listdir(args.path_training) if os.path.isfile(os.path.join(args.path_training, f))])
    # print("{}".format(filenames))

    # filter for CSV files
    csv_filenames = []
    for filename in filenames:
        if ".csv" in filename:
            # collect all files to be archived
            csv_filenames.append(filename)
            # print("{}".format(filename))

    for filename in csv_filenames:
        path_intent_en = args.path_intent_en + filename
        path_intent_jp = args.path_intent_jp + filename
        
        meta_filename_en = os.path.splitext(path_intent_en)[0] + '.json'
        meta_filename_jp = os.path.splitext(path_intent_jp)[0] + '.json'
        # print("{} {}".format(meta_filename_en, meta_filename_jp))
        meta_file(meta_filename_en, meta_filename_jp)

        training_filename_csv = args.path_training + filename
        training_filename_json = os.path.splitext(path_intent_jp)[0] + '_usersays_ja.json'
        # print("{} {}".format(training_filename_csv, training_filename_json))
        training_file(training_filename_csv, training_filename_json)
