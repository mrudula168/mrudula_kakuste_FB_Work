# convert time entered into seconds

hr = int(input('Enter hours:'))
min = int(input('Enter minutes:'))
sec = int(input('Enter seconds:'))

seconds = hr *3600 + min * 60 + sec

print('Seconds:',seconds)