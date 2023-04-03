import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 134277149 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    mean_x = np.mean(x)
    s = np.sqrt(np.sum((x - mean_x) ** 2) / (n - 1))
    t = norm.ppf(1 - alpha / 2)
    left = mean_x - t * s / np.sqrt(n)
    right = mean_x + t * s / np.sqrt(n)
    return (left, right)
