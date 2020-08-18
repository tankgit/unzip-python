#!/usr/bin/env python

import zipfile
import argparse


parser = argparse.ArgumentParser(description="This is an unzip command could be using when you have no permission to install unzip command on the servet.")

parser.add_argument("target",nargs="+",help="the target file you want to unzip.")
parser.add_argument("-d","--destination",help="extract file content to the specific location.")
args = parser.parse_args()


def unzip(i,n,target,destination):
    print("proceeding\033[32m[%d/%d]\033[0m: %s" % (i,n,target))
    with zipfile.ZipFile(target,'r') as z:
        z.extractall(destination)


targets=args.target
total=len(targets)
destination="./" if not args.destination else args.destination
print("\033[33m>>> Extracting\033[31;01m",total,"\033[0;33mfiles into\033[31;01m",destination,"\033[0m<<<\n---")
for i,t in enumerate(targets):
    unzip(i+1,total,t,destination)
print("---\n\033[32;01mDone!\033[0m")

