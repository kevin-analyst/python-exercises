from datetime import datetime;

current_datetime = datetime.now();
current_datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S");

print("Current date and time :\n", current_datetime_string);