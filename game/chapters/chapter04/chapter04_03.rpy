# chapter and lesson labels
label chapter04_03_01:
    $ COMPLETED.add("chapter04_03_01"); save_game()
    call screen chapter04_03_01_screen
label chapter04_03_02:
    $ COMPLETED.add("chapter04_03_02"); save_game()
    call screen chapter04_03_02_screen
label chapter04_03_03:
    call screen chapter04_03_03_screen
label chapter04_03_04:
    $ COMPLETED.add("chapter04_03_04"); save_game()
    call screen chapter04_03_04_screen
label chapter04_03_05:
    $ COMPLETED.add("chapter04_03_05"); save_game()
    call screen chapter04_03_05_screen
label chapter04_03_06:
    $ COMPLETED.add("chapter04_03_06"); save_game()
    call screen chapter04_03_06_screen
label chapter04_03_07:
    $ COMPLETED.add("chapter04_03_07"); save_game()
    call screen chapter04_03_07_screen
label chapter04_03:
    jump chapter04_03_01
    jump chapter_select

# page 1
screen chapter04_03_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter04_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_03_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Множества (Sets): Сущность{/b}{/color}\n\nСледующая структура данных — {font=monospace.ttf}{color=#57f}set{/color}{/font} (множество). Множества в Python — это {b}{i}неупорядоченные{/i}{/b} мешки данных, которые {b}{i}не содержат дубликатов{/i}{/b}. Мы можем объявить переменную множества (и сохранить ее в {font=monospace.ttf}{color=#888}my_set{/color}{/font}) так:\n\n{font=monospace.ttf}    my_set {color=#0f0}={/color} {color=#57f}set{/color}(){/font}\n\nЕсли мы заранее знаем данные для множества, его можно объявить с помощью фигурных скобок:\n\n{font=monospace.ttf}    my_set {color=#0f0}={/color} {{{color=#f00}\"goodbye\"{/color}, {color=#f00}10{/color}, {color=#f00}False{/color}}{/font}\n\nПоскольку множества неупорядочены, они не имеют индексов. Вы можете представить их просто как мешок со сложенными внутрь вещами:":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "bag.png":
        xsize 947
        ysize 960
        xalign 0.5
        yalign 0.95
    text "{font=monospace.ttf}{color=#a00}False{/color}{/font}" xpos 0.5 ypos 0.7
    text "{font=monospace.ttf}{color=#a00}\"goodbye\"{/color}{/font}" xpos 0.42 ypos 0.85
    text "{font=monospace.ttf}{color=#a00}10{/color}{/font}" xpos 0.57 ypos 0.8

# page 2
screen chapter04_03_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter04_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_03_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_03_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Множества (Sets): Вставка{/b}{/color}\n\nМы можем добавлять элементы в {font=monospace.ttf}{color=#57f}set{/color}{/font} с помощью метода {font=monospace.ttf}{color=#888}.{/color}{color=#57f}add{/color}{color=#888}(){/color}{/font}. Допустим, мы уже объявили {font=monospace.ttf}{color=#888}my_set{/color}{/font} с 3 элементами с предыдущей страницы:\n\n{font=monospace.ttf}    my_set {color=#0f0}={/color} {{{color=#f00}\"goodbye\"{/color}, {color=#f00}10{/color}, {color=#f00}False{/color}}{/font}\n\nТеперь добавим еще два значения:\n\n{font=monospace.ttf}    my_set.{color=#57f}add{/color}({color=#f00}\"fresh\"{/color})\n    my_set.{color=#57f}add{/color}({color=#f00}\"data!\"{/color}){/font}\n\nКак упоминалось ранее, множества не содержат повторяющихся значений (дубликатов). Если мы попытаемся добавить то, что уже есть в {font=monospace.ttf}{color=#888}my_set{/color}{/font}, ничего не произойдет:\n\n{font=monospace.ttf}    my_set.{color=#57f}add{/color}({color=#f00}False{/color}){/font}\n\nПосле выполнения этих трех команд {font=monospace.ttf}{color=#888}.{/color}{color=#57f}add{/color}{color=#888}(){/color}{/font} множество выглядит так (обратите внимание, что {font=monospace.ttf}{color=#f00}False{/color}{/font} присутствует всего один раз, хотя мы добавляли его дважды):":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "bag.png":
        xsize 568
        ysize 576
        xalign 0.6
        yalign 0.96
    text "{font=monospace.ttf}{color=#a00}False{/color}{/font}" xpos 0.6 ypos 0.79
    text "{font=monospace.ttf}{color=#a00}\"goodbye\"{/color}{/font}" xpos 0.54 ypos 0.9
    text "{font=monospace.ttf}{color=#a00}10{/color}{/font}" xpos 0.62 ypos 0.87
    text "{font=monospace.ttf}{color=#a00}\"data!\"{/color}{/font}" xpos 0.53 ypos 0.8
    text "{font=monospace.ttf}{color=#a00}\"fresh\"{/color}{/font}" xpos 0.55 ypos 0.85

# page 3
define persistent.chapter04_03_03_correct = 2
default chapter04_03_03_student = ""
screen chapter04_03_03_screen:
    if "chapter04_03_03" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter04_03_03" in INCORRECT:
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
    text "3 / " + str(persistent.NUM_PAGES["chapter04_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_03_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_03_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Сколько элементов будет в {font=monospace.ttf}{color=#888}your_set{/color}{/font} после выполнения следующего кода?\n\n{font=monospace.ttf}    your_set {color=#0f0}={/color} {color=#57f}set{/color}()\n    {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}10{/color}):\n        {color=#ff0}if{/color} i {color=#0f0}%{/color} {color=#f00}2{/color} {color=#0f0}=={/color} {color=#f00}0{/color}:\n            your_set.{color=#57f}add{/color}({color=#f00}\"even\"{/color})\n        {color=#ff0}else{/color}:\n            your_set.{color=#57f}add{/color}({color=#f00}\"odd\"{/color}){/font}"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter04_03_03" in COMPLETED:
                text "{b}{color=#0f0}" + str(persistent.chapter04_03_03_correct) + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter04_03_03_student")
        if "chapter04_03_03" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter04_03_03", persistent.chapter04_03_03_correct, chapter04_03_03_student, cast="int")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter04_03_03_student",""), RemoveFromSet(INCORRECT,"chapter04_03_03")]

# page 4
screen chapter04_03_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter04_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_03_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_03_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Множества (Sets): Доступ{/b}{/color}\n\nПоскольку множества {font=monospace.ttf}{color=#57f}set{/color}{/font} неупорядочены, мы не можем использовать оператор индексации для обращения к элементам по номеру. На самом деле, если вам нужен прямой доступ к конкретным позициям, множество вам вообще не подходит! Данные множества обычно используются двумя способами:\n\n{color=#57f}{i}1. Перебор элементов множества в цикле{/i}{/color}\n\nМы можем перебирать элементы множества так же, как и элементы списка {font=monospace.ttf}{color=#57f}list{/color}{/font}. Однако, поскольку порядок не определен, цикл будет извлекать элементы в произвольном порядке:\n\n{font=monospace.ttf}    {color=#ff0}for{/color} item {color=#0f0}in{/color} my_set:\n        {color=#f0f}# сделать что-то{/color}{/font}\n\n{color=#57f}{i}2. Проверка наличия элемента в множестве{/i}{/color}\n\nМы можем очень быстро проверить принадлежность элемента множеству с помощью логического оператора {font=monospace.ttf}{color=#0f0}in{/color}{/font}:\n\n{font=monospace.ttf}    {color=#ff0}if{/color} item {color=#0f0}in{/color} my_set:\n        {color=#f0f}# сделать что-то{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
screen chapter04_03_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter04_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_03_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_03_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Множества (Sets): Обновление{/b}{/color}\n\nТак как {font=monospace.ttf}{color=#57f}set{/color}{/font} ведет себя как неупорядоченный мешок без позиций, в нем нет прямой операции обновления значения. Вместо этого обновление можно смоделировать двумя шагами:\n\n    1. Удалить старый элемент (как это делать — сейчас узнаем!)\n    2. Добавить новый элемент с обновленными данными":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter04_03_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter04_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_03_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_03_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Множества (Sets): Удаление{/b}{/color}\n\nЧтобы удалить элемент из множества, мы можем использовать функцию {font=monospace.ttf}{color=#888}.{/color}{color=#57f}remove{/color}{color=#888}(){/color}{/font}. Допустим, {font=monospace.ttf}{color=#888}my_set{/color}{/font} все еще содержит наши данные:\n\n\nЧтобы удалить элемент {font=monospace.ttf}{color=#f00}\"goodbye\"{/color}{/font}, мы делаем следующее:\n\n{font=monospace.ttf}    my_set.{color=#57f}remove{/color}({color=#f00}\"goodbye\"{/color}){/font}\n\n\n\nТеперь {font=monospace.ttf}{color=#888}my_set{/color}{/font} выглядит так:\n\n\n\n\nПопытка удалить значение, которого нет в множестве, вызовет ошибку в вашей программе. Поэтому разумно вызывать {font=monospace.ttf}{color=#888}.{/color}{color=#57f}remove{/color}{color=#888}(){/color}{/font} только после проверки, что элемент действительно есть в множестве:\n\n{font=monospace.ttf}    {color=#ff0}if{/color} item {color=#0f0}in{/color} my_set:\n        my_set.{color=#57f}remove{/color}(item){/font}\n\nКроме того, у множества есть функция {font=monospace.ttf}{color=#888}.{/color}{color=#57f}discard{/color}{color=#888}(){/color}{/font}, похожая на {font=monospace.ttf}{color=#888}.{/color}{color=#57f}remove{/color}{color=#888}(){/color}{/font}, за одним исключением: она {b}{i}НЕ{/i}{/b} вызывает ошибку, если элемент отсутствует. Иными словами, {font=monospace.ttf}{color=#888}.{/color}{color=#57f}discard{/color}{color=#888}(){/color}{/font} удаляет элемент, если он есть в множестве, а если его нет — просто ничего не делает.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "bag.png":
        xsize 568
        ysize 576
        xalign 0.91
        yalign 0.15
    text "{font=monospace.ttf}{color=#a00}False{/color}{/font}" xpos 0.87 ypos 0.18
    text "{font=monospace.ttf}{color=#a00}\"goodbye\"{/color}{/font}" xpos 0.8 ypos 0.25
    text "{font=monospace.ttf}{color=#a00}10{/color}{/font}" xpos 0.89 ypos 0.24
    text "{font=monospace.ttf}{color=#a00}\"data!\"{/color}{/font}" xpos 0.8 ypos 0.2
    text "{font=monospace.ttf}{color=#a00}\"fresh\"{/color}{/font}" xpos 0.83 ypos 0.32
    add "bag.png":
        xsize 568
        ysize 576
        xalign 0.43
        yalign 0.47
    text "{font=monospace.ttf}{color=#a00}False{/color}{/font}" xpos 0.46 ypos 0.43
    text "{font=monospace.ttf}{color=#a00}10{/color}{/font}" xpos 0.47 ypos 0.5
    text "{font=monospace.ttf}{color=#a00}\"data!\"{/color}{/font}" xpos 0.4 ypos 0.47
    text "{font=monospace.ttf}{color=#a00}\"fresh\"{/color}{/font}" xpos 0.4 ypos 0.54

# page 7
screen chapter04_03_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter04_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_03_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Множества (Sets): Что еще?{/b}{/color}\n\nБольше информации о множествах доступно в {a=https://docs.python.org/3/tutorial/datastructures.html#sets}официальной документации Python по множествам{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
