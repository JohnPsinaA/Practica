if __name__ == "__main__":
    # Do not change the line below
    a = b = c = d = None

    # Assign the values of correct types to variables a, b, c, d 
    # to make the script work without errors
    a = 1
    b = 1.1
    c = 1 + 1j
    d = "aboba"
    print(a, b, c, d)
    # Do not change the lines below
    assert isinstance(a, int)
    assert isinstance(b, float)
    assert isinstance(c, complex)
    assert isinstance(d, str)