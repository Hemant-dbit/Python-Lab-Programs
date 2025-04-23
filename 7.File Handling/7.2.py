from datetime import datetime

LOG_FILE = "server.txt"
ERROR_FILE = "error.txt"

def create_log_file():
    with open(LOG_FILE, "w") as file:
        file.write(f"[{datetime.now()}] System started.\n")
        file.write(f"[{datetime.now()}] Error: Unable to connect to database.\n")
        file.write(f"[{datetime.now()}] User logged in.\n")
        file.write(f"[{datetime.now()}] Error: Disk space low.\n")
        file.write(f"[{datetime.now()}] Process completed successfully.\n")
    print(" Sample log file created.")

def extract_errors():
    error_lines = []
    count = 0
    with open(LOG_FILE, "r") as file:
        for i, line in enumerate(file, start=1):
            if 'error' in line.lower():
                error_lines.append(f"Line {i}: {line.strip()}")
                count += 1
    return error_lines, count

def save_errors(errors):
    with open(ERROR_FILE, "w") as file:
        file.write("\n".join(errors))
    print(f" Errors saved to '{ERROR_FILE}'")

def main():
    create_log_file()
    errors, count = extract_errors()
    if errors:
        save_errors(errors)
        print(f"\n Total 'error' occurrences: {count}")
        print(" Extracted Errors:")
        for err in errors:
            print(err)
    else:
        print("\n No errors found in the log.")

if __name__ == "__main__":
    main()
