import os
 #        按文件名查找  并输出文件的绝对路径
# def str_search(file_name, dirname=os.path.abspath('.')):
#     for x, y, z in os.walk(dirname):     ## os.walk()  下  x, y, z 分别代表的对象
#         print(x)
#         print(y)
#         print(z)
#         print('abc')
#         for n in z:
#             if n.find(file_name) >= 0:
#                 print('\n'+os.path.join(x, n))
#
# if __name__ == '__main__':
#     file_name = input('Please enter the name or keyword of a file: ')
#     str_search(file_name)


import os

def dirlist():
    if input('请输入你的命令： \n')=='dir -1':
        for x in os.listdir('.'):
            if os.path.isfile(x):
                print(os.path.join(os.path.abspath('.'),x+'\n'))
    else:
        print('输入命令错误！')
if __name__=='__main__':
    dirlist()

