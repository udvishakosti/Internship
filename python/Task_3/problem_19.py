#Q19 Collections.counter()
from collections import Counter

if __name__ == '__main__':
  num_shoes = int(input())
  shoe_sizes = list(map(int, input().split()))
  num_customers = int(input())
  inventory = Counter(shoe_sizes)
  total_earnings = 0

  for _ in range(num_customers):
    size, price = map(int, input().split())
    
    if inventory[size] > 0:
      inventory[size] -= 1  
      total_earnings += price 
  print(total_earnings)
