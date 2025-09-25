import turtle
import random

# === Game Settings ===
SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 600
BG_COLOR      = "#439abf"
TITLE         = "Catch The Turtle"

TIMER_START    = 20
MOVE_INTERVAL  = 400       # How often the turtle moves (ms)
SCORE_FONT     = ("Arial", 24, "bold")
TIMER_FONT     = ("Courier", 20, "bold")
TURTLE_SIZE    = (2, 2, 2) # (stretch_wid, stretch_len, outline)

# === Global Variables ===
screen_board  = None
game_turtle   = None
score_turtle  = None
timer_turtle  = None

game_over   = False
score_count = 0
timer       = TIMER_START
x_limit     = 0
y_limit     = 0


def setup_screen():
    """Initializes the game screen and sets window limits."""
    global screen_board, x_limit, y_limit
    screen_board = turtle.Screen()
    screen_board.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen_board.bgcolor(BG_COLOR)
    screen_board.title(TITLE)

    # Calculate boundaries for random turtle movement
    x_limit = screen_board.window_width() / 2 - 30
    y_limit = screen_board.window_height() / 2 - 30


def setup_score_turtle():
    """Creates and positions the turtle that displays the score."""
    global score_turtle
    score_turtle = turtle.Turtle()
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen_board.window_height() / 2
    y = top_height * 0.9
    score_turtle.goto(0, y)
    score_turtle.write(f"Score: {score_count}", align="center", font=SCORE_FONT)


def setup_timer_turtle():
    """Creates and positions the turtle that displays the timer."""
    global timer_turtle
    timer_turtle = turtle.Turtle()
    timer_turtle.hideturtle()
    timer_turtle.penup()

    top_height = screen_board.window_height() / 2
    y = top_height * 0.8
    timer_turtle.goto(0, y)


def setup_game_turtle():
    """Creates the main turtle that the player tries to catch."""
    global game_turtle
    game_turtle = turtle.Turtle()
    game_turtle.shape("turtle")
    game_turtle.color("green")
    game_turtle.turtlesize(*TURTLE_SIZE)
    game_turtle.penup()
    game_turtle.onclick(click_turtle)


def click_turtle(x, y):
    """Handles player clicks on the turtle (increments score)."""
    global score_count
    if game_over:
        return
    score_count += 1
    score_turtle.clear()
    score_turtle.write(f"Score: {score_count}", align="center", font=SCORE_FONT)


def countdown():
    """Runs the countdown timer and ends the game when time is up."""
    global timer, game_over

    if game_over:
        return

    timer_turtle.clear()
    timer_turtle.write(f"Time: {timer}", align="center", font=TIMER_FONT)

    timer -= 1
    if timer >= 0:
        screen_board.ontimer(countdown, 1000)
    else:
        game_over = True
        timer_turtle.clear()
        timer_turtle.write("Game Over!", align="center", font=TIMER_FONT)

        if game_turtle is not None:
            game_turtle.onclick(None)  # Disable further clicks


def move_turtle():
    """Moves the turtle randomly on the screen."""
    if game_over:
        return

    random_x = random.uniform(-x_limit, x_limit)
    random_y = random.uniform(-y_limit, y_limit)
    game_turtle.goto(random_x, random_y)

    screen_board.ontimer(move_turtle, MOVE_INTERVAL)


def main():
    """Main entry point of the game."""
    setup_screen()
    setup_score_turtle()
    setup_timer_turtle()
    setup_game_turtle()

    countdown()
    move_turtle()

    screen_board.mainloop()


if __name__ == "__main__":
    main()
