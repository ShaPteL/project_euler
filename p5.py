# ここにコードを書いてね :-)
import math
N=20
div_of_ans=[]#1からNまでの最小公倍数の約数


for n in range(1,N+1):
    count=0
    while n%2==0:
        count+=1
        n//=2
        if div_of_ans.count(2)<count:
            for i in range((count-div_of_ans.count(2))):
                div_of_ans.append(2)


    count=0
    f=3
    while f*f<=n:
        while n%f==0:

            count+=1
            n//=f
            if div_of_ans.count(f)<count:
                for i in range((count-div_of_ans.count(f))):
                    div_of_ans.append(f)
        f+=2


    if n!=1:
        if div_of_ans.count(n)<1:
                div_of_ans.append(n)

print(div_of_ans)
print(math.prod(div_of_ans))
