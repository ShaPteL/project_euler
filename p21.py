# ここにコードを書いてね :-)
Answer=0
K=10000
ds=[]
while K>1:
    k=[i for i in range(1,(K+2)//2) if K%i==0]
    #print(str(K)+"の真の約数："+str(k))
    if sum(k) in ds and sum(k)!=1:
        #print(str(sum(k))+" 友愛？")
        N=sum(k)
        n=[i for i in range(1,(N+2)//2) if N%i==0]
        if K==sum(n):
            #print("友愛！")
            Answer+=N+K
    ds.append(K)
    K-=1

print("Answer=",Answer)
