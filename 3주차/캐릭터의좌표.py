def solution(keyinput, board):
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    def move(index, x, y):
        if index == len(keyinput):
            return [x, y]
        
        key = keyinput[index]
        
        dx, dy = 0, 0
        if key == 'up':
            dy = 1
        elif key == 'down':
            dy = -1
        elif key == 'left':
            dx = -1
        elif key == 'right':
            dx = 1
        
        nx, ny = x + dx, y + dy
        if -max_x <= nx <= max_x and -max_y <= ny <= max_y:
            return move(index + 1, nx, ny)
        else:
            return move(index + 1, x, y)

    return move(0, 0, 0)
