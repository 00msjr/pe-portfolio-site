#!/bin/bash

# Activate virtual environment if it exists
if [ -d "python3-virtualenv" ]; then
    source python3-virtualenv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Set testing environment variable
export TESTING=true

# Run the tests
python -m unittest discover -s tests

# Print completion message
echo "Tests completed!"
