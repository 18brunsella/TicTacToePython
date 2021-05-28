import arcade

# Set constants for the screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


class StartView(arcade.View):
    """ Start View Class. """
    def on_show(self):
        arcade.set_background_color(arcade.color.COSMIC_LATTE)
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("TIC TAC TOE", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, arcade.color.BLACK_OLIVE,
                         font_size=50, anchor_x="center")
        arcade.draw_text("Single Player (Press the S Key)", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK_OLIVE, font_size=30, anchor_x="center")
        arcade.draw_text("Two Player (Press the T Key)", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100,
                         arcade.color.BLACK_OLIVE, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.S:
            game_view = TicTacToeGame(True)
            self.window.show_view(game_view)
        elif key == arcade.key.T:
            game_view = TicTacToeGame()
            self.window.show_view(game_view)


class TicTacToeGame(arcade.View):
    """ Main application class. """

    def __init__(self, single=False):
        """ Game Constructor """
        super().__init__()

        self.single = single
        self.board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.game_over = False
        self.turn = 'X'

        arcade.set_background_color(arcade.color.COSMIC_LATTE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_line(375, 525, 375, 100, arcade.color.BLACK)
        arcade.draw_line(575, 525, 575, 100, arcade.color.BLACK)
        arcade.draw_line(200, 385, 750, 385, arcade.color.BLACK)
        arcade.draw_line(200, 225, 750, 225, arcade.color.BLACK)

        arcade.draw_text("Press Esc to Pause", 925, 575, arcade.color.BLACK_OLIVE, font_size=15, anchor_x="center")

        for loc in self.board_state:
            if loc == 'X':
                if self.board_state[0] == "X":
                    arcade.draw_line(210, 520, 365, 395, arcade.color.BLACK)
                    arcade.draw_line(210, 395, 365, 520, arcade.color.BLACK)
                if self.board_state[1] == "X":
                    arcade.draw_line(385, 520, 565, 395, arcade.color.BLACK)
                    arcade.draw_line(385, 395, 565, 520, arcade.color.BLACK)
                if self.board_state[2] == "X":
                    arcade.draw_line(585, 520, 740, 395, arcade.color.BLACK)
                    arcade.draw_line(585, 395, 740, 520, arcade.color.BLACK)
                if self.board_state[3] == "X":
                    arcade.draw_line(210, 375, 365, 230, arcade.color.BLACK)
                    arcade.draw_line(210, 230, 365, 375, arcade.color.BLACK)
                if self.board_state[4] == "X":
                    arcade.draw_line(385, 375, 565, 230, arcade.color.BLACK)
                    arcade.draw_line(385, 230, 565, 375, arcade.color.BLACK)
                if self.board_state[5] == "X":
                    arcade.draw_line(585, 375, 740, 230, arcade.color.BLACK)
                    arcade.draw_line(585, 230, 740, 375, arcade.color.BLACK)
                if self.board_state[6] == "X":
                    arcade.draw_line(210, 220, 365, 125, arcade.color.BLACK)
                    arcade.draw_line(210, 125, 365, 220, arcade.color.BLACK)
                if self.board_state[7] == "X":
                    arcade.draw_line(385, 220, 565, 125, arcade.color.BLACK)
                    arcade.draw_line(385, 125, 565, 220, arcade.color.BLACK)
                if self.board_state[8] == "X":
                    arcade.draw_line(585, 220, 740, 125, arcade.color.BLACK)
                    arcade.draw_line(585, 125, 740, 220, arcade.color.BLACK)
            elif loc == 'O':
                if self.board_state[0] == "O":
                    arcade.draw_circle_outline(285, 470, 60, arcade.color.BLACK_OLIVE, 2)
                if self.board_state[1] == "O":
                    arcade.draw_circle_outline(475, 470, 60, arcade.color.BLACK_OLIVE, 2)
                if self.board_state[2] == "O":
                    arcade.draw_circle_outline(650, 470, 60, arcade.color.BLACK_OLIVE, 2)
                if self.board_state[3] == "O":
                    arcade.draw_circle_outline(285, 300, 60, arcade.color.BLACK_OLIVE, 2)
                if self.board_state[4] == "O":
                    arcade.draw_circle_outline(475, 300, 60, arcade.color.BLACK_OLIVE, 2)
                if self.board_state[5] == "O":
                    arcade.draw_circle_outline(650, 300, 60, arcade.color.BLACK_OLIVE, 2)
                if self.board_state[6] == "O":
                    arcade.draw_circle_outline(285, 155, 60, arcade.color.BLACK_OLIVE, 2)
                if self.board_state[7] == "O":
                    arcade.draw_circle_outline(475, 155, 60, arcade.color.BLACK_OLIVE, 2)
                if self.board_state[8] == "O":
                    arcade.draw_circle_outline(650, 155, 60, arcade.color.BLACK_OLIVE, 2)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            pause_view = PauseView(self)
            self.window.show_view(pause_view)

    def on_mouse_press(self, x, y, _button, _modifiers):
        # Check the click pressed location
        valid_move = self.place_move(x, y)

        if self.single:
            self.place_cpu_move()
        elif valid_move:
            if self.turn == 'O':
                self.turn = 'X'
            elif self.turn == 'X':
                self.turn = 'O'

        if_win = self.check_win()
        if self.single:
            if if_win == 'O':
                if_win = 'CPU'

        if if_win == 'X' and not self.single:
            win_view = WinView('X', False)
            self.window.show_view(win_view)
        elif if_win == 'O' and not self.single:
            win_view = WinView('O', False)
            self.window.show_view(win_view)
        elif if_win == 'CPU' and self.single:
            win_view = WinView('CPU', True)
            self.window.show_view(win_view)
        elif if_win == 'X' and self.single:
            win_view = WinView('X', True)
            self.window.show_view(win_view)
        elif if_win == 'Tie' and self.single:
            win_view = WinView('Tie', True)
            self.window.show_view(win_view)
        elif if_win == 'Tie' and not self.single:
            win_view = WinView('Tie', False)
            self.window.show_view(win_view)

    def place_move(self, x, y):
        if 200 <= x <= 375:
            if 385 <= y <= 525:
                if self.board_state[0] != 'O' and self.board_state[0] != 'X':
                    self.board_state[0] = self.turn
                    return True
            elif 225 <= y <= 385:
                if self.board_state[3] != 'O' and self.board_state[3] != 'X':
                    self.board_state[3] = self.turn
                    return True
            elif 100 <= y <= 225:
                if self.board_state[6] != 'O' and self.board_state[6] != 'X':
                    self.board_state[6] = self.turn
                    return True
        elif 375 <= x <= 575:
            if 385 <= y <= 525:
                if self.board_state[1] != 'O' and self.board_state[1] != 'X':
                    self.board_state[1] = self.turn
                    return True
            elif 225 <= y <= 385:
                if self.board_state[4] != 'O' and self.board_state[4] != 'X':
                    self.board_state[4] = self.turn
                    return True
            elif 100 <= y <= 225:
                if self.board_state[7] != 'O' and self.board_state[7] != 'X':
                    self.board_state[7] = self.turn
                    return True
        elif 575 <= x <= 750:
            if 385 <= y <= 525:
                if self.board_state[2] != 'O' and self.board_state[2] != 'X':
                    self.board_state[2] = self.turn
                    return True
            elif 225 <= y <= 385:
                if self.board_state[5] != 'O' and self.board_state[5] != 'X':
                    self.board_state[5] = self.turn
                    return True
            elif 100 <= y <= 225:
                if self.board_state[8] != 'O' and self.board_state[8] != 'X':
                    self.board_state[8] = self.turn
                    return True

        return False

    def place_cpu_move(self):
        # Checks if the CPU has a winning chance
        if self.board_state[0] == 'O' and self.board_state[1] == 'O' and self.board_state[2] != 'X':
            self.board_state[2] = 'O'
            return
        if self.board_state[1] == 'O' and self.board_state[2] == 'O' and self.board_state[0] != 'X':
            self.board_state[0] = 'O'
            return
        if self.board_state[0] == 'O' and self.board_state[2] == 'O' and self.board_state[1] != 'X':
            self.board_state[1] = 'O'
            return
        if self.board_state[3] == 'O' and self.board_state[4] == 'O' and self.board_state[5] != 'X':
            self.board_state[5] = 'O'
            return
        if self.board_state[4] == 'O' and self.board_state[5] == 'O' and self.board_state[3] != 'X':
            self.board_state[3] = 'O'
            return
        if self.board_state[3] == 'O' and self.board_state[5] == 'O' and self.board_state[4] != 'X':
            self.board_state[4] = 'O'
            return
        if self.board_state[6] == 'O' and self.board_state[7] == 'O' and self.board_state[8] != 'X':
            self.board_state[8] = 'O'
            return
        if self.board_state[7] == 'O' and self.board_state[8] == 'O' and self.board_state[6] != 'X':
            self.board_state[6] = 'O'
            return
        if self.board_state[6] == 'O' and self.board_state[8] == 'O' and self.board_state[7] != 'X':
            self.board_state[7] = 'O'
            return

        if self.board_state[0] == 'O' and self.board_state[3] == 'O' and self.board_state[6] != 'X':
            self.board_state[6] = 'O'
            return
        if self.board_state[3] == 'O' and self.board_state[6] == 'O' and self.board_state[0] != 'X':
            self.board_state[0] = 'O'
            return
        if self.board_state[0] == 'O' and self.board_state[6] == 'O' and self.board_state[3] != 'X':
            self.board_state[3] = 'O'
            return
        if self.board_state[1] == 'O' and self.board_state[4] == 'O' and self.board_state[7] != 'X':
            self.board_state[7] = 'O'
            return
        if self.board_state[4] == 'O' and self.board_state[7] == 'O' and self.board_state[1] != 'X':
            self.board_state[1] = 'O'
            return
        if self.board_state[1] == 'O' and self.board_state[7] == 'O' and self.board_state[4] != 'X':
            self.board_state[4] = 'O'
            return
        if self.board_state[2] == 'O' and self.board_state[5] == 'O' and self.board_state[8] != 'X':
            self.board_state[8] = 'O'
            return
        if self.board_state[5] == 'O' and self.board_state[8] == 'O' and self.board_state[2] != 'X':
            self.board_state[2] = 'O'
            return
        if self.board_state[2] == 'O' and self.board_state[8] == 'O' and self.board_state[5] != 'X':
            self.board_state[5] = 'O'
            return

        if self.board_state[0] == 'O' and self.board_state[4] == 'O' and self.board_state[8] != 'X':
            self.board_state[8] = 'O'
            return
        if self.board_state[0] == 'O' and self.board_state[8] == 'O' and self.board_state[4] != 'X':
            self.board_state[4] = 'O'
            return
        if self.board_state[8] == 'O' and self.board_state[4] == 'O' and self.board_state[0] != 'X':
            self.board_state[0] = 'O'
            return

        if self.board_state[2] == 'O' and self.board_state[4] == 'O' and self.board_state[6] != 'X':
            self.board_state[6] = 'O'
            return
        if self.board_state[4] == 'O' and self.board_state[6] == 'O' and self.board_state[2] != 'X':
            self.board_state[2] = 'O'
            return
        if self.board_state[2] == 'O' and self.board_state[6] == 'O' and self.board_state[4] != 'X':
            self.board_state[4] = 'O'
            return

        # CPU checks if there are any reaches
        if self.board_state[0] == 'X' and self.board_state[1] == 'X' and self.board_state[2] != 'O':
            if self.board_state[2] != 'X':
                self.board_state[2] = 'O'
                return
        if self.board_state[0] == 'X' and self.board_state[2] == 'X' and self.board_state[1] != 'O':
            if self.board_state[1] != 'X':
                self.board_state[1] = 'O'
                return
        if self.board_state[1] == 'X' and self.board_state[2] == 'X' and self.board_state[0] != 'O':
            if self.board_state[0] != 'X':
                self.board_state[0] = 'O'
                return
        if self.board_state[3] == 'X' and self.board_state[4] == 'X' and self.board_state[5] != 'O':
            if self.board_state[5] != 'X':
                self.board_state[5] = 'O'
                return
        if self.board_state[4] == 'X' and self.board_state[5] == 'X' and self.board_state[3] != 'O':
            if self.board_state[3] != 'X':
                self.board_state[3] = 'O'
                return
        if self.board_state[3] == 'X' and self.board_state[5] == 'X' and self.board_state[4] != 'O':
            if self.board_state[4] != 'X':
                self.board_state[4] = 'O'
                return
        if self.board_state[6] == 'X' and self.board_state[7] == 'X' and self.board_state[8] != 'O':
            if self.board_state[8] != 'X':
                self.board_state[8] = 'O'
                return
        if self.board_state[7] == 'X' and self.board_state[8] == 'X' and self.board_state[6] != 'O':
            if self.board_state[6] != 'X':
                self.board_state[6] = 'O'
                return
        if self.board_state[6] == 'X' and self.board_state[8] == 'X' and self.board_state[7] != 'O':
            if self.board_state[7] != 'X':
                self.board_state[7] = 'O'
                return

        if self.board_state[0] == 'X' and self.board_state[3] == 'X' and self.board_state[6] != 'O':
            if self.board_state[6] != 'X':
                self.board_state[6] = 'O'
                return
        if self.board_state[3] == 'X' and self.board_state[6] == 'X' and self.board_state[0] != 'O':
            if self.board_state[0] != 'X':
                self.board_state[0] = 'O'
                return
        if self.board_state[0] == 'X' and self.board_state[6] == 'X' and self.board_state[3] != 'O':
            if self.board_state[3] != 'X':
                self.board_state[3] = 'O'
                return
        if self.board_state[1] == 'X' and self.board_state[4] == 'X' and self.board_state[7] != 'O':
            if self.board_state[7] != 'X':
                self.board_state[7] = 'O'
                return
        if self.board_state[4] == 'X' and self.board_state[7] == 'X' and self.board_state[1] != 'O':
            if self.board_state[1] != 'X':
                self.board_state[1] = 'O'
                return
        if self.board_state[1] == 'X' and self.board_state[7] == 'X' and self.board_state[4] != 'O':
            if self.board_state[4] != 'X':
                self.board_state[4] = 'O'
                return
        if self.board_state[2] == 'X' and self.board_state[5] == 'X' and self.board_state[8] != 'O':
            if self.board_state[8] != 'X':
                self.board_state[8] = 'O'
                return
        if self.board_state[5] == 'X' and self.board_state[8] == 'X' and self.board_state[2] != 'O':
            if self.board_state[2] != 'X':
                self.board_state[2] = 'O'
                return
        if self.board_state[2] == 'X' and self.board_state[8] == 'X' and self.board_state[5] != 'O':
            if self.board_state[5] != 'X':
                self.board_state[5] = 'O'
                return

        if self.board_state[0] == 'X' and self.board_state[4] == 'X' and self.board_state[8] != 'O':
            if self.board_state[8] != 'X':
                self.board_state[8] = 'O'
                return
        if self.board_state[0] == 'X' and self.board_state[8] == 'X' and self.board_state[4] != 'O':
            if self.board_state[4] != 'X':
                self.board_state[4] = 'O'
                return
        if self.board_state[8] == 'X' and self.board_state[4] == 'X' and self.board_state[0] != 'O':
            if self.board_state[0] != 'X':
                self.board_state[0] = 'O'
                return

        if self.board_state[2] == 'X' and self.board_state[4] == 'X' and self.board_state[6] != 'O':
            if self.board_state[6] != 'X':
                self.board_state[6] = 'O'
                return
        if self.board_state[4] == 'X' and self.board_state[6] == 'X' and self.board_state[2] != 'O':
            if self.board_state[2] != 'X':
                self.board_state[2] = 'O'
                return
        if self.board_state[2] == 'X' and self.board_state[6] == 'X' and self.board_state[4] != 'O':
            if self.board_state[4] != 'X':
                self.board_state[4] = 'O'
                return

        if self.board_state[0] == 'X' or self.board_state[2] == 'X' or self.board_state[6] == 'X' or \
                self.board_state[8] == 'X':
            if self.board_state[4] != 'X' and self.board_state[4] != 'O':
                self.board_state[4] = 'O'
                return

        for i in range(len(self.board_state)):
            if self.board_state[i] == 0:
                self.board_state[i] = 'O'
                return

    def check_win(self):
        # Check Column
        if self.board_state[0] == 'X' and self.board_state[3] == 'X' and self.board_state[6] == 'X':
            return 'X'
        if self.board_state[0] == 'O' and self.board_state[3] == 'O' and self.board_state[6] == 'O':
            return 'O'
        if self.board_state[1] == 'X' and self.board_state[4] == 'X' and self.board_state[7] == 'X':
            return 'X'
        if self.board_state[1] == 'O' and self.board_state[4] == 'O' and self.board_state[7] == 'O':
            return 'O'
        if self.board_state[2] == 'X' and self.board_state[5] == 'X' and self.board_state[8] == 'X':
            return 'X'
        if self.board_state[2] == 'O' and self.board_state[5] == 'O' and self.board_state[8] == 'O':
            return 'O'

        # Check Row
        if self.board_state[0] == 'X' and self.board_state[1] == 'X' and self.board_state[2] == 'X':
            return 'X'
        if self.board_state[0] == 'O' and self.board_state[1] == 'O' and self.board_state[2] == 'O':
            return 'O'
        if self.board_state[3] == 'O' and self.board_state[4] == 'O' and self.board_state[5] == 'O':
            return 'O'
        if self.board_state[3] == 'X' and self.board_state[4] == 'X' and self.board_state[5] == 'X':
            return 'X'
        if self.board_state[6] == 'X' and self.board_state[7] == 'X' and self.board_state[8] == 'X':
            return 'X'
        if self.board_state[6] == 'O' and self.board_state[7] == 'O' and self.board_state[8] == 'O':
            return 'O'

        # Check Diagonal
        if self.board_state[0] == 'X' and self.board_state[4] == 'X' and self.board_state[8] == 'X':
            return 'X'
        if self.board_state[0] == 'O' and self.board_state[4] == 'O' and self.board_state[8] == 'O':
            return 'O'

        # Check Anti Diagonal
        if self.board_state[2] == 'X' and self.board_state[4] == 'X' and self.board_state[6] == 'X':
            return 'X'
        if self.board_state[2] == 'O' and self.board_state[4] == 'O' and self.board_state[6] == 'O':
            return 'O'

        for i in range(len(self.board_state)):
            if self.board_state[i] == 0:
                return

        return 'Tie'


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(arcade.color.COSMIC_LATTE)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("GAME PAUSED", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 70, arcade.color.BLACK_OLIVE, font_size=50,
                         anchor_x="center")
        arcade.draw_text("Press Esc. to return", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 10, arcade.color.BLACK_OLIVE,
                         font_size=30, anchor_x="center")
        arcade.draw_text("Press M to the Main Menu", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 70, arcade.color.BLACK_OLIVE,
                         font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)
        elif key == arcade.key.M:
            start_view = StartView()
            self.window.show_view(start_view)


class WinView(arcade.View):
    def __init__(self, winner, if_single):
        super().__init__()
        self.winner = winner
        self.was_single = if_single

    def on_show(self):
        arcade.set_background_color(arcade.color.COSMIC_LATTE)

    def on_draw(self):
        arcade.start_render()
        if self.winner == "Tie":
            player_winner = "It was a tie!"
        elif not self.was_single:
            player_winner = "Player " + self.winner + " wins!"
        else:
            player_winner = self.winner + " wins!"
        arcade.draw_text(player_winner, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, arcade.color.BLACK_OLIVE,
                         font_size=50, anchor_x="center")
        arcade.draw_text("Start New Game (Press the R Key)", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK_OLIVE, font_size=30, anchor_x="center")
        arcade.draw_text("Return to Main Screen (Press the M Key)", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100,
                         arcade.color.BLACK_OLIVE, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.R:
            game_view = TicTacToeGame(self.was_single)
            self.window.show_view(game_view)
        elif key == arcade.key.M:
            start_view = StartView()
            self.window.show_view(start_view)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
