'''
Log File Analyzer 
Kayla Lange
Programming Fundamentals
March 1, 2026

Analyzes Apache server logs to detect suspicious activity such as
failed login attempts, abnormal traffic, and access to sensitive paths.
'''
import re

class LogAnalyzer:

    def __init__(self, log_file) -> None:  # Initializes the class and reads all lines from the log file.
        self.log_file = log_file

    def read_logs(self) -> list: # Opens the log file and returns the list of log entries as lines.
        log_entries = []

        with open(self.log_file, 'r', encoding='utf-8') as file:
            for line in file:
                log_entries.append(line.strip())

        return log_entries
    
    def count_logs_processed(self, log_entries):
        log_count = len(log_entries)
        return log_count
    
    def count_ip_requests(self, log_entries) -> dict: # Processes the log lines to count how many requests were made by each IP address.
        ip_address_requests = {}

        for line in log_entries:
            entry = line.split()
            ip_address = entry[0]

            if ip_address not in ip_address_requests:
                ip_address_requests[ip_address] = 0

            ip_address_requests[ip_address] += 1
        
        return ip_address_requests
    
    def top_five(self, log_entries):
        ip_address_requests = self.count_ip_requests(log_entries)

        sorted_ips= sorted(ip_address_requests.items(), key = lambda x: x[1], reverse = True)

        return sorted_ips[:5]
        
    def detect_failed_logins(self, log_entries): 
    # Identifies IP addresses that triggered 401 (Unauthorized) or 403 (Forbidden) status codes.
        failed_attempts = {}

        for line in log_entries:
            log_entry_line = line.split()
            ip_address = log_entry_line[0]
            status_code = log_entry_line[8]

            if status_code in ['401', '403']:

                failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) +1

        return failed_attempts
    
    def suspicious_attempts(self, log_entries): 
    # Returns IPs that had three or more failed attempts.
        failed_attempts = self.detect_failed_logins(log_entries)
        suspicious = {}

        for ip_address in failed_attempts:
            if failed_attempts[ip_address] >= 3:
                    suspicious[ip_address] = failed_attempts[ip_address]
        
        return suspicious
    
        
    def find_sensitive_access(self, log_entries) -> dict:
    # Searches for access attempts to sensitive paths such as '/admin', '/wp-admin', '.php',or '.bak' files.
        sensitive_access = {}

        for line in log_entries:
            entry = line.split()
            ip_address = entry[0]

            match = re.search(r'"[A-Z]+\s+(\S+)', line)
            if not match: continue
        
            path = match.group(1)

            if  ("/admin" in path
            or "/login" in path
            or "/wp-admin" in path
            or path.endswith(".php")
            or path.endswith(".bak")):
                
                if ip_address not in sensitive_access:
                    sensitive_access[ip_address] = []

                sensitive_access[ip_address].append(path)
            
        return sensitive_access 
    
    def generate_report(self) -> None:
        print('\n----- Log File Analysis Report -----\n')

        log_entries = self.read_logs()
        log_count =  self.count_logs_processed(log_entries)
        top_ips = self.top_five(log_entries)
        suspicious = self.suspicious_attempts(log_entries)
        sensitive = self.find_sensitive_access(log_entries)

        print(f'\nTotal log lines processed: {log_count:,}')

        print('\nThe top 5 most active IPs by number of requests are:\n')
        for ip, count in top_ips:
            print(f'    - {ip}: {count}')

        print ('\nSuspicious IPs:\n')
        if not suspicious:
            print(  'None detected')
        else:
            for ip, count in suspicious.items():
                print(f'  -[{ip}: {count} failed attempts).')

        print('\nSensitive Path Access:')
        for ip, paths in sensitive.items():
            print(f'\n  - {ip} accessed:\n')

            for path in paths:
                print(f'        -{path}')
    
    def __str__(self, generate_report): 
        return generate_report
    
'''
end
'''