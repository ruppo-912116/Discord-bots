import datetime


# finding total seconds from present time to get to 6:00 am the next day
def conversion_to_seconds():
    current_hour = datetime.datetime.now().hour
    current_minute = datetime.datetime.now().minute
    current_delta_time = datetime.timedelta(hours=current_hour, minutes=current_minute)
    destination_delta_time = datetime.timedelta(hours=6, minutes=0) + datetime.timedelta(days=1)
    seconds_until = (destination_delta_time - current_delta_time).total_seconds()
    return seconds_until
