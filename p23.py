# ここにコードを書いてね :-)
def divisors_sum(K):
    return sum([i for i in range(1,(K+2)//2) if K%i==0])

abundants=[]
answers=[]
for i in range(1,28124):#過剰数ならabundants,そうでなければanswersに追加
    if i<divisors_sum(i):
        abundants.append(i)
    else:
        answers.append(i)

print(answers)
print(abundants)
