#!/usr/bin/env bash

if ! hash python3 &> /dev/null; then
  echo "python3 not found."
  exit 1
fi

VENV_DIR=$(mktemp -d)

python3 -m venv "$VENV_DIR"

source "$VENV_DIR"/bin/activate

pip install --no-cache-dir --upgrade pip setuptools

pip install pre-commit==4.3.0

pre-commit install --install-hooks

deactivate
