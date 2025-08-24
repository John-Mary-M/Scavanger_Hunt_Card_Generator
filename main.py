import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit

# Expanded lists of prompts for Year 4 and Year 7
year_4_prompts = [
    "Find someone who has a pet.",
    "Find someone who likes to draw.",
    "Find someone who has the same favorite color as you.",
    "Find someone who has been to another country.",
    "Find someone who plays a sport.",
    "Find someone who likes to read books.",
    "Find someone who has a sibling.",
    "Find someone who loves pizza.",
    "Find someone who can name a superhero.",
    "Find someone who likes to sing.",
    "Find someone who has been to a zoo.",
    "Find someone who enjoys playing video games.",
    "Find someone who has a favorite animal.",
    "Find someone who likes to dance.",
    "Find someone who has tried a new food this year.",
    "Find someone who can name a cartoon character.",
    "Find someone who likes to build things (like LEGO).",
    "Find someone who has a birthday in the same month as you.",
    "Find someone who likes to swim.",
    "Find someone who has a favorite toy or game."
]
year_7_prompts = [
    "Find someone who has a pet and knows its name.",
    "Find someone who has tried a new hobby this year.",
    "Find someone who shares your favorite subject.",
    "Find someone who has traveled outside the country.",
    "Find someone who plays a team sport or club activity.",
    "Find someone who has read a book this month.",
    "Find someone who has an older or younger sibling.",
    "Find someone who can name three types of music they like.",
    "Find someone who has watched a movie this week.",
    "Find someone who knows how to cook something.",
    "Find someone who has been to a concert or live event.",
    "Find someone who likes to write stories or poems.",
    "Find someone who has a favorite app or game on their phone.",
    "Find someone who can name a historical figure.",
    "Find someone who has learned something new this summer.",
    "Find someone who enjoys science experiments.",
    "Find someone who has a favorite TV show.",
    "Find someone who can name three countries.",
    "Find someone who likes to draw or paint.",
    "Find someone who has a goal for this school year."
]

class ScavengerHuntApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scavenger Hunt Card Generator")
        self.setGeometry(100, 100, 400, 300)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Text area to display output
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.layout.addWidget(self.output)

        # Buttons for Year 4 and Year 7
        self.year_4_button = QPushButton("Generate Year 4 Cards")
        self.year_7_button = QPushButton("Generate Year 7 Cards")
        self.layout.addWidget(self.year_4_button)
        self.layout.addWidget(self.year_7_button)

        # Connect buttons to functions
        self.year_4_button.clicked.connect(lambda: self.generate_cards(year_4_prompts, 6, "Year 4"))
        self.year_7_button.clicked.connect(lambda: self.generate_cards(year_7_prompts, 7, "Year 7"))

    def generate_cards(self, prompts, num_items, year):
        # Generate a randomized card
        selected_prompts = random.sample(prompts, num_items)
        card_text = f"--- {year} Scavenger Hunt Card ---\n"
        for i, prompt in enumerate(selected_prompts, 1):
            card_text += f"{i}. {prompt} (Name: _______________)\n"
        card_text += "\nInstructions: Find a different classmate for each prompt. Write their name next to the prompt. First to complete wins a prize!"
        self.output.setText(card_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScavengerHuntApp()
    window.show()
    sys.exit(app.exec())