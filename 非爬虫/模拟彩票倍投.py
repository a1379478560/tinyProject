import random
LOOP=25
winMoney = 0  # 总赢钱数，可以负
RATE=[(1,-1),(1.23,6),(1.23,7),(1.23,7),(1.52,6),(1.52,7),(1.52,7),(1.87,6),(1.87,7),(1.87,7),(2.3,6),(2.3,7),(2.83,6),(3.94,6)]
RANK=[0,0,0,0,0,0,0,0] #八条龙层数
class long:
    def __init__(self,name,ya,id):
        self.id=id
        self.win=0     #这条龙总赢的局数
        self.defeat=0   #总输的局数
        self.flag=0     #是否从后面层数补偿完回到第一层
        self.rank = 0  # 处在那一层
        self.winnum = 0  # 已经赢得局数
        self.index = 0  # 第几小局  其实可以用loopnum%3
        self.game3 = [0, 0, 0]  # 三小局的赢输
        self.ya=ya # 三局分别押什么  1大 -1小
        self.name=name
    def checkReset(self):   #返回1代表需要重置这条龙
        if(self.flag==0):
            return 0
        if (self.defeat*7-self.win>=0):
            return 1
        else:
            return 0
    def check(self):
        if(self.index==2):   #如果是第三小局就检查是不是要到下一层
            if(self.game3==[-1,-1,-1]):

                self.defeat+=1
                if(self.rank==13):
                    self.rank=0
                    self.flag+=1
                    print(self.name + "到0层")
                else:
                    self.rank+=1
                    print(self.name + "进一层")
            else:
                self.winnum+=1
                self.win+=1

            if self.flag and self.checkReset():
                self.rank=0  #重置
                self.win=0
                self.defeat=0
                self.flag=0

        if(self.index==2):     #结算一小局
            self.game3=[0,0,0] #1赢 -1输
            self.index=0

        else:
            self.index+=1

        if(self.winnum==RATE[self.rank][1]):  #达到连赢6（7）局就回退一层
            print(self.name,"winnum",self.winnum)
            self.rank-=1
            self.winnum=0
            if(self.rank==0):
                self.flag+=1    #标记这条龙已经重新回到过第一层
            print(self.name+"退一层")

    def loopOne(self,winCode):   #
        self.rank=RANK[self.id]

        if(winCode==self.ya[self.index]):  #判断赢输
            iswin=1
        else:
            iswin=-1

        ya=1
        if(self.index==1 and self.game3[0]!=-1):   #如果是第二局并且第一句赢了的话这句不下注   (第一局一定都会押)
            ya=0
        if(self.index==2 and self.game3[1]!=-1):   #如果是第三局并且第二局赢了的话这句不下注（第一局赢了的话第二局不可能赢肯定是0）
            ya=0
        if(ya):
            self.game3[self.index] = iswin
        xiazhujine=ya*RATE[self.rank][0]*2**self.index*self.ya[self.index]
        self.check()
        RANK[self.id]=self.rank
        return    xiazhujine #返回下注金额   self.ya[self.index] 是押赢还是输 用正负表示，最后在循环里面八条龙虚注相抵

longlist=[]
longlist.append(long("龙1",[1,1,1],0))   #初始化压注顺序  1押大 -1 押小
longlist.append(long("龙2",[1,1,-1],1))
longlist.append(long("龙3",[1,-1,1],2))
longlist.append(long("龙4",[1,-1,-1],3))
longlist.append(long("龙5",[-1,1,1],4))
longlist.append(long("龙6",[-1,1,-1],5))
longlist.append(long("龙7",[-1,-1,1],6))
longlist.append(long("龙8",[-1,-1,-1],7))



lis=[8,3,8,1,3,4,5,9,6,6,3,6,1,4,5,2,5,9,7,3,6,0,6,0,2,9,1,3,0,5,4,9]
for loo in range(len(lis)):
    winNum=random.randint(0,9)
    winNum=lis[loo]
    winCode=1 if winNum>4.5 else -1
    print("第",loo+1,"次")
    print("本次开奖号码：",winNum)

    r1 =longlist[0].loopOne(winCode)
    r2 =longlist[1].loopOne(winCode)
    r3 =longlist[2].loopOne(winCode)
    r4 =longlist[3].loopOne(winCode)
    r5 =longlist[4].loopOne(winCode)
    r6 =longlist[5].loopOne(winCode)
    r7 =longlist[6].loopOne(winCode)
    r8 =longlist[7].loopOne(winCode)

    print("本次下注",round(abs(r1+r2+r3+r4+r5+r6+r7+r8),3))
    winMoney-=abs(r1+r2+r3+r4+r5+r6+r7+r8)
    if(winCode*(r1+r2+r3+r4+r5+r6+r7+r8)>0):
        winMoney+=(r1+r2+r3+r4+r5+r6+r7+r8)*winCode*1.95
    print("总盈亏",round(winMoney,3))
    print("各龙层数",RANK)
    for ii in RANK:
        if(ii>=12):              #交换
            maxindex=RANK.index(ii)
            minindex=RANK.index(min(RANK))
            temp = min(RANK)
            RANK[minindex]=ii
            RANK[maxindex]=temp
            break

    print("--------------------------------------")

