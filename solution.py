import pandas as pd
import numpy as np

chat_id = 134277149 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    left_interval = (-min(-x) - 1 / 2) / (38**2 / 2)
    right_interval = (-np.log(alpha) / n -min(-x) - 1 / 2) / (38**2 / 2)
    return left_interval, \
           right_interval
