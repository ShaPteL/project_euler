months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
day=1#日月火水木金土だと思いこむことにして、日は0。よって0の登場回数を数えれば良い
count=0
day=(day+365)%7#1901年1月1日の曜日
#print(day)
for year in range(1901,2001):
    if year%4==0 and (year%400==0 or year%100!=0):#うるう年かどうか判定
        months[2]=29
    else:
        months[2]=28
    #print(year,sum(months.values()))
    for month in months.keys():
        day=(day+months[month])%7#次の月の1日目の曜日は？
        if day==0:
            count+=1
print(count)
