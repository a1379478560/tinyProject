def input_num():
    while(True):
        zhangsan_num=input('please in put a number\n')
        try:
            num=int(zhangsan_num)
            break
        except  :
            print('please input a number NOT letters of an alphabet or float!\n')

    return num
def factorization(num):
    while num!=1:
        for i in range(2,num+1):
            if num%i == 0:
                print(i)
                num //= i
                break
print(int(2.2))
print(int('2.2'))
num=input_num()
print('prime factor is:')
factorization(num)