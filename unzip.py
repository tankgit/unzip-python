#!/usr/bin/python

import zipfile
import argparse


parser = argparse.ArgumentParser(description="Unzip file when you have no permission to install unzip command.")

parser.add_argument("target",help="the target file you want to unzip.")
parser.add_argument("-d","--destination",help="extract file content to the specific location.")
args = parser.parse_args()


def unzip(target,destination):
    with zipfile.ZipFile(target,'r') as z:
        z.extractall(destination)


target=args.target
destination="./" if args.destination else args.destination
print("Extracting",args.target,"into",destination)
unzip(target,destination)
print("Done!")

