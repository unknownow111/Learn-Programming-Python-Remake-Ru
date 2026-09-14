# chapter and lesson labels
label chapter03_04_01:
    $ COMPLETED.add("chapter03_04_01"); save_game()
    call screen chapter03_04_01_screen
label chapter03_04_02:
    call screen chapter03_04_02_screen
label chapter03_04_03:
    $ COMPLETED.add("chapter03_04_03"); save_game()
    call screen chapter03_04_03_screen
label chapter03_04_04:
    $ COMPLETED.add("chapter03_04_04"); save_game()
    call screen chapter03_04_04_screen
label chapter03_04_05:
    call screen chapter03_04_05_screen
label chapter03_04:
    jump chapter03_04_01
    jump chapter_select

# page 1
screen chapter03_04_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter03_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter03_04_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Мы уже умеем запускать циклы while и for по заданным диапазонам. Но что если требуется прервать выполнение цикла досрочно прямо в середине итерации?\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Попробуйте решить задачу: дана строка {font=monospace.ttf}{color=#888}data{/color}{/font}, нужно напечатать индекс первого вхождения буквы {font=monospace.ttf}{color=#f00}\"a\"{/color}{/font}.\n\nПервая мысль — написать следующий цикл:\n\n{font=monospace.ttf}    i {color=#0f0}={/color} {color=#f00}0{/color}\n    {color=#ff0}while{/color} i {color=#0f0}<{/color} {color=#57f}len{/color}(data):\n        {color=#ff0}if{/color} data[[i] {color=#0f0}=={/color} {color=#f00}\"a\"{/color}:\n            {color=#57f}print{/color}(i)\n        i {color=#0f0}+={/color} {color=#f00}1{/color}{/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} В чем ошибка этого кода?\n\nЭтот код напечатает {b}{i}все{/i}{/b} индексы, где встречается буква \"a\", а не только первый! Нам же нужно немедленно прекратить работу цикла, как только сработает условие if. Для этого используется инструкция {font=monospace.ttf}{color=#ff0}break{/color}{/font}, которая немедленно завершает текущий цикл:\n\n{font=monospace.ttf}    i {color=#0f0}={/color} {color=#f00}0{/color}\n    {color=#ff0}while{/color} i {color=#0f0}<{/color} {color=#57f}len{/color}(data):\n        {color=#ff0}if{/color} data[[i] {color=#0f0}=={/color} {color=#f00}\"a\"{/color}:\n            {color=#57f}print{/color}(i)\n            {color=#ff0}break{/color}\n        i {color=#0f0}+={/color} {color=#f00}1{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "stop_sign.png":
        xsize 550
        ysize 549
        xalign 0.8
        yalign .98

# page 2
define persistent.chapter03_04_02_correct = "alppla"
default chapter03_04_02_student = ""
screen chapter03_04_02_screen:
    if "chapter03_04_02" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter03_04_02" in INCORRECT:
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
    text "2 / " + str(persistent.NUM_PAGES["chapter03_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03_04_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter03_04_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Что будет напечатано на экране при выполнении следующего кода?\n\n{font=monospace.ttf}    text {color=#0f0}={/color} {color=#f00}\"alphabet\"{/color}\n    i {color=#0f0}={/color} {color=#f00}0{/color}\n\n    {color=#ff0}while{/color} i {color=#0f0}<={/color} {color=#f00}5{/color}:\n        {color=#ff0}if{/color} text[[i] {color=#0f0}=={/color} {color=#f00}\"h\"{/color}:\n            {color=#57f}print{/color}({color=#f00}\"pla\"{/color})\n            {color=#ff0}break{/color}\n        {color=#57f}print{/color}(text[[i], end{color=#0f0}={/color}{color=#f00}\"\"{/color})\n        i {color=#0f0}+={/color} {color=#f00}1{/color}{/font}"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter03_04_02" in COMPLETED:
                text "{b}{color=#0f0}" + persistent.chapter03_04_02_correct + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter03_04_02_student")
        if "chapter03_04_02" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter03_04_02", persistent.chapter03_04_02_correct, chapter03_04_02_student, ignore_chars="\"'")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter03_04_02_student",""), RemoveFromSet(INCORRECT,"chapter03_04_02")]

# page 3
screen chapter03_04_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter03_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03_04_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter03_04_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "А что если вместо полного прерывания цикла через {font=monospace.ttf}{color=#ff0}break{/color}{/font} мы хотим лишь пропустить {b}{i}текущую{/i}{/b} итерацию и сразу перейти к следующей? Для этого служит инструкция {font=monospace.ttf}{color=#ff0}continue{/color}{/font}!\n\nНапример, напечатаем все символы строки {font=monospace.ttf}{color=#888}data{/color}{/font}, кроме буквы {font=monospace.ttf}{color=#f00}\"a\"{/color}{/font}:\n\n{font=monospace.ttf}    {color=#ff0}for{/color} char {color=#0f0}in{/color} data:\n        {color=#ff0}if{/color} char {color=#0f0}=={/color} {color=#f00}\"a\"{/color}:\n            {color=#ff0}continue{/color}\n        {color=#57f}print{/color}(char){/font}\n\nА вот попытка решить ту же задачу через цикл while:\n\n{font=monospace.ttf}    i {color=#0f0}={/color} {color=#f00}0{/color}\n    {color=#ff0}while{/color} i {color=#0f0}<{/color} {color=#57f}len{/color}(data):\n        {color=#ff0}if{/color} data[[i] {color=#0f0}=={/color} {color=#f00}\"a\"{/color}:\n            {color=#ff0}continue{/color}\n        {color=#57f}print{/color}(data[[i])\n        i {color=#0f0}+={/color} 1{/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Один из вариантов выше приведет к фатальной ошибке. Какой и почему?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter03_04_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter03_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03_04_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter03_04_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "В цикле for переменная итерации переключается автоматически. Поэтому при вызове {font=monospace.ttf}{color=#ff0}continue{/color}{/font} цикл for сразу берет следующий символ строки.\n\nА вот в цикле while строка обновления счетчика ({font=monospace.ttf}{color=#888}i{/color} {color=#0f0}+={/color} {color=#f00}1{/color}{/font}) находится внизу тела цикла! Сработав, {font=monospace.ttf}{color=#ff0}continue{/color}{/font} пропускает весь оставшийся код, включая увеличение счетчика. В следующей итерации {font=monospace.ttf}{color=#888}i{/color}{/font} не изменится, условие снова сработает и снова вызовет {font=monospace.ttf}{color=#ff0}continue{/color}{/font}. Цикл зациклится навечно — возникнет {b}{i}бесконечный цикл (infinite loop){/i}{/b}.\n\nИсправить это можно, добавив увеличение счетчика прямо внутрь ветки if:\n\n{font=monospace.ttf}    i {color=#0f0}={/color} {color=#f00}0{/color}\n    {color=#ff0}while{/color} i {color=#0f0}<{/color} {color=#57f}len{/color}(data):\n        {color=#ff0}if{/color} data[[i] {color=#0f0}=={/color} {color=#f00}\"a\"{/color}:\n            i {color=#0f0}+={/color} 1\n            {color=#ff0}continue{/color}\n        {color=#57f}print{/color}(data[[i])\n        i {color=#0f0}+={/color} 1{/font}\n\nЛибо перенести увеличение счетчика {b}{i}перед{/i}{/b} проверкой if:\n\n{font=monospace.ttf}    i {color=#0f0}={/color} {color=#f00}-1{/color}\n    {color=#ff0}while{/color} (i {color=#0f0}+{/color} 1) {color=#0f0}<{/color} {color=#57f}len{/color}(data):\n        i {color=#0f0}+={/color} 1\n        {color=#ff0}if{/color} data[[i] {color=#0f0}=={/color} {color=#f00}\"a\"{/color}:\n            {color=#ff0}continue{/color}\n        {color=#57f}print{/color}(data[[i]){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
define persistent.chapter03_04_05_correct = "alppla,ab"
default chapter03_04_05_student = ""
screen chapter03_04_05_screen:
    if "chapter03_04_05" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter03_04_05" in INCORRECT:
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
    text "5 / " + str(persistent.NUM_PAGES["chapter03_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03_04_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Что будет напечатано при выполнении кода ниже?\n\n{font=monospace.ttf}    text {color=#0f0}={/color} {color=#f00}\"alphabet\"{/color}\n    i {color=#0f0}={/color} {color=#f00}0{/color}\n\n    {color=#ff0}while{/color} i {color=#0f0}<={/color} {color=#f00}5{/color}:\n        {color=#ff0}if{/color} text[[i] {color=#0f0}=={/color} {color=#f00}\"h\"{/color}:\n            {color=#57f}print{/color}({color=#f00}\"pla\"{/color}, end{color=#0f0}={/color}{color=#f00}\",\"{/color})\n            i {color=#0f0}+={/color} {color=#f00}1{/color}\n            {color=#ff0}continue{/color}\n        {color=#57f}print{/color}(text[[i], end{color=#0f0}={/color}{color=#f00}\"\"{/color})\n        i {color=#0f0}+={/color} {color=#f00}1{/color}{/font}"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter03_04_05" in COMPLETED:
                text "{b}{color=#0f0}" + persistent.chapter03_04_05_correct + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter03_04_05_student")
        if "chapter03_04_05" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter03_04_05", persistent.chapter03_04_05_correct, chapter03_04_05_student, ignore_chars="\"'")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter03_04_05_student",""), RemoveFromSet(INCORRECT,"chapter03_04_05")]
