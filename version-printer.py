import shlex
import subprocess
from itertools import chain, zip_longest

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

for cmd, verflag in chain(
    zip_longest(version_flag_cmds, (), fillvalue="--version"),
    zip_longest(version_sub_cmds, (), fillvalue="version"),
):
    print(">", cmd)
    try:
        subprocess.run((*shlex.split(cmd), verflag))
    except FileNotFoundError:
        print("not found")
