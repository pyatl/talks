print '\n'.join((''.join(['Fizz' if not n % 3 else '', 'Buzz' if not n % 5 else '']) or str(n)) for n in range(1, 101))
