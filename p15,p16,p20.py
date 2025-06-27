# ここにコードを書いてね :-)
def digitsum(N):
    return sum([int(n) for n in list(str(N))])
def factorial(N):
    return 1 if N==1 else N*factorial(N-1)

print(15,factorial(40)/(factorial(20)*factorial(20)))
print(16,digitsum(9999**1000))
print(20,digitsum(factorial(100)))
