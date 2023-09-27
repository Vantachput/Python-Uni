from math import sin, radians, pow
def expression():
    a = int(input("Введіть число х(градуси): "))
    y = (1 - 2 * pow(sin(radians(a)),2)) / (1+pow(sin(radians(a)),2))
    print ("Результат потрібного рівняння: ", y)
    return y

def second():
    s = []
    while(True):
        x,y = map(int, input("Введіть два числа x та y(x повинно бути меньше y): ").split())
        if(x >= y):
            continue
        else: break
    for value in range(x,y+1,1):
        if(value % 2 == 0):
            s.append(value)
    for elem in s:
        if(elem == s[0]):
            print("Парні числа від x до y:", elem, end=' ')
        else:
            print(elem, end=' ')
    return s


# expression_ = expression()
# paired_numbers = second()


    
