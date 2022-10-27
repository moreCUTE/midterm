print("how many cookie u got")
cookie = input()
if cookie < "3":
    print("to little cookie")
elif cookie > "10":
    print("U got good amount of cookiwe")
else: 
    print("got too many cookie bruh gimmie sum")

print("---------------------------------------------------")


print("are you jrdi or sith")
w = input()
if w == "jedi":
    print("u get grren lightaber")
elif w == "sith":
    print("u get red lightdbaer")
else:
    print("aint no way bruh u got a breadstick :O")
    
print("---------------------------------------------------")

for i in range (4, 42, 2):
    print(i)
    
print("---------------------------------------------------")
    
j = 100
while j >=50:
    print(j)
    j -= 10

print("---------------------------------------------------")
    
while True:
    print("knock kneock...")
    print("ayo who thereeee")
    choice = input()
    if choice == "orange":
        print("orange you glsd i ditn say banana!!! HEHHEHEHEHHE")
        break
    else:
        print("BANANA")

print("--------------------------------------------------------")

def multiplication(x, y, z):
    a = x*y*z
    return a

print("5 x 7 x 25 = ", multiplication(5,7,25))

print("--------------------------------------------------------")

def SODA(x):
    for h in range(x):
        print(x, "bottle of root bear on the wal...")
        x -= 1
        
print("GUB ME NUMEBRRR: ")
w = int(input())
print(SODA(w))


