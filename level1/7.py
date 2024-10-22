str1 = input("enter first string: ").replace(" ","").lower()
str2 = input("enter second string: ").replace(" ","").lower()
if sorted(str1) == sorted(str2):
    print("yes")
else:
    print("no")