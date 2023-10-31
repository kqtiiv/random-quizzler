from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question text", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label()
        self.score.config(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score.grid(row=0, column=1)

        self.tick_button = Button()
        self.tick_image = PhotoImage(file="images/true.png")
        self.tick_button.config(image=self.tick_image, borderwidth=0, command=self.true_clicked)
        self.tick_button.grid(row=2, column=0)

        self.false_button = Button()
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button.config(image=self.false_image, borderwidth=0, command=self.false_clicked)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.tick_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        self.feedback(self.quiz.check_answer("true"))

    def false_clicked(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, answer):
        if answer:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, func=self.get_next_question)
