# Highthrough-put-Y2H-analysis_NewVersion
This pipeline splits reads using the ATTL recombination sequence.

# ref:Fang Yang, Yingying Lei, Meiling Zhou, Qili Yao, Yichao Han, Xiang Wu, Wanshun Zhong, Chenghang Zhu, Weize Xu, Ran Tao, Xi Chen, Da Lin, Khaista Rahman, Rohit Tyagi, Zeshan Habib, Shaobo Xiao, Dang Wang, Yang Yu, Huanchun Chen, Zhenfang Fu, Gang Cao, Development and application of a recombination-based library versus library high- throughput yeast two-hybrid (RLL-Y2H) screening system, Nucleic Acids Research, Volume 46, Issue 3, 16 February 2018, Page e17, https://doi.org/10.1093/nar/gkx1173

#We generated a pipeline to analyze 3rd sequencing reads to find protein-protein interactions.

# USEAGE:

for i in *.fa;do

name=${i%.fa}

blastn -task blastn-short -query ./${name}.fa -subject ./attL.fa -out ./mapping/${name}.txt -num_threads 1 -outfmt 7 -evalue 1.0e-4 &

done

#Clean reads were mapped to ATTL reconbination sequence in FASTA format to locate the ATTL position in the reads and split the reads.

#Make sure the ATTL reads in FASTA format is in current directory.




python3 PPI_Finder1.py ./mapping/${name}.txt ./${name}.fa ./split/${name}

#Using the python3 script to split the Pacbio 3rd sequencing reads into different file in FASTA format.

#PPI_Finder1.py is avaiable as https://github.com/yannnnLi/Highthrough-put-Y2H-analysis_NewVersion.





makeblastdb -in ../cds/B73_CDS.fa -dbtype nucl -out ../cds/B73 -parse_seqids

#Construct index of sequence alignment





for i in lib*_1.fa;do

name=${i%_*}

blastn -db ../cds/B73 -query ${name}_1.fa -out ${name}_1.txt -evalue 1.0e-4 -num_threads 1 -outfmt 6 -max_target_seqs 1 &

blastn -db ../cds/B73 -query ${name}_2.fa -out ${name}_2.txt -evalue 1.0e-4 -num_threads 1 -outfmt 6 -max_target_seqs 1 &

blastn -task blastn-short -query ${name}_1.fa -subject primer.fa -out ${name}_1_primer.txt -num_threads 1 -outfmt 6 -max_target_seqs 1 -evalue 1.0e-4 &

blastn -task blastn-short -query ${name}_2.fa -subject primer.fa -out ${name}_2_primer.txt -num_threads 1 -outfmt 6 -max_target_seqs 1 -evalue 1.0e-4 &

done

#Split reads were mapped to reference CDS sequence.

#Make sure the primer(AD,BD) reads in FASTA format is in current directory.





for i in libB73*_1.txt;do

name=${i%_*}

python3 PPI_Finder2.py ${name}_1.txt ${name}_1_primer.txt ${name}_2.txt ${name}_2_primer.txt > ${name}_result.txt &

done

#Parsing the mapping result to find protein-protein interactions using python3 script.

#PPI_Finder2.py is avaiable at https://github.com/yannnnLi/Highthrough-put-Y2H-analysis_NewVersion.
