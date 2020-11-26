#!/usr/bin/env python3

import subprocess
import os

#from subprocess import CompletedProcess
from multiprocessing import Pool

def get_dirs():
  directories = []
  proc = subprocess.run(["pwd"], cwd=".")
  print("pwd stdout: ", proc)
  for root, dirs, files in os.walk('./data/prod/'):
    #print("0. dirs: {}".format(dirs))
    for dir in dirs:
      directories.append(os.path.join(root, dir))
  return directories


def run(src):
  dest = "./data/prod_backup/"
  i = src.find("prod")
  print("i: ",  i)
  if i >= 0:
    dest = src[0:i+4] + "_backup" + src[i+4:]

  process = subprocess.run(["rsync", "-arq", src, dest])

  print("rsync process: ", process)
  #print("Output: ", process.stdout.decode().split())
  #print("Errput: ", process.stderr.decode().split())

if __name__ == "__main__":
  dirs = get_dirs();
  #print("\n")
  print("1. Dirs: " + str(dirs))

  # Create a pool of specific number of CPUs
  pool = Pool(len(dirs))

  # Start each task within the pool
  pool.map(run, dirs)
  pool.terminate()
