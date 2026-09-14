# The script of the game goes in this file.

# in-game variables
default COMPLETED = set()
default INCORRECT = set()

# useful constants
define persistent.TITLE_XALIGN = 0.5
define persistent.TITLE_YPOS = 0.05
define persistent.CONTENT_XPOS = 0.1
define persistent.CONTENT_YPOS = 0.15
define persistent.CONTENT_XSIZE = 3072
define persistent.CONTENT_YSIZE = 1512 # currently unused
define persistent.PAGENUM_XPOS = 0.9
define persistent.PAGENUM_YPOS = 0.925
define persistent.NAV_BUTTON_PREV_XPOS = 0.05
define persistent.NAV_BUTTON_NEXT_XPOS = 0.9
define persistent.NAV_BUTTON_YPOS = 0.05
define persistent.EXERCISE_SPACING = 50
define persistent.CHALLENGE_SOLVED_COLOR = "#0f0"
define persistent.CHALLENGE_SOLVED_TEXT = "Верно!"
define persistent.CHALLENGE_INCORRECT_COLOR = "#f00"
define persistent.CHALLENGE_INCORRECT_TEXT = "Неверно"
define persistent.EXERCISE_BREAK_TITLE = "Упражнение"
define persistent.EXERCISE_BREAK_COLOR = "#f0f"
define persistent.INPUT_LABEL_TEXT = "Введите ответ:"
define persistent.INPUT_BACKGROUND_COLOR = "#222"

# list of chapters
define persistent.CHAPTER_ORDER = ["chapter01", "chapter02", "chapter03", "chapter04", "chapter05", "chapter06", "chapter07", "chapter08", "chapter09", "chapter10", "chapter11", "progress", "credits"]
define persistent.CHAPTER_NAME = {
    "chapter01": "Введение: Основы и кирпичики",
    "chapter02": "Условия: Мороженое не едят на завтрак",
    "chapter03": "Циклы: Завтрак, обед, ужин, завтрак, обед, уж...",
    "chapter04": "Структуры данных: Мне комбо №3, пожалуйста!",
    "chapter05": "Функции: Как перестать переписывать код?",
    "chapter06": "Рекурсия: Секунду, мне звонят... от меня же",
    "chapter07": "Объекты: Python, угощайся бургером",
    "chapter08": "Исключения: Нельзя съесть пустую пачку чипсов",
    "chapter09": "Файловый ввод-вывод: Вот рецепт, испеки макаруны",
    "chapter10": "Библиотеки: Неужели никто этого еще не сделал?",
    "chapter11": "Эпилог: Что дальше?",
    "progress":  "Прогресс",
    "credits":   "Титры",
}
define persistent.NUM_LESSONS = {
    "chapter01": 7,
    "chapter02": 4,
    "chapter03": 5,
    "chapter04": 6,
    "chapter05": 4,
    "chapter06": 3,
    "chapter07": 3,
    "chapter08": 3,
    "chapter09": 4,
    "chapter10": 3,
    "chapter11": 2,
}
define persistent.NUM_PAGES = {
    "chapter01_01": 4,
    "chapter01_02": 3,
    "chapter01_03": 7,
    "chapter01_04": 13,
    "chapter01_05": 5,
    "chapter01_06": 6,
    "chapter01_07": 7,
    "chapter02_01": 1,
    "chapter02_02": 11,
    "chapter02_03": 5,
    "chapter02_04": 3,
    "chapter03_01": 1,
    "chapter03_02": 4,
    "chapter03_03": 2,
    "chapter03_04": 5,
    "chapter03_05": 2,
    "chapter04_01": 2,
    "chapter04_02": 7,
    "chapter04_03": 7,
    "chapter04_04": 6,
    "chapter04_05": 7,
    "chapter04_06": 9,
    "chapter05_01": 1,
    "chapter05_02": 7,
    "chapter05_03": 3,
    "chapter05_04": 5,
    "chapter06_01": 3,
    "chapter06_02": 4,
    "chapter06_03": 2,
    "chapter07_01": 1,
    "chapter07_02": 11,
    "chapter07_03": 10,
    "chapter08_01": 1,
    "chapter08_02": 9,
    "chapter08_03": 6,
    "chapter09_01": 2,
    "chapter09_02": 6,
    "chapter09_03": 3,
    "chapter09_04": 4,
    "chapter10_01": 2,
    "chapter10_02": 6,
    "chapter10_03": 6,
    "chapter11_01": 2,
    "chapter11_02": 2,
}
define persistent.ACHIEVEMENTS_REGISTERED = False

# custom screen for selectable list page of Learn Programming: Python Remake; list of (label_ID, label_name) tuples
screen lppr_list(return_label, title, items):
    textbutton "Назад":
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
        if return_label == "main_menu":
            action ShowMenu("main_menu")
        else:
            action Jump(return_label)
    text title:
        size gui.title_text_size
        color gui.accent_color
        xalign persistent.TITLE_XALIGN
        ypos persistent.TITLE_YPOS
    vbox:
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        for label_ID, label_name in items:
            textbutton label_name action Jump(label_ID)

# Chapter Selection
label chapter_select:
    call screen lppr_list("main_menu", "Выбор главы", [(chapter_ID, "Глава " + str(i+1) + " - " + persistent.CHAPTER_NAME[chapter_ID]) if chapter_ID.startswith("chapter") else (chapter_ID, persistent.CHAPTER_NAME[chapter_ID]) for i, chapter_ID in enumerate(persistent.CHAPTER_ORDER)])

# python helper functions
init python:
    # check Steam achievements
    def check_achievements():
        # register achievements (if not already)
        if not persistent.ACHIEVEMENTS_REGISTERED:
            for c in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']:
                achievement.register("CHAPTER%s" % c)
            achievement.register("FIRST_EXERCISE")
            achievement.register("FIRST_LESSON")
            achievement.register("ALL_CHAPTERS")
            achievement.sync()

        # preprocess lesson data
        num_complete = compute_num_complete(); lessons = dict()
        for lesson in persistent.NUM_PAGES:
            chapter = lesson.split('_')[0]
            if chapter not in lessons:
                lessons[chapter] = set()
            lessons[chapter].add(lesson)

        # detect Steam achievements
        finished_chapters = 0
        for k in num_complete:
            if '_' in k and num_complete[k] == persistent.NUM_PAGES[k]:
                achievement.grant("FIRST_LESSON")
        for chapter in lessons:
            if num_complete[chapter] == sum(persistent.NUM_PAGES[v] for v in lessons[chapter]):
                finished_chapters += 1; achievement.grant(chapter.upper())
        if finished_chapters == 11:
            achievement.grant("ALL_CHAPTERS")
        achievement.sync()

    # save/load game
    def save_game():
        check_achievements()
        renpy.force_autosave(take_screenshot=True)

    # grade challenge
    def grade_challenge(from_label, correct, student, ignore_chars=None, ignore_case=False, cast=None, float_precision=None, check=None):
        if check is not None:
            if check(student):
                INCORRECT.discard(from_label); COMPLETED.add(from_label); achievement.grant("FIRST_EXERCISE"); achievement.sync()
            else:
                INCORRECT.add(from_label)
            save_game(); renpy.call(from_label); return
        if ignore_chars is not None:
            for c in ignore_chars:
                student = student.replace(c,'')
        if ignore_case:
            correct = correct.lower(); student = student.lower()
        if cast is not None:
            try:
                if cast == "int":
                    correct = int(correct); student = int(student)
                elif cast == "float":
                    correct = float(correct); student = float(student)
                else:
                    assert False, "Invalid cast: %s" % str(cast)
            except:
                INCORRECT.add(from_label); save_game(); renpy.call(from_label); return
        if (cast == "float" and abs(correct-student) <= float_precision) or (correct == student):
            INCORRECT.discard(from_label); COMPLETED.add(from_label); achievement.grant("FIRST_EXERCISE"); achievement.sync()
        else:
            INCORRECT.add(from_label)
        save_game(); renpy.call(from_label)

    # set all values of dict `d` to `val`
    def set_all(d, val, from_label=None):
        INCORRECT.discard(from_label)
        for k in d:
            d[k] = val
        save_game()

    # compute number of completed pages
    def compute_num_complete():
        count = dict()
        for chapter in persistent.NUM_LESSONS:
            count[chapter] = 0
        for lesson in persistent.NUM_PAGES:
            count[lesson] = 0
        for page in COMPLETED:
            chapter, lesson_num, page_num = page.split("_")
            lesson = "%s_%s" % (chapter, lesson_num)
            count[chapter] += 1; count[lesson] += 1
        return count

# The game starts here.
label start:
    jump chapter_select
    return
