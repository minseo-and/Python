def frequency(toeicScores) :
    counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for toeicScore in toeicScores:
        counters[toeicScore//100] += 1
    return counters

def max_frequency(counters) :
    max = 0
    scoreBase = 0
    a = len(counters)
    for i in range(a) :
        if max < counters[i] :
            max = counters[i]
            scoreBase = i * 100
    return max

def min_frequency(counters) :
    scoreBase = 0
    a = len(counters)
    min = 11
    for i in range(a) :
        if counters[i] !=0 and min>counters[i] :
            scoreBase = i * 100
            min = counters[i]
    return min

def toeic_avg(toeicScores) :
    sum = 0
    for toeicScore in toeicScores :
        sum += toeicScore

    avg = sum/len(toeicScores)
    return avg

toeicScores = [510, 630, 750, 780, 620, 805, 930, 650, 840, 670]

counters = frequency(toeicScores)
maxCount = max_frequency(counters)

for i in range(len(counters)) :
    if counters[i] == maxCount :
        scoreBase = i * 100
    print("가장 많은 점수대= %d, 빈도수=%d" %(scoreBase, maxCount))

minCount = min_frequency(counters)

for i in range(len(counters)) :
    if counters[i] == minCount :
        scoreBase = i * 100
    print("가장 적은 점수대= %d, 빈도수=%d" % (scoreBase, minCount))
