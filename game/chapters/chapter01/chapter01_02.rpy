# chapter and lesson labels
label chapter01_02_01:
    $ COMPLETED.add("chapter01_02_01"); save_game()
    call screen chapter01_02_01_screen
label chapter01_02_02:
    $ COMPLETED.add("chapter01_02_02"); save_game()
    call screen chapter01_02_02_screen
label chapter01_02_03:
    $ COMPLETED.add("chapter01_02_03"); save_game()
    call screen chapter01_02_03_screen
label chapter01_02:
    jump chapter01_02_01
    jump chapter_select

# page 1
screen chapter01_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter01_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 1{/i}{/b}{/size}\n\n{color=#57f}{b}{i}\"Каждый объект рассказывает историю, если уметь ее читать.\"{/i}{/b} — Генри Форд{/color}\n\nОглянитесь вокруг. Задержите взгляд на любом предмете: чашке, карандаше, столе — на чем угодно. А теперь подумайте:\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Как бы вы описали предмет, на который смотрите?\n\nВозможно, вы обратите внимание на свойства объекта: его форму, цвет, вес или объем. А может, опишете его связь с окружающим миром: положение в комнате, что находится внутри или какие эмоции он вызывает.\n\nСмысл этого упражнения в следующем: мы, люди, прекрасно умеем считывать окружающий мир. Мы воспринимаем реальность как совокупность объектов, взаимодействующих друг с другом. Мы понимаем эти объекты, понимаем их связи и, как заметил Генри Форд, понимаем историю, которую они создают.\n\nА вот ваш компьютер — нет. Начиная погружение в Computer Science и особенно в Объектно-Ориентированное Программирование, помните:\n\n{b}{color=#57f}Ваша цель — помочь компьютеру понять этот мир.{/color}{/b}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "radio.png":
        xsize 550
        ysize 550
        xalign 0.75
        yalign .99

# page 2
screen chapter01_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter01_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_02_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Вы умнее своего компьютера. Мы гарантируем, что это чистая правда. В глубине души компьютер понимает лишь нули, единицы и сложение. И всё же, начав этот курс, вы приняли вызов: научить компьютер взаимодействовать с миром.\n\nБезусловно, задача непростая. Будьте готовы к трудностям, к досаде и к ошибкам. Будьте готовы посвятить часы упорного труда, чтобы донести свои сложные человеческие идеи до машины.\n\nНо ни в коем случае не опускайте руки! Если проявить терпение, упорство и гибкость мышления, у вас обязательно всё получится. И когда вы научитесь обращаться с компьютером как с инструментом, вы откроете его подлинную мощь.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "desktop.png":
        xsize 1280
        ysize 985
        xalign 0.5
        yalign 0.95

# page 3
screen chapter01_02_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter01_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_02_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Но прежде чем обучать компьютер представлению о мире, вам потребуется научиться общаться с ним (увы, обычный человеческий язык он не понимает). В этом курсе языком вашего диалога с машиной станет Python.\n\nВ следующем разделе вы познакомитесь с самой базовой азбукой Python.\n\n{font=monospace.ttf}    {color=#57f}max{/color}(luck){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
