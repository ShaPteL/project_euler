# ここにコードを書いてね :-)
def count_divisors(x):
    count=0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            count+=2 if i!=x//i else 1 #重複の場合対の存在はいない
    return count

N=0
n=1
while count_divisors(N)<500:
    N+=n
    n+=1

print("Answer =",N)
