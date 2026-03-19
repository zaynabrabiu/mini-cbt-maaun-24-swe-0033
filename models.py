from collections import deque
from datetime import datetime
from typing import Optional

class Question:
    """OOP Class - maps real-world question entity (Lecture 4)."""
    def __init__(self, text: str, choices: dict, correct: str):
        self.text = text
        self.choices = choices          # {"A": "text", "B": "text", ...}
        self.correct = correct.upper()

    def is_correct(self, user_answer: str) -> bool:
        """Custom behavior method - this is what earns OOP marks."""
        return user_answer.upper() == self.correct

    def __str__(self):
        return f"Q: {self.text[:60]}..."


class MiniCBT:
    """Manages the entire test using Queue (FIFO) for question order."""
    def __init__(self):
        questions_list = self._create_questions()
        self.pending_questions: deque = deque(questions_list)
        self.current_question: Optional[Question] = None
        self.score: int = 0
        self.total: int = len(questions_list)
        self.submission_time: Optional[datetime] = None

    def _create_questions(self):
        """5 course-relevant questions (local university + Python/Flask)."""
        return [
            Question(
                "What is the complete official name of our university (MAAUN)?",
                {
                    "A": "Maryam Abacha American University of Nigeria (MAAUN)",
                    "B": "American University of Nigeria (AUN)",
                    "C": "University of Abuja",
                    "D": "Ahmadu Bello University"
                },
                "A"
            ),
            Question(
                "Which data structure manages questions using FIFO order in this project?",
                {"A": "Stack (LIFO)", "B": "Queue (FIFO)", "C": "Set", "D": "Dictionary"},
                "B"
            ),
            Question(
                "What is the purpose of the __init__ method in Python OOP?",
                {"A": "Destroy object", "B": "Initialize object (constructor)", "C": "Print object", "D": "Import modules"},
                "B"
            ),
            Question(
                "Which Flask decorator defines routes?",
                {"A": "@route", "B": "@app.route", "C": "@get", "D": "@post"},
                "B"
           ),
	    Question(
   		 "What is the capital of Nigeria?",
   		 {"A": "Lagos (economic hub)", "B": "Abuja", "C": "Kano", "D": "Kaduna"},
   		 "B"
            ),
            Question(
                "What does the datetime module help us do in this project?",
                {"A": "Calculate score", "B": "Timestamp the test submission", "C": "Create queues", "D": "Define classes"},
                "B"
            )
        ]

    def load_next_question(self) -> Optional[Question]:
        """Load next question from Queue (FIFO)."""
        if self.current_question is None and self.pending_questions:
            self.current_question = self.pending_questions.popleft()
        return self.current_question

    def submit_current_answer(self, user_answer: str):
        """Submit answer using the current question."""
        if self.current_question and self.current_question.is_correct(user_answer):
            self.score += 1
        self.current_question = None

    def finish_test(self):
        """Timestamp the result (Requirement B)."""
        self.submission_time = datetime.now()

    def get_result(self) -> dict:
        """Return final result with timestamp."""
        if not self.submission_time:
            return {}
        percentage = round((self.score / self.total) * 100, 1) if self.total else 0
        return {
            "score": self.score,
            "total": self.total,
            "percentage": percentage,
            "time": self.submission_time.strftime("%Y-%m-%d %H:%M:%S")
        }


# ====================== TEST IN TERMINAL ======================
if __name__ == "__main__":
    print("=== Mini CBT Terminal Test (models.py) ===")
    quiz = MiniCBT()
    while True:
        q = quiz.load_next_question()
        if not q:
            break
        print("\n" + "="*50)
        print(q)
        print("\nOptions:")
        for key, text in q.choices.items():
            print(f"   {key}: {text}")
        ans = input("\nYour answer (A/B/C/D): ").strip()
        quiz.submit_current_answer(ans)

    quiz.finish_test()
    result = quiz.get_result()
    print("\n" + "="*50)
    print("TEST FINISHED!")
    print(f"Score: {result['score']}/{result['total']} ({result['percentage']}%)")
    print(f"Submitted at: {result['time']}")
