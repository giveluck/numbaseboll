import random

def select_number():
    while True:
        n = random.randint(1000, 10000) #랜덤 4자리 숫자
        string_n = str(n) #문자열로 바꾸기
        tmp_data = [string_n.count(str) for str in string_n] #리스트안에 문자 갯수 넣기
        if tmp_data !=[1,1,1,1]:
            continue
        else:
            return n
            break

for i in range(0,100):
    print(select_number())
