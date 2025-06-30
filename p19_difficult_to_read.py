#可読性ポイ捨て仕様
c,d=0,2
for y in range(1901,2001):
    M={1:31,2:29 if (y%4==0 and (y%400==0 or y%100!=0)) else 28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    for m in M.keys():
        d=(d+M[m])%7
        c+=False if d else True
print(c)
