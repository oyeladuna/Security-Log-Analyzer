# Security Log Analyzer

## Description
Security Log Analyzer is a Python automation tool that reads a security log file and analyzes login activity. The program identifies successful and failed login attempts, warnings, errors, suspicious users, and suspicious IP addresses.
The project was built using multiple reusable functions, with each function responsible for a specific task. The functions are then connected together through the main() function.

## Features
- Accepts a log filename from the user
- Checks whether the requested file exists
- Reads and analyzes the log file line by line
- Counts:
    - Successful logins
    - Failed logins
    - Warnings
    - Errors
    - Malformed log entries
- Tracks users with repeated failed login attempts
- Tracks IP addresses associated with failed login attempts
- Identifies suspicious users
- Identifies suspicious IP addresses
- Detects potential brute-force activity
- Generates a formatted security analysis report
- Saves reports to security_report.txt
- Handles missing files and malformed log entries without crashing

## How It Works
The program starts by asking the user for a filename.
File name: security.log
The filename is passed to analyze_log(), which attempts to open the file using Python's file-handling and exception-handling capabilities.
The analyzer then reads the file line by line and checks each line against specific conditions.
For example:
INFO User abdul logged in
is counted as a successful login.
A line such as:
**ERROR** Failed login for user admin
is counted as a failed login and the username is extracted and tracked.
For entries containing an IP address:
**ERROR** Failed login attempt from 192.168.1.20 user admin
the IP address is extracted and tracked separately.
The program stores the results in a dictionary:
```python
results = {
    "successful_logins": successful_logins,
    "failed_logins": failed_logins,
    "warnings": warnings,
    "errors": errors,
    "malformed": malformed,
    "usernames": USERNAMES,
    "ipAddresses": IP_ADDRESSES
}
```
That dictionary is then passed to build_report(), which creates the final report.
The report is displayed to the user and saved to:
security_report.txt

## Example Output
Security Log Analysis

Successful logins: 3
Failed logins: 17
Warnings: 1
Errors: 0
Malformed: 1

Suspicious users:
admin: 13 failed attempts
abdul: 3 failed attempts

Suspicious IPs:
192.168.1.30: 3 failed attempts

Potential brute-force activity:
192.168.1.20: 7 failed attempts

## Project Structure
security-log-analyzer/
├── analyzer.py
├── security.log
├── security_report.txt
└── README.md

## How to Run
From the project directory:
using Bash
python3 analyzer.py
Enter the name of the log file when prompted:
File name: security.log
The analysis will be displayed in the terminal and saved to security_report.txt.

## What I Learned
What I Learned
This project gave me practical experience with:
- Python functions and reusable code
- Dictionaries and key/value mapping
- Loops and conditional statements
- File handling
- String parsing with .split()
- Searching lists with .index()
- Exception handling with try/except
- Handling FileNotFoundError
- Handling malformed data with ValueError
- Building structured results with dictionaries
- Reading log files line by line
- Detecting patterns in security logs
- Basic suspicious-activity detection
- Writing reports to files
- Git and GitHub project management

## Future Improvements
Potential future improvements include:
- Add timestamps to reports
- Validate IP addresses
- Allow users to specify the report filename
- Add more security-event patterns
- Add command-line arguments
- Add automated testing
- Add more advanced brute-force detection based on time windows