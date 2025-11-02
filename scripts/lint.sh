#!/usr/bin/env bash

if ! hash python3 &> /dev/null; then
  echo "python3 not found."
  exit 1
fi

VENV_DIR=$(mktemp -d -p /tmp venv-XXXXXX)

python3 -m venv "$VENV_DIR"

source "$VENV_DIR"/bin/activate

pip install --upgrade pip setuptools

pip install ".[dev]"

flake8 .
black .
isort .

deactivate
