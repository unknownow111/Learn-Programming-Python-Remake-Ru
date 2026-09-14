# list of Chapter 10 lessons
define persistent.chapter10_ORDER = ["chapter10_01", "chapter10_02", "chapter10_03"]
define persistent.chapter10_NAME = {
    "chapter10_01": "Обзор: Модули и библиотеки",
    "chapter10_02": "Стандартная библиотека Python",
    "chapter10_03": "Внешние библиотеки (PyPI/pip)",
}

label chapter10:
    call screen lppr_list("chapter_select", "Глава 10", [(lesson_ID, "Глава 10." + str(i+1) + " - " + persistent.chapter10_NAME[lesson_ID]) if lesson_ID.startswith("chapter10") else (lesson_ID, persistent.chapter10_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.chapter10_ORDER)])
    jump chapter_select
