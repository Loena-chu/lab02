num=input()
try:
    print(10/int(num))
except ValueError:
    print('ValueError')
except ZeroDivisionError:
    print('ZeroDivisionError')