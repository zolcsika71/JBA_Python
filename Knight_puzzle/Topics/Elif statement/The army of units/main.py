army_count = int(input())

if army_count >= 1000:
    print(f'legion')
elif army_count >= 500:
    print(f'swarm')
elif army_count >= 50:
    print(f'horde')
elif army_count >= 10:
    print(f'pack')
elif army_count >= 1:
    print(f'few')
else:
    print(f'no army')
