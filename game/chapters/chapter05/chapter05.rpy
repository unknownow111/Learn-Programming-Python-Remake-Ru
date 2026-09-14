# list of Chapter 5 lessons
define persistent.chapter05_ORDER = ["chapter05_01", "chapter05_02", "chapter05_03", "chapter05_04"]
define persistent.chapter05_NAME = {
    "chapter05_01": "Обзор: Функции",
    "chapter05_02": "Анатомия функции",
    "chapter05_03": "Значения параметров по умолчанию",
    "chapter05_04": "Переменное число аргументов (*args, **kwargs)",
}

label chapter05:
    call screen lppr_list("chapter_select", "Глава 5", [(lesson_ID, "Глава 5." + str(i+1) + " - " + persistent.chapter05_NAME[lesson_ID]) if lesson_ID.startswith("chapter05") else (lesson_ID, persistent.chapter05_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.chapter05_ORDER)])
    jump chapter_select
