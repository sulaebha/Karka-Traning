for i in range(1,101):
    if i%5==0 and i%3==0:
        print("Fizz Buzz")
        continue
    elif i%3==0:
        print("Fizz")
        continue
    elif i%5==0:
        print("Buzz") 
        continue
    print(i)