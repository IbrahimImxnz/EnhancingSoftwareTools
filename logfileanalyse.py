import re
import os

LOG_FILE_PATH = '/path/to/log/file.log'
ERROR_PATTERN = re.compile(r'ERROR')
WARNING_PATTERN = re.compile(r'WARNING')

def analyze_log_file():
    if not os.path.exists(LOG_FILE_PATH):
        print(f"Log file not found: {LOG_FILE_PATH}")
        return

    with open(LOG_FILE_PATH, 'r') as file:
        lines = file.readlines()

    error_count = 0
    warning_count = 0

    for line in lines:
        if ERROR_PATTERN.search(line):
            error_count += 1
        if WARNING_PATTERN.search(line):
            warning_count += 1

    print(f"Log Analysis Report:")
    print(f"Total Errors: {error_count}")
    print(f"Total Warnings: {warning_count}")

if __name__ == "__main__":
    analyze_log_file()
