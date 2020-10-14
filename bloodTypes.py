# Naomi Duggan
# 260910502

donor="a-"
recipient="AB"
expectedOutput=""

if donor=="O-": #donor is O-, prompts for recipient
    if (recipient=="O-" or recipient=="O+" or recipient=="A+" or recipient=="A-" or recipient=="B+" or recipient=="B-" or recipient=="AB-" or recipient=="AB+"):
        expectedOutput="compatible"
    else: 
        expectedOutput="invalid"
elif donor=="O+": #donor is O+, prompts for recipient 
    if (recipient=="O-" or recipient=="A-" or recipient=="B-" or recipient=="AB-"):
        expectedOutput="incompatible"
    elif (recipient=="O+" or recipient=="A+" or recipient=="B+" or recipient=="AB+"):
        expectedOutput= "compatible"
    else: 
        expectedOutput="invalid"
elif donor=="A-": #donor is A-, promtps for recipient 
    if (recipient=="A-" or recipient=="AB-" or recipient=="AB+" or recipient=="A+"):
        expectedOutput="compatible"
    elif (recipient=="B+" or recipient=="B-" or recipient=="O-" or recipient=="O+"):
        expectedOutput="incompatible"
    else: 
        expectedOutput="invalid"
elif donor=="A+": #donor is A+, prompts for recipient 
    if (recipient=="A+" or recipient=="AB+"):
        expectedOutput="compatible"
    elif (recipient=="A-" or recipient=="AB-" or recipient=="B+" or recipient=="B-" or recipient=="O-" or recipient=="O+"):
        expectedOutput="incompatible"
    else: 
        expectedOutput="invalid"
elif donor=="B-": #donor is B-, promtps for recipient 
    if (recipient=="B-" or recipient=="AB-" or recipient=="B+" or recipient=="AB+"): 
        expectedOutput="compatible"
    elif (recipient=="A+" or recipient=="A-" or recipient=="O+" or recipient=="O-"):
        expectedOutput= "incompatible"
    else: 
        expectedOutput="invalid"
elif donor=="B+": #donor is B+, prompts for recipient 
    if (recipient=="B+" or recipient=="AB+"): 
        expectedOutput= "compatible"
    elif (recipient=="B-" or recipient=="AB-" or recipient=="O-" or recipient=="O+" or recipient=="A+" or recipient=="A-"):
        expectedOutput="incompatible"
    else: 
        expectedOutput="invalid"
elif donor=="AB-": #donor is AB-, prompts for recipient 
    if (recipient=="AB-" or recipient=="AB+"):
        expectedOutput= "compatible"
    elif (recipient=="B+" or recipient=="B-" or recipient=="A+" or recipient=="A-" or recipient=="O+" or recipient=="O-"):
        expectedOutput= "incompatible"
    else: 
        expectedOutput= "invalid"
elif donor=="AB+": #donor is AB+, prompts for recipient 
    if recipient=="AB+":
        expectedOutput= "compatible"
    elif (recipient=="AB-" or recipient=="A+" or recipient=="A-" or recipient=="B+" or recipient=="B-" or recipient=="O+" or recipient=="O-"): 
        expectedOutput= "incompatible"
    else: 
        expectedOutput="invalid"
else:
    expectedOutput="invalid"
    
print(expectedOutput) #print the expected output (compatible/incompatible/invalid)
