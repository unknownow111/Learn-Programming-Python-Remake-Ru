# chapter and lesson labels
label chapter09_04_01:
    $ COMPLETED.add("chapter09_04_01"); save_game()
    call screen chapter09_04_01_screen
label chapter09_04_02:
    $ COMPLETED.add("chapter09_04_02"); save_game()
    call screen chapter09_04_02_screen
label chapter09_04_03:
    $ COMPLETED.add("chapter09_04_03"); save_game()
    call screen chapter09_04_03_screen
label chapter09_04_04:
    $ COMPLETED.add("chapter09_04_04"); save_game()
    call screen chapter09_04_04_screen
label chapter09_04:
    jump chapter09_04_01
    jump chapter_select

# page 1
screen chapter09_04_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter09_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_04_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "А как сохранить на диск не просто строку, а сложный объект со всеми его атрибутами?\n\nДля этого используют {b}{i}сериализацию (serialization){/i}{/b} — преобразование состояния объекта в поток данных для сохранения в файл, и обратный процесс — {b}{i}десериализацию (deserialization){/i}{/b} для восстановления живого объекта в памяти. Для этого применяют специальные библиотеки Python.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "floppy.png":
        xsize 800
        ysize 800
        xalign 0.5
        yalign .99

# page 2
screen chapter09_04_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter09_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_04_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_04_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Сохранение и загрузка JSON{/b}{/color}\n\nФормат {a=https://www.json.org/json-en.html}JSON (JavaScript Object Notation){/a} — легкий человекочитаемый текстовый стандарт обмена данными, очень похожий на словарь Python {font=monospace.ttf}{color=#57f}dict{/color}{/font}.\n\nДля работы с ним используется модуль {font=monospace.ttf}{color=#888}json{/color}{/font}:\n\n{font=monospace.ttf}{size=-10}    {color=#ff0}import{/color} json\n\n    output_file {color=#0f0}={/color} {color=#57f}open{/color}({color=#f00}\"my_dict.json\"{/color}, {color=#f00}\"w\"{/color})\n    json.{color=#57f}dump{/color}(my_dict, output_file)         {color=#f0f}# запись объекта в json-файл{/color}\n    output_file.{color=#57f}close{/color}()\n\n    input_file {color=#0f0}={/color} {color=#57f}open{/color}({color=#f00}\"my_dict.json\"{/color})\n    my_dict_2 {color=#0f0}={/color} json.{color=#57f}load{/color}(input_file)       {color=#f0f}# восстановление объекта из файла{/color}\n    input_file.{color=#57f}close{/color}(){/size}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter09_04_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter09_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_04_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_04_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Сохранение и загрузка Pickle{/b}{/color}\n\nФормат Pickle — специальный встроенный механизм сериализации Python. В отличие от JSON, он сохраняет любые объекты в виде бинарных данных ({color=#f00}\"wb\" / \"rb\"{/color}). Он работает быстрее и файлы получаются меньше, но прочитать их человеком в блокноте невозможно:\n\n{font=monospace.ttf}    {color=#ff0}import{/color} pickle\n\n    output_file {color=#0f0}={/color} {color=#57f}open{/color}({color=#f00}\"my_dict.pkl\"{/color}, {color=#f00}\"wb\"{/color})\n    pickle.{color=#57f}dump{/color}(my_dict, output_file)\n    output_file.{color=#57f}close{/color}()\n\n    input_file {color=#0f0}={/color} {color=#57f}open{/color}({color=#f00}\"my_dict.pkl\"{/color}, {color=#f00}\"rb\"{/color})\n    my_dict_2 {color=#0f0}={/color} pickle.{color=#57f}load{/color}(input_file)\n    input_file.{color=#57f}close{/color}(){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter09_04_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter09_04"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_04_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter09"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Что выбрать?\n\n    – {font=monospace.ttf}{color=#888}json{/color}{/font} понятен человеку и совместим с любыми другими языками и веб-сервисами\n    – {font=monospace.ttf}{color=#888}pickle{/color}{/font} работает только внутри Python, но умеет сохранять почти любые типы объектов быстрее и компактнее.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "pickles.png":
        xsize 1000
        ysize 1179
        xalign 0.5
        yalign .95
