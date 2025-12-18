#1
def push_score(score, scores=None):
    if scores == None:
       scores = []
    scores.append(score)
    return scores
#2
print(push_score("сделать дз"))
print(push_score("приготовить"))
#print(scores)
#3
def top_scores(scores, n=3):
    if scores in n:
       return max(n)
