# chapter and lesson labels
label chapter09_01_01:
    $ COMPLETED.add("chapter09_01_01"); save_game()
    call screen chapter09_01_01_screen
label chapter09_01_02:
    $ COMPLETED.add("chapter09_01_02"); save_game()
    call screen chapter09_01_02_screen
label chapter09_01:
    jump chapter09_01_01
    jump chapter_select

# page 1
screen chapter09_01_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter09_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_01_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 9{/i}{/b}{/size}\n\n{color=#57f}{b}{i}Давайте испечем макаруны!{/i}{/b}{/color}\n\nМы объединили усилия, чтобы открыть собственную кондитерскую BakeHaus. Наша первая задача — приготовить фирменное блюдо: пирожные {a=https://en.wikipedia.org/wiki/Macaron}макарун (macarons){/a}. Мы уже сходили в супермаркет и купили ингредиенты.\n\nСудя по чеку, у нас есть следующее:\n\n{font=monospace.ttf}    powdered sugar (сахарная пудра)\n    almond flour (миндальная мука)\n    salt (соль)\n    egg yolks (яичные желтки)\n    vanilla extract (экстракт ванили){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Можем ли мы приготовить макаруны?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "bakery.png":
        xsize 1440
        ysize 1118
        xalign 0.73
        yalign .95

# page 2
screen chapter09_01_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter09_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_01_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter09"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Если вы не прирожденный шеф-повар ({i}мы, честно признаться, нет{/i}), ваш ответ, скорее всего: {color=#57f}{i}\"Понятия не имею\"{/i}{/color}. Но не переживайте: к концу этой главы вы станете настоящим экспертом в макарунах.\n\nДо сих пор мы получали данные для программ лишь двумя путями:\n\n    1. Мы вписывали их прямо в код программы заранее\n    2. Пользователь вводил их вручную с клавиатуры\n\nДля реального учета на складе кондитерской BakeHaus это ужасно неудобно: пришлось бы сажать сотрудника вбивать каждый чек символ за символом.\n\nВместо этого мы можем научить Python напрямую открывать файлы чеков и извлекать оттуда данные автоматически! Этим мы и займемся.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
