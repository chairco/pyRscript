#!/bin/sh

# simple test command for demo project
# this script will report the demo project coverage

pytest --cov-report term-missing --cov pyRscript
