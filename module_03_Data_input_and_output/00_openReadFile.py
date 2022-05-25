# 用read()將文件讀入
path = './test.txt'
file = open(path, 'r', encoding='utf-8')
file_str = file.read()
print(file_str)
file.close()

print()

# 用readline()將文件讀入，每次只讀一個row
path = './test.txt'
file = open(path, 'r', encoding='utf-8')
line = file.readline()
row = 0
while line:
    print('第 %s 個 row：'%(row), line)
    line = file.readline()
    row += 1
file.close()

print()

# 用readlines()將文件讀入，產生一個list，list中每個物件皆為一個row的字串
path = './test.txt'
file = open(path, 'r', encoding='utf-8')
lines = file.readlines()
print(lines)
file.close()
