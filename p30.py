# ここにコードを書いてね :-)
answers=[]
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                        for f in range(10):
                            abcdef=100000*a+10000*b+1000*c+100*d+10*e+f
                            if a**5+b**5+c**5+d**5+e**5+f**5==abcdef:
                                answers.append(abcdef)
print(answers)
print(sum(answers)-1)
