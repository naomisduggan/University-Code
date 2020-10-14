# Naomi Duggan
# 260910502

mRNA = "AUGAUGAUGAUGAUGUGAUGAUGAUGA"
length=0
for i in range(0,len(mRNA)):
    if mRNA[i:i+3]=="AUG" and length==0: #we first find AUG within the sequence and begin counting 
        for j in range(i+3,len(mRNA),3): #we count every third step, beginning at AUG
            if mRNA[j:j+3]=="UGA" or mRNA[j:j+3]=="UAA" or mRNA[j:j+3]=="UAG": #we stop counting when we reach a UAA, UAG or UGA codon
                if length==0: 
                    length = (j-i)/3 #count the difference in length between the end of the mRNA sequence and from beginning of string to AUG , divided by 3 which finds the number of codons within the string 

print(int(length))
        
