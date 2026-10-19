#Q18 Lists
if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
      command, *args = input().split()
      args = list(map(int, args))

      if command == 'insert':
        lst.insert(args[0], args[1])
      elif command == 'print':
        print(lst)
      elif command == 'remove':
       lst.remove(args[0])
      elif command == 'append':
       lst.append(args[0])
      elif command == 'sort':
        lst.sort()
      elif command == 'pop':
         lst.pop()
      elif command == 'reverse':
        lst.reverse()
