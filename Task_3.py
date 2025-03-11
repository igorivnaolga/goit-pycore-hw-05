import sys

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None
    return {
        "timestamp": f"{parts[0]} {parts[1]}",
        "level": parts[2],
        "message": parts[3]
    }

# test_logs = [
#     "2024-01-22 08:30:01 INFO User logged in successfully.",
#     "2024-01-22 08:45:23 DEBUG Attempting to connect to the database.",
#     "2024-01-22 09:00:45 ERROR Database connection failed.",
#     "2024-01-22 08:45:23 DEBUG Invalid log entry with missing parts",
# ]

# for log in test_logs:
#     print(parse_log_line(log))


def load_logs(file_path: str) -> list:
    logs = []
    try: 
        with open(file_path) as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return logs

# log_file = "logs.txt"

# logs = load_logs(log_file)

# for log in logs:
#         print(log)


def filter_logs_by_level(logs: list, level:str) -> list:
    return [log for log in logs if log['level'].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    levels_count = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}
    for log in logs:
        level = log['level'].upper()
        if level in levels_count:
            levels_count[level] += 1
    return levels_count


def display_log_counts(counts: dict):
    print(f"{'Level': <10}{'Count'}")
    print("-"*16)
    for level, count in counts.items():
        print(f"{level:<10}{count}")


def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a log file path.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    level_filter = sys.argv[2].lower() if len(sys.argv) == 3 else None
    
    logs = load_logs(file_path)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        print(f"Logs with level {level_filter.upper()}: ")
        for log in filtered_logs:
            print(f"{log['timestamp']} {log['level']} {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
    
if __name__ == "__main__":
    main()
    



