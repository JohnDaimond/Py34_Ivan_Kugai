arr = [54, 32, 11, -11, -21, -39]


def divide(array):
    pol = []
    otr = []
    for i in array:
        if i > 0:
            pol.append(i)
        elif i < 0:
            otr.append(i)
    return pol, otr


pol, otr = divide(arr)
print(f"Положительные:{pol}")
print(f"Отрицательные:{otr}")