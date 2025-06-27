# ここにコードを書いてね :-)
n=0
x,y=0,0

#二乗の和x
while n<=100:
    x+=n*n
    n+=1
#和の二乗y
n=0
while n<=100:
    y+=n
    n+=1

y=y*y
print(x)
print(y)
y-=x
print(y)



