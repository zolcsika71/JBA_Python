start = []
end = []
for i in range(6):
    if i < 3:
        start.append(int(input()))
    else:
        end.append(int(input()))

start_sec = start[0] * 3600 + start[1] * 60 + start[2]
end_sec = end[0] * 3600 + end[1] * 60 + end[2]

print(f'{end_sec - start_sec}')
