def add_time(start, duration, day = False):
    new_time = ''

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    if period == 'PM':
        start_hour += 12

    new_minute = start_minute + duration_minute
    new_hour = start_hour + duration_hour + (new_minute // 60)
    added_day = new_hour // 24
    new_minute %= 60
    new_hour %= 24

    if new_hour < 12:
        period = 'AM'
    else:
        period = 'PM'

    new_hour %= 12
    if new_hour == 0:
        new_hour = 12 

    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    if day:
        index_day = (days_of_week.index(day.capitalize()) + added_day) % 7
        new_day = days_of_week[index_day]
        new_time += f'{new_hour}:{new_minute:02d} {period}, {new_day}'
    else:
        new_time += f'{new_hour}:{new_minute:02d} {period}'

    if added_day == 1:
        new_time += f' (next day)'
    if added_day > 1:
        new_time += f' ({added_day} days later)'

    return new_time

print(add_time('11:59 PM', '24:05', 'Wednesday'))