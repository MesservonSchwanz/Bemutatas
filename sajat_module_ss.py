# sajat_module_ss.py

def log_event_ss(event_name):
    """Simple event logger."""
    try:
        with open("event_log.txt", "a") as log_file:
            log_file.write(f"Event: {event_name}\n")
        return "Event logged."
    except Exception as e:
        return f"Error during logging: {e}"