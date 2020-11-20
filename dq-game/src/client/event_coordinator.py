import os
import sys


class EventCoordinator:
    def __init__(self, controller, renderer):
        self.controller = controller
        self.renderer = renderer
        self.current_theme = None

    def on_timeout(self):
        self.renderer.screen_handler.clear_data()
        self.renderer.show_logo()  # TODO: show timeout image or text

    def on_show_instructions(self):
        """
        Gets instructions from server.
        Sends them to the renderer with a ready callback function.
        """
        instructions = self.controller.get_instructions()
        self.renderer.show_instructions_and_confirmation_button(
            instructions, self.controller.ready_up
        )

    def on_choose_theme(self):
        themes = self.controller.get_theme_list()
        self.renderer.select_themes(themes, self.controller.send_client_theme_choices)

    def on_start_first_round(self):
        self.current_theme = self.controller.get_round_theme()
        self.renderer.display_round_theme(self.current_theme)

    def on_answer_question(self):
        current_question = self.controller.get_current_question()
        self.renderer.answer_question(current_question, self.current_theme)
