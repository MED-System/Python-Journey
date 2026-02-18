# Define the structure for what a Question is
class Question:
    # Set the initial values for the object
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer