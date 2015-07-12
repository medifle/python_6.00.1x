def FancyDivide2(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("1")
            
    except Exception, e:
        print (e)
        print 'b'
        print e