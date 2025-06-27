# ここにコードを書いてね :-)
N,k,l=0,1,2#(第N,1,2項の値)
n=3#(添字n)
while len(str(N))<1000:
    N=k+l
    k=l
    l=N
    n+=1
print(n)


