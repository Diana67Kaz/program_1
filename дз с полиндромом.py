n = str(input('Введите '))
def f(n):
    if n==n[::-1]:
        return True
    else:
        return False
print(f(n))