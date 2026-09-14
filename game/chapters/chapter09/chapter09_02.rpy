# chapter and lesson labels
label chapter09_02_01:
    $ COMPLETED.add("chapter09_02_01"); save_game()
    call screen chapter09_02_01_screen
label chapter09_02_02:
    $ COMPLETED.add("chapter09_02_02"); save_game()
    call screen chapter09_02_02_screen
label chapter09_02_03:
    $ COMPLETED.add("chapter09_02_03"); save_game()
    call screen chapter09_02_03_screen
label chapter09_02_04:
    $ COMPLETED.add("chapter09_02_04"); save_game()
    call screen chapter09_02_04_screen
label chapter09_02_05:
    $ COMPLETED.add("chapter09_02_05"); save_game()
    call screen chapter09_02_05_screen
label chapter09_02_06:
    $ COMPLETED.add("chapter09_02_06"); save_game()
    call screen chapter09_02_06_screen
label chapter09_02:
    jump chapter09_02_01
    jump chapter_select

# page 1
screen chapter09_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter09_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Для макарунов требуется 6 ингредиентов:\n\n    1. powdered sugar (сахарная пудра)\n    2. granulated sugar (сахар-песок)\n    3. salt (соль)\n    4. almond flour (миндальная мука)\n    5. egg whites (яичные белки)\n    6. vanilla extract (ванильный экстракт)\n\nЕсли бы мы умели загружать список ингредиентов в переменную {font=monospace.ttf}{color=#888}ingredients{/color}{/font}, мы легко проверили бы рецепт функцией:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}macaron{/color}(ingredients):\n        {color=#ff0}if{/color} {color=#f00}\"powdered sugar\"{/color} {color=#0f0}not in{/color} ingredients {color=#0f0}or{/color} {color=#f00}\"granulated sugar\"{/color} {color=#0f0}not in{/color} ingredients {color=#0f0}or{/color} ...:\n            {color=#ff0}return{/color} {color=#f00}False{/color}\n        {color=#ff0}return{/color} {color=#f00}True{/color}{/font}\n\nНаша цель: {b}{i}научиться представлять содержимое файлов в виде привычных структур данных Python{/i}{/b}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "macarons.png":
        xsize 960
        ysize 522
        xalign 0.9
        yalign 0.26

# page 2
screen chapter09_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter09_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_02_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Главный инструмент для работы с файлами — встроенная функция {font=monospace.ttf}{color=#57f}open{/color}{color=#888}(){/color}{/font}. Она принимает имя файла и возвращает {b}{i}файловый объект{/i}{/b}.\n\nВторой параметр задает режим: чтение ({color=#f00}\"r\"{/color}), запись ({color=#f00}\"w\"{/color}) или добавление в конец ({color=#f00}\"a\"{/color}). По умолчанию используется режим чтения ({color=#f00}\"r\"{/color}):\n\n{font=monospace.ttf}    file {color=#0f0}={/color} {color=#57f}open{/color}({color=#f00}\"receipt.txt\"{/color}){/font}\n\nИли эквивалентно:\n\n{font=monospace.ttf}    file {color=#0f0}={/color} {color=#57f}open{/color}({color=#f00}\"receipt.txt\"{/color}, {color=#f00}\"r\"{/color}){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter09_02_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter09_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_02_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_02_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Файловый объект хранит {b}{i}указатель (курсор){/i}{/b}, отслеживающий текущую позицию в файле. При открытии указатель стоит в самом начале.\n\nМетод {font=monospace.ttf}{color=#888}.{/color}{color=#57f}readline{/color}{color=#888}(){/color}{/font} считывает одну строку и сдвигает указатель на следующую:\n\n{font=monospace.ttf}    {color=#57f}print{/color}(file.{color=#57f}readline{/color}()){/font}\n\nПри повторном вызове программа напечатает следующую строку: {font=monospace.ttf}{color=#f00}almond flour{/color}{/font}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter09_02_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter09_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_02_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_02_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Чтобы прочитать {b}{i}все{/i}{/b} строки разом, используется метод {font=monospace.ttf}{color=#888}.{/color}{color=#57f}readlines{/color}{color=#888}(){/color}{/font}, возвращающий список строк {font=monospace.ttf}{color=#57f}list{/color}{/font}:\n\n{font=monospace.ttf}    file {color=#0f0}={/color} {color=#57f}open{/color}({color=#f00}\"receipt.txt\"{/color})\n    lines {color=#0f0}={/color} file.{color=#57f}readlines{/color}(){/font}\n\nСимвол переноса строки ({color=#f00}\\n{/color}) в конце обычно убирают методом {font=monospace.ttf}{color=#888}.{/color}{color=#57f}strip{/color}{color=#888}(){/color}{/font}.\n\nНо чаще всего файл просто обходят в цикле for напрямую:\n\n{font=monospace.ttf}    {color=#ff0}for{/color} line {color=#0f0}in{/color} file:\n        {color=#57f}print{/color}(line.{color=#57f}strip{/color}()){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
screen chapter09_02_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter09_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_02_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_02_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Часто строка файла содержит несколько полей данных (например, количество, название и цену), разделенных специальным символом — {b}{i}разделителем (delimiter){/i}{/b}:\n\n{font=monospace.ttf}    1x...powdered sugar...for $3\n    1x...almond flour...for $10\n    1x...salt...for $2\n    20x...egg yolks...for $1\n    1x...vanilla extract...for $20{/font}\n\nВ качестве разделителей используют многоточия, запятые (формат CSV — comma-separated values), табуляции и пробелы.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter09_02_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter09_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_02_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter09"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Разбить строку на отдельные части по разделителю помогает строковый метод {font=monospace.ttf}{color=#888}.{/color}{color=#57f}split{/color}{color=#888}(){/color}{/font}:\n\n{font=monospace.ttf}    text {color=#0f0}={/color} {color=#f00}\"1x...powdered sugar...for $3\"{/color}\n    split_text {color=#0f0}={/color} text.{color=#57f}split{/color}({color=#f00}\"...\"{/color}){/font}\n\nРезультат:\n\n{font=monospace.ttf}    [[{color=#f00}\"1x\"{/color}, {color=#f00}\"powdered sugar\"{/color}, {color=#f00}\"for $3\\n\"{/color}]{/font}\n\nТак мы можем разобрать каждую строчку файла на структурированные данные.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
