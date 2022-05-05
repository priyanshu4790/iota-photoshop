colors = ['Blue', 'Yellow', 'Green']

states = ['AndhraPradesh', 'Karnataka', 'TamilNadu', 'Kerala', 'Telangana']

neighbors = {'AndhraPradesh': ['Karnataka', 'TamilNadu', 'Telangana'], 'Karnataka': ['AndhraPradesh', 'TamilNadu', 'Kerala', 'Telangana'],
             'TamilNadu': ['AndhraPradesh', 'Karnataka', 'Kerala'], 'Kerala': ['Karnataka', 'TamilNadu'], 'Telangana': ['Karnataka', 'AndhraPradesh']}

colors_of_states = {}

def check(state, color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if check(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print(colors_of_states)

main()