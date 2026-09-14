# chapter and lesson labels
label chapter08_02_01:
    $ COMPLETED.add("chapter08_02_01"); save_game()
    call screen chapter08_02_01_screen
label chapter08_02_02:
    $ COMPLETED.add("chapter08_02_02"); save_game()
    call screen chapter08_02_02_screen
label chapter08_02_03:
    $ COMPLETED.add("chapter08_02_03"); save_game()
    call screen chapter08_02_03_screen
label chapter08_02_04:
    call screen chapter08_02_04_screen
label chapter08_02_05:
    call screen chapter08_02_05_screen
label chapter08_02_06:
    $ COMPLETED.add("chapter08_02_06"); save_game()
    call screen chapter08_02_06_screen
label chapter08_02_07:
    $ COMPLETED.add("chapter08_02_07"); save_game()
    call screen chapter08_02_07_screen
label chapter08_02_08:
    $ COMPLETED.add("chapter08_02_08"); save_game()
    call screen chapter08_02_08_screen
label chapter08_02_09:
    $ COMPLETED.add("chapter08_02_09"); save_game()
    call screen chapter08_02_09_screen
label chapter08_02:
    jump chapter08_02_01
    jump chapter_select

# page 1
screen chapter08_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter08_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Прежде чем изучать, {b}{i}как{/i}{/b} перехватывать исключения, определим, {b}{i}когда{/i}{/b} это следует делать. Глушить абсолютно все подряд исключения нельзя: так вы просто скроете реальные баги и логические дефекты программы.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} В какой ситуации перехват исключения был бы вреден?\n\nНапример, если написать рекурсивную функцию {b}{i}без базового случая{/i}{/b}, программа рискует уйти в бесконечный цикл. Python защитит вас, возбудив исключение {font=monospace.ttf}{color=#57f}RecursionError{/color}{/font}. Если бездумно перехватывать все исключения подряд, мы никогда не узнаем о критической ошибке в коде.\n\nОбщее правило: перехватывать нужно только те исключения, возникновение которых {b}{i}ожидаемо{/i}{/b} в нормальном сценарии работы (например, при некорректных действиях пользователя или сбое сети).\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Можете ли вы назвать 3 примера ситуаций, где оправдана обработка исключений?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "stack_overflow.png":
        xsize 800
        ysize 800
        xalign 0.5
        yalign .97

# page 2
screen chapter08_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter08_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_02_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Самый частый источник ожидаемых исключений — ввод пользователя. Мы запрашиваем ввод встроенной функцией {font=monospace.ttf}{color=#57f}input{/color}{color=#888}(){/color}{/font}:\n\n{font=monospace.ttf}    user_input {color=#0f0}={/color} {color=#57f}input{/color}({color=#f00}\"Enter your favorite number: \"{/color}){/font}\n\nПрограмма выведет приглашение ко вводу и остановится в ожидании нажатия Enter. Функция {font=monospace.ttf}{color=#57f}input{/color}{color=#888}(){/color}{/font} всегда возвращает строку {font=monospace.ttf}{color=#57f}str{/color}{/font}. Если нам нужно число, мы преобразуем его через {font=monospace.ttf}{color=#57f}int{/color}():\n\n{font=monospace.ttf}    user_input {color=#0f0}={/color} {color=#57f}input{/color}({color=#f00}\"Enter your favorite number: \"{/color})\n    user_input_integer {color=#0f0}={/color} {color=#57f}int{/color}(user_input)\n    {color=#57f}print{/color}({color=#f00}\"Two divided by your favorite number is\"{/color}, {color=#f00}2{/color} {color=#0f0}/{/color} user_input_integer){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Где в этом коде может произойти исключение?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter08_02_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter08_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_02_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_02_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Если пользователь опечатается и введет слово вместо цифр:\n\n{font=monospace.ttf}    Enter your favorite number: carrot{/font}\n\nPython немедленно аварийно завершит программу исключением {font=monospace.ttf}{color=#57f}ValueError{/color}{/font}:\n\n{font=monospace.ttf}    Enter your favorite number: carrot\n    Traceback (most recent call last):\n      File {color=#f00}\"temp.py\"{/color}, line {color=#f00}2{/color}, in <module>\n        user_input_integer {color=#0f0}={/color} {color=#57f}int{/color}(user_input)\n    {color=#57f}ValueError{/color}: invalid literal for {color=#57f}int{/color}() with base {color=#f00}10{/color}: {color=#f00}'carrot'{/color}{/font}\n\nТеперь мы знаем опасное место и готовы его защитить.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
define persistent.chapter08_02_04_correct = {"a": False,  "b": True, "c": False,  "d": False}
default chapter08_02_04_student = {k: False for k in persistent.chapter08_02_04_correct}
define persistent.chapter08_02_04_options = {
    "a": "{font=monospace.ttf}NameError{/font} (вызывается при обращении к несуществующей переменной)",
    "b": "{font=monospace.ttf}IndexError{/font} (вызывается при обращении к несуществующему индексу списка)",
    "c": "{font=monospace.ttf}ZeroDivisionError{/font} (вызывается при попытке деления на 0)",
    "d": "Никакого исключения не возникнет",
}
screen chapter08_02_04_screen:
    if "chapter08_02_04" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter08_02_04" in INCORRECT:
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
    text "4 / " + str(persistent.NUM_PAGES["chapter08_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_02_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_02_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Какое исключение (если вообще возникнет) произойдет при выполнении следующего кода?\n\n{font=monospace.ttf}    arr {color=#0f0}={/color} [[{color=#f00}1{/color}, {color=#f00}2{/color}, {color=#f00}3{/color}]\n    ind {color=#0f0}={/color} {color=#f00}42{/color}\n    den {color=#0f0}={/color} {color=#f00}0{/color}\n    {color=#57f}print{/color}(arr[[ind]{color=#0f0}/{/color}den){/font}"
        for ol in sorted(persistent.chapter08_02_04_options.keys()):
            if "chapter08_02_04" in COMPLETED:
                if persistent.chapter08_02_04_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter08_02_04_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter08_02_04_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter08_02_04_options[ol])) action [Function(set_all, chapter08_02_04_student, False, from_label="chapter08_02_04"), ToggleDict(chapter08_02_04_student, ol)]
        if "chapter08_02_04" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter08_02_04", persistent.chapter08_02_04_correct, chapter08_02_04_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter08_02_04_student, False, from_label="chapter08_02_04")

# page 5
define persistent.chapter08_02_05_correct = {"a": False,  "b": False, "c": True,  "d": False}
default chapter08_02_05_student = {k: False for k in persistent.chapter08_02_05_correct}
define persistent.chapter08_02_05_options = {
    "a": "{font=monospace.ttf}NameError{/font} (вызывается при обращении к несуществующей переменной)",
    "b": "{font=monospace.ttf}IndexError{/font} (вызывается при обращении к несуществующему индексу списка)",
    "c": "{font=monospace.ttf}ZeroDivisionError{/font} (вызывается при попытке деления на 0)",
    "d": "Никакого исключения не возникнет",
}
screen chapter08_02_05_screen:
    if "chapter08_02_05" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter08_02_05" in INCORRECT:
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
    text "5 / " + str(persistent.NUM_PAGES["chapter08_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_02_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_02_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Какое исключение (если вообще возникнет) произойдет при выполнении следующего кода?\n\n{font=monospace.ttf}    arr {color=#0f0}={/color} [[{color=#f00}1{/color}, {color=#f00}2{/color}, {color=#f00}3{/color}]\n    ind {color=#0f0}={/color} {color=#f00}2{/color}\n    den {color=#0f0}={/color} {color=#f00}0{/color}\n    {color=#57f}print{/color}(arr[[ind]{color=#0f0}/{/color}den){/font}"
        for ol in sorted(persistent.chapter08_02_05_options.keys()):
            if "chapter08_02_05" in COMPLETED:
                if persistent.chapter08_02_05_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter08_02_05_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter08_02_05_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter08_02_05_options[ol])) action [Function(set_all, chapter08_02_05_student, False, from_label="chapter08_02_05"), ToggleDict(chapter08_02_05_student, ol)]
        if "chapter08_02_05" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter08_02_05", persistent.chapter08_02_05_correct, chapter08_02_05_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter08_02_05_student, False, from_label="chapter08_02_05")

# page 6
screen chapter08_02_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter08_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_02_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_02_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Конструкция обработки исключений в Python состоит из блока {b}{i}{color=#f00}try{/color}{/i}{/b} и блока {b}{i}{color=#0f0}except{/color}{/i}{/b}. Вместе они образуют конструкцию {b}{i}{color=#f00}try{/color}-{color=#0f0}except{/color}{/i}{/b}:\n\n    1. Выделяем опасный участок кода, где возможна ошибка ({color=#f00}try{/color})\n    2. Задаем действия, если ошибка произойдет ({color=#0f0}except{/color})\n\nБазовый синтаксис:\n\n{font=monospace.ttf}    {color=#ff0}try{/color}:\n        {color=#f0f}# потенциально опасный код{/color}\n    {color=#ff0}except{/color}:\n        {color=#f0f}# что делать при ошибке{/color}{/font}\n\nМы оборачиваем потенциально сбойный код в {color=#f00}try{/color}. Это сигнал для Python: если внутри произойдет исключение, не крашить программу, а перейти к ветке {color=#0f0}except{/color}.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Какую строку ввода нашего любимого числа следует обернуть в try?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 7
screen chapter08_02_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter08_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_02_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_02_08"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Опасная операция — преобразование {font=monospace.ttf}{color=#57f}str{/color}{/font} в {font=monospace.ttf}{color=#57f}int{/color}{/font}. Поэтому оборачиваем в {color=#f00}try{/color} {b}{i}только эту строку{/i}{/b}:\n\n{font=monospace.ttf}    user_input {color=#0f0}={/color} {color=#57f}input{/color}({color=#f00}\"Enter your favorite number: \"{/color})\n    {color=#ff0}try{/color}:\n        user_input_integer {color=#0f0}={/color} {color=#57f}int{/color}(user_input)\n    {color=#ff0}except{/color} {font=monospace.ttf}{color=#57f}ValueError{/color}{/font}:\n        {color=#57f}print{/color}({color=#f00}\"That wasn't a valid number!\"{/color})\n        {color=#57f}exit{/color}({color=#f00}1{/color})\n    {color=#57f}print{/color}({color=#f00}\"Two divided by your favorite number is\"{/color}, {color=#f00}2{/color} {color=#0f0}/{/color} user_input_integer){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Как сделать поведение программы еще более удобным для пользователя при ошибке?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 8
screen chapter08_02_08_screen:
    text "8 / " + str(persistent.NUM_PAGES["chapter08_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_02_07"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_02_09"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Неприятно, когда приложение просто завершает работу из-за одной опечатки. В хороших программах пользователю дают возможность повторить ввод. Для этого блоки {color=#f00}try{/color}-{color=#0f0}except{/color} помещают в {b}{i}бесконечный цикл{/i}{/b}, прерываемый командой {font=monospace.ttf}{color=#ff0}break{/color}{/font} при успешном вводе:\n\n{font=monospace.ttf}    {color=#ff0}while{/color} {color=#f00}True{/color}:\n        user_input {color=#0f0}={/color} {color=#57f}input{/color}({color=#f00}\"Enter your favorite number: \"{/color})\n        {color=#ff0}try{/color}:\n            user_input_integer {color=#0f0}={/color} {color=#57f}int{/color}(user_input)\n            {color=#ff0}break{/color}\n        {color=#ff0}except{/color} {font=monospace.ttf}{color=#57f}ValueError{/color}{/font}:\n            {color=#57f}print{/color}({color=#f00}\"That wasn't a valid number! Try again.\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Two divided by your favorite number is\"{/color}, {color=#f00}2{/color} {color=#0f0}/{/color} user_input_integer){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Может ли этот код все еще вызвать ошибку?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 9
screen chapter08_02_09_screen:
    text "9 / " + str(persistent.NUM_PAGES["chapter08_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_02_08"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter08"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Если ввести {color=#f00}\"0\"{/color}, в последней строке произойдет деление на ноль: {font=monospace.ttf}{color=#57f}ZeroDivisionError{/color}{/font}.\n\nМы можем добавить второй блок {color=#0f0}except{/color} к тому же самому блоку {color=#f00}try{/color}:\n\n{font=monospace.ttf}{size=-8}    {color=#ff0}while{/color} {color=#f00}True{/color}:\n        user_input {color=#0f0}={/color} {color=#57f}input{/color}({color=#f00}\"Enter your favorite number: \"{/color})\n        {color=#ff0}try{/color}:\n            user_input_integer {color=#0f0}={/color} {color=#57f}int{/color}(user_input)\n            {color=#57f}print{/color}({color=#f00}\"Two divided by your favorite number is\"{/color}, {color=#f00}2{/color} {color=#0f0}/{/color} user_input_integer)\n            {color=#ff0}break{/color}\n        {color=#ff0}except{/color} {font=monospace.ttf}{color=#57f}ValueError{/color}{/font}:\n            {color=#57f}print{/color}({color=#f00}\"That wasn't a valid number! Try again.\"{/color})\n        {color=#ff0}except{/color} {font=monospace.ttf}{color=#57f}ZeroDivisionError{/color}{/font}:\n            {color=#57f}print{/color}({color=#f00}\"Sorry, your favorite number can't be zero. Get creative!\"{/color}){/size}{/font}\n\nОбработчики {color=#0f0}except{/color} проверяются сверху вниз: срабатывает первая подходящая ветка.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
