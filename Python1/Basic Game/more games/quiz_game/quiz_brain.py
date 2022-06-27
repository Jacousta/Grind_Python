from main import question_bank

c = 0
w = 0
for n in range(12):
    print(f"Q({n + 1})", question_bank[n].ques)
    answer = input()
    if answer.capitalize() == question_bank[n].Answer:
        print("Correct")
        c = c + 1
    else:
        print("Wrong")
        w = w + 1
print(f"Your {c} answers were correct")
print(f"Your {w} answers were incorrect")


# class Quizbrain:
#     def __init__(self, q_list):
#         self.question_number = 0
#         self.question_list = q_list
#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         ans = input(f"Q{self.question_number+1}:{current_question.ques}(True/False)")

