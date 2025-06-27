# ここにコードを書いてね :-)
N,k,l=0,1,2
S=2
print(k)
print(l)
while N<4000000:
    N=k+l
    #print(N)
    k=l
    l=N
    if N%2==0:
        S+=N
print(S)




