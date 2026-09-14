# chapter and lesson labels
label chapter06_02_01:
    $ COMPLETED.add("chapter06_02_01"); save_game()
    call screen chapter06_02_01_screen
label chapter06_02_02:
    $ COMPLETED.add("chapter06_02_02"); save_game()
    call screen chapter06_02_02_screen
label chapter06_02_03:
    call screen chapter06_02_03_screen
label chapter06_02_04:
    $ COMPLETED.add("chapter06_02_04"); save_game()
    call screen chapter06_02_04_screen
label chapter06_02:
    jump chapter06_02_01
    jump chapter_select

# page 1
screen chapter06_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter06_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter06_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Формально любой рекурсивный алгоритм состоит из двух обязательных частей:\n\n    1. {b}{color=#0f0}Базовый случай (Base Case){/color}:{/b} Простейший, тривиальный вариант задачи, ответ для которого известен сразу без дальнейших вычислений\n    2. {b}{color=#f00}Рекурсивный случай (Recursive Case){/color}:{/b} Более масштабный вариант задачи, решение которого сводится к решению подзадач меньшего размера\n\nВ примере с очередью в театр:\n\n    1. {b}{color=#0f0}Базовый случай:{/color}{/b} Если вы первый в очереди, ответ равен 0\n    2. {b}{color=#f00}Рекурсивный случай:{/color}{/b} Иначе — спросить человека впереди и прибавить 1 к его ответу":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "sierpinski_triangle.png":
        xsize 1160
        ysize 1030
        xalign 0.5
        yalign .9

# page 2
screen chapter06_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter06_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter06_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter06_02_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Общий шаблон структуры рекурсивной функции:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}recursive_function{/color}(input):\n        {color=#ff0}if{/color} {color=#57f}base_case{/color}(input):\n            {color=#ff0}return{/color} trivial_solution\n        {color=#ff0}else{/color}:\n            sub_answer {color=#0f0}={/color} {color=#57f}recursive_function{/color}(sub_input)\n            {color=#ff0}return{/color} {color=#57f}process{/color}(sub_answer){/font}\n\nПрименительно к очереди, где вы представлены объектом {font=monospace.ttf}{color=#888}person{/color}{/font}, алгоритм запишется так:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}people_in_front{/color}(person):\n        {color=#ff0}if{/color} person.{color=#57f}is_front_of_line{/color}():\n            {color=#ff0}return{/color} {color=#f00}0{/color}\n        {color=#ff0}else{/color}:\n            {color=#ff0}return{/color} {color=#f00}1{/color} {color=#0f0}+{/color} {color=#57f}people_in_front{/color}(person.{color=#57f}in_front{/color}()){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
define persistent.chapter06_02_03_correct = {"a": True,  "b": False, "c": False,  "d": False}
default chapter06_02_03_student = {k: False for k in persistent.chapter06_02_03_correct}
define persistent.chapter06_02_03_options = {
    "a": "Вы обязаны указать хотя бы один базовый случай",
    "b": "Входные данные обязаны быть числом",
    "c": "Входные данные всегда должны делиться на более мелкие входные данные",
    "d": "Рекурсивная функция не может вызывать саму себя с теми же аргументами",
}
screen chapter06_02_03_screen:
    if "chapter06_02_03" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter06_02_03" in INCORRECT:
        text persistent.CHALLENGE_INCORRECT_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_INCORRECT_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    else:
        text persistent.EXERCISE_BREAK_TITLE:
            size gui.title_text_size
            color persistent.EXERCISE_BREAK_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    text "3 / " + str(persistent.NUM_PAGES["chapter06_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter06_02_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter06_02_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Какие из следующих утверждений о рекурсивных функциях верны? Выберите все подходящие варианты."
        for ol in sorted(persistent.chapter06_02_03_options.keys()):
            if "chapter06_02_03" in COMPLETED:
                if persistent.chapter06_02_03_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter06_02_03_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter06_02_03_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter06_02_03_options[ol])) action ToggleDict(chapter06_02_03_student, ol)
        if "chapter06_02_03" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter06_02_03", persistent.chapter06_02_03_correct, chapter06_02_03_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter06_02_03_student, False, from_label="chapter06_02_03")

# page 4
screen chapter06_02_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter06_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter06_02_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Проследим по шагам работу рекурсивной функции в Python. Рассмотрим функцию {font=monospace.ttf}{color=#57f}power{/color}{color=#888}(){/color}{/font}, принимающую два целых числа {font=monospace.ttf}{color=#888}x{/color}{/font} и {font=monospace.ttf}{color=#888}n{/color}{/font} и рекурсивно вычисляющую значение {font=monospace.ttf}{color=#888}x{/color}{color=#0f0}**{/color}{color=#888}n{/color}{/font}:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}power{/color}(x, n):\n        {color=#ff0}if{/color} n {color=#0f0}=={/color} {color=#f00}0{/color}:\n            {color=#ff0}return{/color} {color=#f00}1{/color}\n        {color=#ff0}else{/color}:\n            {color=#ff0}return{/color} {color=#57f}power{/color}(x, n{color=#0f0}-{/color}{color=#f00}1{/color}) {color=#0f0}*{/color} x{/font}\n\nЧто происходит при вызове {font=monospace.ttf}{color=#57f}power{/color}{color=#888}({/color}{color=#f00}3{/color}{color=#888},{/color}{color=#f00}2{/color}{color=#888}){/color}{/font}?\n\n    – {b}Шаг 1:{/b} Выполняется {font=monospace.ttf}{color=#57f}power{/color}{color=#888}({/color}{color=#f00}3{/color}{color=#888},{/color}{color=#f00}2{/color}{color=#888}){/color}{/font}:\n        1. {font=monospace.ttf}{color=#f00}2{/color} {color=#0f0}=={/color} {color=#f00}0{/color}{/font}? Нет, переходим в ветку {font=monospace.ttf}{color=#ff0}else{/color}{/font}\n        2. Чтобы вернуть результат, сначала нужно вычислить {font=monospace.ttf}{color=#57f}power{/color}{color=#888}({/color}{color=#f00}3{/color}{color=#888},{/color}{color=#f00}1{/color}{color=#888}){/color}{/font}\n    – {b}Шаг 2:{/b} Выполняется {font=monospace.ttf}{color=#57f}power{/color}{color=#888}({/color}{color=#f00}3{/color}{color=#888},{/color}{color=#f00}1{/color}{color=#888}){/color}{/font}:\n        1. {font=monospace.ttf}{color=#f00}1{/color} {color=#0f0}=={/color} {color=#f00}0{/color}{/font}? Нет, переходим в ветку {font=monospace.ttf}{color=#ff0}else{/color}{/font}\n        2. Нужно сначала вычислить {font=monospace.ttf}{color=#57f}power{/color}{color=#888}({/color}{color=#f00}3{/color}{color=#888},{/color}{color=#f00}0{/color}{color=#888}){/color}{/font}\n    – {b}Шаг 3:{/b} Выполняется {font=monospace.ttf}{color=#57f}power{/color}{color=#888}({/color}{color=#f00}3{/color}{color=#888},{/color}{color=#f00}0{/color}{color=#888}){/color}{/font}:\n        1. {font=monospace.ttf}{color=#f00}0{/color} {color=#0f0}=={/color} {color=#f00}0{/color}{/font}? Да! Срабатывает базовый случай: {font=monospace.ttf}{color=#ff0}return{/color} {color=#f00}1{/color}{/font}\n    – Возврат на Шаг 2.2: считаем {font=monospace.ttf}{color=#ff0}return{/color} {color=#f00}1{/color} {color=#0f0}*{/color} {color=#f00}3{/color}{/font} (получаем 3)\n    – Возврат на Шаг 1.2: считаем {font=monospace.ttf}{color=#ff0}return{/color} {color=#f00}3{/color} {color=#0f0}*{/color} {color=#f00}3{/color}{/font} (получаем 9)\n\nРекурсивных вызовов больше нет, итоговый результат равен {font=monospace.ttf}{color=#f00}9{/color}{/font} (что точно соответствует {font=monospace.ttf}{color=#f00}3{/color}{color=#0f0}**{/color}{color=#f00}2{/color}{/font}).":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
