"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time
from tkinter.tix import X_REGION

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n
        self.binary_vec = list('{0:b}'.format(n))

    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec):
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)

def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y


def quadratic_multiply(x, y):
    xvec = x.binary_vec
    yvec = y.binary_vec
    if len(xvec)<=1 and len(yvec)<=1:
        return x.decimal_val*y.decimal_val
    xvec,yvec=pad(xvec,yvec)
    x_left,x_right = split_number(xvec)
    y_left,y_right = split_number(yvec)
    n=len(xvec)-1
    a = x_left.decimal_val+x_right.decimal_val
    b = y_left.decimal_val+y_right.decimal_val
    mx = BinaryNumber(a)
    my = BinaryNumber(b)
    first = quadratic_multiply(x_left, y_left)
    third = quadratic_multiply(x_right,y_right)
    second = quadratic_multiply(mx, my) - first - third
    return bit_shift(BinaryNumber(2),n).decimal_val*first+bit_shift(BinaryNumber(2),n//2).decimal_val*second+third



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(5)) == 2*5
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
    assert quadratic_multiply(BinaryNumber(1000), BinaryNumber(25)) == 1000*25
    assert quadratic_multiply(BinaryNumber(324), BinaryNumber(456)) == 324*456


def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    assert f(BinaryNumber(x), BinaryNumber(y)) == x*y
    return (time.time() - start)*1000

test_multiply()
print(time_multiply(10000, 10000, quadratic_multiply))
print(time_multiply(100000, 100000, quadratic_multiply))
print(time_multiply(1000000, 10000000, quadratic_multiply))
print(time_multiply(10000000, 100000000, quadratic_multiply))
print(time_multiply(2142657, 214235, quadratic_multiply))
    
    

