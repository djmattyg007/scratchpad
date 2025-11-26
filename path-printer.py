import os
import subprocess

for entry in os.environ["PATH"].split(os.pathsep):
    print(">", entry)
    if os.path.isdir(entry):
        subprocess.check_call(("ls", "-la", entry))
    else:
        print("not exists")
    print("\n\n")
