# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# output is Berry Harry

if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        names.append(input())
        scores.append(float(input()))
    
    scores = list(zip(scores, names))
    scores.sort()
    ans = []
    cur_score = scores[0][0]
    found = False
    i = 1
    while i < len(scores):
      if scores[i][0] != cur_score and not found:
        ans.append(scores[i][1])
        found = True
        cur_score = scores[i][0]
      elif scores[i][0] == cur_score and found:
        ans.append(scores[i][1])
      elif scores[i][0] != cur_score and found:
        break
      
      i += 1
    for n in ans:
      print(n)
          