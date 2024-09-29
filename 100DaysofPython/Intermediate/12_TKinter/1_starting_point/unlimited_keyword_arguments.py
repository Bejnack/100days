def calculate (n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    # for key, value in kwargs:
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(n=2, add=3, multiply=5)