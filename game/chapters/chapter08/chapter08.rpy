# list of Chapter 8 lessons
define persistent.chapter08_ORDER = ["chapter08_01", "chapter08_02", "chapter08_03"]
define persistent.chapter08_NAME = {
    "chapter08_01": "Обзор: Исключения",
    "chapter08_02": "Обработка исключений (try/except)",
    "chapter08_03": "Пользовательские исключения",
}

label chapter08:
    call screen lppr_list("chapter_select", "Глава 8", [(lesson_ID, "Глава 8." + str(i+1) + " - " + persistent.chapter08_NAME[lesson_ID]) if lesson_ID.startswith("chapter08") else (lesson_ID, persistent.chapter08_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.chapter08_ORDER)])
    jump chapter_select
