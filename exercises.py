class Game():
  board = {
  'a1': None, 'b1': None, 'c1': None,
  'a2': None, 'b2': None, 'c2': None,
  'a3': None, 'b3': None, 'c3': None,
}
  def __init__(self , turn='X' , tie=False , winner=None ):
    self.turn = turn
    self.tie = tie
    self.winner = winner
    

  def print_board(self):
    b= self.board 
    print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)     
  def print_message(self):
    ## If there is a tie: print("Tie game!")
    if self.tie:
      print("Tie game!")
    ## If there is a winner: print(f"{self.winner} wins the game!")
    elif self.winner:
      print(f"{self.winner} wins the game!")
    ## Otherwise: print(f"It's player {self.turn}'s turn!")
    else:
      print(f"It's player {self.turn}'s turn!")
      
      
  def render(self):
    # Call upon print_board
    self.print_board()
    ## Call upon print_message
    self.print_message()
    
    
  def get_move(self):
    while True :
      move = input(f"Enter a valid movie (example: A1): ").lower()
      if move in self.board and self.board[move] == None:
        return move
      elif (self.winner !=None):
        exit()
      
      
  def check_winner(self):
    b = self.board
    for player in ['X', 'O']:
      if (b['a1'] == b['b1'] == b['c1'] == player or
          b['a2'] == b['b2'] == b['c2'] == player or
          b['a3'] == b['b3'] == b['c3'] == player or
          b['a1'] == b['a2'] == b['a3'] == player or
          b['b1'] == b['b2'] == b['b3'] == player or
          b['c1'] == b['c2'] == b['c3'] == player or
          b['a1'] == b['b2'] == b['c3'] == player or
          b['a3'] == b['b2'] == b['c1'] == player):
          self.winner = player
          
   
          
        
  def check_tie(self):
      if all(self.board.values()):
        self.tie = True
         
        
  
  def update_board(self):
    move = self.get_move()
    self.board[move]=self.turn
    self.check_winner()
    self.check_tie()
    if self.turn == 'X':
      self.turn = 'O'
    else:
      self.turn = 'X'
 
       
      
  def play_game(self):
    print("Shall we play a game?")
    while self.winner == None and self.tie == False:
      self.render()
      self.update_board()
      self.check_winner()
      self.check_tie()
    self.render()  
    
 
      
    
    
game_instance = Game()
game_instance.play_game()