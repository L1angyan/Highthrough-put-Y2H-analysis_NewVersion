# -*- coding:utf-8 -*-
#Find Protein Protein interactions from the 3rd sequencing data of Yeast 2 hybird
#Author:Liangyan Huazhong Agriculture University College of Plant Science and Technology
#Creating:2021/1/16
#modifying:2021/1/18

import pandas as pd
import sys

fa1,primer1,fa2,primer2 = sys.argv[1:5]

fa1 = pd.read_table(fa1,sep="\t",header=None)
fa1 = fa1.iloc[:,[0,1,6,7,8,9]]
fa1.columns = ["read","gene1","read1_start","read1_end","gene1_start","gene1_end"]

primer1 = pd.read_table(primer1,sep="\t",header=None)
primer1 = primer1.iloc[:,[0,1,6,7]]
primer1.columns = ["read","primer1","read1_primer_start","read1_primer_end"]

fa2 = pd.read_table(fa2,sep="\t",header=None)
fa2 = fa2.iloc[:,[0,1,6,7,8,9]]
fa2.columns = ["read","gene2","read2_start","read2_end","gene2_start","gene2_end"]

primer2 = pd.read_table(primer2,sep="\t",header=None)
primer2 = primer2.iloc[:,[0,1,6,7]]
primer2.columns = ["read","primer2","read2_primer_start","read2_primer_end"]

df1 = pd.merge(fa1,primer1,how="inner",on='read')
df2 = pd.merge(fa2,primer2,how="inner",on='read')
df = pd.merge(df1,df2,how="inner",on='read')

for i in range(df.shape[0]):
    line = df.iloc[i,:]
    gene1_position = (line[2]+line[3])/2
    primer1_position = (line[7]+line[8])/2
    gene2_position = (line[10]+line[11])/2
    primer2_position = (line[15]+line[16])/2
    if (gene1_position-primer1_position)*(gene2_position-primer2_position)<0:
        print(line["read"]+"\t"+line["gene1"]+"\t"+str(line["gene1_start"])+'\t'+str(line["gene1_end"])\
              +"\t"+line["gene2"]+"\t"+str(line["gene2_start"])+"\t"+str(line["gene2_end"]))

#df.to_csv("1.txt",sep="\t",index=False)
