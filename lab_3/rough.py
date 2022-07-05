x = y = 'sex'


def abcd():
    global x, y
    x = y = "prochur sex"


if __name__ == '__main__':
    print(x, y)
    abcd()
    print(x, y)