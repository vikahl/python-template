"""Utility script for updating the Docker base image hashes in cookiecutter.json

No error handling at all, but it is ok given the controlled environment in
which it is run.
"""

import json
import pathlib

import requests


def get_latest_hash(tag: str, architecture: str) -> str:
    r = requests.get(
        f"https://hub.docker.com/v2/repositories/library/python/tags/{tag}"
    )

    for image in r.json()["images"]:
        if image["architecture"] == architecture:
            return f"{tag}@{image['digest']}"

    raise RuntimeError(f"No image found for {tag=} and {architecture=}")


cookie_file = pathlib.Path(__file__).parent.parent / "cookiecutter.json"

with open(cookie_file, "r+") as f:
    cookie_tpl = json.load(f)

    # Get latest hashes from Docker hub
    for architecture, python_versions in cookie_tpl["_base_images"].items():
        for python_version, digest in python_versions.items():
            # Update the dict in place
            python_versions[python_version] = get_latest_hash(
                f"{python_version}-slim", architecture
            )

    f.seek(0)
    json.dump(cookie_tpl, f, indent=2)
