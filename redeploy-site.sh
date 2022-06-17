#!/bin/bash

tmux kill-server
cd "portfolio-site"
git fetch && git reset origin/main --hard

tmux new -d 'source python3-virtualenv/bin/activate && pip3 install -r requirements.txt && flask run --host=0.0.0.0'
