# ここにコードを書いてね :-)
N=1
n=2
divisors=[]
while len(divisors)<500:
    divisors.clear()
    for i in range(1,int(N**0.5)+1):
        if N%i==0:
            divisors.append(i)
            divisors.append(int(N/i))
    divisors=sorted(set(divisors))
    N+=n
    n+=1
print(divisors)
print("Answer =",N-n+1)
