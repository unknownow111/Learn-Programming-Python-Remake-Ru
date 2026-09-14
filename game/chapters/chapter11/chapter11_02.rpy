# chapter and lesson labels
label chapter11_02_01:
    $ COMPLETED.add("chapter11_02_01"); save_game()
    call screen chapter11_02_01_screen
label chapter11_02_02:
    $ COMPLETED.add("chapter11_02_02"); save_game()
    call screen chapter11_02_02_screen
label chapter11_02:
    jump chapter11_02_01
    jump chapter_select

# page 1
screen chapter11_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter11_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter11"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter11_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Вы изучали программирование на Python с помощью учебных материалов и интерактивных задач, но навыки программирования по-настоящему раскрываются только тогда, когда у вас есть среда, в которой вы можете свободно создавать все, что пожелаете! Поэтому мы настоятельно рекомендуем настроить собственную среду разработки Python.\n\nВ качестве первого шага мы советуем попробовать {a=https://jupyter.org/}Jupyter Notebooks{/a} — интерактивные блокноты, в которых можно писать и сразу исполнять код на Python в удобном интерфейсе. Установка Jupyter на свой компьютер может вызвать некоторые трудности у новичков, поэтому отлично подойдет {a=https://colab.research.google.com/}Google Colab{/a} — аналог Jupyter Notebook от Google, работающий прямо в браузере (примерно как Google Docs для Word).":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "jupyter.png":
        xsize 884
        ysize 1024
        xalign 0.3
        yalign .9
    add "colab.png":
        xsize 776
        ysize 343
        xalign 0.65
        yalign .72

# page 2
screen chapter11_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter11_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter11_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "В меню" action Jump("chapter11"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Когда вы освоитесь в интерактивных блокнотах вроде Google Colab и захотите еще {b}{i}больше{/i}{/b} свободы и возможностей в разработке на Python, рекомендуем установить Python прямо на ваш компьютер. Вы можете {a=https://www.python.org/downloads/}скачать Python{/a} и следовать {a=https://realpython.com/installing-python/}руководству по установке{/a}.\n\nВ отличие от Jupyter, который предоставляет удобный графический интерфейс не только для {b}{i}запуска{/i}{/b}, но и для {b}{i}написания{/i}{/b} кода, установка самого Python на компьютер даст вам инструменты для {b}{i}запуска{/i}{/b} скриптов из командной строки. А для удобного написания кода можно использовать многофункциональные среды разработки (IDE), например {a=https://code.visualstudio.com/docs/languages/python}Visual Studio Code{/a}, либо более простые редакторы вроде {a=https://notepad-plus-plus.org/}Notepad++{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "vscode.png":
        xsize 1024
        ysize 1024
        xalign 0.2
        yalign .9
    add "notepadplusplus.png":
        xsize 1184
        ysize 1024
        xalign 0.8
        yalign .87
