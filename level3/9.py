def run_length_encode(input_str):
    if not input_str: 
        return ""
    
    encoded_str = ""
    count = 1  
    current_char = input_str[0]

    for i in range(1, len(input_str)):
        if input_str[i] == current_char:
            count += 1 
        else:
          
            encoded_str += f"{current_char}{count}"
            current_char = input_str[i] 
            count = 1  

    encoded_str += f"{current_char}{count}"

    return encoded_str

input_str = "wwwwaaadebbbbbw"
output_str = run_length_encode(input_str)
print(output_str) 
