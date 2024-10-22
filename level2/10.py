def make_stone_piles(n):
    piles = []
    current = 2
    while current<=n:
        piles.append(current)
        current += 2 
    
    return piles

n = int(input("enter number of piles: "))
piles = make_stone_piles(n)
print("Stones in each pile =", piles)