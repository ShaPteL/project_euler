# ここにコードを書いてね :-)
def isprime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

forans=[]
for k in range (3,2000001,2):
    if isprime(k):
        forans.append(k)
print(sum(forans)+2)

