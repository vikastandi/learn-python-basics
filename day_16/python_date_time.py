from datetime import datetime, time

def datetime_operations():
    # Get the current day, month, year, hour, minute and timestamp from datetime module
    current_date = datetime.now()
    print("Current date and time: ", current_date)
    print("Current year: ", current_date.year)
    print("Current month: ", current_date.month)
    print("Current day: ", current_date.day)
    print("Current hour: ", current_date.hour)
    print("Current minute: ", current_date.minute)
    print("Current timestamp: ", current_date.timestamp())

    # Format the current date time using this format: %Y-%m-%d %H:%M:%S
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted date: ", formatted_date)

    # Change time string "5 December, 2019" to time
    time_string = "5 December, 2019"
    time_object = datetime.strptime(time_string, "%d %B, %Y")
    print("Time object: ", time_object)

    # Calculate the time difference between now and new year
    new_year = datetime(current_date.year + 1, 1, 1)
    time_difference = new_year - current_date
    print("Time difference: ", time_difference)

    # calculate the time dofference between 1 January 1970 and now
    unix_time = datetime(1970, 1, 1)
    time_difference = current_date - unix_time
    print("Time difference: ", time_difference)
    

if __name__ == '__main__':
    datetime_operations()