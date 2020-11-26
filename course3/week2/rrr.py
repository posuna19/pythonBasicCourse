import subprocess
import os

def get_dirs(dir):
  directories = []
  for root, dirs, files in os.walk('../data/prod'):
    for dir in dirs:
      directories.append(os.path.join(root, dir))

#if __name__ == "__main__":
  dirs = get_dirs();
  print(dirs)

  # Create a pool of specific number of CPUs
  # pool = Pool(len(tasks))

  # Start each task within the pool
  # pool.map(run, tasks)
