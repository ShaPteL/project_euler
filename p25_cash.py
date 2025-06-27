from functools import lru_cache
@lru_cache
def f(n):
    return n if n<2 else f(n-1)+f(n-2)

x=0
while len(str(f(x)))<10000:
    x+=1
print(x)


