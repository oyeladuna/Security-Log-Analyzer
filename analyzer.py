
def get_filename():
    filename = input("File name: ") 
    return filename

def analyze_log(filename: str):

    successful_logins = 0
    failed_logins = 0
    warnings = 0
    errors = 0
    malformed = 0
    USERNAMES = {}
    IP_ADDRESSES = {}
    try:
        with open(filename) as file:

            for line in file:

                if "logged in" in line:
                    successful_logins += 1

                elif "Failed login" in line:
                    failed_logins += 1
                    
                    parts = line.split()
                    try:
                        user = parts[parts.index("user") + 1]
                        if user not in USERNAMES:
                            USERNAMES[user] = 1
                        else:
                            USERNAMES[user] += 1 
                    except ValueError:
                        malformed += 1
                        pass   
                    
                    if "from" in parts:
                        userIp = parts[parts.index("from") + 1]
            
                        if userIp not in IP_ADDRESSES:
                            IP_ADDRESSES[userIp] = 1
                        else:
                            IP_ADDRESSES[userIp] += 1    

                elif "WARNING" in line:
                    warnings += 1

                elif "ERROR" in line:
                    errors += 1
    except FileNotFoundError:
        print(f"{filename} doesn't exist")
        return None
            
    results = {
            "successful_logins": successful_logins,
            "failed_logins": failed_logins,
            "warnings": warnings,
            "errors": errors,
            "malformed": malformed,
            "usernames": USERNAMES,
            "ipAddresses": IP_ADDRESSES
            }
        
    return results
def build_report(results: dict):
    report = ""
    
    report += "Security Log Analysis\n"
    report += "-" * 25 + "\n"
    report += f"Successful logins: {results['successful_logins']}\n"
    report += f"Failed logins: {results['failed_logins']}\n"
    report += f"Warnings: {results['warnings']}\n"
    report += f"Errors: {results['errors']}\n"
    report += f"Malformed: {results['malformed']}\n"

    report += "-" * 25 + "\n"
    report += "Suspicious users:\n"
    for key, value in results["usernames"].items():
        if value >= 3:
            report += f"{key}: {value} failed attempts\n"
            
    report += "-" * 25 + "\n"
    report += "Suspicious IPs:\n"
    for userIP, attempt in results["ipAddresses"].items(): 
        if attempt >= 3 and attempt < 5:
            report += f"{userIP}: {attempt} failed attempts\n" 
    
    report += "-" * 25 + "\n"
    report += "Potential brute-force activity:\n"
    for userIP, attempt in results["ipAddresses"].items(): 
        if attempt >= 5:
            report += f"{userIP}: {attempt} failed attempts\n"

    return report
def save_report(report: str):
    with open("security_report.txt", "a") as log_file:
        log_file.write(report+"\n")

def display_summary(report: str):
    print(report)
        
def main():
    filename = get_filename()
    results = analyze_log(filename)
    
    if results != None:
        report = build_report(results)
        display_summary(report)
        save_report(report)
        

if __name__ == "__main__":
    main()
    