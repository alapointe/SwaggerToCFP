#!/usr/bin/sh

python -m unittest discover -s test -p 'test_*.py'
python -m unittest discover -s test_integration -p 'test_*.py'