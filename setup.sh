#!/usr/bin/env bash

python3 -m venv .venv
source .venv/bin/activate
pip3 install pip --upgrade
pip3 install -r requirements.txt