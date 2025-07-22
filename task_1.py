s = '1h 45m,360s,25m,30m 120s,2h 60s'
result = 0
new_s = s.replace('1h 45m', '105').replace('360s', '6').replace('25m', '25').replace('30m 120s', '32').replace('2h 60s', '121')
s_list = new_s.split(',')
for number in s_list:
    result += int(number)
print(f'Общее количество минут в строке равно {result}')