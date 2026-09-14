# chapter and lesson labels
label chapter05_04_01:
    $ COMPLETED.add("chapter05_04_01"); save_game()
    call screen chapter05_04_01_screen
label chapter05_04_02:
    $ COMPLETED.add("chapter05_04_02"); save_game()
    call screen chapter05_04_02_screen
label chapter05_04_03:
    $ COMPLETED.add("chapter05_04_03"); save_game()
    call screen chapter05_04_03_screen
label chapter05_04_04:
    $ COMPLETED.add("chapter05_04_04"); save_game()
    call screen chapter05_04_04_screen
label chapter05_04_05:
    $ COMPLETED.add("chapter05_04_05"); save_game()
    call screen chapter05_04_05_screen
label chapter05_04:
    jump chapter05_04_01
    jump chapter_select

# page 1
screen chapter05_04_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter05_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_04_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "До этого момента мы вызывали {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} лишь с одним аргументом:\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}\"Hello World\"{/color}){/font}\n\nНо знали ли вы, что следующий код тоже корректен и {i}также{/i} выведет {font=monospace.ttf}{color=#f00}Hello World{/color}{/font}?\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}\"Hello\"{/color}, {color=#f00}\"World\"{/color}){/font}\n\nАналогично, следующий вызов напечатает {font=monospace.ttf}{color=#f00}1 2 3 4 True False{/color}{/font}:\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}1{/color}, {color=#f00}\"2\"{/color}, {color=#f00}3{/color}, {color=#f00}4{/color}, {color=#f00}True{/color}, {color=#f00}False{/color}){/font}\n\nМы можем передать в {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} {b}{i}любое количество{/i}{/b} аргументов, и функция {b}{i}напечатает их все!{/i}{/b}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "ring.png":
        xsize 1000
        ysize 607
        xalign 0.5
        yalign .8
    text "{font=cursive.ttf}{size=+50}{color=#ffd700}{i}Один вызов, чтоб напечатать их всех...{/i}{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.92

# page 2
screen chapter05_04_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter05_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_04_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_04_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Это должно вас озадачить.\n\nВспомните: когда мы определяем функцию, мы явно указываем, какие параметры она принимает. Это делается заранее, что означает строго фиксированное количество аргументов! Как же функция вроде {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} справляется с произвольным их количеством?\n\nОтвет — {b}{i}переменное число аргументов (variable arguments){/i}{/b}. В Python есть два специальных синтаксиса для параметров:\n\n    1. {font=monospace.ttf}{color=#0f0}*{/color}{color=#888}args{/color}{/font} — позволяет передать любое количество {b}{u}позиционных{/u}{/b} аргументов\n    2. {font=monospace.ttf}{color=#0f0}**{/color}{color=#888}kwargs{/color}{/font} — позволяет передать любое количество {b}{u}именованных{/u}{/b} аргументов (keyword arguments)\n\nДавайте разберем, как устроен каждый из них.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter05_04_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter05_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_04_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_04_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{font=monospace.ttf}{color=#0f0}*{/color}{color=#888}args{/color}{/font}{/size}\n\nФормально {font=monospace.ttf}{color=#0f0}*{/color}{color=#888}args{/color}{/font} собирает все неименованные аргументы и помещает их в {font=monospace.ttf}{color=#57f}tuple{/color}{/font} (кортеж). Параметр {font=monospace.ttf}{color=#0f0}*{/color}{color=#888}args{/color}{/font} должен стоять последним среди позиционных параметров. Например, следующий код принимает один обязательный параметр {font=monospace.ttf}{color=#888}param1{/color}{/font}, а затем произвольное число аргументов:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}output_var_args{/color}(param1, {color=#0f0}*{/color}args):\n        {color=#57f}print{/color}(param1)\n        {color=#ff0}for{/color} arg {color=#0f0}in{/color} args:\n            {color=#57f}print{/color}(arg)\n\n    {color=#57f}output_var_args{/color}({color=#f00}\"a\"{/color}, {color=#f00}\"b\"{/color}, {color=#f00}\"c\"{/color}){/font}\n\n{size=+20}{font=monospace.ttf}{color=#0f0}**{/color}{color=#888}kwargs{/color}{/font}{/size}\n\nФормально {font=monospace.ttf}{color=#0f0}**{/color}{color=#888}kwargs{/color}{/font} собирает все переданные именованные аргументы и упаковывает их в словарь {font=monospace.ttf}{color=#57f}dict{/color}{/font}: {font=monospace.ttf}{color=#888}{{keyword: value}{/color}{/font}. {font=monospace.ttf}{color=#0f0}**{/color}{color=#888}kwargs{/color}{/font} должен быть самым последним параметром функции. Например:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}output_var_kwargs{/color}(param1, {color=#0f0}**{/color}kwargs):\n        {color=#57f}print{/color}(param1)\n        {color=#ff0}for{/color} key, arg {color=#0f0}in{/color} kwargs.{color=#57f}items{/color}():\n            {color=#57f}print{/color}(key, arg)\n\n    {color=#57f}output_var_kwargs{/color}({color=#f00}\"a\"{/color}, x{color=#0f0}={/color}{color=#f00}\"b\"{/color}, y{color=#0f0}={/color}{color=#f00}\"c\"{/color}){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Упорядочен ли {font=monospace.ttf}{color=#0f0}*{/color}{color=#888}args{/color}{/font}? А что насчет {font=monospace.ttf}{color=#0f0}**{/color}{color=#888}kwargs{/color}{/font}?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter05_04_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter05_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_04_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_04_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Надеемся, прочитав эти два правила, вы подумали: \"Минуточку... как {b}{i}оба{/i}{/b} из них могут быть самым последним параметром?\"\n\n    1. {font=monospace.ttf}{color=#0f0}*{/color}{color=#888}args{/color}{/font} должен быть последним параметром.\n    2. {font=monospace.ttf}{color=#0f0}**{/color}{color=#888}kwargs{/color}{/font} должен быть последним параметром.\n\nВ Python абсолютно допустимо использовать {font=monospace.ttf}{color=#0f0}*{/color}{color=#888}args{/color}{/font} и {font=monospace.ttf}{color=#0f0}**{/color}{color=#888}kwargs{/color}{/font} одновременно в одной функции. В этом случае {font=monospace.ttf}{color=#0f0}*{/color}{color=#888}args{/color}{/font} становится {b}{i}предпоследним{/i}{/b}, а {font=monospace.ttf}{color=#0f0}**{/color}{color=#888}kwargs{/color}{/font} — {b}{i}последним{/i}{/b}:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}output_var_KwArgs{/color}(param1, {color=#0f0}*{/color}args, {color=#0f0}**{/color}kwargs):\n        {color=#57f}print{/color}(param1)\n        {color=#ff0}for{/color} arg {color=#0f0}in{/color} args:\n            {color=#57f}print{/color}(arg)\n        {color=#ff0}for{/color} key, arg {color=#0f0}in{/color} kwargs.{color=#57f}items{/color}():\n            {color=#57f}print{/color}(key, arg){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
screen chapter05_04_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter05_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_04_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "До сих пор мы всегда использовали названия {font=monospace.ttf}{color=#0f0}*{/color}{color=#888}args{/color}{/font} и {font=monospace.ttf}{color=#0f0}**{/color}{color=#888}kwargs{/color}{/font}. Однако строгой привязки к этим словам нет: для Python имеют значение лишь сами звездочки: одна звездочка ({font=monospace.ttf}{color=#0f0}*{/color}{/font}) для позиционных аргументов и две звездочки ({font=monospace.ttf}{color=#0f0}**{/color}{/font}) для именованных. Например:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}foo{/color}(zap, {color=#0f0}*{/color}bar, {color=#0f0}**{/color}baz):\n        ...{/font}\n\nТем не менее, общепринятым стандартом в сообществе Python является использование именно названий {font=monospace.ttf}{color=#0f0}*{/color}{color=#888}args{/color}{/font} и {font=monospace.ttf}{color=#0f0}**{/color}{color=#888}kwargs{/color}{/font}, так как это делает код понятным для любого разработчика.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
