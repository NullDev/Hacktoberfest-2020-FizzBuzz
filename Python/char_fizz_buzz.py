
char_nums = [chr(i) for i in range(1, 101)]

for char_num in char_nums:
    char_sol = []
    if ord(char_num)%3 == 0:
        char_sol.extend(['f','i','z','z'])
    if ord(char_num)%5 == 0:
        char_sol.extend(['b','u','z','z'])
    
    if not char_sol:
        char_sol = [char_num]
    
    print(char_sol)



