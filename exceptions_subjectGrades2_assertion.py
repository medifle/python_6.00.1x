def getSubjectStats(subject, weights):
    return [[elt[0], elt[1], avg(elt[1], weights)] for elt in subject]

def dotProduct(a,b):
    result = 0.0
    for i in range(len(a)):
        result += convertLetterGrade(a[i])*b[i]
    return result

def avg(grades, weights):
    assert type(weights) == list, 'weights type should be a list'
    assert len(weights) != 0, 'no weights data'
    result = dotProduct(grades, weights)/sum(weights)
    assert 0.0 <= result <= 100.0
    return result
    
def convertLetterGrade(grade):
    if type(grade) == float:
        return grade
    elif grade == 'A':
        return 90.0
    elif grade == 'B':
        return 80.0
    elif grade == 'C':
        return 70.0
    elif grade == 'D':
        return 60.0
    else:
        return 50.0
        
test = [[['fred', 'flintstone'], [10.0, 5.0, 85.0]],
        [['barney', 'rubble'], [10.0, 8.0, 74.0]],
        [['wilma', 'flintstone'], [8.0, 10.0, 96.0]],
        [['dino'], []]]

weights = [.3, .2, .5]


test1 = [[['fred', 'flintstone'], [10.0, 5.0, 85.0, 'D']],
         [['barney', 'rubble'], [10.0, 8.0, 74.0, 'B']],
         [['wilma', 'flintstone'], [8.0, 10.0, 96.0, 'A']],
         [['dino'], []]]

test2 = [[['fred', 'flintstone'], [10.0, 5.0, 8500, 'D']],
         [['barney', 'rubble'], [10.0, 8.0, 74.0, 'B']],
         [['wilma', 'flintstone'], [8.0, 10.0, 96.0, 'A']]]
         
weights1 = [.15, .1, .25, .25]