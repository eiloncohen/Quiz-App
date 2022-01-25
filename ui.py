from tkinter import *
from quiz_brain import QuizBrain
CORRECT_IMG_PATH = "C:/Users/eilon/PycharmProjects/Quiz-App/images/true.png"
WRONG_IMG_PATH = "C:/Users/eilon/PycharmProjects/Quiz-App/images/false.png"
THEME_COLOR = "#375362"


class UI(Tk):
    def __init__(self, quiz_brain: QuizBrain):
        super(UI, self).__init__()
        self.quiz = quiz_brain
        self.configure(padx=20, pady=20, bg=THEME_COLOR)
        self.title("Quizzer")
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)
        self.score = Label(text=f"Score: {self.quiz.score}", fg="white", font=("Ariel", 20, "italic"),
                           bg=THEME_COLOR, highlightthickness=0)
        self.score.grid(row=0, column=1, pady=20)
        self.correct_img = PhotoImage(file=CORRECT_IMG_PATH)
        self.known_button = Button(image=self.correct_img, highlightthickness=0,
                                   command=self.true_pressed)
        self.known_button.grid(row=2, column=0)
        self.wrong_img = PhotoImage(file=WRONG_IMG_PATH)
        self.unknown_button = Button(image=self.wrong_img, highlightthickness=0,
                                   command=self.false_pressed)
        self.unknown_button.grid(row=2, column=1)
        self.enter_question_to_canvas()
        self.mainloop()

    def enter_question_to_canvas(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question, fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text, text="Game Over", fill=THEME_COLOR)
            self.known_button.config(state="disabled")
            self.unknown_button.config(state="disabled")

    def true_pressed(self):
        self.is_answer_correct("True")

    def false_pressed(self):
        self.is_answer_correct("False")

    def is_answer_correct(self, answer):
        is_correct = self.quiz.check_answer(answer)
        if is_correct:
            self.canvas.configure(bg='green')
            self.score.configure(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.configure(bg='red')
        self.after(1000, self.enter_question_to_canvas)






