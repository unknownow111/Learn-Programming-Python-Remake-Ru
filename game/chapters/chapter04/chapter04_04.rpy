# chapter and lesson labels
label chapter04_04_01:
    $ COMPLETED.add("chapter04_04_01"); save_game()
    call screen chapter04_04_01_screen
label chapter04_04_02:
    $ COMPLETED.add("chapter04_04_02"); save_game()
    call screen chapter04_04_02_screen
label chapter04_04_03:
    $ COMPLETED.add("chapter04_04_03"); save_game()
    call screen chapter04_04_03_screen
label chapter04_04_04:
    $ COMPLETED.add("chapter04_04_04"); save_game()
    call screen chapter04_04_04_screen
label chapter04_04_05:
    call screen chapter04_04_05_screen
label chapter04_04_06:
    $ COMPLETED.add("chapter04_04_06"); save_game()
    call screen chapter04_04_06_screen
label chapter04_04:
    jump chapter04_04_01
    jump chapter_select

# page 1
screen chapter04_04_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter04_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_04_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Кортежи (Tuples): Сущность{/b}{/color}\n\nСледующая структура данных — это {font=monospace.ttf}{color=#57f}tuple{/color}{/font} (кортеж), который по сути является списком, но {b}{i}неизменяемым{/i}{/b} ({b}{i}immutable{/i}{/b} — его нельзя изменить после создания). Если мы знаем данные, которые хотим сохранить в кортеже, мы используем следующий синтаксис (такой же, как и у списка, но в круглых скобках вместо квадратных):\n\n{font=monospace.ttf}    my_tuple {color=#0f0}={/color} ({color=#f00}\"apples\"{/color}, {color=#f00}2.0{/color}, {color=#f00}None{/color}){/font}\n\nКортежи в Python (как и списки!) индексируются с нуля. Представьте {font=monospace.ttf}{color=#888}my_tuple{/color}{/font} так:\n\n{font=monospace.ttf}    ---------------------------------\n    | {color=#57f}Index{/color} |     0    |  1  |   2  |\n    ---------------------------------\n    | {color=#57f}Data{/color}  | {color=#f00}\"apples\"{/color} | {color=#f00}2.0{/color} | {color=#f00}None{/color} |\n    ---------------------------------{/font}\n\nМы также можем преобразовать {b}{i}другие{/i}{/b} структуры данных {b}{i}в{/i}{/b} кортеж с помощью функции {font=monospace.ttf}{color=#57f}tuple{/color}{color=#888}(){/color}{/font}:\n\n{font=monospace.ttf}    num_list {color=#0f0}={/color} {color=#57f}list{/color}()\n    {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}100{/color}):\n        num_list.{color=#57f}append{/color}({color=#f00}100{/color})\n    num_tuple {color=#0f0}={/color} {color=#57f}tuple{/color}(num_list){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "lock.png":
        xsize 800
        ysize 800
        xalign 0.9
        yalign 0.8

# page 2
screen chapter04_04_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter04_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_04_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_04_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Кортежи (Tuples): Вставка{/b}{/color}\n\nКак только {font=monospace.ttf}{color=#57f}tuple{/color}{/font} объявлен, мы больше не можем добавлять в него значения.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Как вы думаете, почему? Какое ключевое свойство кортежа было бы нарушено, если бы добавление элементов было разрешено?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter04_04_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter04_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_04_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_04_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Кортежи (Tuples): Доступ{/b}{/color}\n\nПоскольку кортежи {font=monospace.ttf}{color=#57f}tuple{/color}{/font} — это по сути неизменяемые списки фиксированной длины, мы можем использовать точно такой же синтаксис, как и для списков, чтобы обращаться к элементам кортежа! Допустим, {font=monospace.ttf}{color=#888}my_tuple{/color}{/font} все еще содержит:\n\n{font=monospace.ttf}    ---------------------------------\n    | {color=#57f}Index{/color} |     0    |  1  |   2  |\n    ---------------------------------\n    | {color=#57f}Data{/color}  | {color=#f00}\"apples\"{/color} | {color=#f00}2.0{/color} | {color=#f00}None{/color} |\n    ---------------------------------{/font}\n\nМы можем извлечь значения по индексам {font=monospace.ttf}{color=#f00}0{/color}{/font}, {font=monospace.ttf}{color=#f00}1{/color}{/font} и {font=monospace.ttf}{color=#f00}2{/color}{/font} вот так:\n\n{font=monospace.ttf}    extract_apples {color=#0f0}={/color} my_tuple[[{color=#f00}0{/color}]\n    extract_2 {color=#0f0}={/color} my_tuple[[{color=#f00}1{/color}]\n    extract_none {color=#0f0}={/color} my_tuple[[{color=#f00}2{/color}]{/font}\n\nВ Python также есть замечательная возможность — {b}{i}распаковка кортежей{/i}{/b} ({b}{i}tuple unpacking{/i}{/b}). Если указать слева от знака присваивания столько же переменных, сколько элементов в кортеже справа, Python автоматически присвоит первой переменной первый элемент, второй — второй и так далее. Например, следующая строчка делает в точности то же самое, что и три строчки выше:\n\n{font=monospace.ttf}    extract_apples, extract_2, extract_none {color=#0f0}={/color} my_tuple{/font}\n\nОператор среза также поддерживается для кортежей в полной мере:\n\n{font=monospace.ttf}    my_tuple[[start : end {color=#0f0}+{/color} {color=#f00}1{/color}]{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter04_04_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter04_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_04_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_04_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Кортежи (Tuples): Обновление и удаление{/b}{/color}\n\nКортежи в Python неизменяемы ({b}{i}immutable{/i}{/b}). Это значит, что после создания их невозможно изменить никоим образом (то есть мы не можем ни перезаписать элемент по индексу, ни удалить элемент из кортежа).":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
define persistent.chapter04_04_05_correct = {"a": True,  "b": True, "c": False,  "d": True}
default chapter04_04_05_student = {k: False for k in persistent.chapter04_04_05_correct}
define persistent.chapter04_04_05_options = {
    "a": "{font=monospace.ttf}your_tuple {color=#0f0}={/color} your_tuple {color=#0f0}+{/color} {color=#f00}1{/color}{/font}",
    "b": "{font=monospace.ttf}your_tuple[[{color=#f00}0{/color}] {color=#0f0}+={/color} {color=#f00}1{/color}{/font}",
    "c": "{font=monospace.ttf}your_tuple {color=#0f0}={/color} ({color=#f00}\"hello\"{/color}){/font}",
    "d": "{font=monospace.ttf}your_tuple.{color=#57f}append{/color}({color=#f00}\"!\"{/color}){/font}",
}
screen chapter04_04_05_screen:
    if "chapter04_04_05" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter04_04_05" in INCORRECT:
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
    text "5 / " + str(persistent.NUM_PAGES["chapter04_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_04_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_04_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Допустим, мы объявили {font=monospace.ttf}{color=#888}your_tuple{/color}{/font} следующим образом:\n\n{font=monospace.ttf}    your_tuple {color=#0f0}={/color} ({color=#f00}\"Hello\"{/color}, {color=#f00}\"Friends\"{/color}){/font}\n\nКакие из следующих инструкций вызовут ошибку? Выберите все подходящие варианты."
        for ol in sorted(persistent.chapter04_04_05_options.keys()):
            if "chapter04_04_05" in COMPLETED:
                if persistent.chapter04_04_05_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter04_04_05_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter04_04_05_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter04_04_05_options[ol])) action ToggleDict(chapter04_04_05_student, ol)
        if "chapter04_04_05" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter04_04_05", persistent.chapter04_04_05_correct, chapter04_04_05_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter04_04_05_student, False, from_label="chapter04_04_05")

# page 6
screen chapter04_04_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter04_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_04_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Кортежи (Tuples): Что еще?{/b}{/color}\n\nБольше информации о кортежах доступно в {a=https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences}официальной документации Python по кортежам{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
