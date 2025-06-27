# ここにコードを書いてね :-)
collatz={1:0}
def collatz_count(N):
    n=N
    count=0
    while n!=1:#コラッツ
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        count+=1
        if n in collatz:
            count+=collatz[n]
            break
    collatz[N]=count
    return None

for i in range(1,1000001):
    collatz_count(i)
print(max(collatz,key=collatz.get))
