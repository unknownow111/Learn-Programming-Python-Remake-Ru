# chapter and lesson labels
label chapter10_03_01:
    $ COMPLETED.add("chapter10_03_01"); save_game()
    call screen chapter10_03_01_screen
label chapter10_03_02:
    $ COMPLETED.add("chapter10_03_02"); save_game()
    call screen chapter10_03_02_screen
label chapter10_03_03:
    $ COMPLETED.add("chapter10_03_03"); save_game()
    call screen chapter10_03_03_screen
label chapter10_03_04:
    $ COMPLETED.add("chapter10_03_04"); save_game()
    call screen chapter10_03_04_screen
label chapter10_03_05:
    $ COMPLETED.add("chapter10_03_05"); save_game()
    call screen chapter10_03_05_screen
label chapter10_03_06:
    $ COMPLETED.add("chapter10_03_06"); save_game()
    call screen chapter10_03_06_screen
label chapter10_03:
    jump chapter10_03_01
    jump chapter_select

# page 1
screen chapter10_03_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter10_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_03_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Стандартная библиотека покрывает общие потребности, но для узких областей (машинное обучение, биоинформатика, анализ данных, разработка игр) созданы тысячи {b}{i}внешних сторонних библиотек{/i}{/b}, размещенных в репозитории PyPI и устанавливаемых командой pip.\n\nРассмотрим три самые популярные библиотеки научного и прикладного Python.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "library.png":
        xsize 1400
        ysize 1041
        xalign 0.5
        yalign 0.99

# page 2
screen chapter10_03_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter10_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_03_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_03_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{b}{i}NumPy{/i}{/b}\n\n{a=https://numpy.org/}NumPy{/a} — фундаментальный пакет для научных вычислений и работы с многомерными массивами. Массивы NumPy ({font=monospace.ttf}{color=#57f}ndarray{/color}{/font}) в десятки раз быстрее стандартных списков Python за счет низкоуровневой оптимизации на C:\n\n{font=monospace.ttf}    {color=#ff0}import{/color} numpy\n\n    my_array {color=#0f0}={/color} numpy.{color=#57f}array{/color}([[{color=#f00}1{/color}, {color=#f00}2{/color}, {color=#f00}3{/color}, {color=#f00}4{/color}, {color=#f00}5{/color}]){/font}\n\nNumPy нативно поддерживает векторные операции, матричное умножение и линейную алгебру. Подробнее — в {a=https://numpy.org/doc/}документации NumPy{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "numpy.png":
        xsize 1540
        ysize 480
        xalign 0.5
        yalign 0.99

# page 3
screen chapter10_03_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter10_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_03_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_03_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{b}{i}Pandas{/i}{/b}\n\n{a=https://pandas.pydata.org/}Pandas{/a} — мощный инструмент для анализа табличных данных (подобно Excel внутри кода). Главная структура — {font=monospace.ttf}{color=#57f}DataFrame{/color}{/font}:\n\n{font=monospace.ttf}    {color=#ff0}import{/color} pandas\n\n    df {color=#0f0}={/color} pandas.{color=#57f}DataFrame{/color}()\n    df[[{color=#f00}\"grade\"{/color}] {color=#0f0}={/color} [[{color=#f00}75{/color}, {color=#f00}85{/color}, {color=#f00}100{/color}, {color=#f00}94{/color}]\n    df[[{color=#f00}\"hours of sleep\"{/color}] {color=#0f0}={/color} [[{color=#f00}8{/color}, {color=#f00}9{/color}, {color=#f00}7{/color}, {color=#f00}4{/color}]\n    df.index {color=#0f0}={/color} [[{color=#f00}\"Bob\"{/color}, {color=#f00}\"Amy\"{/color}, {color=#f00}\"Janet\"{/color}, {color=#f00}\"Michelle\"{/color}]{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter10_03_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter10_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_03_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_03_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Таблица наглядно объединяет колонки и строки с именованными индексами:\n\n{font=monospace.ttf}               --------------------------\n               | {color=#0f0}Grade{/color} | {color=#0f0}Hours of Sleep{/color} |\n    -------------------------------------\n    | {color=#0f0}Bob{/color}      |    {color=#f00}75{/color} |              {color=#f00}8{/color} |\n    -------------------------------------\n    | {color=#0f0}Amy{/color}      |    {color=#f00}85{/color} |              {color=#f00}9{/color} |\n    -------------------------------------\n    | {color=#0f0}Janet{/color}    |   {color=#f00}100{/color} |              {color=#f00}7{/color} |\n    -------------------------------------\n    | {color=#0f0}Michelle{/color} |    {color=#f00}94{/color} |              {color=#f00}4{/color} |\n    -------------------------------------{/font}\n\nPandas умеет читать и сохранять таблицы в CSV, Excel, SQL и другие форматы за одну строчку. Подробнее — в {a=https://pandas.pydata.org/docs/}документации Pandas{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "pandas.png":
        xsize 2000
        ysize 809
        xalign 0.95
        yalign 0.63

# page 5
screen chapter10_03_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter10_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_03_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_03_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{b}{i}Matplotlib{/i}{/b}\n\n{a=https://matplotlib.org/}Matplotlib{/a} — библиотека для построения графиков и визуализации данных. Например, точечная диаграмма на основе таблицы Pandas:\n\n{font=monospace.ttf}    {color=#ff0}import{/color} matplotlib.pyplot\n    matplotlib.pyplot.{color=#57f}scatter{/color}(df[[{color=#f00}\"grade\"{/color}], df[[{color=#f00}\"hours of sleep\"{/color}])\n    matplotlib.pyplot.{color=#57f}xlabel{/color}({color=#f00}\"grade\"{/color})\n    matplotlib.pyplot.{color=#57f}ylabel{/color}({color=#f00}\"hours of sleep\"{/color})\n    matplotlib.pyplot.{color=#57f}show{/color}(){/font}\n\nПодробнее — в {a=https://matplotlib.org/stable/index.html}документации Matplotlib{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "matplotlib.png":
        xsize 550
        ysize 110
        xalign 0.81
        yalign 0.35
    add "scatterplot.png":
        xsize 914
        ysize 713
        xalign 0.85
        yalign 0.8

# page 6
screen chapter10_03_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter10_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_03_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter10"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}{i}И тысячи других!{/i}{/b}{/color}\n\nМы лишь прикоснулись к огромной экосистеме Python. От веб-разработки (Django, FastAPI) до искусственного интеллекта (PyTorch, TensorFlow) — для любой мыслимой задачи в мире Python уже создана великолепная библиотека.\n\nНадеемся, этот урок стал ключом к дверям вашего дальнейшего развития как программиста!\n\nОсталось сказать лишь одно...":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
