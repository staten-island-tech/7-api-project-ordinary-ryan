def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("cannot divide by 0")
    else:
        print(result)

divide(10,0)