author='menghaohao'

# stringio测试

# from io import StringIO
# from datetime import datetime
# with open("F://test1.txt", 'w',encoding="utf-8") as data1:
#content = str(open("F://test.txt").read(), 'gbk').encode('utf8')
    # data1.write("我的大学")
    # data1.write(datetime.now().strftime('%Y-%m-%d'))
    #for oneLine in data1:
    #   print(oneLine)
from io import StringIO
with open('F://test3.txt','w',encoding='utf-8') as f:
    for i in range(10):
        f.write(str(i)+'\n')
print('haohao')
with open('F://test2.txt','r') as f:
    print(f.readlines())