from main.luhn import luhn


def test_luhn():
    assert luhn("13673252525772") == False
    assert luhn("4539 3195 0343 6467") == True
    assert luhn('584929217191') == True

def test_error()

    