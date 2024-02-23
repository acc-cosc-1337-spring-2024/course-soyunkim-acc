def get_hours(epoch_seconds):
    hours = (epoch_seconds // 3600) % 24
    return hours

def get_minutes(epoch_seconds):
    minutes = (epoch_seconds // 60) % 60
    return minutes

def get_seconds(epoch_seconds):
    seconds = (epoch_seconds % 3600) % 60
    return seconds