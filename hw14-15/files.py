class Student:
    def __init__(self, student_name, student_group, student_grades):
        self.name = student_name
        self.group = student_group
        self.grades = student_grades


class Statistics:
    def __init__(self, all_students):
        self.students = all_students

    def count_students(self):
        return len(self.students)

    def calculate_group_statistics(self):
        group_statistics = {}
        for current_student in self.students:
            if current_student.group not in group_statistics:
                group_statistics[current_student.group] = {
                    "total_students": 0,
                    "all_grades": [],
                }
            group_statistics[current_student.group]["total_students"] += 1
            group_statistics[current_student.group]["all_grades"].extend(
                current_student.grades
            )

        final_result = {}
        for group_name, group_data in group_statistics.items():
            average_grade = (
                sum(group_data["all_grades"]) / len(group_data["all_grades"])
                if group_data["all_grades"]
                else 0
            )
            final_result[group_name] = {
                "students": group_data["total_students"],
                "avg_grade": round(average_grade, 2),
            }
        return final_result

    def write_to_file(self, output_filename):
        with open(output_filename, "w", encoding="utf-8") as file:
            for individual_student in self.students:
                file.write(
                    f"{individual_student.name}, {individual_student.group}, "
                    f"Оценки: {','.join(map(str, individual_student.grades))}\n"
                )

            file.write(f"\nОбщее количество студентов: {self.count_students()}\n")
            group_stats = self.calculate_group_statistics()
            for group_name, group_info in group_stats.items():
                file.write(
                    f"{group_name}: Студентов - {group_info['students']}, "
                    f"Средняя оценка - {group_info['avg_grade']}\n"
                )


ivan = Student("Иванов Иван", "Группа 1", [4, 5, 5])
petya = Student("Петров Петр", "Группа 2", [3, 4, 4])
anna = Student("Сидорова Анна", "Группа 1", [5, 5, 4])
olya = Student("Кузнецова Ольга", "Группа 2", [4, 4, 3])


all_students = [ivan, petya, anna, olya]


stats = Statistics(all_students)

print(f"Общее количество студентов: {stats.count_students()}")
group_statistics = stats.calculate_group_statistics()
for group_name, group_info in group_statistics.items():
    print(
        f"{group_name}: students: {group_info['students']}, Avg : {group_info['avg_grade']}"
    )

stats.write_to_file("students.txt")
