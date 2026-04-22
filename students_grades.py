from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)
        if score < 50:
            return "F"
        elif 50<= score < 60:
            return "E"
        elif 60 <= score <70:
            return "D"
        elif 70 <= score < 80:
            return "C"
        elif 80 <= score < 90:
            return "B"
        else:
            return "A"

    def find(self,score):
        positions = []
        count = 0
        searched_data = self.scores
        while count < len(searched_data):
            if searched_data[count] == score:
                positions.append(count)
            count += 1
        return positions

    def get_sorted(self):
        numbers_copy = self.scores[:]
        n = len(numbers_copy)

        for num in range(n - 1):
            for idx in range(n - 1 - num):
                if numbers_copy[idx] > numbers_copy[idx + 1]:
                    numbers_copy[idx], numbers_copy[idx + 1] = numbers_copy[idx + 1], numbers_copy[idx]

        return numbers_copy


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(f"Počet studentů: {results.count()}")
    for student in range(results.count()):
        print(f"Student{student}: {results.get_by_index(student)} points – {results.get_grade(student)}")
    print(f"Plný počet bodů: {results.find(100)}")
    print(results.get_sorted())

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

if __name__ == "__main__":
    main()
