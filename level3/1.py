def get_even_length_words(filename):
    even_length_words = []

    with open(filename, 'r') as file:

        content = file.read()

        words = content.split()
        

        even_length_words = [word for word in words if len(word) % 2 == 0]

    return even_length_words

filename = 'C:\\Users\\manid\\OneDrive\\Desktop\\codes\\consultadd\\level3\\doc.txt'

even_length_content = get_even_length_words(filename)

for line in even_length_content:
    print(line)