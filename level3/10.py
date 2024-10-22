def count_customers_walked_away(N, S):
    available_computers = N
    walked_away_customers = set()  
    used_computers = set() 

    for customer in S:
        if customer not in used_computers:
           
            if available_computers > 0:
             
                available_computers -= 1
                used_computers.add(customer)
            else:
               
                walked_away_customers.add(customer)
        else:
            
            if customer in used_computers:
                available_computers += 1
                used_computers.remove(customer)

    return len(walked_away_customers)

if __name__ == "__main__":

    N1 = 3
    S1 = "GACCBDDBAGEE"
    print(count_customers_walked_away(N1, S1))  # Output: 1

    N2 = 1
    S2 = "ABCBAC"
    print(count_customers_walked_away(N2, S2))  # Output: 2
