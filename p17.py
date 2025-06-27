onedigits={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
teens={10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
tys={20:'twenty',30: 'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
#値を文字数に変換する
#辞書で20が重複してたから解けなかっただけってマジ？？？
for w in onedigits:
    onedigits[w]=len(onedigits[w])
for w in teens:
    teens[w]=len(teens[w])
for w in tys:
    tys[w]=len(tys[w])
#ここまで前準備

ans=0

x1_x9=sum(onedigits.values())#1~9
x10_x19=sum(teens.values())#10~19

x20_x99=0
for second in tys:#20~99
    x20_x99+=tys[second]*10+x1_x9#twenty+twenty*9+(one+two+...+nine)

x1_x99=x1_x9+x10_x19+x20_x99


#以降、andが必要なことに注意
x100_x999=0
for third in onedigits:#100,200,...,900=one hundred,two hundred,...,nine hundred
    x100_x999+=onedigits[third]+len('hundred')

for third in onedigits:#101~199,201~299,...,901~999     101~199=[one hundred and]*99+(1~99)
    x100_x999+=(onedigits[third]+len('hundredand'))*99+x1_x99


ans=x1_x99+x100_x999+len('onethousand')
print(ans)
