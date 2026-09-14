# list of Chapter 7 lessons
define persistent.chapter07_ORDER = ["chapter07_01", "chapter07_02", "chapter07_03"]
define persistent.chapter07_NAME = {
    "chapter07_01": "Обзор: Объекты и классы",
    "chapter07_02": "Анатомия объекта",
    "chapter07_03": "Работа с объектами",
}

label chapter07:
    call screen lppr_list("chapter_select", "Глава 7", [(lesson_ID, "Глава 7." + str(i+1) + " - " + persistent.chapter07_NAME[lesson_ID]) if lesson_ID.startswith("chapter07") else (lesson_ID, persistent.chapter07_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.chapter07_ORDER)])
    jump chapter_select
