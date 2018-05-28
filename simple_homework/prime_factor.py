def input_num():
    while(True):
        num=input('please in put a number\n')
        try:
            num=int(num)
            break
        except  :
            print('please input a number NOT letters of an alphabet!')
    return num
def factorization(num):
    while num!=1:
        for i in range(2,num+1):
            if num%i == 0:
                print(i)
                num //= i
                break

num=input_num()
print('prime factor is:')
factorization(num)