# list of Chapter 4 lessons
define persistent.chapter04_ORDER = ["chapter04_01", "chapter04_02", "chapter04_03", "chapter04_04", "chapter04_05", "chapter04_06"]
define persistent.chapter04_NAME = {
    "chapter04_01": "Обзор: Структуры данных",
    "chapter04_02": "Списки (Lists)",
    "chapter04_03": "Множества (Sets)",
    "chapter04_04": "Кортежи (Tuples)",
    "chapter04_05": "Словари (Dicts)",
    "chapter04_06": "Генераторы (Comprehensions)",
}

label chapter04:
    call screen lppr_list("chapter_select", "Глава 4", [(lesson_ID, "Глава 4." + str(i+1) + " - " + persistent.chapter04_NAME[lesson_ID]) if lesson_ID.startswith("chapter04") else (lesson_ID, persistent.chapter04_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.chapter04_ORDER)])
    jump chapter_select
