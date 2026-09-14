# chapter and lesson labels
label chapter08_03_01:
    $ COMPLETED.add("chapter08_03_01"); save_game()
    call screen chapter08_03_01_screen
label chapter08_03_02:
    $ COMPLETED.add("chapter08_03_02"); save_game()
    call screen chapter08_03_02_screen
label chapter08_03_03:
    $ COMPLETED.add("chapter08_03_03"); save_game()
    call screen chapter08_03_03_screen
label chapter08_03_04:
    call screen chapter08_03_04_screen
label chapter08_03_05:
    $ COMPLETED.add("chapter08_03_05"); save_game()
    call screen chapter08_03_05_screen
label chapter08_03_06:
    $ COMPLETED.add("chapter08_03_06"); save_game()
    call screen chapter08_03_06_screen
label chapter08_03:
    jump chapter08_03_01
    jump chapter_select

# page 1
screen chapter08_03_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter08_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_03_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "При моделировании реального мира стандартных встроенных исключений часто недостаточно. Есть вещи, которые мы считаем абсурдными, но для стандартного Python они абсолютно легитимны.\n\nВспомним класс {b}{color=#57f}Burger{/color}{/b} и попробуем создать бургер со странными ингредиентами:\n\n{font=monospace.ttf}    fake_burger {color=#0f0}={/color} {color=#57f}Burger{/color}({color=#f00}\"happiness\"{/color}, {color=#f00}\"heartbeat\"{/color}, {color=#f00}\"clouds\"{/color}, {color=#f00}\"ringring\"{/color}, {color=#f00}True{/color}, {color=#f00}True{/color}, {color=#f00}-10{/color}){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Какое исключение будет вызвано?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "burger_alive.png":
        xsize 960
        ysize 741
        xalign 0.97
        yalign 0.75

# page 2
screen chapter08_03_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter08_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_03_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_03_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "На самом деле — никакого! С точки зрения Python, это просто строки, булевы значения и отрицательное число. Чтобы научить программу понимать недопустимость таких данных, создаются {b}{i}пользовательские исключения{/i}{/b} ({b}{i}custom exceptions{/i}{/b}).\n\nПользовательские исключения — это обычные классы, которые {b}{i}наследуются{/i}{/b} от встроенного класса {font=monospace.ttf}{color=#57f}Exception{/color}{/font}:\n\n{font=monospace.ttf}    {color=#ff0}class{/color} {color=#57f}BurgerException{/color}({color=#57f}Exception{/color}):{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter08_03_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter08_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_03_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_03_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Определим для класса метод {font=monospace.ttf}{color=#57f}__init__{/color}{color=#888}(){/color}{/font} и метод {font=monospace.ttf}{color=#57f}__str__{/color}{color=#888}(){/color}{/font}:\n\n{font=monospace.ttf}    {color=#ff0}class{/color} {color=#57f}BurgerException{/color}({color=#57f}Exception{/color}):\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, message{color=#0f0}={/color}{color=#f00}None{/color}):\n            self.message {color=#0f0}={/color} message\n\n        {color=#ff0}def{/color} {color=#57f}__str__{/color}(self):\n            {color=#ff0}if{/color} self.message {color=#0f0}is{/color} {color=#f00}None{/color}:\n                {color=#ff0}return{/color} {color=#f00}\"You cannot have a burger with these ingredients.\"{/color}\n            {color=#ff0}else{/color}:\n                {color=#ff0}return{/color} self.message{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
define persistent.chapter08_03_04_correct = {"a": False,  "b": True, "c": True,  "d": False}
default chapter08_03_04_student = {k: False for k in persistent.chapter08_03_04_correct}
define persistent.chapter08_03_04_options_v2 = {
    "a": "Мы можем возбуждать различные типы исключений через один класс {font=monospace.ttf}{color=#57f}Exception{/color}{/font}",
    "b": "Мы можем указывать кастомные сообщения об ошибках при вызове исключения",
    "c": "Мы можем задать стандартное сообщение при вызове исключения без параметров",
    "d": "Мы можем перехватывать исключения внутри их собственного класса до их возбуждения",
}
screen chapter08_03_04_screen:
    if "chapter08_03_04" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter08_03_04" in INCORRECT:
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
    text "4 / " + str(persistent.NUM_PAGES["chapter08_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_03_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_03_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} По каким из следующих причин имеет смысл задать значение по умолчанию для параметра {font=monospace.ttf}{color=#888}message{/color}{/font} в методе {font=monospace.ttf}{color=#57f}__init__{/color}{color=#888}(){/color}{/font} класса исключения? Выберите все подходящие варианты."
        for ol in sorted(persistent.chapter08_03_04_options_v2.keys()):
            if "chapter08_03_04" in COMPLETED:
                if persistent.chapter08_03_04_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter08_03_04_options_v2[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter08_03_04_options_v2[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter08_03_04_options_v2[ol])) action ToggleDict(chapter08_03_04_student, ol)
        if "chapter08_03_04" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter08_03_04", persistent.chapter08_03_04_correct, chapter08_03_04_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter08_03_04_student, False, from_label="chapter08_03_04")

# page 5
screen chapter08_03_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter08_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_03_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter08_03_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь добавим валидацию в конструктор {font=monospace.ttf}{color=#57f}__init__{/color}{color=#888}(){/color}{/font} с помощью ключевого слова {font=monospace.ttf}{color=#ff0}raise{/color}{/font}:\n\n{font=monospace.ttf}{size=-5}    {color=#ff0}class{/color} {color=#57f}Burger{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, bun, cheese, patty, sauce, lettuce, tomato, num_pickles):\n            {color=#ff0}if{/color} bun {color=#0f0}not in{/color} {{{color=#f00}\"brioche\"{/color}, {color=#f00}\"sesame seed\"{/color}, {color=#f00}\"potato\"{/color}, {color=#f00}\"english muffin\"{/color}}:\n                {color=#ff0}raise{/color} {color=#57f}BurgerException{/color}({color=#f00}\"You cannot have a bun made of \"{/color} {color=#0f0}+{/color} bun)\n            {color=#ff0}if{/color} cheese {color=#0f0}not in{/color} {{{color=#f00}\"american\"{/color}, {color=#f00}\"swiss\"{/color}, {color=#f00}\"cheddar\"{/color}, {color=#f00}\"provolone\"{/color}, {color=#f00}\"pepperjack\"{/color}}:\n                {color=#ff0}raise{/color} {color=#57f}BurgerException{/color}({color=#f00}\"You cannot have \"{/color} {color=#0f0}+{/color} cheese {color=#0f0}+{/color} {color=#f00}\" as a cheese\"{/color})\n            ...{/size}{/font}\n\nТеперь попытка создать несуществующий бургер выбросит наше собственное исключение с понятным описанием ошибки!":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter08_03_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter08_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08_03_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter08"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Если мы возбуждаем {font=monospace.ttf}{color=#57f}BurgerException{/color}{/font} с конкретным текстом сообщения — пользователь увидит именно этот текст. Если же вызвать {font=monospace.ttf}{color=#ff0}raise{/color} {color=#57f}BurgerException{/color}{/font} без параметров, сработает дефолтная ветка из метода {font=monospace.ttf}{color=#57f}__str__{/color}{color=#888}(){/color}{/font} и будет выведено стандартное сообщение об ошибке.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
