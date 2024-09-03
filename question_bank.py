import uuid

class QuestionBank:
    def __init__(self):
        self.questions = []

    def add_question(self, text, category, difficulty, tags=None):
        question_id = str(uuid.uuid4())  # Generate a unique identifier using UUID
        question = {
            "id": question_id,
            "text": text,
            "category": category,
            "difficulty": difficulty,
            "tags": tags if tags else []
        }
        self.questions.append(question)
        return question

    def retrieve_questions(self, category=None, difficulty=None, tags=None):
        # Using list comprehension for optimized filtering
        return [
            question for question in self.questions
            if (category is None or question['category'] == category) and
               (difficulty is None or question['difficulty'] == difficulty) and
               (tags is None or any(tag in question['tags'] for tag in tags))
        ]

    def search_by_keywords(self, keywords):
        # Using list comprehension for optimized keyword search
        return [
            question for question in self.questions
            if any(keyword.lower() in question['text'].lower() for keyword in keywords)
        ]

# Example Usage and Test Cases

def run_tests():
    qb = QuestionBank()

    # Test Case 1: Adding a question and retrieving it by category and difficulty
    question1 = qb.add_question("What is a binary search tree?", "Data Structures", "Medium", tags=["trees", "algorithms"])
    assert qb.retrieve_questions(category="Data Structures", difficulty="Medium") == [question1]
    print("Test Case 1 Passed")

    # Test Case 2: Search by keywords
    question2 = qb.add_question("Explain quicksort algorithm.", "Algorithms", "Hard", tags=["sorting", "algorithms"])
    search_results = qb.search_by_keywords(["quicksort"])
    assert search_results == [question2]
    print("Test Case 2 Passed")

    # Test Case 3: Retrieve with no filters (should return all questions)
    question3 = qb.add_question("Describe the OSI model.", "Networking", "Easy", tags=["network", "protocols"])
    all_questions = qb.retrieve_questions()
    assert set([q['id'] for q in all_questions]) == {question1['id'], question2['id'], question3['id']}
    print("Test Case 3 Passed")

run_tests()
