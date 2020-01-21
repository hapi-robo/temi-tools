#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert CSV to XML format

Converts all entities from translation-CSV file to an XML file.

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
from lxml import etree
import csv
import argparse
import os


def convert(path):
    """Convert CSV to XML

    Args:
        path (str): Path to translation CSV file

    Returns:
        XML file

    """
    path_no_ext = os.path.splitext(args.path)[0]

    # create the root element
    root = etree.Element('resources')

    # make a new document tree
    doc = etree.ElementTree(root)

    with open(path_no_ext + ".csv") as csvDataFile:

        # create the csv reader object
        csvReader = csv.reader(csvDataFile, delimiter=';')

        # skip header
        next(csvReader, None)

        # step through each row of the CSV file 
        # row[0]: name
        # row[1]: translatable
        # row[2]: string-EN
        # row[3]: string-JP
        for row in csvReader:
            print(row)
            if row[1] is None:
                etree.SubElement(root, 'string', name=row[0]).text = row[2]
            else:
                etree.SubElement(root, 'string', name=row[0], translatable=row[1]).text = row[3]

    # save to XML file
    doc.write(path_no_ext + '.xml', pretty_print=True, 
                                    xml_declaration=True, 
                                    encoding='utf-8') 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for translation CSV file to be converted to XML')
    args = parser.parse_args()
    
    convert(args.path)