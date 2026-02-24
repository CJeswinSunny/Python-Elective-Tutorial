class Student:
    """Represents a student."""

    def __init__(self, name, number_of_scores):
        self.name = name
        self.test_scores = [0] * number_of_scores

    def getName(self):
        return self.name

    def setScore(self, position, value):
        self.test_scores[position - 1] = value

    def getScore(self, position):
        return self.test_scores[position - 1]

    def getHighestScore(self):
        if len(self.test_scores) == 0:
            return 0
        return max(self.test_scores)

    def getAverageScore(self):
        if len(self.test_scores) == 0:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.test_scores))

if __name__ == "__main__":
    name = input("Enter the student's name: ")
    num_scores = int(input("Enter the number of scores: "))
    
    student = Student(name, num_scores)
    
    for i in range(1, num_scores + 1):
        score = float(input(f"Enter score {i}: "))
        student.setScore(i, score)
    
    print("\n--- Student Details ---")
    print(student)
    print("Highest score:", student.getHighestScore())
    print("Average score:", student.getAverageScore())
