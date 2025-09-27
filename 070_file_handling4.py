# Write a program that appends a log entry with timestamp 
# to a file log.txt every time it runs.

import datetime

def append_log():
    time = datetime.datetime.now()
    log_entry = f"{time} - program executed\n"

    try:
        with open("log.txt", "a") as f:
            f.write(log_entry)
    except IOError as e:
        print(f"Error writing to log file: {e}")

append_log()
