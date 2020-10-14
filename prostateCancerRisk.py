# Naomi Duggan
# 260910502

history = "No"
european = "Yes"
copy_number = 1
haplotype = "AA"

riskLevel= ""

if history == "Yes" : #Input is yes for genetic history for prostate cancer
    if european == "Yes" : #Input is Yes for European Ancestry, prompts for CYPA4 haplotype
        if (haplotype== "GA" or haplotype =="AG" or haplotype =="GG"):
            riskLevel = "high risk"
        elif haplotype == "AA":
            riskLevel = "low risk"
        else: 
            riskLevel = "invalid"    
    elif european == "No": #Input is No for European Ancestry, prompts for AR_GCC copy number 
        if copy_number < 16 and copy_number > 0 :
            riskLevel = "high risk"
        elif copy_number >= 16:
            riskLevel = "medium risk"
        else:
            riskLevel = "invalid"
    elif european == "Mixed": #Input is Mixed for European Ancestry, prompts for AR_GCC copy number
        if copy_number < 16 and copy_number > 0 :
            #prompts for CYP3A4 haplotype for copy_number < 16
            if (haplotype =="GA" or haplotype =="AG" or haplotype =="GG"):
                riskLevel = "high risk"
            elif haplotype == "AA":
                riskLevel = "medium risk"
            else: 
                print("Invalid entry")
        elif copy_number >= 16: #prompts for CYP3A4 haplotype for copy_number >= 16
            if (haplotype=="GA" or haplotype =="AG" or haplotype =="GG"):
                riskLevel = "high risk"
            elif haplotype == "AA":
                riskLevel = "medium risk"
            else: 
                riskLevel = "invalid"
        else: 
            riskLevel = "invalid"
    else:
        riskLevel = "invalid"
        
elif history == "No":
    riskLevel = "low risk"

else:
    riskLevel = "invalid"

print(riskLevel) #print the risk level


        