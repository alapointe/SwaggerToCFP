#!/usr/bin/sh

export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
echo $PYTHONPATH

python main.py
# python -m unittest discover -s test -p 'test_*.py'