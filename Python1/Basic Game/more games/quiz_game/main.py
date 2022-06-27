from question_model import Question
from data import question_data


question_bank = []
for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    new_question = Question(q_text, q_ans)
    question_bank.append(new_question)

#     quiz = Quizbrain(question_bank)
#     w =0
#     c = 0
# for quiz.question_number in range(12):
#     quiz.next_question()

