def main(ctx):
    return {
        "kind": "pipeline",
        "name": "scratch",
        "steps": [
            {
                "name": "print-env",
                "image": "debian:bullseye-slim",
                "pull": "always",
                "commands": [
                    "env | sort",
                ],
            },
        ],
    }
