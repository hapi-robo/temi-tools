#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert XML to CSV format

Converts all entities from temi-XML file to a translation-CSV file.

    translation-CSV:
    NAME, STRING-EN, STRING-JP

    temi-XML File-Format:
    <resources>
        <string name=NAME>STRING-JP</string>
        ...
    </resources>

Reference:
	http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-xml-to-csv-using-python/

"""
import xml.etree.cElementTree as ET
import csv
import argparse
import os


def convert(path):
	"""Convert temi XML to CSV

	Args:
		path (str): Path to XML file

	Returns:
		CSV file

	"""
	path_no_ext = os.path.splitext(args.path)[0]

	tree = ET.parse(path_no_ext + ".xml")
	root = tree.getroot()

	# open a file for writing
	with open(path_no_ext + ".csv", 'w') as csvDataFile:

		# create the csv writer object
		csvwriter = csv.writer(csvDataFile)

		# write header
		csvwriter.writerow(["Name", "Translatable", "String EN", "String JP"])

		# collect data
		for member in root.findall("string"):
			name = member.get("name")
			translatable = member.get("translatable")
			string = member.text
			print("{}, {}, {}".format(name, translatable, string))
			
			# write to csv
			csvwriter.writerow([name, translatable, string])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for temi XML file to be converted to CSV')
    args = parser.parse_args()
    
    convert(args.path)
