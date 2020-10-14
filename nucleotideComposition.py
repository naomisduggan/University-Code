# Naomi Duggan
# 260910502

sequence="AGGCAG"
isNucleotide=False

for index in range(len(sequence)):
    
    if (sequence.count("A")+ sequence.count("C")+ sequence.count("G")+ sequence.count("T"))<len(sequence): 
        isNucleotide=False #if the sum of A, C, G and T in the sequence is lower that the length of the sequence, the sequence is not composed solely of A,C,G and T. Hence, it is not valid 
    if (sequence.count("A")+ sequence.count("C")+ sequence.count("G")+ sequence.count("T"))==len(sequence):
        isNucleotide=True #if the sum of A, C, G and T equals that of the length of the sequence, it is valid


if isNucleotide== True: #if the sequence is valid, we print the number of A, C, G and T found on the string, respectively (separated by a space)
    print(sequence.count("A")," ",sequence.count("C")," ",sequence.count("G")," ",sequence.count("T")) 
else: #if the sequence is not valid, we print 'invalid'
    print("invalid")
