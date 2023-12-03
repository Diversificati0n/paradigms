

from functools import reduce

def mean(values):
    return sum(values) / len(values)

def pearson_correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(x)

    mean_x = mean(x)
    mean_y = mean(y)

    def calc_numerator_denominator(acc, xy):
        xi, yi = xy
        acc["numerator"] += (xi - mean_x) * (yi - mean_y)
        acc["denominator_x"] += (xi - mean_x)**2
        acc["denominator_y"] += (yi - mean_y)**2
        return acc

    result = reduce(calc_numerator_denominator, zip(x, y), {"numerator": 0, "denominator_x": 0, "denominator_y": 0})

    correlation = result["numerator"] / (result["denominator_x"]**0.5 * result["denominator_y"]**0.5)

    return correlation

array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]

correlation = pearson_correlation(array1, array2)
print(f"Корреляция Пирсона: {correlation}")
