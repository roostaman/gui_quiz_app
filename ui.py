import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizz")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        self.canvas = tk.Canvas(self.window, width=300, height=250, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(
            145, 120, text='Abc is where?',
            width=280,
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        image_yes = tk.PhotoImage(file="./images/true.png")
        image_no = tk.PhotoImage(file="./images/false.png")

        self.yes_button = tk.Button(image=image_yes, command=self.button_true, highlightthickness=0, bg=THEME_COLOR)
        self.yes_button.grid(column=0, row=2)
        self.no_button = tk.Button(image=image_no, command=self.button_false, highlightthickness=0, bg=THEME_COLOR)
        self.no_button.grid(column=1, row=2)

        self.score_label = tk.Label(text=f"Score: 0", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

            self.canvas.itemconfig(
                self.question_text, text=f"You've completed the quiz.\n"
                                         f"Your final score was: {self.quiz.score}/{self.quiz.question_number}"
            )

    def button_true(self):
        is_right = self.quiz.check_answer(user_answer='True')
        self.give_feedback(is_right)

    def button_false(self):
        is_right = self.quiz.check_answer(user_answer='False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(350, func=self.get_next_question)
