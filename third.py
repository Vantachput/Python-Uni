n = int(input("Число від 1 до 9: "))
while(n < 1 or n > 9):
    n = int(input("Число від 1 до 9: ")) 
for i in range(0, n, 1):
    print(" " * i, end = "")
    for j in range(n-i, 0, -1):
        if(j == 1):
            print(j, end='\n')
        else: 
            print(j, end=' ') 
