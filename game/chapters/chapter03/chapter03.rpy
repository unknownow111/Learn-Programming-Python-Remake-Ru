# list of Chapter 3 lessons
define persistent.CHAPTER03_ORDER = ["chapter03_01", "chapter03_02", "chapter03_03", "chapter03_04", "chapter03_05"]
define persistent.CHAPTER03_NAME = {
    "chapter03_01": "Обзор: Циклы",
    "chapter03_02": "Циклы while",
    "chapter03_03": "Циклы for",
    "chapter03_04": "Операторы break и continue",
    "chapter03_05": "Вложенные циклы",
}

label chapter03:
    call screen lppr_list("chapter_select", "Глава 3", [(lesson_ID, "Глава 3." + str(i+1) + " - " + persistent.CHAPTER03_NAME[lesson_ID]) if lesson_ID.startswith("chapter03") else (lesson_ID, persistent.CHAPTER03_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.CHAPTER03_ORDER)])
    jump chapter_select
