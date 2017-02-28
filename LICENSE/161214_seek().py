from io import StringIO
f=StringIO()
f.write('hello world!')
#f.seek(0)                 #  stream position() 的位置
s=f.readline()
print(s)
