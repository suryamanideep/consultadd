def parse_encoded_string(encoded_str):

    parts = encoded_str.split('0')
    
    filtered_parts = [part for part in parts if part] 
    
    if len(filtered_parts) >= 3:
        first_name = filtered_parts[0]
        last_name = filtered_parts[1]
        id_value = filtered_parts[2]
    else:
        raise ValueError("Input string does not contain enough information.")
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_value
    }

# Example usage
input_str = "Robert000Smith000123"
output_dict = parse_encoded_string(input_str)
print(output_dict) 
