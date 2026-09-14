# chapter and lesson labels
label chapter07_01_01:
    $ COMPLETED.add("chapter07_01_01"); save_game()
    call screen chapter07_01_01_screen
label chapter07_01:
    jump chapter07_01_01
    jump chapter_select

# page 1
screen chapter07_01_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter07_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 7{/i}{/b}{/size}\n\n{color=#57f}{b}{i}\"Я до сих пор не научил свой компьютер ничему о реальном мире... вообще ничему.\"\n    — Вы, пройдя шесть глав этого курса{/i}{/b}{/color}\n\nВ самом начале пути мы пообещали вам следующее:\n\n{color=#57f}{i}\"Ваша цель — помочь компьютеру понять окружающий мир.\"{/i}{/color}\n\nТеперь, открывая седьмую главу (кстати, отличный прогресс!), вы можете подумать, что мы вас обманули. До сих пор мы работали лишь с базовыми типами и структурами данных, условиями, циклами и функциями.\n\nМы просим вас дать нам шанс еще на одну главу. Вы узнали достаточно о синтаксисе Python, чтобы начать по-настоящему общаться с компьютером. Пришло время, друг наш, научить компьютер понимать окружающий мир.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "robot.png":
        xsize 600
        ysize 713
        xalign 0.5
        yalign .99
