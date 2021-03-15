def f21(x):
    if x[0] == 'slim':
        if x[3] == 'http':
            if x[2] == 1997:
                if x[1] == 'cmake':
                    return 0
                elif x[1] == 'latte':
                    return 1
            elif x[2] == 2007:
                return 2
            elif x[2] == 1986:
                if x[1] == 'cmake':
                    return 3
                elif x[1] == 'latte':
                    return 4
        elif x[3] == 'css':
            return 5
        elif x[3] == 'ats':
            if x[4] == 1989:
                if x[1] == 'cmake':
                    return 6
                elif x[1] == 'latte':
                    return 7
            elif x[4] == 1976:
                return 8
            elif x[4] == 1996:
                if x[2] == 1997:
                    return 9
                elif x[2] == 2007:
                    return 10
                elif x[2] == 1986:
                    return 11
    elif x[0] == 'hyphy':
        return 12


# print(f21(['slim', 'latte', 1986, 'http', 1976]))
# print(f21(['hyphy', 'cmake', 1997, 'http', 1989]))
