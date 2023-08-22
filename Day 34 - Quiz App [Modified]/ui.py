from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Quizzler_UI():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        # self.window.minsize(width=400, height=500)
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_label = Label(text=f"Score : {self.score}", fg = "white", background=THEME_COLOR, font=("Arial",12))
        # self.score_text = score_label.config(text=f"Score : {self.score}")
        self.score_label.grid(row=0, column= 1)

        # Canvas for the text
        self.canvas = Canvas(background="white", width=300, height=250)
        self.question_text = self.canvas.create_text(150,125, width=280, text="", fill=THEME_COLOR, font=("Arial",16,"italic"))
        self.canvas.grid(row=1, column=0, columnspan = 2, pady = 50)

        # Buttons
        image_true = PhotoImage(file="./images/true.png")
        self.true_Button = Button(image=image_true, highlightthickness=0, command=self.true_pressed)
        self.true_Button.grid(row=2,column=0)

        image_false = PhotoImage(file="./images/false.png")
        self.false_Button = Button(image=image_false, highlightthickness=0, command=self.false_pressed)
        self.false_Button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_Button.config(state="disabled")
            self.false_Button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, func=self.get_next_question)



