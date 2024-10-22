def count_vowels(str1):
    vowels = "aeiou"
    count =0
    for i in str1:
        if i in vowels:
            count+=1
    return count

str1 = input("enter string: ")
print(f"total number of vowels in the given String: {count_vowels(str1)}")
