# ここにコードを書いてね :-)
maxPP=0

for a in range(999,99,-1):
    for b in range(a,99,-1):
            N=a*b
            if str(N)==str(N)[::-1]:
                if N>maxPP:
                    maxPP=N
                    A=a
                    B=b
print('Answer',':',maxPP,'=',A,'*',B)
