import copy

board = [['_','_','_'],['_','_','_'],['_','_','_']]
finished = False
ismaxturn = True


def eval(b):
  for i in range(3):
    if b[i][0] == b[i][1] and b[i][0] == b[i][2]:
      if b[i][0] == 'x':
        return 10
      elif b[i][0] == 'o':
        return -10
  
  for i in range(3):
    if b[0][i] == b[1][i] and b[0][i] == b[2][i]:
      if b[0][i] == 'x':
        return 10
      elif b[0][i] == 'o':
        return -10

  if b[0][0] == b[1][1] and b[0][0] == b[2][2]:
    if b[0][0] == 'x':
      return 10
    elif b[0][0] == 'o':
      return -10
  
  if b[0][2] == b[1][1] and b[0][2] == b[2][0]:
    if b[1][1] == 'x':
      return 10
    elif b[1][1] == 'o':
      return -10

  for i in range(3):
    for j in range(3):
      if b[i][j] == '_':
        return None
  
  return 0

def minmax(b, ismaxplayer):
  if ismaxplayer:
    best_val = -1000
    best_ij = [0,0]
    for i in range(3):
      for j in range(3):
        if b[i][j] == '_':
          new_b = copy.deepcopy(b)
          new_b[i][j] = 'x'
          new_val = eval(new_b)
          
          if new_val == None:
            new_val = minmax(new_b, False)[0]
          if new_val > best_val:
            best_val = new_val
            best_ij = [i,j]

  else:
    best_val = 1000
    best_ij = [0,0]
    for i in range(3):
      for j in range(3):
        if b[i][j] == '_':
          new_b = copy.deepcopy(b)
          new_b[i][j] = 'o'
          new_val = eval(new_b)
          if new_val == None:
            new_val = minmax(new_b, True)[0]
          if new_val < best_val:
            best_val = new_val
            best_ij = [i,j]

  return [best_val, best_ij]

def print_b(b):
  print('\n\n\n')
  print(b[0][0], '|', b[0][1], '|', b[0][2], '|')
  print('___________')
  print(b[1][0], '|', b[1][1], '|', b[1][2], '|')
  print('___________')
  print(b[2][0], '|', b[2][1], '|', b[2][2], '|')
  print('\n\n\n')

def get_player_move(b):
  while True:
    i = int(input("What row? "))
    j = int(input("What column? "))
    if b[i][j] == '_':
      return [i,j]
    print('invalid move')


while not finished:
  if ismaxturn:
    ij = get_player_move(board)
    board[ij[0]][ij[1]] = 'x'


  else:
    ij = minmax(board, False)[1]
    board[ij[0]][ij[1]] = 'o'

  if eval(board) != None:
    finished = True

  ismaxturn = not ismaxturn
  print_b(board)
  

if eval(board) == 0:
  print("\nDraw!")
elif eval(board) == 10:
  print("\nYou win!")
else:
  print("\nYou lose!")
