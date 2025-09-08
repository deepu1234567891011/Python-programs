user=input("Enter a string:").upper()
vowels="aeiou".upper()
vowel_list=[]#for storing vowels enter in string
consonants=[]#for storing consonants in string
vowel_count=0#count the vowels enter in the string
consonant_count=0#count the consonants in the string
for i in user:#loop through each charcter
    if i in vowels:
        vowel_list.append(i)
        vowel_count+=1# increment the count of vowels in the enetr string
    else:
        consonants.append(i)
        consonant_count+=1# increment the count of consonant in the enter string
print("count of vowels in the enetered string is:",vowel_count)
print("vowels are:",vowel_list)
print("count of consonants in the entered string is:",consonant_count)
print("consonants are:",consonants)