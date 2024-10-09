from Perceptron1_AND import AND
from Perceptron3_Gates_with_bias import NAND
from Perceptron3_Gates_with_bias import OR

def XOR(x1, x2):        # 0층
    s1 = NAND(x1, x2)   # 1층
    s2 = OR(x1, x2)
    y = AND(s1, s2)     # 2층
    return y

print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))