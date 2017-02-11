
def hotpo(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def collatz(n, acc = 0):
    if n == 1:
        return acc
    else:
        return collatz(hotpo(n), acc + 1)

