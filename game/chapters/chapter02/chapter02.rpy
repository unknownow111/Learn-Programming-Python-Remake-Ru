# list of Chapter 2 lessons
define persistent.CHAPTER02_ORDER = ["chapter02_01", "chapter02_02", "chapter02_03", "chapter02_04"]
define persistent.CHAPTER02_NAME = {
    "chapter02_01": "Обзор: Условные конструкции",
    "chapter02_02": "Булева логика",
    "chapter02_03": "Условные операторы if",
    "chapter02_04": "Короткое замыкание (Short-Circuiting)",
}

label chapter02:
    call screen lppr_list("chapter_select", "Глава 2", [(lesson_ID, "Глава 2." + str(i+1) + " - " + persistent.CHAPTER02_NAME[lesson_ID]) if lesson_ID.startswith("chapter02") else (lesson_ID, persistent.CHAPTER02_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.CHAPTER02_ORDER)])
    jump chapter_select
