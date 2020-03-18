def get_number_of_boats(dwarfs, limit):
    res = 0
    while len(dwarfs) > 0:
        mx = max(dwarfs)
        mn = min(dwarfs)
        if mx + mn <= limit and len(dwarfs) > 1:
            dwarfs.remove(mn)
        dwarfs.remove(mx)
        res += 1
    return res
    
    
dwarfs = [3,2,2,1,2,2,2]
limit = 4
print(get_number_of_boats( dwarfs, limit ))