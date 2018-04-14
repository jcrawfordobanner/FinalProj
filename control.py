#Dictates how the player can interact with the model

class MouseController(object):
    """ Handles input for space game """
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Event handler"""
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            s=2
            #action
        if event.key == pygame.K_RIGHT:
            s=1
