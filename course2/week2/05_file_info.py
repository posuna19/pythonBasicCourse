import datetime
import os
from os import path

print("File size: {}".format(path.getsize("spider.txt")))
print("File last time modified: {}".format(path.getmtime("spider.txt")))

timestamp = path.getmtime("spider.txt")
date = datetime.datetime.fromtimestamp(timestamp)
print("File's modified date: {}".format(date))
print("Path of the file: {}".format(path.abspath("spider.txt")))