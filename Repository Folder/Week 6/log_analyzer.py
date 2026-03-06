'''
Kayla Lange
March 1, 2026
log_analyzer.py

Description:
Analyzes Apache server logs to detect suspicious activity such as
failed login attempts, abnormal traffic, and access to sensitive paths.

'''
from pathlib import Path
from log_analyzer_class import LogAnalyzer

def get_logfile():
    file = input("\nPlease enter the full path and  name of the text file to begin (example.txt):\n")

    log_file = Path(file)

    if log_file.is_file(): return log_file
    else:
        print("\nFile does not exist. Please try again." \
                "\nAn example of the file pathway is: C:\\Users\\username\\Documents\\file.txt\n")

def analyze_logfile(log_file):
    analyzer = LogAnalyzer(log_file)
    analyzer.generate_report()

def would_you_like_to_continue():
    analyze_another_file = input('\nWould you like to analyze another file? (y/n): ').strip().lower()
    if analyze_another_file == 'n': return False
    else: return True



def main():
    print('-----Welcome to the Log Analyzer Tool.-----')

    while True:
        log_file = get_logfile()

        analyze_logfile(log_file)

        if not would_you_like_to_continue():break
    

if __name__=='__main__':
    main()

    print("\nThank you for using the Log Analyzer Tool. Goodbye!")

'''
End
'''