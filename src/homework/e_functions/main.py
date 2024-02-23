import value_return

epoch_seconds = 3800

hour = value_return.get_hours(epoch_seconds)
minute = value_return.get_minutes(epoch_seconds)
second = value_return.get_seconds(epoch_seconds)

print(hour, ":", minute, ":", second)