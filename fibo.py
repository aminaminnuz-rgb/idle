n=int(input("Enter a number"))
a,b=0,1
nterm=0
for i in range (1,n+1):
    nterm=a
    print(a,end=' ')
    a,b=b,a+b
print(f'\nThe {n}th number is{nterm}')    


    
    
    
    

