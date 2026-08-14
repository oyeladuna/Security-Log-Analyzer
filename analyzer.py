
def get_filename():
    filename = input("File name: ") 
    return filename

def analyze_log(filename: str):

    successful_logins = 0
    failed_logins = 0
    warnings = 0
    errors = 0
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
                    user = parts[parts.index("user") + 1]
                    if user not in USERNAMES:
                        USERNAMES[user] = 1
                    else:
                        USERNAMES[user] += 1    
                    
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
    except Exception as e:
        print(e)
            
    results = {
            "successful_logins": successful_logins,
            "failed_logins": failed_logins,
            "warnings": warnings,
            "errors": errors,
            "usernames": USERNAMES,
            "ipAddresses": IP_ADDRESSES
            }
        
    return results

def display_summary(results: dict):
    print("Security Log Analysis")
    print("-" * 25)

    print(f"Successful logins: {results['successful_logins']}")
    print(f"Failed logins: {results['failed_logins']}")
    print(f"Warnings: {results['warnings']}")
    print(f"Errors: {results['errors']}")
    
    print("-" * 25)
    print("Suspicious users: ")
    for key, value in results["usernames"].items():
        if value >= 3:
            print(f"{key}: {value} failed attempts")
    
    print("-" * 25)
    print("Suspicious IPs:")
    for userIP, attempt in results["ipAddresses"].items(): 
        if attempt >= 3 and attempt < 5:
            print(f"{userIP}: {attempt} failed attempts") 
            
    print("-" * 25)
    print("Potential brute-force activity:")
    for userIP, attempt in results["ipAddresses"].items(): 
            if attempt >= 5:
                print(f"{userIP}: {attempt} failed attempts")
        
def main():
    filename = get_filename()
    results = analyze_log(filename)
    display_summary(results)

if __name__ == "__main__":
    main()
    