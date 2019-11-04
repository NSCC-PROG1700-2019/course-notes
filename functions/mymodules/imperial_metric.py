
def mm_to_cm(mm):
    return mm / 10.0


def in_to_mm(inches):
    return inches * 25.4


def ft_to_in(feet):
    return feet * 12.0


def ft_to_cm(feet):
    inches = ft_to_in(feet)
    mm = in_to_mm(inches)
    return mm_to_cm(mm)


if __name__ == '__main__':
    # test
    ft = 1
    cm = ft_to_cm(ft)
    print(f"{ft}ft = {cm}cm")
    assert round(ft_to_cm(ft), 2) == 30.48