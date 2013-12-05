# -*- coding: cp936 -*-
import os
import shutil

if not os.path.exists("failure/"):
    os.makedirs("failure/")

            
print "本脚本将自动读取当前目录下的 a.csv 文件"
print "然后根据 a.csv 中的数据对当前文件夹内文件批量重命名"
raw_input("按下回车键开始")

f = open("a.csv", "r")
open("error.txt", "w")
for line in f:
    names = line.split(",")
    n1 = names[0].strip()
    n2 = names[1].strip()
    
    try:
        os.rename(n1, n2)
        print n1, "-->", n2
    except:
        print n1, "  X"
        open("error.txt", "a").write(n1 + "\n")

        try:
            shutil.copyfile(n1, "failure/" + n2)
        except:
            pass

f.close()

raw_input("完成")



