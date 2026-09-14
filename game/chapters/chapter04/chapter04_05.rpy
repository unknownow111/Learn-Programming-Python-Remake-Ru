# chapter and lesson labels
label chapter04_05_01:
    $ COMPLETED.add("chapter04_05_01"); save_game()
    call screen chapter04_05_01_screen
label chapter04_05_02:
    $ COMPLETED.add("chapter04_05_02"); save_game()
    call screen chapter04_05_02_screen
label chapter04_05_03:
    call screen chapter04_05_03_screen
label chapter04_05_04:
    $ COMPLETED.add("chapter04_05_04"); save_game()
    call screen chapter04_05_04_screen
label chapter04_05_05:
    $ COMPLETED.add("chapter04_05_05"); save_game()
    call screen chapter04_05_05_screen
label chapter04_05_06:
    $ COMPLETED.add("chapter04_05_06"); save_game()
    call screen chapter04_05_06_screen
label chapter04_05_07:
    $ COMPLETED.add("chapter04_05_07"); save_game()
    call screen chapter04_05_07_screen
label chapter04_05:
    jump chapter04_05_01
    jump chapter_select

# page 1
screen chapter04_05_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter04_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_05_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Словари (Dicts): Сущность{/b}{/color}\n\nПоследняя базовая структура данных, которую мы рассмотрим — {font=monospace.ttf}{color=#57f}dict{/color}{/font} (сокращение от dictionary, словарь). Словари в Python — это {i}{b}неупорядоченные{/b}*{/i} отображения ключей на значения. Мы можем объявить переменную словаря (и сохранить ее в {font=monospace.ttf}{color=#888}my_dict{/color}{/font}) так:\n\n{font=monospace.ttf}    my_dict {color=#0f0}={/color} {color=#57f}dict{/color}(){/font}\n\nЕсли данные известны заранее, словарь можно объявить с помощью фигурных скобок и двоеточий, связывающих ключ со значением:\n\n{font=monospace.ttf}    my_dict {color=#0f0}={/color} {{{color=#f00}\"key1\"{/color}: {color=#f00}True{/color}, {color=#f00}\"key2\"{/color}: {color=#f00}\"fox\"{/color}, {color=#f00}3{/color}: {color=#f00}\"red\"{/color}} {/font}\n\nСловарь {font=monospace.ttf}{color=#888}my_dict{/color}{/font} можно представить как список, где числовые индексы заменены произвольными ключами (без фиксированного порядка!):\n\n{font=monospace.ttf}    -----------------------------------\n    | {color=#57f}Key{/color}   | {color=#f00}\"key2\"{/color} |   {color=#f00}3{/color}   | {color=#f00}\"key1\"{/color} |\n    -----------------------------------\n    | {color=#57f}Value{/color} | {color=#f00}\"fox\"{/color}  | {color=#f00}\"red\"{/color} |  {color=#f00}True{/color}  |\n    -----------------------------------{/font}\n\nСловарь похож на множество {font=monospace.ttf}{color=#57f}set{/color}{/font} в том, что касается его {b}{i}ключей{/i}{/b} (все ключи уникальны, и можно быстро проверить наличие ключа), но с дополнительной возможностью связать с каждым ключом {b}{i}значение{/i}{/b} (то есть получить не просто ответ \"да, есть\" / \"нет, отсутствует\", а извлечь {b}{i}конкретное значение{/i}{/b}).\n\n{i}*Начиная с Python 3.7, словари сохраняют порядок добавления элементов при итерации.{/i}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "dictionary.png":
        xsize 379
        ysize 407
        xalign 0.45
        yalign 0.67

# page 2
screen chapter04_05_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter04_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_05_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_05_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Словари (Dicts): Вставка{/b}{/color}\n\nМы можем добавлять элементы в {font=monospace.ttf}{color=#57f}dict{/color}{/font} с помощью оператора квадратных скобок (индексации). Допустим, мы уже объявили {font=monospace.ttf}{color=#888}my_dict{/color}{/font} с 3 элементами:\n\n{font=monospace.ttf}    my_dict {color=#0f0}={/color} {{{color=#f00}\"key1\"{/color}: {color=#f00}True{/color}, {color=#f00}\"key2\"{/color}: {color=#f00}\"fox\"{/color}, {color=#f00}3{/color}: {color=#f00}\"red\"{/color}} {/font}\n\nТеперь добавим еще две пары ключ-значение:\n\n{font=monospace.ttf}    my_dict[[{color=#f00}\"meow\"{/color}] {color=#0f0}={/color} {color=#f00}\"cat\"{/color}\n    my_dict[[{color=#f00}\"woof\"{/color}] {color=#0f0}={/color} {color=#f00}\"dog\"{/color}{/font}\n\nТеперь {font=monospace.ttf}{color=#888}my_dict{/color}{/font} выглядит так:\n\n{font=monospace.ttf}    -----------------------------------------------------\n    | {color=#57f}Key{/color}   | {color=#f00}\"key2\"{/color} |   {color=#f00}3{/color}   | {color=#f00}\"meow\"{/color} | {color=#f00}\"key1\"{/color} | {color=#f00}\"woof\"{/color} |\n    -----------------------------------------------------\n    | {color=#57f}Value{/color} | {color=#f00}\"fox\"{/color}  | {color=#f00}\"red\"{/color} | {color=#f00}\"cat\"{/color}  |  {color=#f00}True{/color}  | {color=#f00}\"dog\"{/color}  |\n    -----------------------------------------------------{/font}\n\nОбратите внимание, что добавленные элементы концептуально отображаются без фиксированного порядка, иллюстрируя идею ключ-значение.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
define persistent.chapter04_05_03_correct = 5
default chapter04_05_03_student = ""
screen chapter04_05_03_screen:
    if "chapter04_05_03" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter04_05_03" in INCORRECT:
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
    text "3 / " + str(persistent.NUM_PAGES["chapter04_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_05_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_05_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Сколько элементов будет в словаре {font=monospace.ttf}{color=#888}your_dict{/color}{/font} после выполнения следующего кода?\n\n{font=monospace.ttf}    keys {color=#0f0}={/color} [[{color=#f00}\"red\"{/color}, {color=#f00}\"blue\"{/color}, {color=#f00}\"green\"{/color}, {color=#f00}\"yellow\"{/color}, {color=#f00}\"green\"{/color}, {color=#f00}\"purple\"{/color}, {color=#f00}\"blue\"{/color}]\n    your_dict {color=#0f0}={/color} {color=#57f}dict{/color}()\n    {color=#ff0}for{/color} key {color=#0f0}in{/color} keys:\n        your_dict[[key] {color=#0f0}={/color} {color=#f00}None{/color}{/font}\n\n{i}Примечание: Одна пара (ключ, значение) считается за один элемент.{/i}"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter04_05_03" in COMPLETED:
                text "{b}{color=#0f0}" + str(persistent.chapter04_05_03_correct) + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter04_05_03_student")
        if "chapter04_05_03" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter04_05_03", persistent.chapter04_05_03_correct, chapter04_05_03_student, cast="int")
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter04_05_03_student",""), RemoveFromSet(INCORRECT,"chapter04_05_03")]

# page 4
screen chapter04_05_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter04_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_05_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_05_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Словари (Dicts): Доступ{/b}{/color}\n\nМы также используем оператор квадратных скобок для доступа к существующим элементам по их ключу. Допустим, {font=monospace.ttf}{color=#888}my_dict{/color}{/font} по-прежнему содержит:\n\n{font=monospace.ttf}    -----------------------------------------------------\n    | {color=#57f}Key{/color}   | {color=#f00}\"key2\"{/color} |   {color=#f00}3{/color}   | {color=#f00}\"meow\"{/color} | {color=#f00}\"key1\"{/color} | {color=#f00}\"woof\"{/color} |\n    -----------------------------------------------------\n    | {color=#57f}Value{/color} | {color=#f00}\"fox\"{/color}  | {color=#f00}\"red\"{/color} | {color=#f00}\"cat\"{/color}  |  {color=#f00}True{/color}  | {color=#f00}\"dog\"{/color}  |\n    -----------------------------------------------------{/font}\n\nМы можем извлечь значения по ключам следующим образом:\n\n{font=monospace.ttf}    extract_fox {color=#0f0}={/color} my_dict[[{color=#f00}\"key2\"{/color}]\n    extract_cat {color=#0f0}={/color} my_dict[[{color=#f00}\"meow\"{/color}]\n    extract_red {color=#0f0}={/color} my_dict[[{color=#f00}3{/color}]{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
screen chapter04_05_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter04_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_05_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_05_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Словари (Dicts): Обновление{/b}{/color}\n\nОператор квадратных скобок позволяет также обновлять значение для уже существующего ключа. Если {font=monospace.ttf}{color=#888}my_dict{/color}{/font} изначально выглядел так:\n\n{font=monospace.ttf}    -----------------------------------------------------\n    | {color=#57f}Key{/color}   | {color=#f00}\"key2\"{/color} |   {color=#f00}3{/color}   | {color=#f00}\"meow\"{/color} | {color=#f00}\"key1\"{/color} | {color=#f00}\"woof\"{/color} |\n    -----------------------------------------------------\n    | {color=#57f}Value{/color} | {color=#f00}\"fox\"{/color}  | {color=#f00}\"red\"{/color} | {color=#f00}\"cat\"{/color}  |  {color=#f00}True{/color}  | {color=#f00}\"dog\"{/color}  |\n    -----------------------------------------------------{/font}\n\nМы можем обновить значение, связанное с ключом {font=monospace.ttf}{color=#f00}3{/color}{/font}, следующим образом:\n\n{font=monospace.ttf}    my_dict[[{color=#f00}3{/color}] {color=#0f0}={/color} {color=#f00}\"blue\"{/color}{/font}\n\nТеперь {font=monospace.ttf}{color=#888}my_dict{/color}{/font} выглядит так (обратите внимание: {font=monospace.ttf}{color=#f00}\"red\"{/color}{/font} сменилось на {font=monospace.ttf}{color=#f00}\"blue\"{/color}{/font}):\n\n{font=monospace.ttf}    ------------------------------------------------------\n    | {color=#57f}Key{/color}   | {color=#f00}\"key2\"{/color} |    {color=#f00}3{/color}   | {color=#f00}\"meow\"{/color} | {color=#f00}\"key1\"{/color} | {color=#f00}\"woof\"{/color} |\n    ------------------------------------------------------\n    | {color=#57f}Value{/color} | {color=#f00}\"fox\"{/color}  | {color=#f00}\"blue\"{/color} | {color=#f00}\"cat\"{/color}  |  {color=#f00}True{/color}  | {color=#f00}\"dog\"{/color}  |\n    ------------------------------------------------------{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter04_05_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter04_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_05_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_05_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Словари (Dicts): Удаление{/b}{/color}\n\nСуществуют два способа удалить элемент из {font=monospace.ttf}{color=#57f}dict{/color}{/font}: ключевое слово {font=monospace.ttf}{color=#ff0}del{/color}{/font} и функция {font=monospace.ttf}{color=#888}.{/color}{color=#57f}pop{/color}{color=#888}(){/color}{/font}. В обоих случаях указывается {b}{i}ключ{/i}{/b} пары, которую вы хотите удалить. Допустим, {font=monospace.ttf}{color=#888}my_dict{/color}{/font} по-прежнему содержит:\n\n{font=monospace.ttf}    ------------------------------------------------------\n    | {color=#57f}Key{/color}   | {color=#f00}\"key2\"{/color} |    {color=#f00}3{/color}   | {color=#f00}\"meow\"{/color} | {color=#f00}\"key1\"{/color} | {color=#f00}\"woof\"{/color} |\n    ------------------------------------------------------\n    | {color=#57f}Value{/color} | {color=#f00}\"fox\"{/color}  | {color=#f00}\"blue\"{/color} | {color=#f00}\"cat\"{/color}  |  {color=#f00}True{/color}  | {color=#f00}\"dog\"{/color}  |\n    ------------------------------------------------------{/font}\n\n{b}Использование {font=monospace.ttf}{color=#ff0}del{/color}{/font}:{/b} Мы можем удалить пару (ключ, значение) {font=monospace.ttf}{color=#888}({/color}{color=#f00}\"key2\"{/color}{color=#888},{/color} {color=#f00}\"fox\"{/color}{color=#888}){/color}{/font} вот так:\n\n{font=monospace.ttf}    {color=#ff0}del{/color} my_dict[[{color=#f00}\"key2\"{/color}]{/font}\n\n{b}Использование {font=monospace.ttf}{color=#888}.{/color}{color=#57f}pop{/color}{color=#888}(){/color}{/font}:{/b} Мы можем удалить пару {font=monospace.ttf}{color=#888}({/color}{color=#f00}\"key1\"{/color}{color=#888},{/color} {color=#f00}True{/color}{color=#888}){/color}{/font} так:\n\n{font=monospace.ttf}    my_dict.{color=#57f}pop{/color}({color=#f00}\"key1\"{/color}){/font}\n\nПосле выполнения {b}{i}обеих{/i}{/b} команд выше {font=monospace.ttf}{color=#888}my_dict{/color}{/font} будет выглядеть так:\n\n{font=monospace.ttf}    ------------------------------------\n    | {color=#57f}Key{/color}   |    {color=#f00}3{/color}   | {color=#f00}\"meow\"{/color} | {color=#f00}\"woof\"{/color} |\n    ------------------------------------\n    | {color=#57f}Value{/color} | {color=#f00}\"blue\"{/color} | {color=#f00}\"cat\"{/color}  | {color=#f00}\"dog\"{/color}  |\n    ------------------------------------{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 7
screen chapter04_05_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter04_05"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_05_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Словари (Dicts): Что еще?{/b}{/color}\n\nБольше информации о словарях доступно в {a=https://docs.python.org/3/tutorial/datastructures.html#dictionaries}официальной документации Python по словарям{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
