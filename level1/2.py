letters_small = "abcdefghijklmnopqrstuvwxyz"
letters_caps  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
alphabet_count=0
numbers_count=0
string1 = input("enter a String :")
for i in string1:
    if i in letters_small or i in letters_caps:
        alphabet_count+=1
    if i in numbers:
        numbers_count+=1
print(f"Alphabets: {alphabet_count} & Numbers: {numbers_count}")