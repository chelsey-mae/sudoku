import pygame

class Cell:
    CS=500/9
    pygame.init()
    font=pygame.font.Font(None, 30)
    is_user_input = False

    def __init__(self, row, col, screen, value = 0,cs=500/9):
        self.row = row
        self.col = col
        self.screen = screen
        self.value = value
        self.cs=cs
        self.sketched_value = None
        self.is_user_input = True

    def set_cell_value(self, value):
        self.value = value
        self.is_user_input = True
    def set_sketched_value(self, value):
        self.sketched_value = value
    def draw(self, cell_selected = False):
        #chelsey-mae (check)
        cell_x, cell_y = self.col * self.cs, self.row * self.cs
        pygame.draw.rect(self.screen, "white", (cell_x, cell_y, Cell.CS, Cell.CS)) #cell background
        pygame.draw.rect(self.screen, "red" if cell_selected else "black", (cell_x, cell_y,Cell.CS, Cell.CS), width=1) #cell border
        if self.value != 0: self.screen.blit((src:=Cell.font.render(str(self.value), True, (0,0,0))), (cell_x, cell_y, Cell.CS, Cell.CS)) #draw value in cell
        pygame.font.Font(None, 100)
        if self.sketched_value is not None: self.screen.blit((src:=Cell.font.render(str(self.sketched_value), True, (0,0,0))),(cell_x,cell_y))




class Board:
    def __init__(self, width, height, screen, board):
        self.width,self.height,self.screen,self.board=width,height,screen,board
        self.grid=[[Cell(row,col,self.screen,val) for (col,val) in enumerate(board[row])] for row in range(len(board))]
        self.selected_cell = None

    def draw(self):
        #chelsey-mae (check)
        if self.selected_cell is not None:
            row, col = self.selected_cell
            Cell.draw(self.grid[row][col], False)
        #check if the cell has been selected and pass in whether it has or not to Cell.draw() to determine border color
        for row in range(0,9): [self.grid[row][col].draw(self.selected_cell == (row, col)) for col in range(0,9)]


        #draw thick lines
        for i in range(1, 3): 
            pygame.draw.line(self.screen, color = "black", start_pos= (0,3*Cell.CS*i), end_pos=(self.width, 3*Cell.CS*i), width = 10)
            pygame.draw.line(self.screen, color="black", start_pos= (3*Cell.CS*i, 0), end_pos = (3*Cell.CS*i, self.width), width = 10)

    def select(self, row, col): self.selected_cell = (row, col) if None not in (row,col) else None

    def click(self, x, y): return (int(y // Cell.CS),int(x // Cell.CS)) if 0 < x < self.width and 0 < y < self.width else None
        #if the x, y position of the click is inside the board, the row is the y coordinate // cell size, column is x-coordinate // cell size
        #if the click is outside the board return None


    def clear(self):
        #chelsey-mae (check)
        if self.selected_cell is not None:
            row, col = self.selected_cell
            if self.grid[row][col].is_user_input:
                self.grid[row][col].value = None
                self.grid[row][col].sketched_value = None
                self.grid[row][col].is_user_input = False

    def sketch(self, value):
        #chelsey-mae (check)
        if self.selected_cell is not None:
            row, col = self.selected_cell
            self.grid[row][col].sketched_value = value




# def main():
#     pygame.init()
#
#
#     screen = pygame.display.set_mode((500, 500))
#     board = Board(500, 500, screen, "easy")
#
#     running = True
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 #get x, y coordinates of the click and pass them in to Board.click() to get the corresponding row, col
#                 click_x, click_y = event.pos
#
#                 cell_clicked = board.click(click_x, click_y)
#                 print(cell_clicked)
#
#                 if cell_clicked is not None:
#                 #use cell_clicked to select the cell at row, col
#                     row, col = cell_clicked
#                     board.select(row, col)






#         screen.fill("white")
#
#         board.draw()
#
#         pygame.display.flip()
#
# if __name__ == "__main__":
#     main()
