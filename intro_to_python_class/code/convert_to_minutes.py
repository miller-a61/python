def convert_to_minutes(hours):
    minutes = hours * 60
    return minutes

def convert_to_seconds(hours):
    minutes = convert_to_minutes(hours)
    seconds = minutes * 60
    return seconds
