#!/usr/bin/env bash

cd Paranuara-Challenge

python3 -m venv .venv
source .venv/bin/activate
pip3 install pip --upgrade
pip3 install -r requirements.txt

cd app