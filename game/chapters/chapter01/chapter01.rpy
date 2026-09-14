# list of Chapter 1 lessons
define persistent.CHAPTER01_ORDER = ["chapter01_01", "chapter01_02", "chapter01_03", "chapter01_04", "chapter01_05", "chapter01_06", "chapter01_07"]
define persistent.CHAPTER01_NAME = {
    "chapter01_01": "Добро пожаловать на курс!",
    "chapter01_02": "Введение в программирование",
    "chapter01_03": "Переменные",
    "chapter01_04": "Строки",
    "chapter01_05": "Вывод на экран (print)",
    "chapter01_06": "Операторы и приоритет",
    "chapter01_07": "Комментарии",
}

label chapter01:
    call screen lppr_list("chapter_select", "Глава 1", [(lesson_ID, "Глава 1." + str(i+1) + " - " + persistent.CHAPTER01_NAME[lesson_ID]) if lesson_ID.startswith("chapter01") else (lesson_ID, persistent.CHAPTER01_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.CHAPTER01_ORDER)])
    jump chapter_select
