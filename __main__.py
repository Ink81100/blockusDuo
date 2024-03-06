from controller.gameController import GameController
from logic.gameLogic import Game
from view.gameView import GameView

def main():
    game = Game()
    view = GameView(None)
    controller = GameController(game,view)
    view.controller = controller
    view.mainloop()


if __name__ == "__main__":
    main()