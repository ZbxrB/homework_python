seconds = input('Enter number of seconds: ')
seconds = int(seconds)

str_time = f"{seconds // 3600:02}:{seconds % 60:02}:{seconds // 3600 %  60:02}"

print('Time is', str_time)