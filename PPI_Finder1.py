# -*- coding:utf-8 -*-
#Find Protein Protein interactions from the 3rd sequencing data of Yeast 2 hybird
#Author:Liangyan Huazhong Agriculture University College of Plant Science and Technology
#Creating:2021/1/8
#modifying:2021/1/9

import sys
txt  = sys.argv[1]
fa = sys.argv[2]
prefix = sys.argv[3]

out_obj1 = open(prefix+"_1.fa","a")
out_obj2 = open(prefix+"_2.fa","a")

fa_obj = open(fa,"r")
sequence = {}
while 1:
    line = fa_obj.readline().strip()
    if line == "":break
    if ">" in line:name = line[1:]
    sequence[name] = fa_obj.readline().strip()
#将fa文件的序列读入一个字典，序列名为索引
fa_obj.close()

txt_obj = open(txt,"r")
read = ""
while 1:
    line = txt_obj.readline().strip()
    if line=="":break
    #为空结束，跳出循环
    if "#" in line:continue
    #注释跳过
    attL = []
    linelist = line.split("\t")
    if read == linelist[0]:continue
    read,qstart,qend = linelist[0],linelist[6],linelist[7]
    read_sequence = sequence[read]
    fa1 = read_sequence[:int(qstart)-1]
    fa2 = read_sequence[int(qend):]
    out_obj1.write(">"+read+"\n"+fa1+"\n")
    out_obj2.write(">"+read+"\n"+fa2+"\n")

txt_obj.close()
out_obj1.close()
out_obj2.close()
