# ; A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# ; Пример:
# ; если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random,string
file=open('forA.txt','w',encoding='UTF-8')

k=random.randint(1,5)
koefs=[]
print(k)
i=0
while i<k+1:
    koefs.append(random.randint(0,100))
    i+=1
print(koefs)
equation =''
for ind,koef in enumerate(koefs):
        if ind==len(koefs)-1:
            if koef>0:
                equation+=str(koef)
            equation+='=0'
        else:
            if koef>1:
                equation+=str(koef)
            equation+='*x'
            if ind<len(koefs)-2:
                equation+='**'+str(len(koefs)-1-ind)
            equation+='+'
file.writelines(equation)
file.close
print(equation)


