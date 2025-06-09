class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        if len(self.question_list) != self.question_number:
            return True

    def next_question(self):
        display_number = self.question_number + 1
        input(f"Q{display_number}. {self.question_list[self.question_number].text} "
              f"True or False?\n").lower()
        self.question_number += 1