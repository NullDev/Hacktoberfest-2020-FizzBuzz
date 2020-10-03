fizz_list = [x for x in range(0,100) if(x % 3 == 0)]
buzz_list = [x for x in range(0,100) if(x % 5 == 0)]

dict_nos = {'fizz': fizz_list, 'buzz': buzz_list}

def find_key(no, dict_nos):
    output = ''
    for k,v in dict_nos.items():
        if no in v:
            output += k
        
    return output

# print(find_key(3, dict_nos))
# print(find_key(4, dict_nos))
# print(find_key(30, dict_nos))
