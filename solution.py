import pandas as pd
import numpy as np

from scipy.stats import t


chat_id = 134277149 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)  # количество наблюдений
    
    # вычисляем t-критическое значение для выбранного уровня доверия и количества степеней свободы
    t_crit1 = t.ppf((1 - alpha)/2, n-1)
    t_crit2 = t.ppf((1 + alpha)/2, n-1)

    # находим левую и правую границы интервала
    left_border = 2/(38**2) * (((t_crit1 + np.sum(x))/n) - 1/2)
    right_border = 2/(38**2) * (((t_crit2 + np.sum(x))/n) - 1/2)

    return left_border, right_border
