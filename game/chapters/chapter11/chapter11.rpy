# list of Chapter 11 lessons
define persistent.chapter11_ORDER = ["chapter11_01", "chapter11_02"]
define persistent.chapter11_NAME = {
    "chapter11_01": "Поздравляем!",
    "chapter11_02": "Что дальше: Как продолжать путь в Python",
}

label chapter11:
    call screen lppr_list("chapter_select", "Глава 11", [(lesson_ID, "Глава 11." + str(i+1) + " - " + persistent.chapter11_NAME[lesson_ID]) if lesson_ID.startswith("chapter11") else (lesson_ID, persistent.chapter11_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.chapter11_ORDER)])
    jump chapter_select
