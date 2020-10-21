xmin = 0
xmax = 10
n = 5
y = [4, 6, 6, 4, 4, 5]


def trapezoidal_rule(y):
    change_in_x = ((xmax - xmin) / n)
    size_of_y = len(y)
    result = 0
    for i in range(size_of_y):
        if i != 0 and i != size_of_y - 1:
            result += 2*y[i]
        else:
            result += y[i]
    result *= (change_in_x / 2)
    return result


final_result = trapezoidal_rule(y)
print(final_result)
