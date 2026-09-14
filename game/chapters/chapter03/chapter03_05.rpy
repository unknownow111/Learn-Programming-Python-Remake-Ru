# chapter and lesson labels
label chapter03_05_01:
    $ COMPLETED.add("chapter03_05_01"); save_game()
    call screen chapter03_05_01_screen
label chapter03_05_02:
    call screen chapter03_05_02_screen
label chapter03_05_03:
    $ COMPLETED.add("chapter03_05_03"); save_game()
    call screen chapter03_05_03_screen
label chapter03_05_04:
    $ COMPLETED.add("chapter03_05_04"); save_game()
    call screen chapter03_05_04_screen
label chapter03_05_05:
    call screen chapter03_05_05_screen
label chapter03_05:
    jump chapter03_05_01
    jump chapter_select

# page 1
screen chapter03_05_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter03_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter03_05_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Мы познакомились с циклами как с инструментом для автоматизации повторяющихся задач. А что, если требуется автоматизировать повторяющееся действие {b}{i}внутри{/i}{/b} другого цикла? Взгляните на следующий код:\n\n{font=monospace.ttf}    {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}3{/color}):\n        {color=#57f}print{/color}(i {color=#0f0}*{/color} {color=#f00}1{/color})\n        {color=#57f}print{/color}(i {color=#0f0}*{/color} {color=#f00}2{/color})\n        {color=#57f}print{/color}(i {color=#0f0}*{/color} {color=#f00}3{/color})\n        {color=#57f}print{/color}(i {color=#0f0}*{/color} {color=#f00}4{/color}){/font}\n\nЭто можно автоматизировать еще сильнее с помощью {b}{i}вложенных циклов (nested loops){/i}{/b} — цикла внутри другого цикла. Мы просто создаем внутренний цикл {i}с собственной независимой переменной-счетчиком{/i}:\n\n{font=monospace.ttf}    {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}3{/color}):\n        {color=#ff0}for{/color} j {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}1{/color}, {color=#f00}5{/color}):\n            {color=#57f}print{/color}(i {color=#0f0}*{/color} j){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "nested_loop.png":
        xsize 1313
        ysize 890
        xalign 0.75
        yalign .85

# page 2
define persistent.chapter03_05_02_correct = 6
default chapter03_05_02_student = ""
screen chapter03_05_02_screen:
    if "chapter03_05_02" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter03_05_02" in INCORRECT:
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
    text "2 / " + str(persistent.NUM_PAGES["chapter03_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03_05_01"):
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
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Каким будет значение {font=monospace.ttf}{color=#888}x{/color}{/font} после выполнения кода ниже?\n\n{font=monospace.ttf}    n {color=#0f0}={/color} {color=#f00}4{/color}\n    x {color=#0f0}={/color} {color=#f00}0{/color}\n    {color=#ff0}while{/color} n {color=#0f0}>{/color} {color=#f00}0{/color}:\n        {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}(n):\n            x {color=#0f0}+={/color} {color=#f00}1{/color}\n            {color=#57f}print{/color}(x)\n        n {color=#0f0}-={/color} {color=#f00}2{/color}{/font}"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter03_05_02" in COMPLETED:
                text "{b}{color=#0f0}" + str(persistent.chapter03_05_02_correct) + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter03_05_02_student")
        if "chapter03_05_02" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter03_05_02", persistent.chapter03_05_02_correct, chapter03_05_02_student, cast="int")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter03_05_02_student",""), RemoveFromSet(INCORRECT,"chapter03_05_02")]
