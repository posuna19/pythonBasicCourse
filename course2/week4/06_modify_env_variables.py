import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

command = ["myapp"]
result = subprocess.run(command, env=my_env, capture_output=True, shell=True)
print("Err:", result.stderr)