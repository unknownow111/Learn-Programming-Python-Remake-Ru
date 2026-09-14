# chapter and lesson labels
label chapter05_03_01:
    $ COMPLETED.add("chapter05_03_01"); save_game()
    call screen chapter05_03_01_screen
label chapter05_03_02:
    $ COMPLETED.add("chapter05_03_02"); save_game()
    call screen chapter05_03_02_screen
label chapter05_03_03:
    $ COMPLETED.add("chapter05_03_03"); save_game()
    call screen chapter05_03_03_screen
label chapter05_03:
    jump chapter05_03_01
    jump chapter_select

# page 1
screen chapter05_03_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter05_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_03_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Ранее мы упоминали, что можно изменить окончание строки в функции {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} с помощью {font=monospace.ttf}{color=#888}end{/color}{color=#0f0}={/color}{/font}:\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}\"hello\"{/color}, end{color=#0f0}={/color}{color=#f00}\"!\"{/color}){/font}\n\nТеперь, узнав, как устроены функции, вы, возможно, спросите: {i}а что здесь вообще происходит?{/i}\n\nВ этом примере параметр {font=monospace.ttf}{color=#888}end{/color}{/font} имеет так называемое {b}{i}значение по умолчанию{/i}{/b} ({b}{i}default parameter value{/i}{/b}). Это запасное значение, которое используется автоматически, если при вызове аргумент не был передан. Благодаря этому параметры могут быть опциональными.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Каково значение по умолчанию для {font=monospace.ttf}{color=#888}end{/color}{/font} в функции {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font}?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "default_user.png":
        xsize 1000
        ysize 1000
        xalign 0.5
        yalign .95

# page 2
screen chapter05_03_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter05_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_03_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_03_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Синтаксис для задания значения параметра по умолчанию:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}function_name{/color}(param_1, default_param{color=#0f0}={/color}default_value):\n        {color=#f0f}# тело функции{/color}{/font}\n\nВспомните: функция {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} по умолчанию ставит символ переноса строки ({font=monospace.ttf}{color=#f00}\\n{/color}{/font}) в конце вывода. Это значит, что в заголовке функции определен параметр {font=monospace.ttf}{color=#888}end{/color}{color=#0f0}={/color}{color=#f00}\"\\n\"{/color}{/font}. Когда мы вызываем {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} с {font=monospace.ttf}{color=#888}end{/color}{color=#0f0}={/color}{color=#f00}\"!\"{/color}{/font}, мы просто переопределяем это значение по умолчанию.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter05_03_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter05_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_03_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "При объявлении функции с параметрами по умолчанию Python требует, чтобы они располагались в {b}{i}конце{/i}{/b} списка параметров — строго после всех обязательных параметров. При вызове функции именованные параметры со значениями по умолчанию можно указывать в любом порядке. Допустим, у нас есть функция:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}bar{/color}(a, b, c, d{color=#0f0}={/color}{color=#f00}None{/color}, e{color=#0f0}={/color}{color=#f00}5{/color}):\n        {color=#57f}print{/color}(a {color=#0f0}+{/color} b {color=#0f0}+{/color} c)\n        {color=#57f}print{/color}(d)\n        {color=#57f}print{/color}(e){/font}\n\nКаждый из следующих вариантов вызова {font=monospace.ttf}{color=#57f}bar{/color}{color=#888}(){/color}{/font} абсолютно корректен:\n\n{font=monospace.ttf}    {color=#57f}bar{/color}({color=#f00}1{/color}, {color=#f00}2{/color}, {color=#f00}3{/color})\n    {color=#57f}bar{/color}({color=#f00}1{/color}, {color=#f00}2{/color}, {color=#f00}3{/color}, {color=#f00}4{/color})\n    {color=#57f}bar{/color}({color=#f00}1{/color}, {color=#f00}2{/color}, {color=#f00}3{/color}, {color=#f00}4{/color}, {color=#f00}5{/color})\n    {color=#57f}bar{/color}({color=#f00}1{/color}, {color=#f00}2{/color}, {color=#f00}3{/color}, d{color=#0f0}={/color}{color=#f00}4{/color}, e{color=#0f0}={/color}{color=#f00}5{/color})\n    {color=#57f}bar{/color}({color=#f00}1{/color}, {color=#f00}2{/color}, {color=#f00}3{/color}, e{color=#0f0}={/color}{color=#f00}5{/color}, d{color=#0f0}={/color}{color=#f00}4{/color}){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Что выведет каждый из этих вызовов?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
