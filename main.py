from question_model import Question
from data import question_bank
from quiz_brain import QuizBrain

# Create list of Question objects
question_list = []
for q in question_bank:
    question = Question(q["text"], q["answer"])
    question_list.append(question)

# Initialize QuizBrain
quiz = QuizBrain(question_list)

# Run quiz loop
while quiz.still_has_questions():
    quiz.next_question()

print("🎉 You've completed the quiz!")
print(f"Your final score: {quiz.score}/{len(question_list)}")
