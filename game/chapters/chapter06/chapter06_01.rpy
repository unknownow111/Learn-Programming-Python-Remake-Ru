# chapter and lesson labels
label chapter06_01_01:
    $ COMPLETED.add("chapter06_01_01"); save_game()
    call screen chapter06_01_01_screen
label chapter06_01_02:
    $ COMPLETED.add("chapter06_01_02"); save_game()
    call screen chapter06_01_02_screen
label chapter06_01_03:
    $ COMPLETED.add("chapter06_01_03"); save_game()
    call screen chapter06_01_03_screen
label chapter06_01:
    jump chapter06_01_01
    jump chapter_select

# page 1
screen chapter06_01_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter06_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter06_01_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 6{/i}{/b}{/size}\n\n{color=#57f}{b}{i}\"Чтобы понять рекурсию, нужно сначала понять рекурсию.\"{/i}{/b} — Стивен Хокинг{/color}\n\nВы стоите в очереди в театр, где через 15 минут начнется выступление вашего любимого артиста. Вам очень хочется узнать, сколько людей стоит впереди вас, чтобы понять, успеете ли вы занять свои места вовремя. Но очередь длинная и извилистая — начала очереди вам просто не видно.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Как вы можете выяснить, сколько людей стоит перед вами?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "long_line.png":
        xsize 1877
        ysize 1028
        xalign 0.5
        yalign .95

# page 2
screen chapter06_01_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter06_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter06_01_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter06_01_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Вы находите элегантное решение. Вы спрашиваете стоящего впереди человека:\n\n{color=#57f}{i}\"Ты видишь, сколько людей перед тобой? Если нет, можешь спросить то же самое у человека перед тобой?\"{/i}{/color}\n\nЧеловек впереди тоже не видит начала очереди. Поэтому он задает точно такой же вопрос следующему человеку. Тот передает вопрос дальше, следующий — дальше...\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Будет ли эта цепочка бесконечной?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter06_01_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter06_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter06_01_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Конечно же нет! Вопрос будет передаваться по очереди ровно {i}до тех пор{/i}, пока не дойдет до самого первого человека. А он уверенно ответит: {color=#57f}{i}\"Передо мной {font=monospace.ttf}{color=#f00}0{/color}{/font} человек!\"{/i}{/color}\n\nТеперь стоящий за ним может сказать: {color=#57f}{i}\"Передо мной {font=monospace.ttf}{color=#f00}1{/color}{/font} человек!\"{/i}{/color}\n\nСледующий скажет: {color=#57f}{i}\"Передо мной {font=monospace.ttf}{color=#f00}2{/color}{/font} человека!\"{/i}{/color}\n\nИ так далее в обратном направлении... В конце концов, человек перед вами скажет: {color=#57f}{i}\"Передо мной {font=monospace.ttf}{color=#888}n{/color}{/font} человек!\"{/i}{/color}, и вы точно узнаете свой ответ: {font=monospace.ttf}{color=#888}n{/color}{color=#0f0}+{/color}{color=#f00}1{/color}{/font}.\n\nТо, что мы только что проделали (разбиение сложной задачи на меньшие и простые подзадачи того же типа), называется {b}{i}рекурсией{/i}{/b} ({b}{i}recursion{/i}{/b}). В этой главе мы научимся реализовывать рекурсию в Python.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
