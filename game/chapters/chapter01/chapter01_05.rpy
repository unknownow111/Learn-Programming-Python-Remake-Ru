# chapter and lesson labels
label chapter01_05_01:
    $ COMPLETED.add("chapter01_05_01"); save_game()
    call screen chapter01_05_01_screen
label chapter01_05_02:
    $ COMPLETED.add("chapter01_05_02"); save_game()
    call screen chapter01_05_02_screen
label chapter01_05_03:
    $ COMPLETED.add("chapter01_05_03"); save_game()
    call screen chapter01_05_03_screen
label chapter01_05_04:
    $ COMPLETED.add("chapter01_05_04"); save_game()
    call screen chapter01_05_04_screen
label chapter01_05_05:
    call screen chapter01_05_05_screen
label chapter01_05:
    jump chapter01_05_01
    jump chapter_select

# page 1
screen chapter01_05_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter01_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_05_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Прежде чем изучать остальные типы данных, ответим на важный вопрос: а как компьютер общается с нами? Диалог должен быть двусторонним!\n\nДля этого мы призовем на помощь встроенную функцию {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font}, которая выводит текст на экран. В программировании это формально называют выводом в {b}{i}стандартный поток вывода (standard output / stdout){/i}{/b}.\n\nЧтобы использовать {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font}, достаточно поместить нужное сообщение внутрь круглых скобок. Например, чтобы напечатать {font=monospace.ttf}{color=#f00}Hello World!{/color}{/font}, напишите следующее:\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}\"Hello World!\"{/color}){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "printer.png":
        xsize 1500
        ysize 1104
        xalign 0.5
        yalign .95

# page 2
screen chapter01_05_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter01_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_05_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_05_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Куда полезнее вывода фиксированных литералов — возможность печатать значения переменных. Передав переменную в {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font}, мы увидим на экране ее текущее {i}значение{/i}. Например, следующий код выведет {font=monospace.ttf}{color=#f00}Niagara Falls{/color}{/font}:\n\n{font=monospace.ttf}    waterfall {color=#0f0}={/color} {color=#f00}\"Niagara Falls\"{/color}\n    {color=#57f}print{/color}(waterfall){/font}\n\nВывод можно комбинировать с индексацией и оператором сложения строк {font=monospace.ttf}{color=#0f0}+{/color}{/font}:\n\n{font=monospace.ttf}    waterfall {color=#0f0}={/color} {color=#f00}\"Niagara Falls\"{/color}\n    {color=#57f}print{/color}(waterfall[[{color=#f00}0{/color}] {color=#0f0}+{/color} waterfall[[{color=#f00}2{/color}] {color=#0f0}+{/color} waterfall[[{color=#f00}1{/color}] {color=#0f0}+{/color} waterfall[[{color=#f00}-2{/color}:{color=#f00}-1{/color}]){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Что напечатает приведенный выше фрагмент кода?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter01_05_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter01_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_05_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_05_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "До сих пор мы выводили только строки. Однако печатать можно данные любого типа (или переменные, хранящие любые типы). Например, следующий код выведет {font=monospace.ttf}{color=#f00}7{/color}{/font} и {font=monospace.ttf}{color=#f00}False{/color}{/font}:\n\n{font=monospace.ttf}    nob {color=#0f0}={/color} {color=#f00}7{/color}\n    brem {color=#0f0}={/color} {color=#f00}False{/color}\n    {color=#57f}print{/color}(nob)\n    {color=#57f}print{/color}(brem){/font}\n\nКаждый вызов функции {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} по умолчанию добавляет в конце {a=https://en.wikipedia.org/wiki/Newline}символ перевода строки{/a} ({font=monospace.ttf}{color=#f00}\\n{/color}{/font}). Это означает, что следующий вызов {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} напечатает текст уже с новой строки. Например, результатом выполнения кода выше будет:\n\n{font=monospace.ttf}    7\n    False{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter01_05_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter01_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_05_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_05_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "По умолчанию функция {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} вставляет перенос строки ({font=monospace.ttf}{color=#f00}\\n{/color}{/font}) в конце выводимого текста. По сути, код ниже выводит строку {font=monospace.ttf}{color=#f00}\"One\\nTwo\\n\"{/color}{/font}, но компьютер скрывает спецсимвол {font=monospace.ttf}{color=#f00}\\n{/color}{/font} и отображает текст на двух раздельных строках экрана:\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}\"One\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Two\"{/color}){/font}\n\nА если мы хотим изменить это поведение? Python позволяет явно указать, какой символ должен добавляться в конце через именованный параметр {font=monospace.ttf}end{/font}:\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}\"Текст\"{/color}, end{color=#0f0}={/color}{color=#f00}\"нужные_символы\"{/color}){/font}\n\nНапример, чтобы напечатать {font=monospace.ttf}{color=#f00}One Two{/color}{/font} на одной строке через пробел:\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}\"One\"{/color}, end{color=#0f0}={/color}{color=#f00}\" \"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Two\"{/color}, end{color=#0f0}={/color}{color=#f00}\"\"{/color}){/font}\n\nАналогично можно получить {font=monospace.ttf}{color=#f00}One#Two${/color}{/font}:\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}\"One\"{/color}, end{color=#0f0}={/color}{color=#f00}\"#\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Two\"{/color}, end{color=#0f0}={/color}{color=#f00}\"$\"{/color}){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
define persistent.chapter01_05_05_correct = 4
default chapter01_05_05_student = ""
screen chapter01_05_05_screen:
    if "chapter01_05_05" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter01_05_05" in INCORRECT:
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
    text "5 / " + str(persistent.NUM_PAGES["chapter01_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_05_04"):
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
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Сколько строк будет напечатано на экране при выполнении следующего кода?\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}\"The\\n logs\\n wo\\n't chop themselves\"{/color}, end{color=#0f0}={/color}{color=#f00}\"!\"{/color}){/font}"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter01_05_05" in COMPLETED:
                text "{b}{color=#0f0}" + str(persistent.chapter01_05_05_correct) + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter01_05_05_student")
        if "chapter01_05_05" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter01_05_05", persistent.chapter01_05_05_correct, chapter01_05_05_student, cast="int")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter01_05_05_student",""), RemoveFromSet(INCORRECT,"chapter01_05_05")]
