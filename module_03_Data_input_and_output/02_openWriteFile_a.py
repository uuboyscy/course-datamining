# 以a模式開啟文件，利用write()將字串寫入文件
path = './test.txt'
tmp_str1 = '在文件結尾插入此字串'
tmp_str2 = '再插入這一段\n'
tmp_str3 = '最後插入這一段'
file = open(path, 'a', encoding='utf-8')
file.write(tmp_str1)
file.write(tmp_str2)
file.write(tmp_str3)
file.close()