import re
def read_file(filename):
    try:
        file = open(filename,'r')
        return  file.readlines()
    except FileNotFoundError as e:
        print(f"File not found at {filename}",e)
    finally:
        file.close()
        print("File parsed and closed")
    
    
def find_error(log_lines, error_patterns):
    errors = []
    for line_num, line in enumerate(log_lines):
        for pattern in error_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                errors.append({"line_number": line_num + 1, "content": line.strip()})
                break
    return errors
    
    
def generate_report(errors):
    report="-------------Summary Report--------------\n\n"
    report+=f"Total error found {len(errors)}\n\n"
    if errors:
        for error in errors:
            print(f"Error found at line: {error['line_number']} and message:{error['content']}\n\n")
    else:
        print("No error found\n\n\n")
    return report


def run():
    log_file = read_file("log.txt")
    error_patterns = ["error", "critical", "failure", "exception", "denied","warning"]
    if log_file:
        error = find_error(log_file,error_patterns)
        report = generate_report(error)
        print(report)
print("-------------end of report---------------")


run()
        