import shutil
import sys, os


class ActionManager():
    def __init__(self):
        self.actions = {}

    def add_action(self, c, action):
        self.actions[c.lower()] = action

    def remove_action(self, c):
        del self.actions[c]

    def get_keys(self):
        keys = []
        for key in self.actions:
            keys.append(key)
        return keys

    def get_actions(self):
        acts = []
        for key in self.actions:
            acts.append(self.actions[key])
        return acts

    def dump(self):
        self.actions = {}

    # switches sets of options
    def switch(self, code):
        if code == 'MAIN':
            self.dump()
            self.add_action('Q', 'QUIT')
            self.add_action('N', 'NEW CKT')
            self.add_action('L', 'LOAD CKT')

    def execute(self, action):
        if action in self.actions.values():
            if action == 'QUIT':
                sys.exit()
            if action == 'NEW CKT':
                initialize_ckt(input('Circuit name: '))

# a generic function that prepares a new circuit for building
def initialize_ckt(name):
    # create new directory



# a generic function that prints text to the screen and receives input from the user
# String ActionManager -> Action Code
def prompt_user(display, action_manager):
    print(display)
    for key in action_manager.actions:
        print('%s: %s' % (key, action_manager.actions[key]))
    user_input = input('> ').lower()
    while not(user_input in action_manager.actions):
        print('Error: Input one of the following.')
        for key in action_manager.actions:
            print(action_manager.actions[key])
        user_input = input('> ').lower()
    return user_input
