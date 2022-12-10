# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
import math
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
    for item in enumerate(pre_eq):
            eq.append(str(item[1]))
    for item in enumerate(eq):
        temp_str=str(item[1])
        if temp_str.find('x')!=-1:         
            temp_str=temp_str.split('x')
            temp_str[0]=temp_str[0].replace('*','')
            temp_str[1]=temp_str[1].replace('*','')
            if temp_str[0]!= '':
                koefvalue=int(temp_str[0])
            else:
                koefvalue=0
            if temp_str[1]!= '':
                k=int(temp_str[1])
            else:
                k=1           
        else:
            k=0
            koefvalue=int(temp_str)
        indexes[k]=koefvalue
    return  indexes

def sum_eqs(ind1, ind2):
    result_ind={}
    size=max(len(ind1),len(ind2))
    i=0
    while i<size:
        result_ind[i] = int(ind1.get(i))+int(ind2.get(i))
        i+=1
    return result_ind

def indexes_to_eqs (eqs):
    equation =''
    for key in range(len(eqs)-1, -1, -1):
            print(key,eqs[key])
            if key==0: 
                if int(eqs[key])>0:
                    equation+=str(eqs[key])
                equation+='=0'
            else:
                if eqs[key]>0:
                    if int(eqs[key])>1:
                        equation+=str(eqs[key])+'*'
                    equation+='x'
                    if int(key)>1:
                        equation+='**'+str(key)
                    equation+='+'
    return equation

indexes_eq1=read_eq_indexes(eq1)
indexes_eq2=read_eq_indexes(eq2)
total_eqs_ind=sum_eqs(indexes_eq1,indexes_eq2)
print(total_eqs_ind)
result_eq3=indexes_to_eqs(total_eqs_ind)
print(result_eq3)
result_file.writelines(result_eq3)
result_file.close
