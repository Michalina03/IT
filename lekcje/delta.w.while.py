import math
while True:
    print("li8cz a / zamknij b ")
    inp=input().upper()
    if inp == "A":
        a=float(input())
        b=float(input())
        c=float(input())
        delta = b**2 - 4*a*c
        if delta >0:
             x1 = (-b-math.sqrt(delta)/(2*a))
             x2 = (-b+math.sqrt(delta)/(2*a))
             print(f"mam 2 pierwiatki x1={x1}x2={x2}")
        elif delta==0:
             x=-b/2*a 
             print(f"x{x}")
        else:
          print("nie ma pierwiastków")
    elif inp == "B":
        break
    else:
        print("nie ma takiej komendy")
