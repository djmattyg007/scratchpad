def main(ctx):
    return {
        "kind": "pipeline",
        "name": "scratch",
        "steps": [
            "name": "print-env",
            "image": "debian:bullseye",
            "pull": "always",
            "commands": [
                "env | sort",
            ],
        ],
    }
