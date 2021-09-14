def hoursandmin(a):
    hours = a // 60
    if hours <= 0:
        hours = 0
    minutes = a % 60
    return print(f" {hours} hours and {minutes} minutes")

hoursandmin(1440)