#!/usr/bin/env bash


function lint {
  flake8 ./src ./tests
  black ./src ./tests
  isort ./src ./tests
}


if [[ -z "$VIRTUAL_ENV" ]]; then
  if ! hash python3 &> /dev/null; then
    echo "python3 not found."
    exit 1
  fi

  VENV_DIR=$(mktemp -d -p /tmp venv-XXXXXX)
  python3 -m venv "$VENV_DIR"
  source "$VENV_DIR"/bin/activate

  pip install --upgrade pip setuptools
  pip install ".[dev]"

  lint

  deactivate
else
  lint
fi
