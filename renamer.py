#!/usr/bin/python
# Rename Series Easily

import os, sys, re

if(len(sys.argv) != 2):
	print "Usage: ./%s dirname" % sys.argv[0]
	sys.exit(0)
	
directory = sys.argv[1]
print "Filename:",
filename = raw_input()

regex = r'.*?[s|S](\d{1,2})[e|E](\d{1,2}).*\.(.*)$'
list = os.listdir(directory)

for file in list:
	rename = re.match(regex, file)
	new_name = filename+"-S"
	if(len(rename.group(1)) == 1): new_name += "0"
	new_name += rename.group(1) + "E"
	if(len(rename.group(2)) == 1): new_name += "0"
	new_name += rename.group(2) + "." + rename.group(3)
	print "Renaming \"%s\" to \"%s\"" % (file, new_name)
	os.rename(directory+"/"+file, directory+"/"+new_name)