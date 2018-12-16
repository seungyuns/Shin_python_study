import itertools   # 경우의 수 모듈

#숫자와 연산자 갯수 입력 받기
n = int(input("숫자 수 입력 \n"))
n_list = list(map(int, input().split()))
operation_number_list=list(map(int, input().split()))
operation_list =[]
case_list=''
result=[]
c=0

# 연산자 배열에 입력
for i in range(0,operation_number_list[0]):
    operation_list.append('+')
for i in range(0,operation_number_list[1]):
    operation_list.append('-')
for i in range(0,operation_number_list[2]):
    operation_list.append('*')
for i in range(0,operation_number_list[3]):
    operation_list.append('//')

mypermuatation =  itertools.permutations(operation_list)
for i in mypermuatation:
    case_list += str(n_list[0])
    for j in range(0,n-1):
        if i[j]=='//' and int(case_list) < 0:
            c = (-int(case_list)//n_list[j+1])
            case_list= str(-c)
        else:
            case_list += i[j]
            case_list += str(n_list[j+1])
            case_list = str(eval(case_list))
    result.append(case_list)
    case_list=''

result=list(map(int,result))
print(max(result))
print(min(result))

