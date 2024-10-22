class Question:
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices


class Survey:
    def __init__(self, title, instructions, questions):
        self.title = title
        self.instructions = instructions
        self.questions = questions


# Example questions for the satisfaction survey
questions = [
    Question("Did you enjoy your experience?", ["Yes", "No"]),
    Question("Would you recommend us to a friend?", ["Definitely", "Maybe", "Not at all"]),
    Question("How would you rate our service?", ["Excellent", "Good", "Average", "Poor"]),
    Question("Any additional comments?", ["None", "Other feedback"])
]

# Create the satisfaction survey
satisfaction_survey = Survey("Satisfaction Survey", "Please answer the following questions.", questions)