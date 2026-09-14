# chapter and lesson labels
label chapter01_04_01:
    $ COMPLETED.add("chapter01_04_01"); save_game()
    call screen chapter01_04_01_screen
label chapter01_04_02:
    $ COMPLETED.add("chapter01_04_02"); save_game()
    call screen chapter01_04_02_screen
label chapter01_04_03:
    call screen chapter01_04_03_screen
label chapter01_04_04:
    call screen chapter01_04_04_screen
label chapter01_04_05:
    $ COMPLETED.add("chapter01_04_05"); save_game()
    call screen chapter01_04_05_screen
label chapter01_04_06:
    $ COMPLETED.add("chapter01_04_06"); save_game()
    call screen chapter01_04_06_screen
label chapter01_04_07:
    $ COMPLETED.add("chapter01_04_07"); save_game()
    call screen chapter01_04_07_screen
label chapter01_04_08:
    call screen chapter01_04_08_screen
label chapter01_04_09:
    call screen chapter01_04_09_screen
label chapter01_04_10:
    $ COMPLETED.add("chapter01_04_10"); save_game()
    call screen chapter01_04_10_screen
label chapter01_04_11:
    $ COMPLETED.add("chapter01_04_11"); save_game()
    call screen chapter01_04_11_screen
label chapter01_04_12:
    $ COMPLETED.add("chapter01_04_12"); save_game()
    call screen chapter01_04_12_screen
label chapter01_04_13:
    $ COMPLETED.add("chapter01_04_13"); save_game()
    call screen chapter01_04_13_screen
label chapter01_04:
    jump chapter01_04_01
    jump chapter_select

# page 1
screen chapter01_04_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь подробнее разберем строки (а вскоре исследуем {font=monospace.ttf}{color=#57f}int{/color}{/font}, {font=monospace.ttf}{color=#57f}float{/color}{/font} и {font=monospace.ttf}{color=#57f}bool{/color}{/font}).\n\nПредположим, мы присвоили переменной {font=monospace.ttf}{color=#888}foobar{/color}{/font} следующее значение:\n\n{font=monospace.ttf}    foobar {color=#0f0}={/color} {color=#f00}\"goat legs\"{/color}{/font}\n\nПодумайте над следующим:\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Какой символ находится на позиции 1?\n\nКажется очевидным, что ответ — {font=monospace.ttf}{color=#888}g{/color}{/font}. Однако в программировании это не так! В Python (как и во многих языках) используется {b}{i}нулевая индексация (zero-indexing){/i}{/b}. Это означает, что \"первый\" элемент имеет индекс 0, \"второй\" — индекс 1 и так далее. Как видно из таблицы ниже, на позиции 1 в строке {font=monospace.ttf}{color=#888}foobar{/color}{/font} на самом деле находится буква {font=monospace.ttf}{color=#888}o{/color}{/font}.\n\n{font=monospace.ttf}    -------------------------------------------------\n    | {color=#57f}Индекс{/color}    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |\n    -------------------------------------------------\n    | {color=#57f}Символ{/color}    | g | o | a | t |   | l | e | g | s |\n    -------------------------------------------------{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "string.png":
        xsize 1500
        ysize 379
        xalign 0.8
        yalign .85

# page 2
screen chapter01_04_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Как получить доступ к определенному символу строки? Для этого используется {b}{i}оператор индексации{/i}{/b} — квадратные скобки. Например, мы можем сохранить первый символ строки {font=monospace.ttf}{color=#888}foobar{/color}{/font} (находящийся, помните, по индексу 0) в отдельную переменную:\n\n{font=monospace.ttf}    first {color=#0f0}={/color} foobar[[{color=#f00}0{/color}]{/font}\n\nОднако оператор индексации умеет не только извлекать одиночные символы: он позволяет получать срез последовательных символов строки — {b}{i}подстроку (substring){/i}{/b}. Срез строки извлекается по общему шаблону ниже, где {font=monospace.ttf}{color=#888}start{/color}{/font} и {font=monospace.ttf}{color=#888}end{/color}{/font} — целые числа ({color=#57f}int{/color}), обозначающие начальный и конечный индекс подстроки:\n\n{font=monospace.ttf}    substring {color=#0f0}={/color} string[[start : end {color=#0f0}+{/color} 1]{/font}\n\nК примеру, подстрока с позиций 1 по 3 в строке {font=monospace.ttf}{color=#f00}\"goat legs\"{/color}{/font} — это {font=monospace.ttf}{color=#f00}\"oat\"{/color}{/font}.\n\n{font=monospace.ttf}    -------------------------------------------------\n    | {color=#57f}Индекс{/color}    | 0 | {color=#f00}1{/color} | {color=#f00}2{/color} | {color=#f00}3{/color} | 4 | 5 | 6 | 7 | 8 |\n    -------------------------------------------------\n    | {color=#57f}Символ{/color}    | g | {color=#f00}o{/color} | {color=#f00}a{/color} | {color=#f00}t{/color} |   | l | e | g | s |\n    -------------------------------------------------{/font}\n\nМы извлекаем эту подстроку следующим образом:\n\n{font=monospace.ttf}    substring {color=#0f0}={/color} foobar[[{color=#f00}1{/color}:{color=#f00}4{/color}]{/font}\n\nВас может удивить, почему правый индекс указан как 4, а не 3. Дело в том, что в срезах Python правая граница {b}{i}не включается{/i}{/b} (exclusive) — подстрока извлекается {b}{i}вплоть до указанного индекса, не включая его{/i}{/b}. (Именно поэтому в общем шаблоне среза записано {font=monospace.ttf}{color=#888}end{/color} {color=#0f0}+{/color} {color=#f00}1{/color}{/font}).\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Судя по примеру, левая граница (start) является включающей или невключающей?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
define persistent.chapter01_04_03_correct = "a"
default chapter01_04_03_student = ""
screen chapter01_04_03_screen:
    if "chapter01_04_03" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter01_04_03" in INCORRECT:
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
    text "3 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Каково значение переменной {font=monospace.ttf}{color=#888}ans{/color}{/font} после выполнения следующего кода?\n\n{font=monospace.ttf}    res {color=#0f0}={/color} {color=#f00}\"Programming is fun!\"{/color}\n    ans {color=#0f0}={/color} res[[{color=#f00}5{/color}]{/font}\n\nКавычки вокруг ответа ставить не нужно."
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter01_04_03" in COMPLETED:
                text "{b}{color=#0f0}" + persistent.chapter01_04_03_correct + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter01_04_03_student")
        if "chapter01_04_03" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter01_04_03", persistent.chapter01_04_03_correct, chapter01_04_03_student, ignore_chars="\"'")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter01_04_03_student",""), RemoveFromSet(INCORRECT,"chapter01_04_03")]

# page 4
define persistent.chapter01_04_04_correct = "rogr"
default chapter01_04_04_student = ""
screen chapter01_04_04_screen:
    if "chapter01_04_04" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter01_04_04" in INCORRECT:
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
    text "4 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Каково значение переменной {font=monospace.ttf}{color=#888}ans{/color}{/font} после выполнения следующего кода?\n\n{font=monospace.ttf}    res {color=#0f0}={/color} {color=#f00}\"Programming is fun!\"{/color}\n    ans {color=#0f0}={/color} res[[{color=#f00}1{/color}:{color=#f00}5{/color}]{/font}\n\nКавычки вокруг ответа ставить не нужно."
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter01_04_04" in COMPLETED:
                text "{b}{color=#0f0}" + persistent.chapter01_04_04_correct + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter01_04_04_student")
        if "chapter01_04_04" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter01_04_04", persistent.chapter01_04_04_correct, chapter01_04_04_student, ignore_chars="\"'")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter01_04_04_student",""), RemoveFromSet(INCORRECT,"chapter01_04_04")]

# page 5
screen chapter01_04_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Одна из самых частых операций над строкой — узнать ее длину (общее количество символов в строке). Для этого достаточно вызвать функцию {font=monospace.ttf}{color=#57f}len{/color}{color=#888}(){/color}{/font}*.\n\nНапример, мы можем сохранить длину строки {font=monospace.ttf}{color=#888}foobar{/color}{/font} в переменную с именем {font=monospace.ttf}{color=#888}length_of_foobar{/color}{/font}:\n\n{font=monospace.ttf}    foobar {color=#0f0}={/color} {color=#f00}\"goat legs\"{/color}\n    length_of_foobar {color=#0f0}={/color} {color=#57f}len{/color}(foobar){/font}\n\nФункцию {font=monospace.ttf}{color=#57f}len{/color}{/font} можно вызывать не только для переменной, но и напрямую для явно заданной строки:\n\n{font=monospace.ttf}    length_of_string {color=#0f0}={/color} {font=monospace.ttf}{color=#57f}len{/color}{/font}({color=#f00}\"goat legs\"{/color}){/font}\n\n\n{i}*Подробнее о функциях мы поговорим чуть позже. Пока воспринимайте функцию как удобный способ повторно совершать определенное действие над переданными данными. (Или просто как маленькую магию, если хотите!){/i}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter01_04_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Две наиболее частые операции среза подстроки:\n\n    1. Получение префикса (начала строки) до индекса {font=monospace.ttf}{color=#888}N{/color}{/font}\n    2. Получение суффикса (окончания строки), начиная с индекса {font=monospace.ttf}{color=#888}N{/color}{/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Как бы мы извлекли эти подстроки, используя оператор среза?\n\nПолучить префикс строки {font=monospace.ttf}{color=#888}foobar{/color}{/font} (включая индекс {font=monospace.ttf}{color=#888}N{/color}{/font}) и суффикс (начиная с индекса {font=monospace.ttf}{color=#888}N{/color}{/font}) можно так:\n\n{font=monospace.ttf}    prefix {color=#0f0}={/color} foobar[[{color=#f00}0{/color} : N {color=#0f0}+{/color} {color=#f00}1{/color}]\n    suffix {color=#0f0}={/color} foobar[[N : {color=#57f}len{/color}(foobar)]{/font}\n\nОднако в Python существует удобная сокращенная запись: если опустить левый индекс, Python автоматически считает его равным 0. Если же опустить правый индекс, Python берет срез до самого конца строки. Таким образом, строки ниже полностью эквивалентны коду выше:\n\n{font=monospace.ttf}    prefix {color=#0f0}={/color} foobar[[:N {color=#0f0}+{/color} {color=#f00}1{/color}]\n    suffix {color=#0f0}={/color} foobar[[N:]{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 7
screen chapter01_04_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_08"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Что вы думаете о следующем коде?\n\n{font=monospace.ttf}    res {color=#0f0}={/color} {color=#f00}\"12 is > than 1.\"{/color}\n    hogwash {color=#0f0}={/color} res[[{color=#f00}-4{/color}]{/font}\n\nОтрицательный индекс? На первый взгляд это бессмыслица. Но в Python это абсолютно корректно и очень удобно! Отрицательный индекс {font=monospace.ttf}{color=#888}-n{/color}{/font} означает {font=monospace.ttf}{color=#888}n{/color}{/font}-й символ {b}{i}с конца строки{/i}{/b}. В нашем примере {color=#f00}-4{/color} — это 4-й символ с конца: буква {color=#f00}n{/color}.\n\nРаботу {b}{i}{color=#f00}отрицательных индексов{/font}{/i}{/b} удобно представить наглядно на примере строки {font=monospace.ttf}{color=#888}res{/color}{/font}:\n\n{font=monospace.ttf}    --------------------------------------------------------------------------\n    | {color=#57f}Индекс{/color}    | ... | {color=#f00}-5{/color} | {color=#f00}-4{/color} | {color=#f00}-3{/color} | {color=#f00}-2{/color} | {color=#f00}-1{/color} | 0 | 1 | 2 | 3 | 4 | 5 | ... |\n    --------------------------------------------------------------------------\n    | {color=#57f}Символ{/color}    | ... |  {color=#f00}a{/color} |  {color=#f00}n{/color} |    |  {color=#f00}1{/color} |  {color=#f00}.{/color} | 1 | 2 |   | i | s |   | ... |\n    --------------------------------------------------------------------------{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 8
define persistent.chapter01_04_08_correct = "h"
default chapter01_04_08_student = ""
screen chapter01_04_08_screen:
    if "chapter01_04_08" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter01_04_08" in INCORRECT:
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
    text "8 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_07"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_09"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Каково значение переменной {font=monospace.ttf}{color=#888}ans{/color}{/font} после выполнения следующего кода?\n\n{font=monospace.ttf}    res {color=#0f0}={/color} {color=#f00}\"12 is > than 1.\"{/color}\n    ans {color=#0f0}={/color} res[[{color=#f00}-6{/color}]{/font}\n\nОтветом должна быть извлеченная подстрока. Кавычки вокруг ответа ставить не нужно."
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter01_04_08" in COMPLETED:
                text "{b}{color=#0f0}" + persistent.chapter01_04_08_correct + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter01_04_08_student")
        if "chapter01_04_08" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter01_04_08", persistent.chapter01_04_08_correct, chapter01_04_08_student, ignore_chars="\"'")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter01_04_08_student",""), RemoveFromSet(INCORRECT,"chapter01_04_08")]

# page 9
define persistent.chapter01_04_09_correct = "an 1"
default chapter01_04_09_student = ""
screen chapter01_04_09_screen:
    if "chapter01_04_09" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter01_04_09" in INCORRECT:
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
    text "9 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_08"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_10"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Каково значение переменной {font=monospace.ttf}{color=#888}ans{/color}{/font} после выполнения следующего кода?\n\n{font=monospace.ttf}    res {color=#0f0}={/color} {color=#f00}\"12 is > than 1.\"{/color}\n    ans {color=#0f0}={/color} res[[{color=#f00}-5{/color}:{color=#f00}-1{/color}]{/font}\n\nОтветом должна быть извлеченная подстрока. Кавычки вокруг ответа ставить не нужно."
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter01_04_09" in COMPLETED:
                text "{b}{color=#0f0}" + persistent.chapter01_04_09_correct + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter01_04_09_student")
        if "chapter01_04_09" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter01_04_09", persistent.chapter01_04_09_correct, chapter01_04_09_student, ignore_chars="\"'")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter01_04_09_student",""), RemoveFromSet(INCORRECT,"chapter01_04_09")]

# page 10
screen chapter01_04_10_screen:
    text "10 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_09"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_11"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь мы умеем разбивать строку на подстроки с помощью индексов и срезов. А что если требуется наоборот — соединить (сконкатенировать) несколько строк?\n\nДля этого используется {b}оператор {font=monospace.ttf}{color=#0f0}+{/color}{/font}{/b}! К примеру, мы можем соединить {font=monospace.ttf}{color=#888}one{/color}{/font}, {font=monospace.ttf}{color=#888}two{/color}{/font} и {font=monospace.ttf}{color=#888}three{/color}{/font} в переменную {font=monospace.ttf}{color=#888}one_two_three{/color}{/font}:\n\n{font=monospace.ttf}    one {color=#0f0}={/color} {color=#f00}\"Py\"{/color}\n    two {color=#0f0}={/color} {color=#f00}\"th\"{/color}\n    three {color=#0f0}={/color} {color=#f00}\"on\"{/color}\n    one_two_three {color=#0f0}={/color} one {color=#0f0}+{/color} two {color=#0f0}+{/color} three{/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Каково значение переменной {font=monospace.ttf}{color=#888}one_two_three{/color}{/font} после выполнения кода выше?\n\nPython поддерживает конкатенацию только строк со строками. Если требуется соединить со строкой данные другого типа, их необходимо сначала преобразовать в {b}{i}строковое представление{/i}{/b} встроенной функцией {font=monospace.ttf}{color=#57f}str{/color}{color=#888}(){/color}{/font}. Например, объединим {font=monospace.ttf}{color=#888}a{/color}{/font}, {font=monospace.ttf}{color=#888}b{/color}{/font} и {font=monospace.ttf}{color=#888}c{/color}{/font} в {font=monospace.ttf}{color=#888}abc{/color}{/font}, получив строку со значением {font=monospace.ttf}{color=#f00}\"True2Life\"{/color}{/font}:\n\n{font=monospace.ttf}    a {color=#0f0}={/color} {color=#f00}True{/color}\n    b {color=#0f0}={/color} {color=#f00}2{/color}\n    c {color=#0f0}={/color} {color=#f00}\"Life\"{/color}\n    abc {color=#0f0}={/color} {color=#57f}str{/color}(a) {color=#0f0}+{/color} {color=#57f}str{/color}(b) {color=#0f0}+{/color} c{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 11
screen chapter01_04_11_screen:
    text "11 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_10"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_12"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Как мы знаем, по умолчанию Python воспринимает каждую новую строку файла как отдельную команду.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Какие трудности это может вызвать при работе с длинным текстом?\n\nПредставьте, что вы хотите сохранить очень длинную цитату в переменную {font=monospace.ttf}{color=#888}long_string{/color}{/font}. Строка в редакторе растянется на сотни символов в ширину, и код станет тяжело читать и поддерживать. К счастью, Python позволяет разбить одну длинную строковую инструкцию на несколько физических строк кода, используя символ обратного слэша (\\):\n\n{font=monospace.ttf}    long_string {color=#0f0}={/color} {color=#f00}\"В норе под землей жил хоббит. \"{/color} \\\n                  {color=#f00}\"Не в сырой и грязной норе, \"{/color} \\\n                  {color=#f00}\"где пахнет червями, \"{/color} \\\n                  {color=#f00}\"и не в песчаной пустой норе: \"{/color} \\\n                  {color=#f00}\"это была уютная нора хоббита.\"{/color}{/font}\n\nВ результате получается единая цельная строка — склейка всех фрагментов. Обратите внимание: необходимо явно ставить пробелы перед закрывающими кавычками на каждой строке, иначе фрагменты сольются вместе без пробелов между словами. Это очень распространенная ошибка у новичков, будьте внимательны!":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 12
screen chapter01_04_12_screen:
    text "12 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_11"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_04_13"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Мы выяснили, как переносить длинную строку текста в редакторе. А что, если сама строка должна содержать переносы строк при выводе на экран (быть многострочной)? Например, если мы хотим сохранить в переменную следующий стих:\n\n{font=monospace.ttf}{color=#f00}    One Fish\n    Two Fish\n    Red Fish\n    Blue Fish{/color}{/font}\n\nОдин вариант — вручную вставить {a=https://en.wikipedia.org/wiki/Newline}символ переноса строки{/a} ({font=monospace.ttf}{color=#f00}\\n{/color}{/font}) в местах перехода на новую строку:\n\n{font=monospace.ttf}    text {color=#0f0}={/color} {color=#f00}\"One Fish\\nTwo Fish\\nRed Fish\\nBlue Fish\"{/color}{/font}\n\nОднако читать такой код неудобно. К счастью, Python поддерживает {b}{i}многострочные строки{/i}{/b} с помощью тройных кавычек в начале и в конце строки:\n\n{font=monospace.ttf}    text {color=#0f0}={/color} {color=#f00}\"\"\"One Fish\n    Two Fish\n    Red Fish\n    Blue Fish\"\"\"{/color}{/font}\n\nЭто выглядит гораздо аккуратнее! Также можно использовать тройные одинарные кавычки ({font=monospace.ttf}{color=#888}'''{/color}{/font}):\n\n{font=monospace.ttf}    text {color=#0f0}={/color} {color=#f00}'''One Fish\n    Two Fish\n    Red Fish\n    Blue Fish'''{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 13
screen chapter01_04_13_screen:
    text "13 / " + str(persistent.NUM_PAGES["chapter01_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_04_12"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Важно помнить, что строки в Python {b}{i}неизменяемы (immutable){/i}{/b}: после создания строки ее содержимое нельзя изменить на месте. Например, если объявлена строка:\n\n{font=monospace.ttf}    foo {color=#0f0}={/color} {color=#f00}\"Hello, partner!\"{/color}{/font}\n\nМы не можем заменить отдельный символ в этой строке. Следующий код вызовет ошибку:\n\n{font=monospace.ttf}    foo[[{color=#f00}0{/color}] {color=#0f0}={/color} {color=#f00}\"J\"{/color}{/font}\n\nЕсли вы хотите изменить значение переменной {font=monospace.ttf}{color=#888}foo{/color}{/font}, строку придется сформировать заново:\n\n{font=monospace.ttf}    foo {color=#0f0}={/color} {color=#f00}\"Jello, partner!\"{/color}{/font}\n\nА чтобы изменить строку программно (не перепечатывая ее целиком вручную), можно собрать новую строку из частей через срез и оператор сложения:\n\n{font=monospace.ttf}    foo {color=#0f0}={/color} {color=#f00}\"J\"{/color} {color=#0f0}+{/color} foo[[{color=#f00}1{/color}:]{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
