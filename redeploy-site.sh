#!/bin/bash

tmux kill-server 2>/dev/null
cd ~/pe-portfolio-site || exit 1
git fetch && git reset origin/main --hard
rm -rf python3-venv
python3 -m venv python3-venv
source python3-venv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s flask-server -c ~/pe-portfolio-site \; \
  send-keys 'source python3-venv/bin/activate' Enter \; \
  send-keys 'export FLASK_ENV=development' Enter \; \
  send-keys 'flask run --host=0.0.0.0 --port=5000' Enter
