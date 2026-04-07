from act6 import loop, den

# def loop(deno):
#     counter = 0
#     global num

#     while num >= deno:
#         num -= deno
#         counter  += 1

#     return {deno: counter}

# def den():
#     global l, num

#     l.update(loop(1000))
#     l.update(loop(500))
#     l.update(loop(100))
#     l.update(loop(50))
#     l.update(loop(20))
#     l.update(loop(10))
#     l.update(loop(5))
#     l.update(loop(1))

while 1:
    l = {}
    try:
        num = int(input("input amount: "))
    except ValueError:
        print("invalid input. try again")
        continue

    den()

    for k, a in l.items():
        print(f"{k}: {a}")
    iexit = 0
    
    while 1:
        try:
            ans2 = input("Enter More [Y/N]? ").strip().upper()
            
            if ans2 not in ['Y', 'N']:
                raise ValueError("invalid input, try again")
        
            if ans2 == 'N':
                iexit = 1
                break
            elif ans2 == 'Y':
                break

        except ValueError as e:
            print(e)
            continue

    if iexit:
        break
