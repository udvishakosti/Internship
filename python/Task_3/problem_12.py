#Q12 Intro to sets
def average(array):
  s = set(array)
  avg = sum(s) / len(s)
  return round(avg, 3)
