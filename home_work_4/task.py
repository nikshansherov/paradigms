from statistics import mean


def find_r(lst_1, lst_2):
    m_x = mean(lst_1)
    m_y = mean(lst_2)
    numerator = sum(map(lambda x, y: (x - m_x) * (y - m_y), lst_1, lst_2))
    den_1 = sum(map(lambda x: (x - m_x) **2, lst_1))
    den_2 = sum(map(lambda y: (y - m_y) **2, lst_2))
    denominator = (den_1 * den_2) ** 0.5
    return numerator /denominator

lst_1 = [1, 2, 3, 4, 5]
lst_2 = [5, 4, 3, 2, 1]
print(round(find_r(lst_1, lst_2), 2))
