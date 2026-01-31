def convert_seconds_to_time(seconds_since_midnight):
    """
    Converts a given number of seconds since midnight into a formatted
    time string showing hours, minutes, seconds, and AM/PM.

    Also, if the input is invalid, returns an appropriate error message.

    """

    # Validate input range
    if seconds_since_midnight < 0 or seconds_since_midnight >= 24 * 60 * 60:
        return "Invalid input: seconds must be between 0 and 86399."

    # Calculate hours, minutes, and seconds
    total_hours = seconds_since_midnight // 3600
    remaining_seconds = seconds_since_midnight % 3600

    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    # Determine AM or PM
    if total_hours < 12:
        am_pm = "AM"
    else:
        am_pm = "PM"

    # Convert to 12-hour format
    hours = total_hours % 12
    if hours == 0:
        hours = 12

    # Return formatted time string
    return f"{hours:02d}:{minutes:02d}:{seconds:02d} {am_pm}"

#printing some of the time
print(convert_seconds_to_time(0))
print(convert_seconds_to_time(45000))
