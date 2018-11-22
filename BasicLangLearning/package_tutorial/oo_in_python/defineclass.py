# https: // openhome.cc/Gossip/Python/Class.html

class Score:
    pass

def ScoreWeight(score, weights):
    a = 0
    for i in range(len(score)):
        a += int(score[i])*int(weights[i])
    return a

ss = Score()
ss.a = [1,2]
ws = [2,3]

print(getattr(ss, 'a'))

print(ScoreWeight(ss.a, ws))
