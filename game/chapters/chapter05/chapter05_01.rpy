# chapter and lesson labels
label chapter05_01_01:
    $ COMPLETED.add("chapter05_01_01"); save_game()
    call screen chapter05_01_01_screen
label chapter05_01:
    jump chapter05_01_01
    jump chapter_select

# page 1
screen chapter05_01_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter05_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 5{/i}{/b}{/size}\n\n{color=#57f}{b}{i}\"Отличная гора кода получилась! Было бы очень обидно, если бы в ней завелся баг...\"{/i}{/b}{/color}\n\nДо сих пор мы писали код, который выполнялся последовательно — сверху вниз (за небольшим исключением циклов). Для простых задач этого достаточно, но сложные проекты требуют многократного выполнения нетривиальных операций.\n\nЦиклы отлично помогают автоматизировать повторения и следовать принципу {a=https://en.wikipedia.org/wiki/Don%27t_repeat_yourself}DRY (Don't Repeat Yourself / Не повторяйся){/a}. Однако их возможностей недостаточно для написания чистого и поддерживаемого кода. Если полагаться только на них, мы быстро окажемся с бесконечными циклами внутри циклов внутри циклов.\n\nТакой стиль программирования плох по двум ключевым причинам:\n\n    {b}1. Он {i}нечитаем{/i}{/b}\n    {b}2. Его часто {i}невозможно отладить{/i}{/b}\n\nНикто не хочет разбираться в сотнях строк сплошного полотна кода. Вместо этого код нужно разбивать на независимые модули. Встречайте: {b}{i}функции{/i}{/b} ({b}{i}functions{/i}{/b}).":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "bugs.png":
        xsize 700
        ysize 553
        xalign 0.65
        yalign .99
