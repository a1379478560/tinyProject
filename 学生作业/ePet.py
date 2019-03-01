import threading
import time
import random

record_file = 'record.txt'

def everyhourdo():
    global hours
    global health
    global hungry
    global happiness
    global status

    if hungry>80 or hungry<20:
        health-=2
    if happiness<20:
        health-=1

    if status==1:
        hungry+=1
    if status==2:
        hungry+=2
        happiness-=1
    if status==3:
        hungry+=3
        health+=1
    if status==4:
        hungry+=3
        happiness+=1
    if status==5:
        hungry-=3
    if status==6:
        health+=4

    if health<0:
        health=0
    if health>100:
        health=100

    if happiness<0:
        happiness=0
    if happiness>100:
        happiness=100

    if hungry<0:
        hungry=0
    if hungry>100:
        hungry=100


def fun_timer():
    global timer,hours
    global status
    hours+=1

    everyhourdo()

    if hours >23:
        hours=0
        status=1
    if hours==8 and status==1:
        status=2
    
    timer = threading.Timer(5.0, fun_timer)#5s执行一次fun_timer
    timer.start()

def getstatus():
    record_file = 'record.txt'
    try:
        with open(record_file,'r') as f:
            txt=f.read()
        status_t,hours_t,health_t,hungry_t,happiness_t=txt.split(',')
        status=int(status_t)
        hours=int(hours_t)
        hungry=int(hungry_t)
        health=int(health_t)
        happiness=int(happiness_t)
        newstartflag=0
    except:
        status=random.randint(1,6)
        hours=random.randint(0,23)
        health = random.randint(20, 80)
        hungry = random.randint(20, 80)
        happiness = random.randint(20, 80)
        newstartflag=1
    return status,hours,health,hungry,happiness,newstartflag

def savestatus(staus,hours,health,hungry,happiness,):
    s=str(staus)+','+str(hours)+','+str(health)+','+str(hungry)+','+str(happiness)
    with open(record_file,'w') as f:
        f.write(s)
def greeting():
    s='''
    我的名字叫Tommy，一只可爱的猫咪....
    你可以和我一起散步，玩耍，你也需要给我好吃的东西，带我去看病，也可以让我发呆.....
    Command：
    1.wolk：散步
    2.play：玩耍
    3.feed：喂我
    4.deedoctor：看医生
    5:letalone：让我独自一人
    6.status：查看我的状态
    7.bye：不想见到我
    '''
    print(s)
    see_status()
def see_status():

    global hours
    global health
    global hungry
    global happiness
    global status
    if status==1:
        status_str='我在睡觉.....'
    if status==2:
        status_str='我醒着但很无聊.....'
    if status==3:
        status_str='我在散步.....'
    if status==4:
        status_str='我在玩耍.....'
    if status==5:
        status_str='我在吃饭.....'
    if status==6:
        status_str='我在看医生.....'
    print(status_str)
    print('')
    print('当前时间：%s点'%hours)
    print('我当前状态：%s'%(status_str))
    print('Happiness:  Sad %s Happy(%03d)' % ('*' * (happiness // 2) + '-' * (50 - happiness // 2), happiness))
    print('Hungry:    Full %s Hungry(%03d)' % ('*' * (hungry // 2) + '-' * (50 - hungry // 2), hungry))
    print('Health:    Sick %s Health(%03d)' % ('*' * (health // 2) + '-' * (50 - health // 2), health))


def main():
    global hours
    global health
    global hungry
    global happiness
    global status
    status,hours,health,hungry,happiness,newstartflag=getstatus()

    greeting()

    fun_timer()  #启动定时器
    while True:
        command = input("你想:")
        if command == "status":
            see_status()
        elif command == "bye":
            savestatus(status,hours,health,hungry,happiness)
            print("记得来找我！Bye....")
            timer.cancel()
            break
        elif command=='seedoctor':
            if status==1:
                yesorno=input('你确认要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！（y表示是，其他表示不是）')
                if yesorno!='y':
                    continue
            happiness-=4
            status=6
            print('我在看医生.....')
        elif command == 'walk':
            if status == 1:
                yesorno = input('你确认要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！（y表示是，其他表示不是）')
                if yesorno != 'y':
                    continue
            happiness -= 4
            status = 3
            print('我在散步.....')
        elif command == 'feed':
            if status == 1:
                yesorno = input('你确认要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！（y表示是，其他表示不是）')
                if yesorno != 'y':
                    continue
            happiness -= 4
            status = 5
            print('我在吃饭.....')
        elif command == 'play':
            if status == 1:
                yesorno = input('你确认要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！（y表示是，其他表示不是）')
                if yesorno != 'y':
                    continue
            happiness -= 4
            status = 4
            print('我在玩耍.....')
        else:
            print('我不懂你在说什么')
        if happiness<0:     #happaniess 不能小于0
            happiness=0
if __name__ =="__main__":
    main()

##在使用Python定时器时需要注意如下4个方面：
##（1）定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名，第一个参数表示多长时间后调用后面第二个参数指明的函数。第二个参数注意是函数对象，进行参数传递，用函数名(如fun_timer)表示该对象，不能写成函数执行语句fun_timer()，不然会报错。用type查看下，可以看出两者的区别。
##（2）必须在定时器执行函数内部重复构造定时器，因为定时器构造后只执行1次，必须循环调用。
##（3）定时器间隔单位是秒，可以是浮点数，如5.5，0.02等，在执行函数fun_timer内部和外部中给的值可以不同。
##（4）可以使用cancel停止定时器的工作
