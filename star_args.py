def print_backwards(*args, **kwargs):
    print(kwargs)
    kwargs.pop('end', None)
    for word in args[::-1]:
        print(word[::-1],end = '',**kwargs)

print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')