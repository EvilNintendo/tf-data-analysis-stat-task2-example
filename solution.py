import pandas as pd
import numpy as np

from scipy.stats import t


chat_id = 134277149 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)  # количество наблюдений

    # вычисляем среднее значение ускорения по каждой машине
    a = 2 * x / 38 ** 2

    # среднее значение ускорения по всей выборке
    a_mean = np.mean(a)

    # стандартная ошибка среднего значения
    std_error = np.std(a, ddof=1) / np.sqrt(n)

    # вычисляем t-критическое значение для выбранного уровня доверия и количества степеней свободы
    t_crit = t.ppf(1 - alpha/2, n-1)

    # вычисляем границы доверительного интервала
    interval = t_crit * std_error

    # находим левую и правую границы интервала
    left_border = a_mean - interval
    right_border = a_mean + interval

    return left_border, right_border
