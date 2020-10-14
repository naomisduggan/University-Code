# Naomi Duggan
# 260910502 

#input of sequence and cut site
sequence = "AAAAAAA"
cut_site = "AA"

expectedOutput = sum([
    sequence.startswith(cut_site, i) for i in range(len(sequence))
    ]) #within the length of the sequence, we find the cut_site and count its occurence with overlap

print(expectedOutput) #print the number of times cut_site is found in sequence