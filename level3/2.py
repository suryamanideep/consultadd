def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        
        return line_count
    
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return 0

filename = 'C:\\Users\\manid\\OneDrive\\Desktop\\codes\\consultadd\\level3\\doc.txt'

lines_counted = count_lines_in_file(filename)

print(f"Number of lines in '{filename}': {lines_counted}")
