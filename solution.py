import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 134277149 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    mean_x = np.mean(x)
    std_x = np.std(x, ddof=1)
    z_alpha_2 = norm.ppf(1 - alpha / 2)
    left_bound = mean_x - z_alpha_2 * std_x / np.sqrt(n)
    right_bound = mean_x + z_alpha_2 * std_x / np.sqrt(n)
    return (left_bound, right_bound)
