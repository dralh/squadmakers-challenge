#!/usr/bin/env bash

export SQUADMAKERS_CHALLENGE_CONFIG_PATH="config.yaml"
export FLASK_APP="squadmakers.challenge.flask_app:app"
export FLASK_ENV=development
export FLASK_DEBUG=1

./venv/bin/flask run --host=0.0.0.0 --port=6000 --no-reload
