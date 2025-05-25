# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        """
        Initializes a new instance of the Teacher class.

        Args:
            first_name (str): The first name of the teacher.
            last_name (str): The last name of the teacher.
            age (int): The age of the teacher.
            email (str): The email address of the teacher.
            can_teach_subjects (set): A set of subjects the teacher is capable of teaching.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()  # буде заповнено під час створення розкладу


def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    selected_teachers = []

    while uncovered_subjects:
        # Пошук викладача, який може покрити найбільше з того, що залишилося
        best_teacher = None
        max_new_subjects = 0

        for teacher in teachers:
            # Предмети, які цей викладач може покрити з ще не покритих
            teachable = teacher.can_teach_subjects & uncovered_subjects
            if len(teachable) > max_new_subjects or (
                len(teachable) == max_new_subjects
                and best_teacher
                and teacher.age < best_teacher.age
            ):
                best_teacher = teacher
                max_new_subjects = len(teachable)

        if not best_teacher or max_new_subjects == 0:
            return None  # неможливо покрити всі предмети

        # Призначаємо предмети цьому викладачу
        assigned = best_teacher.can_teach_subjects & uncovered_subjects
        best_teacher.assigned_subjects = assigned
        uncovered_subjects -= assigned
        selected_teachers.append(best_teacher)
        teachers.remove(best_teacher)  # більше не розглядаємо цього викладача

    return selected_teachers


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
