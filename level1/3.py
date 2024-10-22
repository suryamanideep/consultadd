arr = [int(i) for i in input("enter 5 subject  marks (out of 100) :").split()]
percentage = (sum(arr)/500)*100
print(percentage,end=" ")
if percentage >= 90:
    print("Grade A")
if percentage < 90 and percentage >= 80:
    print("Grade B")
if percentage < 80 and percentage >= 70:
    print("Grade C")
if percentage < 70 and percentage >= 60:
    print("Grade D")
if percentage < 60 and percentage >= 40:
    print("Grade E")
if percentage < 40:
    print("Grade F")