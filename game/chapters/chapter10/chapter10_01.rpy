# chapter and lesson labels
label chapter10_01_01:
    $ COMPLETED.add("chapter10_01_01"); save_game()
    call screen chapter10_01_01_screen
label chapter10_01_02:
    $ COMPLETED.add("chapter10_01_02"); save_game()
    call screen chapter10_01_02_screen
label chapter10_01:
    jump chapter10_01_01
    jump chapter_select

# page 1
screen chapter10_01_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter10_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter10_01_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 10{/i}{/b}{/size}\n\n{color=#57f}{b}{i}\"Я не могу прокладывать новый путь: я все еще собираю огнемет\"{/i}{/b}{/color}\n\nКогда вы беретесь за работу в реальной жизни, вам редко приходится делать абсолютно все с нуля. Собрать стол? Отлично, но вам не нужно лично выплавлять гвозди или валить лес. Приготовить ужин? Пожалуйста, но вам не придется добывать соль на солончаках.\n\nОднако на протяжении этого курса мы писали логику почти с нуля. На практике это неэффективно: мы постоянно изобретаем велосипед!\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} На каких типовых операциях вы ощущали, что заново изобретаете колесо?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "wheel.png":
        xsize 900
        ysize 900
        xalign 0.5
        yalign .96

# page 2
screen chapter10_01_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter10_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter10_01_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter10"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Чтобы избавить нас от рутины, Python позволяет повторно использовать уже написанный другими разработчиками код с помощью {b}{i}библиотек (libraries){/i}{/b}.\n\nБиблиотеки Python — это готовые наборы модулей и пакетов с полезными функциями и классами, решающими практические задачи. Их можно использовать как готовый \"черный ящик\", не тратя время на написание с нуля.\n\nБиблиотеки делятся на две группы:\n\n    1. {b}Стандартная библиотека Python (PSL):{/b} набор базовых инструментов, идущий в комплекте с самим языком Python\n    2. {b}Внешние библиотеки:{/b} мощные специализированные пакеты от сторонних разработчиков со всего мира (устанавливаемые через менеджер pip)\n\nДавайте познакомимся с обеими категориями.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
