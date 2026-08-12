
def get_filename():
    filename = input("File name: ") 
    return filename

def analyze_log(filename: str):

    successful_logins = 0
    failed_logins = 0
    warnings = 0
    errors = 0

    try:
        with open(filename) as file:

            for line in file:

                if "logged in" in line:
                    successful_logins += 1

                elif "Failed login" in line:
                    failed_logins += 1

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
            "errors": errors
            }
        
    return results

def display_summary(results: dict):
    print("Security Log Analysis")
    print("-" * 25)

    print(f"Successful logins: {results['successful_logins']}")
    print(f"Failed logins: {results['failed_logins']}")
    print(f"Warnings: {results['warnings']}")
    print(f"Errors: {results['errors']}")
    
def main():
    filename = get_filename()
    results = analyze_log(filename)
    display_summary(results)

if __name__ == "__main__":
    main()
    