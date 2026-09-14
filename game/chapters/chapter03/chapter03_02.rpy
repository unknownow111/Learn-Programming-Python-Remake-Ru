# chapter and lesson labels
label chapter03_02_01:
    $ COMPLETED.add("chapter03_02_01"); save_game()
    call screen chapter03_02_01_screen
label chapter03_02_02:
    $ COMPLETED.add("chapter03_02_02"); save_game()
    call screen chapter03_02_02_screen
label chapter03_02_03:
    call screen chapter03_02_03_screen
label chapter03_02_04:
    $ COMPLETED.add("chapter03_02_04"); save_game()
    call screen chapter03_02_04_screen
label chapter03_02:
    jump chapter03_02_01
    jump chapter_select

# page 1
screen chapter03_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter03_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter03_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Первый тип циклов, который мы разберем — это {b}{i}цикл while{/i}{/b}. Цикл while выполняет блок инструкций до тех пор, пока проверяемое логическое выражение остается истинным ({font=monospace.ttf}{color=#f00}True{/color}{/font}). Базовая структура:\n\n{font=monospace.ttf}    {color=#f0f}# код до цикла while{/color}\n\n    {color=#ff0}while{/color} logical_expression:\n        {color=#f0f}# код тела цикла{/color}\n\n    {color=#f0f}# код после цикла while{/color}{/font}\n\nОбратите внимание на поразительное сходство между циклом while и условным оператором if:\n\n    – {b}Инструкция if:{/b} блок кода выполняется ровно один раз, {b}{i}если{/i}{/b} логическое условие равно {font=monospace.ttf}{color=#f00}True{/color}{/font}\n    – {b}Цикл while:{/b} блок кода выполняется повторно {b}{i}до тех пор, пока{/i}{/b} логическое условие равно {font=monospace.ttf}{color=#f00}True{/color}{/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Как условие, бывшее истинным ({font=monospace.ttf}{color=#f00}True{/color}{/font}) до входа в цикл, сможет стать ложным ({font=monospace.ttf}{color=#f00}False{/color}{/font}), чтобы цикл когда-нибудь завершился?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "while_loop.png":
        xsize 567
        ysize 774
        xalign 0.5
        yalign .98

# page 2
screen chapter03_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter03_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter03_02_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "В большинстве циклов while проверяемое выражение использует хотя бы одну переменную. Это необходимо для того, чтобы значение переменной изменялось внутри цикла — тогда условие, бывшее изначально {font=monospace.ttf}{color=#f00}True{/color}{/font}, со временем станет {font=monospace.ttf}{color=#f00}False{/color}{/font}.\n\nТакую переменную называют {b}{i}счетчиком цикла (переменной итерации){/i}{/b}. Обычно ее обозначают именем {font=monospace.ttf}{color=#888}i{/color}{/font} (от слова iterator/index):\n\n{font=monospace.ttf}    i {color=#0f0}={/color} {color=#f00}0{/color}              {color=#f0f}# Строка 1{/color}\n    {color=#ff0}while{/color} i {color=#0f0}<{/color} {color=#f00}2{/color}:       {color=#f0f}# Строка 2{/color}\n        {color=#57f}print{/color}(i)       {color=#f0f}# Строка 3{/color}\n        i {color=#0f0}+={/color} {color=#f00}1{/color}         {color=#f0f}# Строка 4{/color}\n    {color=#57f}print{/color}({color=#f00}\"Complete!\"{/color}) {color=#f0f}# Строка 5{/color}{/font}\n\nПорядок выполнения строк программы:\n\n    1. {color=#f0f}Строка 1:{/color} Присваиваем {font=monospace.ttf}{color=#888}i{/color}{/font} значение {font=monospace.ttf}{color=#f00}0{/color}{/font}\n    2. {color=#f0f}Строка 2:{/color} Проверяем {font=monospace.ttf}{color=#888}i{/color} {color=#0f0}<{/color} {color=#f00}2{/color}{/font} (0 < 2). Это {font=monospace.ttf}{color=#f00}True{/color}{/font}, входим в цикл\n    3. {color=#f0f}Строка 3:{/color} Печатаем {font=monospace.ttf}{color=#888}i{/color}{/font} (выводится {font=monospace.ttf}{color=#f00}0{/color}{/font})\n    4. {color=#f0f}Строка 4:{/color} Увеличиваем {font=monospace.ttf}{color=#888}i{/color}{/font} на {font=monospace.ttf}{color=#f00}1{/color}{/font}; теперь {font=monospace.ttf}{color=#888}i{/color}{/font} равно {font=monospace.ttf}{color=#f00}1{/color}{/font}\n    5. {color=#f0f}Строка 2:{/color} Проверяем {font=monospace.ttf}{color=#888}i{/color} {color=#0f0}<{/color} {color=#f00}2{/color}{/font} (1 < 2). Это {font=monospace.ttf}{color=#f00}True{/color}{/font}, продолжаем цикл\n    6. {color=#f0f}Строка 3:{/color} Печатаем {font=monospace.ttf}{color=#888}i{/color}{/font} (выводится {font=monospace.ttf}{color=#f00}1{/color}{/font})\n    7. {color=#f0f}Строка 4:{/color} Увеличиваем {font=monospace.ttf}{color=#888}i{/color}{/font} на {font=monospace.ttf}{color=#f00}1{/color}{/font}; теперь {font=monospace.ttf}{color=#888}i{/color}{/font} равно {font=monospace.ttf}{color=#f00}2{/color}{/font}\n    8. {color=#f0f}Строка 2:{/color} Проверяем {font=monospace.ttf}{color=#888}i{/color} {color=#0f0}<{/color} {color=#f00}2{/color}{/font} (2 < 2). Это {font=monospace.ttf}{color=#f00}False{/color}{/font}, выходим из цикла\n    9. {color=#f0f}Строка 5:{/color} Печатаем {font=monospace.ttf}{color=#f00}\"Complete!\"{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
define persistent.chapter03_02_03_correct = 3
default chapter03_02_03_student = ""
screen chapter03_02_03_screen:
    if "chapter03_02_03" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter03_02_03" in INCORRECT:
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
    text "3 / " + str(persistent.NUM_PAGES["chapter03_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03_02_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter03_02_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Сколько раз будет напечатано слово {font=monospace.ttf}{color=#f00}\"hello\"{/color}{/font} при выполнении следующего кода?\n\n{font=monospace.ttf}    x {color=#0f0}={/color} {color=#f00}4{/color}\n    {color=#ff0}while{/color} x {color=#0f0}%{/color} {color=#f00}2{/color} {color=#0f0}=={/color} {color=#f00}0{/color} {color=#0f0}or{/color} x {color=#0f0}%{/color} {color=#f00}13{/color} {color=#0f0}=={/color} {color=#f00}0{/color}:\n        {color=#57f}print{/color}({color=#f00}\"hello\"{/color})\n        x {color=#0f0}={/color} {color=#f00}3{/color}{color=#0f0}*{/color}x {color=#0f0}+{/color} {color=#f00}1{/color}{/font}"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter03_02_03" in COMPLETED:
                text "{b}{color=#0f0}" + str(persistent.chapter03_02_03_correct) + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter03_02_03_student")
        if "chapter03_02_03" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter03_02_03", persistent.chapter03_02_03_correct, chapter03_02_03_student, cast="int")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter03_02_03_student",""), RemoveFromSet(INCORRECT,"chapter03_02_03")]

# page 4
screen chapter03_02_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter03_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03_02_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Одно из основных применений циклов — последовательный обход элементов данных (например, каждого символа строки). Предположим, у нас есть строка {font=monospace.ttf}{color=#888}var{/color} {color=#0f0}={/color} {color=#f00}\"apple\"{/color}{/font}:\n\n{font=monospace.ttf}    ---------------------------------\n    | {color=#57f}Индекс{/color}    | 0 | 1 | 2 | 3 | 4 |\n    ---------------------------------\n    | {color=#57f}Символ{/color}    | a | p | p | l | e |\n    ---------------------------------{/font}\n\nЕсли условие цикла задано неаккуратно, можно случайно запросить несуществующий элемент {font=monospace.ttf}{color=#888}var{/color}[[{color=#f00}5{/color}]{/font}. Python выбросит ошибку выхода за границы индекса и аварийно завершит программу. Чтобы этого избежать, условие цикла должно вовремя останавливать счетчик, когда тот достигает длины строки.\n\nВстроенная функция {font=monospace.ttf}{color=#57f}len{/color}{color=#888}(){/color}{/font} возвращает длину строки. Мы используем ее в условии while для безопасного обхода:\n\n{font=monospace.ttf}    var {color=#0f0}={/color} {color=#f00}\"apple\"{/color}\n    i {color=#0f0}={/color} {color=#f00}0{/color}\n    {color=#ff0}while{/color} i {color=#0f0}<{/color} {color=#57f}len{/color}(var):\n        {color=#57f}print{/color}(var[[i])\n        i {color=#0f0}+={/color} {color=#f00}1{/color}{/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Почему в условии стоит строгое неравенство \"меньше\" ({font=monospace.ttf}{color=#0f0}<{/color}{/font}), а не \"меньше либо равно\" ({font=monospace.ttf}{color=#0f0}<={/color}{/font}) длине строки?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
