#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summarize all Dialogflow intents into a CSV file

References:
    https://dialogflow.com/docs

"""
import json
import csv
import os
import random


PATH = "../assets/ja/dialogflow/temi-weather/intents/"
FILENAME = "temi-weather.csv"
# LANGUAGE = 'en'
LANGUAGE = 'ja'

def main():
    # collect all filenames from PATH
    filenames = sorted([f for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, f))])

    # collect all intent filenames
    all_intent_filenames = []
    for filename in filenames:
        # look only for intent file containing meta data
        if '_usersays_' + LANGUAGE + '.json' not in filename:
            # collect all files to be archived
            all_intent_filenames.append(filename)
     
    # open a CSV file for writing
    with open(FILENAME, "w") as csvfile:
        wr = csv.writer(csvfile, 
                            delimiter=',',
                            quoting=csv.QUOTE_MINIMAL)

        all_actions = []
        all_entities = []

        # step through each intent
        for filename in sorted(all_intent_filenames):
            intent = os.path.splitext(filename)[0]

            # do not consider fallback intents
            if (intent.find('fallback') == -1) and (intent.find('unrecognized') == -1 and 
                intent.find('yes') == -1):

                # open intent file
                with open(PATH + filename) as intent_file:
                    intent_data = json.load(intent_file)
        
                    # intent priority must be greater than zero
                    print(intent)
                    if intent_data["priority"] > 0:

                        # check if training data is available
                        if os.path.isfile(PATH + intent + '_usersays_' + LANGUAGE + '.json'):
                            training_available = True

                            with open(PATH + intent + '_usersays_' + LANGUAGE + '.json') as training_file:
                                training_data = json.load(training_file)
                                all_utterances = []
                                for training in training_data:
                                    # concatenate string
                                    utterance = ""
                                    for data in training["data"]:
                                        utterance += data["text"]
                                    
                                    all_utterances.append(utterance)

                            # collect action
                            for response_elem in intent_data["responses"]:
                                if "action" in response_elem:
                                    actions = response_elem["action"]
                                    all_actions.append(response_elem["action"])

                            # collect entities
                            entities = []
                            for response_elem in intent_data["responses"]:
                                for parameter_elem in response_elem["parameters"]:
                                    if "dataType" in parameter_elem:
                                        entities.append(parameter_elem["dataType"])
                                        all_entities.append(parameter_elem["dataType"])

                            sample_utterances = []
                            for i in range(3):
                                index = random.randint(0,len(all_utterances)-1)
                                sample_utterances.append(all_utterances[index])

                            # write to CSV file (sample utterance)
                            utterances_string = sample_utterances[0] + '\n' + \
                                                sample_utterances[1] + '\n' + \
                                                sample_utterances[2]
                            wr.writerow([intent.split(' ', 1)[0], utterances_string])

                        else:
                            print("Training unavailable: {}".format(intent))
                            training_available = False

                    else:
                        print("Intent priority zero: {}".format(intent))

            else:
                print("Fallback or Unrecognized intent: {}".format(intent))

                    


    # print to console
    print("CSV Filename: {}".format(FILENAME))
    print("Total Files: {}".format(len(all_intent_filenames)))
    print("Total Actions: {}".format(len(all_actions)))
    print("Total Entities: {}".format(len(all_entities)))

    # print all filenames
    # for filename in sorted(list(set(all_intent_filenames))):
    #     print(filename)

    # print all actions
    # for item in sorted(list(set(all_actions))):
    #     print(item)

    # print all entities
    # for item in sorted(list(set(all_entities))):
    #     print(item)



if __name__ == '__main__':
    main()