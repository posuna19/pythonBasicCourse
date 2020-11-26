import os

for root, dirs, files in os.walk(".\\data\\prod"):
   for dir in dirs:
      print(os.path.join(root, dir))


def run(src):
  dest = "\\data\\prod_backup\\"
  subprocess.call(["rsync", "-aq", src, dest])
