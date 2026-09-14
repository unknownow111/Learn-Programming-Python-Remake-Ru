# chapter and lesson labels
label chapter01_06_01:
    $ COMPLETED.add("chapter01_06_01"); save_game()
    call screen chapter01_06_01_screen
label chapter01_06_02:
    $ COMPLETED.add("chapter01_06_02"); save_game()
    call screen chapter01_06_02_screen
label chapter01_06_03:
    $ COMPLETED.add("chapter01_06_03"); save_game()
    call screen chapter01_06_03_screen
label chapter01_06_04:
    call screen chapter01_06_04_screen
label chapter01_06_05:
    $ COMPLETED.add("chapter01_06_05"); save_game()
    call screen chapter01_06_05_screen
label chapter01_06_06:
    call screen chapter01_06_06_screen
label chapter01_06:
    jump chapter01_06_01
    jump chapter_select

# page 1
screen chapter01_06_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter01_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_06_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь обратимся к типам {font=monospace.ttf}{color=#57f}int{/color}{/font} и {font=monospace.ttf}{color=#57f}float{/color}{/font} (до {font=monospace.ttf}{color=#57f}bool{/color}{/font} мы тоже скоро доберемся!). Поскольку оба они представляют числовые значения, над ними производятся арифметические операции:\n\n{font=monospace.ttf}    -------------------------------------------------------\n    | {color=#57f}Операция{/color}           | {color=#57f}Оператор{/color} | {color=#57f}Пример{/color}               |\n    -------------------------------------------------------\n    | Сложение           | {color=#0f0}+{/color}        | x {color=#0f0}={/color} y {color=#0f0}+{/color} {color=#f00}1{/color}             |\n    -------------------------------------------------------\n    | Вычитание          | {color=#0f0}-{/color}        | x {color=#0f0}={/color} y {color=#0f0}-{/color} {color=#f00}1{/color}             |\n    -------------------------------------------------------\n    | Умножение          | {color=#0f0}*{/color}        | x {color=#0f0}={/color} y {color=#0f0}*{/color} {color=#f00}1{/color}             |\n    -------------------------------------------------------\n    | Деление            | {color=#0f0}/{/color}        | x {color=#0f0}={/color} y {color=#0f0}/{/color} {color=#f00}2{/color}             |\n    -------------------------------------------------------\n    | Остаток от деления*| {color=#0f0}%{/color}        | x {color=#0f0}={/color} y {color=#0f0}%{/color} {color=#f00}2{/color}             |\n    -------------------------------------------------------\n    | Возведение в степ. | {color=#0f0}**{/color}       | x {color=#0f0}={/color} y {color=#0f0}**{/color} {color=#f00}2{/color}            |\n    -------------------------------------------------------\n    | Отрицание (унарное)| {color=#0f0}-{/color}        | x {color=#0f0}={/color} {color=#0f0}-{/color}y                |\n    -------------------------------------------------------{/font}\n\nОчень распространенная задача — обновить значение переменной с учетом константы. Например, увеличить {font=monospace.ttf}{color=#888}x{/color}{/font} на {font=monospace.ttf}{color=#f00}1{/color}{/font} или умножить {font=monospace.ttf}{color=#888}x{/color}{/font} на {font=monospace.ttf}{color=#f00}3{/color}{/font}. Это можно записать как: {font=monospace.ttf}{color=#888}x{/color} {color=#0f0}={/color} {color=#888}x{/color} {color=#0f0}+{/color} {color=#f00}1{/color}{/font} или {font=monospace.ttf}{color=#888}x{/color} {color=#0f0}={/color} {color=#888}x{/color} {color=#0f0}*{/color} {color=#f00}3{/color}{/font}. Однако в Python принято использовать краткую запись: {font=monospace.ttf}{color=#888}x{/color} {color=#0f0}+={/color} {color=#f00}1{/color}{/font} или {font=monospace.ttf}{color=#888}x{/color} {color=#0f0}*={/color} {color=#f00}3{/color}{/font}. Такие составные операторы присваивания доступны для всех операций выше (кроме унарного минуса).\n\n{i}*Если вы не знакомы с операцией взятия остатка (по модулю), {a=https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic}см. справку{/a}.{/i}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "calculator.png":
        xsize 656
        ysize 935
        xalign 0.75
        yalign .45

# page 2
screen chapter01_06_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter01_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_06_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_06_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Простые выражения с одним действием редко вызывают вопросы. Но что происходит в составных выражениях? В школе вы изучали порядок математических действий (умножение перед сложением и т.д.). В Python это называется {b}{i}приоритетом операторов (operator precedence){/i}{/b}:\n\n{font=monospace.ttf}    -------------------------------------------------------------------------\n    | {color=#57f}Приоритет{/color}         | {color=#57f}Оператор{/color} | {color=#57f}Действие{/color}                               |\n    -------------------------------------------------------------------------\n    | Высший            | ()       | Скобки (группировка)                  |\n    -------------------------------------------------------------------------\n    |                   | {color=#0f0}**{/color}       | Возведение в степень                  |\n    -------------------------------------------------------------------------\n    |                   | {color=#0f0}-{/color}x       | Унарный минус (отрицание)             |\n    -------------------------------------------------------------------------\n    |                   | {color=#0f0}*{/color}, {color=#0f0}/{/color}, {color=#0f0}%{/color}  | Умножение, деление, остаток           |\n    -------------------------------------------------------------------------\n    |                   | {color=#0f0}+{/color}, {color=#0f0}-{/color}     | Сложение и вычитание                  |\n    -------------------------------------------------------------------------\n    | Низший            | {color=#0f0}:={/color}, {color=#0f0}={/color}    | Присваивание                          |\n    -------------------------------------------------------------------------{/font}\n\nЕсли операторы имеют одинаковый приоритет, они вычисляются {b}{i}слева направо{/i}{/b}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter01_06_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter01_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_06_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_06_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Хороший код должен легко читаться с первого взгляда, не заставляя программиста судорожно вспоминать таблицу приоритетов. Допустим, у нас есть строка:\n\n{font=monospace.ttf}    y {color=#0f0}={/color} b {color=#0f0}+{/color} m {color=#0f0}*{/color} x{/font}\n\nСначала выполнится умножение {font=monospace.ttf}{color=#888}m{/color}{/font} на {font=monospace.ttf}{color=#888}x{/color}{/font}, а затем результат прибавится к {font=monospace.ttf}{color=#888}b{/color}{/font}, так как умножение имеет более высокий приоритет. Но что если читатель засомневается? Для ясности можно явно добавить скобки:\n\n{font=monospace.ttf}    y {color=#0f0}={/color} b {color=#0f0}+{/color} (m {color=#0f0}*{/color} x){/font}\n\nФункционально эти строки абсолютно идентичны, но второй вариант воспринимается гораздо быстрее. Впрочем, не злоупотребляйте скобками без необходимости, чтобы код не превратился в нечитаемый частокол.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
define persistent.chapter01_06_04_correct = 361
default chapter01_06_04_student = ""
screen chapter01_06_04_screen:
    if "chapter01_06_04" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter01_06_04" in INCORRECT:
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
    text "4 / " + str(persistent.NUM_PAGES["chapter01_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_06_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_06_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Каково значение переменной {font=monospace.ttf}{color=#888}ultimate{/color}{/font} после выполнения кода? Учитывайте приоритет операторов.\n\n{font=monospace.ttf}    foo {color=#0f0}={/color} {color=#f00}11{/color}\n    bar {color=#0f0}={/color} {color=#f00}11{/color} {color=#0f0}*{/color} {color=#f00}2{/color}\n    baz {color=#0f0}={/color} {color=#f00}11{/color} {color=#0f0}**{/color} {color=#f00}2{/color} {color=#0f0}+{/color} {color=#f00}7{/color}\n    foobar {color=#0f0}={/color} foo {color=#0f0}+{/color} bar\n    qup {color=#0f0}={/color} baz {color=#0f0}-{/color} {color=#f00}20{/color} {color=#0f0}+{/color} foobar\n\n    ultimate {color=#0f0}={/color} (foo {color=#0f0}*{/color} bar) {color=#0f0}+{/color} (foo {color=#0f0}**{/color} {color=#f00}2{/color}) {color=#0f0}-{/color} {color=#f00}2{/color}{/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Были ли скобки в выражении для ultimate обязательны?"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter01_06_04" in COMPLETED:
                text "{b}{color=#0f0}" + str(persistent.chapter01_06_04_correct) + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter01_06_04_student")
        if "chapter01_06_04" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter01_06_04", persistent.chapter01_06_04_correct, chapter01_06_04_student, cast="int")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter01_06_04_student",""), RemoveFromSet(INCORRECT,"chapter01_06_04")]

# page 5
screen chapter01_06_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter01_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_06_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_06_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "В предыдущем задании мы намеренно не использовали оператор деления ({font=monospace.ttf}{color=#0f0}/{/color}{/font}). Дело в том, что в Python есть целых два оператора деления: обычное {font=monospace.ttf}{color=#0f0}/{/color}{/font} и целочисленное {font=monospace.ttf}{color=#0f0}//{/color}{/font}!\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Чему равно значение {font=monospace.ttf}{color=#f00}14{/color} {color=#0f0}/{/color} {color=#f00}5{/color}{/font}?\n\nЕсли вы посчитали, что получится {font=monospace.ttf}{color=#f00}2.8{/color}{/font} — вы совершенно правы. Это {b}{i}деление с плавающей точкой{/i}{/b}: результат автоматически преобразуется в тип {font=monospace.ttf}{color=#57f}float{/color}{/font}, сохраняя дробную часть.\n\nОднако Python также поддерживает {b}{i}целочисленное деление{/i}{/b} с помощью оператора {font=monospace.ttf}{color=#0f0}//{/color}{/font}. В этом случае результат отбрасывает (усекает) дробную часть и преобразуется в целое число {font=monospace.ttf}{color=#57f}int{/color}{/font}:\n\nПоэтому:\n{font=monospace.ttf}{color=#f00}14{/color} {color=#0f0}/{/color} {color=#f00}5{/color}{/font} дает {font=monospace.ttf}{color=#f00}2.8{/color}{/font},\nно {font=monospace.ttf}{color=#f00}14{/color} {color=#0f0}//{/color} {color=#f00}5{/color}{/font} дает {font=monospace.ttf}{color=#f00}2{/color}{/font}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "truncate.png":
        xsize 854
        ysize 776
        xalign 0.5
        yalign .8

# page 6
define persistent.chapter01_06_06_correct = 33.33
default chapter01_06_06_student = ""
screen chapter01_06_06_screen:
    if "chapter01_06_06" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter01_06_06" in INCORRECT:
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
    text "6 / " + str(persistent.NUM_PAGES["chapter01_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_06_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Каково значение {font=monospace.ttf}{color=#888}bat{/color}{/font} после выполнения кода?\n\n{font=monospace.ttf}    kax {color=#0f0}={/color} {color=#f00}100{/color}\n    mar {color=#0f0}={/color} kax {color=#0f0}//{/color} {color=#f00}7{/color}\n    rep {color=#0f0}={/color} mar {color=#0f0}%{/color} {color=#f00}5{/color} {color=#0f0}/{/color} {color=#57f}float{/color}({color=#f00}2{/color})\n\n    bat {color=#0f0}={/color} kax {color=#0f0}/{/color} (rep {color=#0f0}+{/color} {color=#f00}1{/color}){/font}"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter01_06_06" in COMPLETED:
                text "{b}{color=#0f0}" + str(persistent.chapter01_06_06_correct) + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter01_06_06_student")
        if "chapter01_06_06" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter01_06_06", persistent.chapter01_06_06_correct, chapter01_06_06_student, cast="float", float_precision=0.01)
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter01_06_06_student",""), RemoveFromSet(INCORRECT,"chapter01_06_06")]
