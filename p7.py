# ここにコードを書いてね :-)
# 脳筋仕様なのでかなり時間がかかる
n=1
Pcount=0
while 1:
    nod=0
    i=1
    while i<=sqrt(n)+1:
        if n%i==0:
            nod+=1
        i+=1
    if nod==2:
        Pcount+=1
        if Pcount==10001:
            print(n)
            break
    n+=1 #ここまで
