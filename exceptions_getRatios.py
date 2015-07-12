def getRatios(v1, v2):
    ratios = []
    for index in range(len(v1)):
        try:
            ratios.append(v1[index] / float(v2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('getRatios called with bag arg')
    return ratios