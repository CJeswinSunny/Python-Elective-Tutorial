class Student:
    """Represents a student."""

    def __init__(self, name, number_of_scores):
        """All scores are initially 0."""
        self.name = name
        self.test_scores = [0] * number_of_scores

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, position, value):
        """Assigns the score at the given position (1-based index)."""
        # position - 1 ensures 1-based index matches 0-based list
        self.test_scores[position - 1] = value

    def getScore(self, position):
        """Returns the score at the given position (1-based index)."""
        return self.test_scores[position - 1]

    def getHighestScore(self):
        """Returns the maximum score."""
        if len(self.test_scores) == 0:
            return 0
        return max(self.test_scores)

    def getAverageScore(self):
        """Returns the average score."""
        if len(self.test_scores) == 0:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.test_scores))

if __name__ == "__main__":
    # Get user input for student details
    name = input("Enter the student's name: ")
    num_scores = int(input("Enter the number of scores: "))
    
    student = Student(name, num_scores)
    
    # Get user input for each score
    for i in range(1, num_scores + 1):
        score = float(input(f"Enter score {i}: "))
        student.setScore(i, score)
    
    print("\n--- Student Details ---")
    print(student)
    print("Highest score:", student.getHighestScore())
    print("Average score:", student.getAverageScore())
