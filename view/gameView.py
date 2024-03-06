import tkinter as tk

class GameView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        # Initialize UI components
        self.title("Blokus Duo")
        self.geometry("800x600")
        # Additional UI elements

    def update_board(self):
        # Update the board display
        pass

    def show_win(self):
        # Display win message
        pass
