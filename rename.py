# -*- coding: cp936 -*-
import os
import shutil

if not os.path.exists("failure/"):
    os.makedirs("failure/")

            
print "���ű����Զ���ȡ��ǰĿ¼�µ� a.csv �ļ�"
print "Ȼ����� a.csv �е����ݶԵ�ǰ�ļ������ļ�����������"
raw_input("���»س�����ʼ")

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

raw_input("���")



