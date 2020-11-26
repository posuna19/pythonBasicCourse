#!/usr/bin/env python3

import subprocess
import os

from subprocess import CompletedProcess
from multiprocessing import Pool

def get_dirs():
  directories = []
  for root, dirs, files in os.walk('./data/prod'):
    #print("0. dirs: {}".format(dirs))
    for dir in dirs:
      directories.append(os.path.join(root, dir))
  return directories


def run(src):
  dest = "./data/prod_backup/"
  process = subprocess.run(["rsync", "-arq", src, dest], capture_output=True, cwd=".")

  print("Return code: ", process.returncode)
  #print("Output: ", process.stdout.decode().split())
  #print("Errput: ", process.stderr.decode().split())

if __name__ == "__main__":
  #dirs = get_dirs();
  #print("\n")
  #print("1. Dirs: " + str(dirs))

  # Create a pool of specific number of CPUs
  #pool = Pool(len(dirs))

  # Start each task within the pool
  #pool.map(run, dirs)
  #pool.terminate()
  s =  "./data/prod/alpha"
  #d = "./data/prod_backup/"
  dest = ""
  i = s.find("prod")
  print("i: ",  i)
  if i >= 0:
    dest = s[0:i+4] + "_backup" + s[i+4:]

  print(dest)