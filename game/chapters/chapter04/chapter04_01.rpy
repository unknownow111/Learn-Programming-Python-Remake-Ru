# chapter and lesson labels
label chapter04_01_01:
    $ COMPLETED.add("chapter04_01_01"); save_game()
    call screen chapter04_01_01_screen
label chapter04_01_02:
    $ COMPLETED.add("chapter04_01_02"); save_game()
    call screen chapter04_01_02_screen
label chapter04_01:
    jump chapter04_01_01
    jump chapter_select

# page 1
screen chapter04_01_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter04_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_01_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 4{/i}{/b}{/size}\n\n{color=#57f}{b}{i}\"Мне комбо №3, пожалуйста!\"{/i}{/b} — Вы в любимом ресторане быстрого питания{/color}\n\nМеню во многих ресторанах быстрого питания можно разделить на четыре категории: основные блюда, гарниры, напитки и десерты. Приходя туда, вы часто хотите взять по одному пункту из каждой категории, чтобы получился полноценный обед. Вместо того чтобы заставлять вас заказывать каждую позицию по отдельности, заведения часто предлагают комбо-наборы, объединяющие блюда вместе.\n\nДо сих пор мы создавали отдельную переменную для каждого фрагмента данных, который хотели сохранить. Теперь мы научимся создавать подобные комбо-наборы, группирующие данные вместе. Такие наборы называются {b}{i}структурами данных{/i}{/b} ({b}{i}data structures{/i}{/b}).":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "combo_meal.png":
        xsize 832
        ysize 960
        xalign 0.5
        yalign .96

# page 2
screen chapter04_01_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter04_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_01_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Структуры данных универсальны и поддерживают множество различных операций и возможностей. В этом курсе мы рассмотрим пять аспектов каждой структуры данных:\n\n    1. {color=#57f}{b}{i}Сущность (Nature){/i}{/b}{/color} — Как устроена структура данных? Как в ней хранятся данные?\n    2. {color=#57f}{b}{i}Вставка (Insertion){/i}{/b}{/color} — Как добавлять данные?\n    3. {color=#57f}{b}{i}Доступ (Access){/i}{/b}{/color} — Как находить и извлекать данные?\n    4. {color=#57f}{b}{i}Обновление (Update){/i}{/b}{/color} — Как изменять существующие данные?\n    5. {color=#57f}{b}{i}Удаление (Deletion){/i}{/b}{/color} — Как удалять данные?\n\nТакже обратите внимание: каждая из этих структур поддерживает перебор в цикле (с помощью циклов for или while). Проще всего обходить структуру данных с помощью цикла for. Вспомним синтаксис цикла for:\n\n{font=monospace.ttf}    {color=#f0f}# код до цикла for{/color}\n    {color=#ff0}for{/color} iterator_var {color=#0f0}in{/color} data:\n        {color=#f0f}# код внутри цикла for{/color}\n    {color=#f0f}# код после цикла for{/color}{/font}\n\nРанее мы рассматривали в качестве {font=monospace.ttf}{color=#888}data{/color}{/font} только строки, но {font=monospace.ttf}{color=#888}data{/color}{/font} может быть {i}любой{/i} из этих структур данных! Это возможно потому, что {i}все{/i} они (включая строки) являются {b}{i}итерируемыми{/i}{/b} ({b}{i}iterable{/i}{/b}): они поддерживают последовательный перебор элементов.\n\nПорядок обхода зависит от конкретной структуры (как мы скоро увидим). Если структура {b}{i}упорядоченная{/i}{/b} ({b}{i}ordered{/i}{/b}), вы получите элементы строго от начала к концу. В противном случае определенный порядок не гарантируется.\n\nРазумеется, каждая структура данных уникальна и обладает массой возможностей — куда больше, чем поместится в этом курсе. Поэтому для каждой структуры мы оставим ссылку на официальную документацию Python, чтобы вы могли изучить их глубже.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
