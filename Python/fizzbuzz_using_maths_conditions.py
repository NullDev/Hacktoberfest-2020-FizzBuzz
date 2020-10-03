for i in range(1,101):
    if sum(list(map(int,str(i))))%3==0 and str(i)[-1] == '0' or str(i)[-1] == '5': 
        # condition for 3 sum element divided by 3 and last element should be 0 or 5
        print('fizzbuzz')  
    elif sum(list(map(int,str(i))))%3==0:
        # condition for 3 sum element divided by 3 and last element should be 0 or 5
        print('fizz')
    elif str(i)[-1] == '0' or str(i)[-1] == '5' :
        # condition for 3 sum element divided by 3 and last element should be 0 or 5
        print('buzz')
    else:
        print(i)