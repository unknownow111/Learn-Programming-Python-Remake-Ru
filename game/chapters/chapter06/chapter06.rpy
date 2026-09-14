# list of Chapter 6 lessons
define persistent.chapter06_ORDER = ["chapter06_01", "chapter06_02", "chapter06_03"]
define persistent.chapter06_NAME = {
    "chapter06_01": "Обзор: Рекурсия",
    "chapter06_02": "Анатомия рекурсивной функции",
    "chapter06_03": "Рекурсия против итерации",
}

label chapter06:
    call screen lppr_list("chapter_select", "Глава 6", [(lesson_ID, "Глава 6." + str(i+1) + " - " + persistent.chapter06_NAME[lesson_ID]) if lesson_ID.startswith("chapter06") else (lesson_ID, persistent.chapter06_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.chapter06_ORDER)])
    jump chapter_select
