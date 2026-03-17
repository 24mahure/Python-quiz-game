import tkinter as tk
import random

# ---------------- CONFIG & COLORS ---------------- #
BG_COLOR = "#ee9b2d"
CARD_COLOR = "#16213e"
TEXT_COLOR = "#0da34b"
BTN_COLOR = "#0f3460"
BTN_HOVER = "#ACD119"
WHITE = "#ffffff"
SUCCESS = "#3c8fd7"

# ---------------- QUESTIONS ---------------- #
questions_pool = [
    ("What is the capital of India?", ["Mumbai","Delhi","Pune","Chennai"], 1),
    ("Which language is used for AI?", ["Python","HTML","CSS","MS Word"], 0),
    ("What is 5 + 7 ?", ["10","11","12","13"], 2),
    ("Which planet is called Red Planet?", ["Earth","Mars","Venus","Jupiter"], 1),
    ("Which is the largest ocean?", ["Atlantic","Indian","Pacific","Arctic"], 2),
    ("Who invented the computer?", ["Charles Babbage","Newton","Tesla","Einstein"], 0),
    ("Binary of decimal 2?", ["10","11","01","100"], 0),
    ("Which keyword used for loop in Python?", ["repeat","loop","for","iterate"], 2),
    ("Which device stores data permanently?", ["RAM","ROM","CPU","Cache"], 1),
    ("Which symbol used for comments in Python?", ["//","#","/*","--"], 1),
    ("What is 9 x 3 ?", ["18","27","21","24"], 1),
    ("Which is programming language?", ["Python","Photoshop","Excel","Chrome"], 0),
    ("Which company created Windows?", ["Apple","Google","Microsoft","IBM"], 2),
    ("HTML used for?", ["Design webpage","Structure webpage","Database","AI"], 1),
    ("CPU stands for?", ["Central Processing Unit","Computer Power Unit","Control Program Unit","Central Program Unit"],0),
    ("Which is input device?", ["Monitor","Keyboard","Printer","Speaker"],1),
    ("Which is output device?", ["Scanner","Mouse","Monitor","Keyboard"],2),
    ("Which number system computers use?", ["Decimal","Binary","Octal","Hex"],1),
    ("Python created by?", ["Guido van Rossum","Elon Musk","Bill Gates","Mark"],0),
    ("Which is fastest memory?", ["RAM","Cache","ROM","Hard Disk"],1)
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Python Quiz")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg=BG_COLOR)
        
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        
        self.q_index = 0
        self.score = 0
        self.setup_quiz()
        
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, 
                               bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack()
        
        self.create_widgets()
        self.load_question()

    def setup_quiz(self):
        random.shuffle(questions_pool)
        self.quiz_questions = questions_pool[:10]
        self.q_index = 0
        self.score = 0

    def create_widgets(self):
        # Exit Button
        self.exit_btn = tk.Button(self.root, text="✕", font=("Arial", 20, "bold"),
                                 bg="#e94560", fg=WHITE, bd=0, cursor="hand2",
                                 command=self.root.destroy)
        self.canvas.create_window(self.width - 50, 50, window=self.exit_btn)

        # Title
        self.canvas.create_text(self.width/2, 100, text="QUIZ MASTER", 
                                font=("Impact", 60), fill=TEXT_COLOR)

        # Question Text
        self.question_display = self.canvas.create_text(
            self.width/2, self.height/3, text="", font=("Segoe UI", 28, "bold"),
            fill=WHITE, width=self.width*0.8, justify="center"
        )

        # Answer Buttons
        self.buttons = []
        positions = [
            (self.width/2 - 250, self.height/2),
            (self.width/2 + 250, self.height/2),
            (self.width/2 - 250, self.height/2 + 120),
            (self.width/2 + 250, self.height/2 + 120)
        ]

        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Segoe UI", 16, "bold"),
                           width=30, height=2, bg=BTN_COLOR, fg=WHITE,
                           activebackground=BTN_HOVER, activeforeground=WHITE,
                           bd=0, cursor="hand2", command=lambda idx=i: self.check_answer(idx))
            
            # Hover animations
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=BTN_HOVER))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=BTN_COLOR))
            
            btn_window = self.canvas.create_window(positions[i][0], positions[i][1], window=btn)
            self.buttons.append((btn, btn_window))

    def load_question(self):
        if self.q_index < len(self.quiz_questions):
            q_data = self.quiz_questions[self.q_index]
            self.canvas.itemconfig(self.question_display, text=f"{self.q_index + 1}. {q_data[0]}")
            
            for i in range(4):
                self.buttons[i][0].config(text=q_data[1][i], state="normal", bg=BTN_COLOR)
        else:
            self.show_score()

    def check_answer(self, idx):
        correct_idx = self.quiz_questions[self.q_index][2]
        
        if idx == correct_idx:
            self.score += 1
            self.buttons[idx][0].config(bg=SUCCESS)
        else:
            self.buttons[idx][0].config(bg="#e30a11")

        self.root.after(500, self.next_question)

    def next_question(self):
        self.q_index += 1
        self.load_question()

    def show_score(self):
        self.canvas.itemconfig(self.question_display, 
                               text=f"COMPLETED!\n\nFinal Score: {self.score} / 10",
                               fill=SUCCESS)
        
        for btn, btn_window in self.buttons:
            btn.destroy()
        
        restart_btn = tk.Button(self.root, text="PLAY AGAIN", font=("Segoe UI", 18, "bold"),
                               bg=SUCCESS, fg=BG_COLOR, padx=20, pady=10, bd=0,
                               command=self.restart_game)
        self.canvas.create_window(self.width/2, self.height/2 + 100, window=restart_btn)

    def restart_game(self):
        # Refresh the entire UI by clearing the canvas and starting over
        self.canvas.destroy()
        self.__init__(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()