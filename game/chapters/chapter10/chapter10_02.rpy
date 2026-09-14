# chapter and lesson labels
label chapter10_02_01:
    $ COMPLETED.add("chapter10_02_01"); save_game()
    call screen chapter10_02_01_screen
label chapter10_02_02:
    $ COMPLETED.add("chapter10_02_02"); save_game()
    call screen chapter10_02_02_screen
label chapter10_02_03:
    $ COMPLETED.add("chapter10_02_03"); save_game()
    call screen chapter10_02_03_screen
label chapter10_02_04:
    $ COMPLETED.add("chapter10_02_04"); save_game()
    call screen chapter10_02_04_screen
label chapter10_02_05:
    $ COMPLETED.add("chapter10_02_05"); save_game()
    call screen chapter10_02_05_screen
label chapter10_02_06:
    $ COMPLETED.add("chapter10_02_06"); save_game()
    call screen chapter10_02_06_screen
label chapter10_02:
    jump chapter10_02_01
    jump chapter_select

# page 1
screen chapter10_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter10_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Начнем со {b}{i}Стандартной библиотеки Python (Python Standard Library — PSL){/i}{/b}. Это богатейший встроенный арсенал модулей, доступный сразу после установки Python.\n\nМы дадим краткий обзор самых востребованных модулей, а полный список вы всегда найдете в {a=https://docs.python.org/3/library/index.html}официальной документации PSL{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "python_logo_words.png":
        xsize 2000
        ysize 592
        xalign 0.5
        yalign 0.75

# page 2
screen chapter10_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter10_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_02_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Чтобы использовать модуль, его необходимо {font=monospace.ttf}{color=#ff0}импортировать (import){/color}{/font}:\n\n{font=monospace.ttf}    {color=#ff0}import{/color} pack\n\n    pack.{color=#57f}a{/color}()\n    pack.{color=#57f}b{/color}(){/font}\n\nЛибо импортировать конкретные нужные функции с помощью ключевого слова {font=monospace.ttf}{color=#ff0}from{/color}{/font}:\n\n{font=monospace.ttf}    {color=#ff0}from{/color} pack {color=#ff0}import{/color} a, b\n\n    {color=#57f}a{/color}()\n    {color=#57f}b{/color}(){/font}\n\nСинтаксис {font=monospace.ttf}{color=#ff0}from{/color} ... {color=#ff0}import{/color} ...{/font} считается хорошим тоном, так как подключает только необходимое и не загромождает пространство имен программы.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter10_02_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter10_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_02_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_02_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Модуль {/b}{font=monospace.ttf}math{/font}{/color}\n\nМодуль {font=monospace.ttf}{color=#888}math{/color}{/font} предоставляет математические функции и константы:\n\n    – {font=monospace.ttf}{color=#888}math.{/color}{color=#57f}factorial{/color}{color=#888}(n){/color}{/font} — факториал {i}n{/i}!\n    – {font=monospace.ttf}{color=#888}math.{/color}{color=#57f}log{/color}{color=#888}(n, b){/color}{/font} — логарифм {i}n{/i} по основанию {i}b{/i}\n    – {font=monospace.ttf}{color=#888}math.{/color}{color=#57f}sqrt{/color}{color=#888}(n){/color}{/font} — квадратный корень из {i}n{/i}\n    – {font=monospace.ttf}{color=#888}math.{/color}{color=#57f}sin{/color}{color=#888}(n){/color}{/font} — синус угла {i}n{/i}\n    – {font=monospace.ttf}{color=#888}math.{/color}{color=#57f}pi{/color}{/font} — число {i}π{/i} (3.1415...)\n    – {font=monospace.ttf}{color=#888}math.{/color}{color=#57f}e{/color}{/font} — число {i}e{/i} (2.7182...)\n\nПодробнее — в {a=https://docs.python.org/3/library/math.html}официальной документации math{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter10_02_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter10_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_02_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_02_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Модуль {/b}{font=monospace.ttf}random{/font}{/color}\n\nМодуль {font=monospace.ttf}{color=#888}random{/color}{/font} генерирует псевдослучайные числа:\n\n    – {font=monospace.ttf}{color=#888}random.{/color}{color=#57f}randint{/color}{color=#888}(start, stop){/color}{/font} — случайное целое число от start до stop включительно\n    – {font=monospace.ttf}{color=#888}random.{/color}{color=#57f}uniform{/color}{color=#888}(start, stop){/color}{/font} — случайное вещественное число с плавающей точкой\n    – {font=monospace.ttf}{color=#888}random.{/color}{color=#57f}choice{/color}{color=#888}(sequence){/color}{/font} — случайный элемент из последовательности (списка, кортежа)\n    – {font=monospace.ttf}{color=#888}random.{/color}{color=#57f}shuffle{/color}{color=#888}(sequence){/color}{/font} — случайное перемешивание списка прямо на месте (in-place)\n\nПодробнее — в {a=https://docs.python.org/3/library/random.html}документации по random{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
screen chapter10_02_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter10_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_02_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_02_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Модуль {/b}{font=monospace.ttf}statistics{/font}{/color}\n\nМодуль {font=monospace.ttf}{color=#888}statistics{/color}{/font} помогает проводить статистический анализ числовых данных:\n\n    – {font=monospace.ttf}{color=#888}statistics.{/color}{color=#57f}mean{/color}{color=#888}(data){/color}{/font} — среднее арифметическое\n    – {font=monospace.ttf}{color=#888}statistics.{/color}{color=#57f}median{/color}{color=#888}(data){/color}{/font} — медиана ряда данных\n    – {font=monospace.ttf}{color=#888}statistics.{/color}{color=#57f}mode{/color}{color=#888}(data){/color}{/font} — наиболее часто встречающееся значение (мода)\n    – {font=monospace.ttf}{color=#888}statistics.{/color}{color=#57f}stdev{/color}{color=#888}(data){/color}{/font} — стандартное отклонение выборки\n\nПодробнее — в {a=https://docs.python.org/3/library/statistics.html}документации statistics{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter10_02_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter10_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_02_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter10"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Модуль {/b}{font=monospace.ttf}json{/font}{/color}\n\nИ, как вы помните из главы 9.4, модуль {font=monospace.ttf}{color=#888}json{/color}{/font} для сохранения и чтения структурированных данных также является частью стандартной библиотеки Python (PSL).":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
