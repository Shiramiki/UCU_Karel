from stanfordkarel import*

def main():
    turn_left()
    pick_many_beepers()
    right_turn()
    four_step()
    right_turn()
    pick_many_beepers()
    
def pick_many_beepers():
    vertical_pick()
    horizontal_pick()
    vertical_pick()

def horizontal_pick():
    turn_left()
    four_step()
    turn_left()

def vertical_pick():
    for k in range(4):
        pick_beeper()
        move()
    pick_beeper()

def right_turn():
    for l in range(3):
        turn_left()
    

        
        
def four_step():
    for m in range(4):
        move()
    
    
if __name__ == "__main__":
    run_karel_program()
