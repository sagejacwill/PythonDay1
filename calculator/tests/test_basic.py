import basic

def test_add():
    assert basic.add(4, 3, 2, 1) == 10.1, "Should be 10.1"
    assert basic.add(30, 20) == 50.0, "Should be 50.0"
    return None

def test_mul():
    assert basic.mul(4, 3, 2) == 25.0, "Should be 25.0"
    return None

def test_div():
    assert basic.div(4, 3) == 1.334, "Should be 1.334"
    return None

def main():
    print("Starting Tests...")
    test_add()
    test_mul()
    test_div()
    print("All TESTS Successful")
    return None

# Namespace Trick
if __name__ == "__main__":
    main()

