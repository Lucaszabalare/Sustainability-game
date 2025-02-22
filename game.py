import pgzrun
import random

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X,CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["bag","battery","bottle","chips"]

game_over = False
game_complete = False
current_level = 1
animations = []
items = []

def draw():
    global items,game_over,game_complete,current_level
    screen.clear()
    screen.blit("bg",(0,0))
    if game_over:
        display_message("YOU LOST!","Try again next time.")#
    elif game_complete:
        display_message("YOU WON!","Good job!")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)


def make_items(extra_items):
    items_to_create = get_option(extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items
    


def get_option(extra_items):
    items_to_create = ["paper"]
    for i in range(extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option + "img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        item.anchor = ("center","bottom")
        animation = animate(item,duration=duration,on_finished=handle_game_over,y = HEIGHT)
        animations.append(animation)
    
def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global items, current_level, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(main_text,sub_text):
    screen.draw.text(main_text,fontsize = 60,color = "Black",center = CENTER)
    screen.draw.text(sub_text,fontsize = 30, color = "Black",center = (CENTER_X,CENTER_Y + 40))

pgzrun.go()