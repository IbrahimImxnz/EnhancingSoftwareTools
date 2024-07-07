import re

def analyze_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    
    error_pattern = re.compile(r'ERROR')
    error_count = sum(1 for log in logs if error_pattern.search(log))
    
    return f'Total Errors: {error_count}'

if __name__ == '__main__':
    log_file = 'server.log'
    print(analyze_logs(log_file))
