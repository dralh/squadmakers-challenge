import os

import yaml

from squadmakers.challenge.utils.logging import setup_logging

__all__ = ["config"]


def load_config(config_path: str) -> dict:
    if not os.path.isfile(config_path):
        raise RuntimeError(
            "A configuration file was provided but it was not found. "
            "Please make sure the SQUADMAKERS_CHALLENGE_CONFIG_PATH "
            "environment variable points to a valid configuration file."
        )

    with open(config_path) as f:
        try:
            config = yaml.load(f, Loader=yaml.SafeLoader)
        except yaml.YAMLError as exc:
            raise RuntimeError(f"Error parsing config file {config_path}")

    if config.get("Logging"):
        setup_logging(config.get("Logging"))

    return config


config_path = os.environ.get(
    "SQUADMAKERS_CHALLENGE_CONFIG_PATH", "config.yaml"
)
config = load_config(config_path)
