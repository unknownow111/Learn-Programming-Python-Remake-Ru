# chapter and lesson labels
label chapter02_04_01:
    $ COMPLETED.add("chapter02_04_01"); save_game()
    call screen chapter02_04_01_screen
label chapter02_04_02:
    call screen chapter02_04_02_screen
label chapter02_04_03:
    call screen chapter02_04_03_screen
label chapter02_04:
    jump chapter02_04_01
    jump chapter_select

# page 1
screen chapter02_04_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter02_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_04_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Представьте, что вас попросили смешать {color=#f0f}фиолетовую краску{/color}. Вы знаете, что для этого требуются {color=#f00}красная краска{/color} и {color=#57f}синяя краска{/color}. Вы идете в кладовую за {color=#f00}красной краской{/color}, но ее там нет совсем!\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Нужно ли вам проверять наличие {color=#57f}синей краски{/color}?\n\nРазумеется, нет! Без красной краски получить фиолетовую невозможно в любом случае, поэтому проверять наличие синей нет никакого смысла — результат уже известен.\n\nЭту ситуацию можно представить логическим выражением:\n\n    {font=monospace.ttf}    has_red_paint {color=#0f0}and{/color} has_blue_paint{/font}\n\nОтсюда следует важное свойство: составным логическим выражениям (с операторами {font=monospace.ttf}{color=#0f0}and{/color}{/font} или {font=monospace.ttf}{color=#0f0}or{/color}{/font}) не всегда требуется вычислять каждое условие до конца, если результат уже предрешен. Такая оптимизация называется {b}{i}коротким замыканием (short-circuit evaluation){/i}{/b}, и она встроена в язык Python.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "paint.png":
        xsize 709
        ysize 768
        xalign 0.6
        yalign .95

# page 2
define persistent.chapter02_04_02_correct = {"a": True,  "b": False, "c": False,  "d": False, "e": False}
default chapter02_04_02_student = {k: False for k in persistent.chapter02_04_02_correct}
define persistent.chapter02_04_02_options = {
    "a": "Если хотя бы одно из условий равно {font=monospace.ttf}{color=#f00}False{/color}{/font}, все выражение равно {font=monospace.ttf}{color=#f00}False{/color}{/font}",
    "b": "Если хотя бы одно из условий равно {font=monospace.ttf}{color=#f00}False{/color}{/font}, все выражение равно {font=monospace.ttf}{color=#f00}True{/color}{/font}",
    "c": "Если хотя бы одно из условий равно {font=monospace.ttf}{color=#f00}True{/color}{/font}, все выражение равно {font=monospace.ttf}{color=#f00}False{/color}{/font}",
    "d": "Если хотя бы одно из условий равно {font=monospace.ttf}{color=#f00}True{/color}{/font}, все выражение равно {font=monospace.ttf}{color=#f00}True{/color}{/font}",
    "e": "Для оператора {font=monospace.ttf}{color=#0f0}and{/color}{/font} короткое замыкание не применяется",
}
screen chapter02_04_02_screen:
    if "chapter02_04_02" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter02_04_02" in INCORRECT:
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
    text "2 / " + str(persistent.NUM_PAGES["chapter02_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_04_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_04_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Какое из следующих утверждений верно описывает короткое замыкание для оператора {font=monospace.ttf}{color=#0f0}and{/color}{/font}?\n\n{i}Примечание: Таблица истинности для {font=monospace.ttf}{color=#0f0}and{/color}{/font} приведена ниже:{/i}\n\n{font=monospace.ttf}    ---------------------------\n    |   x   |   y   | x {color=#0f0}and{/color} y |\n    ---------------------------\n    | {i}{color=#f00}False{/color}{/i} | {i}{color=#f00}False{/color}{/i} | {color=#f00}False{/color}   |\n    ---------------------------\n    | {i}{color=#f00}True{/color}{/i}  | {i}{color=#f00}False{/color}{/i} | {color=#f00}False{/color}   |\n    ---------------------------\n    | {i}{color=#f00}False{/color}{/i} | {i}{color=#f00}True{/color}{/i}  | {color=#f00}False{/color}   |\n    ---------------------------\n    | {i}{color=#f00}True{/color}{/i}  | {i}{color=#f00}True{/color}{/i}  | {color=#f00}True{/color}    |\n    ---------------------------{/font}"
        for ol in sorted(persistent.chapter02_04_02_options.keys()):
            if "chapter02_04_02" in COMPLETED:
                if persistent.chapter02_04_02_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter02_04_02_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter02_04_02_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter02_04_02_options[ol])) action [Function(set_all, chapter02_04_02_student, False, from_label="chapter02_04_02"), ToggleDict(chapter02_04_02_student, ol)]
        if "chapter02_04_02" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter02_04_02", persistent.chapter02_04_02_correct, chapter02_04_02_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter02_04_02_student, False, from_label="chapter02_04_02")

# page 3
define persistent.chapter02_04_03_correct = {"a": False,  "b": False, "c": False,  "d": True, "e": False}
default chapter02_04_03_student = {k: False for k in persistent.chapter02_04_03_correct}
define persistent.chapter02_04_03_options = {
    "a": "Если хотя бы одно из условий равно {font=monospace.ttf}{color=#f00}False{/color}{/font}, все выражение равно {font=monospace.ttf}{color=#f00}False{/color}{/font}",
    "b": "Если хотя бы одно из условий равно {font=monospace.ttf}{color=#f00}False{/color}{/font}, все выражение равно {font=monospace.ttf}{color=#f00}True{/color}{/font}",
    "c": "Если хотя бы одно из условий равно {font=monospace.ttf}{color=#f00}True{/color}{/font}, все выражение равно {font=monospace.ttf}{color=#f00}False{/color}{/font}",
    "d": "Если хотя бы одно из условий равно {font=monospace.ttf}{color=#f00}True{/color}{/font}, все выражение равно {font=monospace.ttf}{color=#f00}True{/color}{/font}",
    "e": "Для оператора {font=monospace.ttf}{color=#0f0}or{/color}{/font} короткое замыкание не применяется",
}
screen chapter02_04_03_screen:
    if "chapter02_04_03" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter02_04_03" in INCORRECT:
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
    text "3 / " + str(persistent.NUM_PAGES["chapter02_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_04_02"):
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
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Какое из следующих утверждений верно описывает короткое замыкание для оператора {font=monospace.ttf}{color=#0f0}or{/color}{/font}?\n\n{i}Примечание: Таблица истинности для {font=monospace.ttf}{color=#0f0}or{/color}{/font} приведена ниже:{/i}\n\n{font=monospace.ttf}    --------------------------\n    |   x   |   y   | x {color=#0f0}or{/color} y |\n    --------------------------\n    | {i}{color=#f00}False{/color}{/i} | {i}{color=#f00}False{/color}{/i} | {color=#f00}False{/color}  |\n    --------------------------\n    | {i}{color=#f00}True{/color}{/i}  | {i}{color=#f00}False{/color}{/i} | {color=#f00}True{/color}   |\n    --------------------------\n    | {i}{color=#f00}False{/color}{/i} | {i}{color=#f00}True{/color}{/i}  | {color=#f00}True{/color}   |\n    --------------------------\n    | {i}{color=#f00}True{/color}{/i}  | {i}{color=#f00}True{/color}{/i}  | {color=#f00}True{/color}   |\n    --------------------------{/font}"
        for ol in sorted(persistent.chapter02_04_03_options.keys()):
            if "chapter02_04_03" in COMPLETED:
                if persistent.chapter02_04_03_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter02_04_03_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter02_04_03_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter02_04_03_options[ol])) action [Function(set_all, chapter02_04_03_student, False, from_label="chapter02_04_03"), ToggleDict(chapter02_04_03_student, ol)]
        if "chapter02_04_03" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter02_04_03", persistent.chapter02_04_03_correct, chapter02_04_03_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter02_04_03_student, False, from_label="chapter02_04_03")
