# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

file1=open('forB1.txt','r',encoding='UTF-8')
file2=open('forB2.txt','r',encoding='UTF-8')
result_file=open('forB3.txt','w',encoding='UTF-8')
eq1=file1.read()
eq2=file2.read()
file1.close
file2.close


def read_eq_indexes(pre_eq:str):
    indexes={}
    pre_eq=pre_eq.replace(' ','')
    pre_eq=pre_eq[:-2]
    pre_eq=pre_eq.split('+')
    print(pre_eq)
    eq=[]
    for i,item in enumerate(pre_eq):
            eq.append(str(item))
            print(eq)

    for item in enumerate(eq):
        if 'x' in str(item) == True:
            print(item)
            if item[1] not in 'x' == True:
                koefvalue=item[1].split('*x')
                koefvalue=int(koefvalue[0])
                if "*" in koefvalue[1] == True:             
                    k=int(koefvalue[1].replace('*',''))
                else:
                    k=1
        else:
            k=0
            koefvalue=int(item[1])
        indexes[k]=koefvalue
        
read_eq_indexes(eq1)