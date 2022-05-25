# 利用with自動關閉文件
path = './test.txt'
with open(path, 'w', encoding='utf-8') as f:
    f.write('利用with自動關閉文件')

with open(path, 'r', encoding='utf-8') as f:
    tmp_str = f.read()

print(tmp_str)

