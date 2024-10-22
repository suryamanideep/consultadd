def JtoI(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        corrected_content = content.replace('J', 'I')
        
        print(corrected_content)
    
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

filename = 'C:\\Users\\manid\\OneDrive\\Desktop\\codes\\consultadd\\level3\\words.txt'

JtoI(filename)
