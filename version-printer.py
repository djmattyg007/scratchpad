import shlex
import subprocess

version_flag_cmds = (
    "bash",
    "pwsh",
    "python3",
    "pip",
    "pipx",
    "perl",
    "cargo",
    "node",
    "npm",
    "yarn",
    "git",
    "git lfs",
    "gh",
    "jq",
)

version_sub_cmds = (
    "go",
    "docker",
    "docker compose",
)

for cmd in version_flag_cmds:
    print(">", cmd)
    try:
        subprocess.run((*shlex.split(cmd), "--version"))
    except FileNotFoundError:
        print("not found")

for cmd in version_sub_cmds:
    print(">", cmd)
    try:
        subprocess.run((*shlex.split(cmd), "version"))
    except FileNotFoundError:
        print("not found")
