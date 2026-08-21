time = '1h 45m,360s,25m,30m 120s,2h 60s'

summ_minutes = 0

for times in time.split(','):
    for all_time in times.split():
        if 'h' in all_time:
            summ_minutes += int(all_time.replace('h', '')) * 60
        elif 'm' in all_time:
            summ_minutes += int(all_time.replace('m', ''))
        elif 's' in all_time:
            summ_minutes += int(all_time.replace('s', '')) / 60

print(summ_minutes)