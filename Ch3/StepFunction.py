import numpy as np

def step_function(x): # 넘파이 배열을 넣을 수 없는 계단 함수
    if x > 0:
        return 1
    else:
        return 0

def step_function2(x):
    y = x > 0
    return y.astype(np.int_)