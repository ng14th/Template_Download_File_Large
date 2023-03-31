#!/bin/bash
cmd_set_poetry_venv_in_project="poetry config virtualenvs.in-project true"
cmd_poetry_install="poetry install"
cmd_poetry_shell="poetry shell"
cmd_clear_pycache="find . -type d -name '__pycache__' -exec rm -r {} +"

eval $cmd_clear_pycache
eval $cmd_set_poetry_venv_in_project
eval $cmd_poetry_install
eval $cmd_poetry_shell

echo "Done root"