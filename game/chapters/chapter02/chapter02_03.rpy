# chapter and lesson labels
label chapter02_03_01:
    $ COMPLETED.add("chapter02_03_01"); save_game()
    call screen chapter02_03_01_screen
label chapter02_03_02:
    call screen chapter02_03_02_screen
label chapter02_03_03:
    $ COMPLETED.add("chapter02_03_03"); save_game()
    call screen chapter02_03_03_screen
label chapter02_03_04:
    $ COMPLETED.add("chapter02_03_04"); save_game()
    call screen chapter02_03_04_screen
label chapter02_03_05:
    call screen chapter02_03_05_screen
label chapter02_03:
    jump chapter02_03_01
    jump chapter_select

# page 1
screen chapter02_03_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter02_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_03_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь мы готовы использовать логические выражения для управления потоком программы с помощью {b}{i}инструкции if (ветвления){/i}{/b}. Блок if выполняется только в том случае, если проверяемое логическое выражение истинно ({font=monospace.ttf}{color=#f00}True{/color}{/font}). Базовая структура выглядит так:\n\n{font=monospace.ttf}    {color=#f0f}# код до проверки условия if{/color}\n\n    {color=#ff0}if{/color} logical_expression:\n        {color=#f0f}# код внутри блока if{/color}\n\n    {color=#f0f}# код после блока if{/color}{/font}\n\nКод до и после блока if выполнится всегда, а вот инструкции {b}{i}внутри{/i}{/b} if выполнятся только тогда, когда {font=monospace.ttf}{color=#888}logical_expression{/color}{/font} равно {font=monospace.ttf}{color=#f00}True{/color}{/font}.\n\nОбратите внимание, что принадлежность кода к блоку if в Python задается с помощью {b}{i}отступов (indentation){/i}{/b}. Любой код с отступом после строки с if составляет тело условия ({b}{i}if-блок{/i}{/b}). Правило простое: если строка оканчивается двоеточием ({font=monospace.ttf}{color=#888}:{/color}{/font}), следующие за ней строки пишутся с отступом. Первая строка без отступа означает завершение if-блока.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "conditional.png":
        xsize 1000
        ysize 675
        xalign 0.8
        yalign .96

# page 2
define persistent.chapter02_03_02_correct = "My name is Mr. Slim Shady."
default chapter02_03_02_student = ""
screen chapter02_03_02_screen:
    if "chapter02_03_02" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter02_03_02" in INCORRECT:
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
    text "2 / " + str(persistent.NUM_PAGES["chapter02_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_03_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_03_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Каково значение переменной {font=monospace.ttf}{color=#888}ans{/color}{/font} после выполнения приведенного фрагмента кода?\n\n{font=monospace.ttf}    ans {color=#0f0}={/color} {color=#f00}\"My name is \"{/color}\n    age {color=#0f0}={/color} {color=#f00}20{/color}\n\n    {color=#ff0}if{/color} age {color=#0f0}>={/color} {color=#f00}20{/color}:\n        ans {color=#0f0}={/color} ans {color=#0f0}+{/color} {color=#f00}\"Mr. \"{/color}\n\n    ans {color=#0f0}={/color} ans {color=#0f0}+{/color} {color=#f00}\"Slim Shady.\"{/color}{/font}\n\nКавычки вокруг ответа ставить не нужно."
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter02_03_02" in COMPLETED:
                text "{b}{color=#0f0}" + persistent.chapter02_03_02_correct + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter02_03_02_student")
        if "chapter02_03_02" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter02_03_02", persistent.chapter02_03_02_correct, chapter02_03_02_student, ignore_chars="\"'")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter02_03_02_student",""), RemoveFromSet(INCORRECT,"chapter02_03_02")]

# page 3
screen chapter02_03_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter02_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_03_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_03_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Оператор if позволяет задать условие для выполнения участка кода. Если условие ложно ({font=monospace.ttf}{color=#f00}False{/color}{/font}), блок кода просто пропускается. А что если при ложном условии мы хотим выполнить {b}{i}другой{/i}{/b} альтернативный код?\n\nДля этого предусмотрена ветка {b}{i}else{/i}{/b}. Блок else выполняется тогда и только тогда, когда условие в предшествующем if оказалось ложным ({font=monospace.ttf}{color=#f00}False{/color}{/font}):\n\n{font=monospace.ttf}    {color=#f0f}# код до блока ветвления{/color}\n\n    {color=#ff0}if{/color} logical_expression:\n        {color=#f0f}# код внутри ветки if{/color}\n    {color=#ff0}else{/color}:\n        {color=#f0f}# код внутри ветки else{/color}\n\n    {color=#f0f}# код после блока ветвления{/color}{/font}\n\nКод до и после блока выполняется всегда. Если {font=monospace.ttf}{color=#888}logical_expression{/color}{/font} истинно, срабатывает ветка if. Если же оно ложно — запускается ветка else.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter02_03_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter02_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_03_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_03_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Конструкция if-else дает выбор ровно из двух вариантов. А как быть, когда возможных исходов три и более? Для этого используется ключевое слово {b}{i}elif{/i}{/b} (сокращение от else-if) — оно проверяет новое условие, если предыдущее условие оказалось ложным:\n\n{font=monospace.ttf}    {color=#f0f}# код до блока{/color}\n\n    {color=#ff0}if{/color} logical_expression:\n        {color=#f0f}# код ветки if{/color}\n    {color=#ff0}elif{/color} different_logical_expression:\n        {color=#f0f}# код ветки elif{/color}\n\n    {color=#f0f}# код после блока{/color}{/font}\n\nВеток elif можно добавлять сколько угодно, а в самом конце можно добавить необязательный блок else, который сработает, если ни одно из условий выше не подошло:\n\n{font=monospace.ttf}    {color=#f0f}# код до блока{/color}\n\n    {color=#ff0}if{/color} logical_expression:\n        {color=#f0f}# код ветки if{/color}\n    {color=#ff0}elif{/color} different_logical_expression:\n        {color=#f0f}# код первой ветки elif{/color}\n    {color=#ff0}elif{/color} another_different_logical_expression:\n        {color=#f0f}# код второй ветки elif{/color}\n    ...\n    {color=#ff0}else{/color}:\n        {color=#f0f}# код ветки else (по умолчанию){/color}\n\n    {color=#f0f}# код после блока{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
define persistent.chapter02_03_05_correct = "odd"
default chapter02_03_05_student = ""
screen chapter02_03_05_screen:
    if "chapter02_03_05" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter02_03_05" in INCORRECT:
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
    text "5 / " + str(persistent.NUM_PAGES["chapter02_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_03_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Что будет напечатано на экране после выполнения следующего кода?\n\n{font=monospace.ttf}    num {color=#0f0}={/color} {color=#f00}41{/color}\n\n    {color=#ff0}if{/color} num {color=#0f0}%{/color} {color=#f00}2{/color} {color=#0f0}=={/color} {color=#f00}0{/color}:\n        {color=#57f}print{/color}({color=#f00}\"even\"{/color})\n    {color=#ff0}elif{/color} num {color=#0f0}%{/color} {color=#f00}2{/color} {color=#0f0}=={/color} {color=#f00}1{/color}:\n        {color=#57f}print{/color}({color=#f00}\"odd\"{/color})\n    {color=#ff0}else{/color}:\n        {color=#57f}print{/color}({color=#f00}\"er, what\"{/color}){/font}\n\nКавычки вокруг ответа ставить не нужно.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Выполнится ли ветка else хоть когда-нибудь?"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter02_03_05" in COMPLETED:
                text "{b}{color=#0f0}" + persistent.chapter02_03_05_correct + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter02_03_05_student")
        if "chapter02_03_05" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter02_03_05", persistent.chapter02_03_05_correct, chapter02_03_05_student, ignore_chars="\"'")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter02_03_05_student",""), RemoveFromSet(INCORRECT,"chapter02_03_05")]
