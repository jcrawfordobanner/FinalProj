class KeyBoardController(object):
    """ Handles input for space game """
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Event handler"""
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            #action
        if event.key == pygame.K_RIGHT:
            #action
