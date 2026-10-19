#Q6
def average(array):
  s = set(array)
  avg = sum(s) / len(s)
  return round(avg, 3)
