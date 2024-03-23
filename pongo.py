from random import choice, random
from turtle import *

from freegames import vector

score1 = 0
score2 = 0

def value(difficulty):
    """Randomly generate value between (-5, -3) or (3, 5)."""
    speed = 3 + random() * 2
    return speed * choice([1, -1]) * (difficulty / 2)

ball = vector(0, 0)
aim = vector(value(1), value(1))
state = {1: 0, 2: 0}
difficulty = 1
rectangle_size = 50  # Tamaño inicial del rectángulo
size_changed = False  # Indica si el tamaño del rectángulo ha cambiado
paused = False  # Indica si el juego está pausado
score = {1: 0, 2: 0}  # Puntuación de los jugadores

def set_difficulty(diff):
    """Set the difficulty level and update the ball's color."""
    global difficulty
    difficulty = diff
    aim.x = value(diff)
    aim.y = value(diff)
    set_ball_color()  

    
def set_ball_color():
    """Set the ball's color based on the difficulty level."""
    if difficulty == 1:
        color('green')
    elif difficulty == 2:
        color('orange')
    elif difficulty == 3:
        color('red')
    else:
        color('white')  


def set_rectangle_size(size_change):
    """Set the size of the rectangle."""
    global rectangle_size, size_changed
    if not size_changed:  # Si el tamaño no ha cambiado aún
        rectangle_size += size_change
        size_changed = True

def reset_rectangle_size():
    """Restaura el tamaño original del rectángulo."""
    global rectangle_size, size_changed
    rectangle_size = 50
    size_changed = False

def toggle_pause():
    """Toggle the pause state of the game."""
    global paused
    paused = not paused

def move(player, change):
    """Move player position by change."""
    if not paused:  # Solo mueve si el juego no está pausado
        new_position = state[player] + change
        # Verifica si la nueva posición está dentro de los límites
        if -200 <= new_position <= 225 - rectangle_size:
            state[player] = new_position

def rectangle(x, y, width, height):
    """Draw rectangle at (x, y) with given width and height."""
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
    
def update_scores():
    """Update and display scores."""
    goto(-185, 157)
    color('Black')
    write(f"Score: {score1}", font=("Arial", 20, "normal"))
    goto(-185, 180)
    write(f"Player 1", font=("Arial", 20, "normal"))
    
    goto(110, 157)
    write(f"Score: {score2}", font=("Arial", 20, "normal"))
    goto(110, 180)
    write(f"Player 2", font=("Arial", 20, "normal"))

def draw():
    """Draw game and move pong ball."""
    global paused
    global score1
    global score2
    
    set_ball_color() 

    
    if not paused:  # Solo dibuja si el juego no está pausado
        clear()
        rectangle(-200, state[1], 10, rectangle_size)
        rectangle(190, state[2], 10, rectangle_size)

        ball.move(aim)
        x = ball.x
        y = ball.y

        up()
        goto(x, y)
        dot(10)
        update()

        if y < -200 or y > 200:
            aim.y = -aim.y

        if x < -185:
            low = state[1]
            high = state[1] + rectangle_size

            if low <= y <= high:
                aim.x = -aim.x
            else:
                paused = True
                score2 += 1
                reset_game()

        if x > 185:
            low = state[2]
            high = state[2] + rectangle_size

            if low <= y <= high:
                aim.x = -aim.x
            else:
                score1 += 1
                print(score1)
                paused = True
                reset_game()
                
    update_scores()

    ontimer(draw, 50)

def reset_game():
    """Reset the game."""
    global ball, aim, paused
    ball = vector(0, 0)
    aim = vector(value(difficulty), value(difficulty))
    paused = False

    # Reset player positions
    state[1] = 0
    state[2] = 0

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'w')
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, -20), 'k')
onkey(lambda: set_difficulty(1), '1')
onkey(lambda: set_difficulty(2), '2')
onkey(lambda: set_difficulty(3), '3')
onkey(lambda: set_rectangle_size(10), '4')  # Aumenta el tamaño del rectángulo
onkey(lambda: set_rectangle_size(-10), '6')  # Reduce el tamaño del rectángulo
onkey(lambda: reset_rectangle_size(), '5')    # Restaura el tamaño original del rectángulo
onkey(toggle_pause, 't')  # Pausa el juego al presionar 't'
draw()
done()