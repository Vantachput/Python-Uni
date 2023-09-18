while True:
    a,b = map(int, input("Введіть два числа від 1 до 100: ").split())
    if(a <= 0 or a > 100 or b <= 0 or b > 100):
        print("Числа мають бути тільки від 1 до 100")
    else:
        break    
if(a < b):
    print("x = ", b / a + 1)
elif(a == b):
    print("x = ",25)
else:
    print("x = ",(a**3 - 5)/b)
    

