# 以w模式開啟文件，利用write()將字串寫入文件
path = './test.txt'
tmp_str = '將此字串寫入文件中'
file = open(path, 'w', encoding='utf-8')
file.write(tmp_str)
file.close()

