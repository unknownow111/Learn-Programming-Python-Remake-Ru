# chapter and lesson labels
label chapter09_03_01:
    $ COMPLETED.add("chapter09_03_01"); save_game()
    call screen chapter09_03_01_screen
label chapter09_03_02:
    $ COMPLETED.add("chapter09_03_02"); save_game()
    call screen chapter09_03_02_screen
label chapter09_03_03:
    $ COMPLETED.add("chapter09_03_03"); save_game()
    call screen chapter09_03_03_screen
label chapter09_03:
    jump chapter09_03_01
    jump chapter_select

# page 1
screen chapter09_03_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter09_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_03_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь поговорим о записи в файлы. До сих пор мы просто выводили текст на экран, но реальные программы должны сохранять результаты работы на диск для будущего использования. Наша кондитерская BakeHaus хочет записывать актуальный статус производства в файл {font=monospace.ttf}{color=#f00}message.txt{/color}{/font}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "write.png":
        xsize 1920
        ysize 1214
        xalign 0.5
        yalign .87

# page 2
screen chapter09_03_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter09_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_03_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter09_03_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Для записи открываем файл с параметром {font=monospace.ttf}{color=#f00}\"w\"{/color}{/font} (write):\n\n{font=monospace.ttf}    file {color=#0f0}={/color} {color=#57f}open{/color}({color=#f00}\"message.txt\"{/color}, {color=#f00}\"w\"{/color}){/font}\n\nВнимание: режим {font=monospace.ttf}{color=#f00}\"w\"{/color}{/font} полностью перезаписывает существующий файл!\n\nДля записи текста используется метод {font=monospace.ttf}{color=#888}.{/color}{color=#57f}write{/color}{color=#888}(){/color}{/font}:\n\n{font=monospace.ttf}    file.{color=#57f}write{/color}({color=#f00}\"Macarons are the best!\"{/color}){/font}\n\nДля записи последовательности строк — метод {font=monospace.ttf}{color=#888}.{/color}{color=#57f}writelines{/color}{color=#888}(){/color}{/font}:\n\n{font=monospace.ttf}    file.{color=#57f}writelines{/color}([[{color=#f00}\"Do you agree?\"{/color}, {color=#f00}\"We should hope so!\"{/color}]){/font}\n\nПомните: эти методы не добавляют перенос строки автоматически.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter09_03_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter09_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter09_03_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter09"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Если вам нужно дописать новые данные в конец существующего файла без удаления старых, откройте файл в режиме добавления ({font=monospace.ttf}{color=#f00}\"a\"{/color}{/font} — append):\n\n{font=monospace.ttf}    file {color=#0f0}={/color} {color=#57f}open{/color}({color=#f00}\"message.txt\"{/color}, {color=#f00}\"a\"{/color}){/font}\n\nНовая строка будет аккуратно добавлена в самый конец файла.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
