# chapter and lesson labels
label chapter06_03_01:
    $ COMPLETED.add("chapter06_03_01"); save_game()
    call screen chapter06_03_01_screen
label chapter06_03_02:
    $ COMPLETED.add("chapter06_03_02"); save_game()
    call screen chapter06_03_02_screen
label chapter06_03:
    jump chapter06_03_01
    jump chapter_select

# page 1
screen chapter06_03_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter06_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter06_03_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Обычно рекурсию и итерацию представляют как две принципиально разные вещи. Поэтому для вас может стать открытием тот факт, что обе они представляют собой реализацию {i}одного и того же фундаментального принципа!{/i} Более того, они {b}{i}эквивалентны по вычислительной мощности{/i}{/b}: любую рекурсивную программу можно переписать итеративно (через циклы), и любую циклическую программу можно переписать рекурсивно!\n\nПосмотрим на составляющие обычного цикла:\n\n    1. {color=#0f0}Условие цикла (Looping Condition){/color}\n    2. {color=#f0f}Переменная счетчика (Iterator Variable){/color}\n    3. {color=#f00}Тело цикла (Loop Body){/color}\n\nИх можно сопоставить с частями рекурсивной функции (по соответствующим цветам):\n\n    1. {color=#0f0}Базовый случай (Base Case){/color}\n    2. {color=#f0f}Обновление аргументов при вызове{/color}\n    3. {color=#f00}Рекурсивный случай (Recursive Case){/color}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "hanoi.png":
        xsize 1280
        ysize 878
        xalign 0.5
        yalign .97

# page 2
screen chapter06_03_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter06_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter06_03_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Сравним итеративное и рекурсивное решение одной и той же задачи. Напишем функцию, которая принимает параметр {font=monospace.ttf}{color=#888}num{/color}{/font} и выводит числа от {font=monospace.ttf}{color=#f00}1{/color}{/font} до {font=monospace.ttf}{color=#888}num{/color}{/font} (включительно).\n\n{font=monospace.ttf}    {color=#f0f}# Итеративное решение{/color}\n    {color=#ff0}def{/color} {color=#57f}count_iter{/color}(num):\n        {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}1{/color}, num {color=#0f0}+{/color} {color=#f00}1{/color}):\n            {color=#57f}print{/color}(i)\n\n    {color=#f0f}# Рекурсивное решение{/color}\n    {color=#ff0}def{/color} {color=#57f}count_rec{/color}(num):\n        {color=#ff0}if{/color} num {color=#0f0}=={/color} {color=#f00}1{/color}:\n            {color=#57f}print{/color}({color=#f00}1{/color})\n        {color=#ff0}else{/color}:\n            {color=#57f}count_rec{/color}(num {color=#0f0}-{/color} {color=#f00}1{/color})\n            {color=#57f}print{/color}(num){/font}\n\nПросто, правда? Не дайте тривиальности этого примера усыпить вашу бдительность. В реальной разработке не все задачи одинаково просто решаются обоими способами. Да, любую задачу {b}{i}можно{/i}{/b} решить и циклом, и рекурсией, но зачастую один из подходов оказывается {b}{i}в разы проще и естественнее{/i}{/b} другого. Ваша задача как программиста — выбрать наиболее подходящий инструмент перед написанием кода.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Какие свойства задачи делают ее более удобной для рекурсии? А для итерации?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
