def outer():
    x = "outer value"
    print("Outer:", x)
    def inner():
        nonlocal x  # refers to outer variable
        x = "modified by inner"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
