from stanfordkarel import*
def main():
    two_step()
    turn_right()
    two_step()
    put_beeper()
    turn_around()
    for w in range(3):
        seven_step()
    move()

"''the cat is redfkfflllflf;l,flffl'"

def two_step():
    move()
    move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for k in range(2):
        turn_left()

def seven_step():
    for k in range(7):
        move()
    put_beeper()
    turn_left()

if __name__ == "__main__":
    run_karel_program()
