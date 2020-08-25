# Descirbes Usage of Utils Scripts

This file describes the usage of scripts located in this directory.

## log_handler.py

The log handler is a utility script to be used when logging. The GetLogger class can used as a 
direct replacement for the `logging` module.

Usage:
```python
GetLogger(log_level, log_file_name, print_to_console)
```

Optional Arguments:
- log_level: (str) level to log e.g. DEBUG, ERROR etc.
- log_file_name: (str) filename/location to log too - Default is script name calling GetLogger()
- print_to_console: (Bool) True or False to stream log to console when running

Basic usage:
```python
logger = GetLogger().logger
logger.debug(f"Add: {num_1} + {num_2} = {num1 + num_2}")
```
