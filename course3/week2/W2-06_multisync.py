#!/usr/bin/env python3
from multiprocessing import Pool

def run(task):
    # Do something with task here
    print("Handling {}".format(task))

if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']

  # Create a pool of specific number of CPUs
  pool = Pool(len(tasks))

  # Start each task within the pool
  pool.map(run, tasks)
