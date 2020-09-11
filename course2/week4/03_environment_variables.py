#!/usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", ""))
print("PATH: " + os.environ.get("PATH", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
print("Fruits2: " + os.environ.get("Fruits2", ""))
print("Docker: " + os.environ.get("DOCKER_TOOLBOX_INSTALL_PATH", ""))
print("testEnv: " + os.environ.get("testEnv", ""))


