'''
@author=haohaomeng
Create on monday Decenber 12 21:12
生成优惠码或验证码

'''
from  random import Random

def codegenerater(num,codelength=15):
    print(' generate code ')
    codefile=open('code.txt','wb+')
    char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    if num<1:
        print('invaild input num ')
    else:
        for i in range(1,num+1):
            random=Random()
            str=''
            for it in range(1,codelength+1):
                index=random.randint(1,len(char))
                str+=char[index-1]
            str+='\r\n'
            str=str.encode('utf-8')
            codefile.write(str)
codegenerater(10)


