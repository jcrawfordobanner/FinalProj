class MouseController(object):
    """ Handles input for space game """
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Event handler"""
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            itemC = self.model.get_clicked(pos)
            msg = self.model.messages.get(itemC)
            self.model.update(pos, msg)

        if event.type != KEYDOWN:
            return
