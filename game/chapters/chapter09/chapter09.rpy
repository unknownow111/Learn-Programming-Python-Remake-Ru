# list of Chapter 9 lessons
define persistent.chapter09_ORDER = ["chapter09_01", "chapter09_02", "chapter09_03", "chapter09_04"]
define persistent.chapter09_NAME = {
    "chapter09_01": "Обзор: Файловый ввод-вывод (I/O)",
    "chapter09_02": "Чтение из файлов",
    "chapter09_03": "Запись в файлы",
    "chapter09_04": "Экспорт объектов (pickle)",
}

label chapter09:
    call screen lppr_list("chapter_select", "Глава 9", [(lesson_ID, "Глава 9." + str(i+1) + " - " + persistent.chapter09_NAME[lesson_ID]) if lesson_ID.startswith("chapter09") else (lesson_ID, persistent.chapter09_NAME[lesson_ID]) for i, lesson_ID in enumerate(persistent.chapter09_ORDER)])
    jump chapter_select
