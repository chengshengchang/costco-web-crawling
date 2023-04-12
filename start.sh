#!/bin/bash

# Run the main_handler.py file and redirect stdout and stderr to log files
python main_handler.py > logs/output.log 2> logs/error.log
