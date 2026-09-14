# chapter and lesson labels
label chapter04_02_01:
    $ COMPLETED.add("chapter04_02_01"); save_game()
    call screen chapter04_02_01_screen
label chapter04_02_02:
    $ COMPLETED.add("chapter04_02_02"); save_game()
    call screen chapter04_02_02_screen
label chapter04_02_03:
    $ COMPLETED.add("chapter04_02_03"); save_game()
    call screen chapter04_02_03_screen
label chapter04_02_04:
    $ COMPLETED.add("chapter04_02_04"); save_game()
    call screen chapter04_02_04_screen
label chapter04_02_05:
    $ COMPLETED.add("chapter04_02_05"); save_game()
    call screen chapter04_02_05_screen
label chapter04_02_06:
    $ COMPLETED.add("chapter04_02_06"); save_game()
    call screen chapter04_02_06_screen
label chapter04_02_07:
    $ COMPLETED.add("chapter04_02_07"); save_game()
    call screen chapter04_02_07_screen
label chapter04_02:
    jump chapter04_02_01
    jump chapter_select

# page 1
screen chapter04_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter04_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Списки (Lists): Сущность{/b}{/color}\n\nПервая структура данных, которую мы рассмотрим — это {font=monospace.ttf}{color=#57f}list{/color}{/font} (список), самая популярная структура данных в Python. Списки в Python представляют собой {b}{i}упорядоченные{/i}{/b} последовательности данных. Мы можем объявить переменную списка (и сохранить в {font=monospace.ttf}{color=#888}my_list{/color}{/font}) следующим образом:\n\n{font=monospace.ttf}    my_list {color=#0f0}={/color} {color=#57f}list{/color}(){/font}\n\nЕсли мы заранее знаем, что хотим поместить в {font=monospace.ttf}{color=#57f}list{/color}{/font}, мы также можем объявить его с помощью квадратных скобок:\n\n{font=monospace.ttf}    my_list {color=#0f0}={/color} [[{color=#f00}\"hello\"{/color}, {color=#f00}2{/color}, {color=#f00}True{/color}]{/font}\n\nСписки в Python (прямо как строки!) имеют нулевую индексацию (начинаются с 0). Вы можете представить {font=monospace.ttf}{color=#888}my_list{/color}{/font} в таком виде:\n\n{font=monospace.ttf}    ------------------------------\n    | {color=#57f}Index{/color} |    0    | 1 |   2  |\n    ------------------------------\n    | {color=#57f}Data{/color}  | {color=#f00}\"hello\"{/color} | {color=#f00}2{/color} | {color=#f00}True{/color} |\n    ------------------------------{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "list.png":
        xsize 800
        ysize 800
        xalign 0.9
        yalign .85

# page 2
screen chapter04_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter04_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_02_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Списки (Lists): Вставка{/b}{/color}\n\nМы можем добавлять элементы в {font=monospace.ttf}{color=#57f}list{/color}{/font} с помощью функции (метода) {font=monospace.ttf}{color=#888}.{/color}{color=#57f}append{/color}{color=#888}(){/color}{/font}*, которая добавляет элемент в {b}{i}конец{/i}{/b} списка. Допустим, мы уже объявили {font=monospace.ttf}{color=#888}my_list{/color}{/font} с тремя элементами с предыдущей страницы:\n\n{font=monospace.ttf}    my_list {color=#0f0}={/color} [[{color=#f00}\"hello\"{/color}, {color=#f00}2{/color}, {color=#f00}True{/color}]{/font}\n\nТеперь мы можем добавить в конец еще два значения:\n\n{font=monospace.ttf}    my_list.{color=#57f}append{/color}({color=#f00}\"new\"{/color})\n    my_list.{color=#57f}append{/color}({color=#f00}\"values!\"{/color}){/font}\n\nТеперь {font=monospace.ttf}{color=#888}my_list{/color}{/font} выглядит так (обратите внимание на два новых элемента в конце):\n\n{font=monospace.ttf}    --------------------------------------------------\n    | {color=#57f}Index{/color} |    0    | 1 |   2  |   3   |     4     |\n    --------------------------------------------------\n    | {color=#57f}Data{/color}  | {color=#f00}\"hello\"{/color} | {color=#f00}2{/color} | {color=#f00}True{/color} | {color=#f00}\"new\"{/color} | {color=#f00}\"values!\"{/color} |\n    --------------------------------------------------{/font}\n\n{i}*Ого! Почему синтаксис именно {font=monospace.ttf}{color=#888}my_list{/color}{color=#888}.{/color}{color=#57f}append{/color}{color=#888}(){/color}{/font}, а не что-то вроде {font=monospace.ttf}{color=#888}.{/color}{color=#57f}append{/color}{color=#888}(my_list){/color}{/font}? Это связано с тем, каким типом функций является {font=monospace.ttf}{color=#57f}append{/color}{color=#888}(){/color}{/font} (методом объекта). Мы скоро это подробно объясним! Пока можете считать, что любая функция, имя которой вызывается через точку, используется именно так.{/i}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter04_02_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter04_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_02_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_02_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Списки (Lists): Доступ{/b}{/color}\n\nВспомните: мы использовали оператор индексации для доступа к символам в строке. Точно такой же синтаксис используется для доступа к элементам списка {font=monospace.ttf}{color=#57f}list{/color}{/font}! Допустим, {font=monospace.ttf}{color=#888}my_list{/color}{/font} все еще содержит:\n\n{font=monospace.ttf}    --------------------------------------------------\n    | {color=#57f}Index{/color} |    0    | 1 |   2  |   3   |     4     |\n    --------------------------------------------------\n    | {color=#57f}Data{/color}  | {color=#f00}\"hello\"{/color} | {color=#f00}2{/color} | {color=#f00}True{/color} | {color=#f00}\"new\"{/color} | {color=#f00}\"values!\"{/color} |\n    --------------------------------------------------{/font}\n\nМы можем извлечь значения по индексам {font=monospace.ttf}{color=#f00}0{/color}{/font}, {font=monospace.ttf}{color=#f00}1{/color}{/font} и {font=monospace.ttf}{color=#f00}2{/color}{/font} вот так:\n\n{font=monospace.ttf}    extract_hello {color=#0f0}={/color} my_list[[{color=#f00}0{/color}]\n    extract_2 {color=#0f0}={/color} my_list[[{color=#f00}1{/color}]\n    extract_true {color=#0f0}={/color} my_list[[{color=#f00}2{/color}]{/font}\n\nОператор индексации умеет не только обращаться к отдельным элементам. Чтобы получить все элементы от индекса {font=monospace.ttf}{color=#888}start{/color}{/font} до индекса {font=monospace.ttf}{color=#888}end{/color}{/font}, мы используем формулу {b}{i}срезов{/i}{/b} ({b}{i}slicing{/i}{/b}):\n\n{font=monospace.ttf}    my_list[[start : end{color=#0f0}+{/color}{color=#f00}1{/color}]{/font}\n\nПри работе со строками мы называли это \"извлечением подстроки\". Здесь мы говорим, что извлекли {b}{i}подсписок (sublist){/i}{/b} из {font=monospace.ttf}{color=#57f}list{/color}{/font}. Чтобы извлечь срез элементов со 2-го по 4-й включительно:\n\n{font=monospace.ttf}    my_list[[{color=#f00}2{/color}:{color=#f00}5{/color}]{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter04_02_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter04_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_02_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_02_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Списки (Lists): Обновление{/b}{/color}\n\nВ отличие от строк, мы можем использовать оператор индексации для обновления элементов в {font=monospace.ttf}{color=#57f}list{/color}{/font}. Если {font=monospace.ttf}{color=#888}my_list{/color}{/font} изначально выглядел так:\n\n{font=monospace.ttf}    --------------------------------------------------\n    | {color=#57f}Index{/color} |    0    | 1 |   2  |   3   |     4     |\n    --------------------------------------------------\n    | {color=#57f}Data{/color}  | {color=#f00}\"hello\"{/color} | {color=#f00}2{/color} | {color=#f00}True{/color} | {color=#f00}\"new\"{/color} | {color=#f00}\"values!\"{/color} |\n    --------------------------------------------------{/font}\n\nИ мы затем выполним следующий код:\n\n{font=monospace.ttf}    my_list[[{color=#f00}1{/color}] {color=#0f0}={/color} {color=#f00}100{/color}{/font}\n\nТо {font=monospace.ttf}{color=#888}my_list{/color}{/font} примет следующий вид (внимательно посмотрите на индекс {font=monospace.ttf}{color=#f00}1{/color}{/font}):\n\n{font=monospace.ttf}    ----------------------------------------------------\n    | {color=#57f}Index{/color} |    0    |  1  |   2  |   3   |     4     |\n    ----------------------------------------------------\n    | {color=#57f}Data{/color}  | {color=#f00}\"hello\"{/color} | {color=#f00}100{/color} | {color=#f00}True{/color} | {color=#f00}\"new\"{/color} | {color=#f00}\"values!\"{/color} |\n    ----------------------------------------------------{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
screen chapter04_02_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter04_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_02_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_02_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Списки (Lists): Удаление{/b}{/color}\n\nЧтобы удалить значение по определенному индексу в {font=monospace.ttf}{color=#57f}list{/color}{/font}, мы можем применить функцию {font=monospace.ttf}{color=#888}.{/color}{color=#57f}pop{/color}{color=#888}(){/color}{/font}. Допустим, {font=monospace.ttf}{color=#888}my_list{/color}{/font} по-прежнему выглядит так:\n\n{font=monospace.ttf}    --------------------------------------------------\n    | {color=#57f}Index{/color} |    0    | 1 |   2  |   3   |     4     |\n    --------------------------------------------------\n    | {color=#57f}Data{/color}  | {color=#f00}\"hello\"{/color} | {color=#f00}2{/color} | {color=#f00}True{/color} | {color=#f00}\"new\"{/color} | {color=#f00}\"values!\"{/color} |\n    --------------------------------------------------{/font}\n\nЧтобы удалить элемент по индексу {font=monospace.ttf}{color=#f00}2{/color}{/font}, мы пишем:\n\n{font=monospace.ttf}    my_list.{color=#57f}pop{/color}({color=#f00}2{/color}){/font}\n\nТеперь {font=monospace.ttf}{color=#888}my_list{/color}{/font} выглядит следующим образом:\n\n{font=monospace.ttf}    -------------------------------------------\n    | {color=#57f}Index{/color} |    0    | 1 |   2   |     3     |\n    -------------------------------------------\n    | {color=#57f}Data{/color}  | {color=#f00}\"hello\"{/color} | {color=#f00}2{/color} | {color=#f00}\"new\"{/color} | {color=#f00}\"values!\"{/color} |\n    -------------------------------------------{/font}\n\nОбратите внимание: данные сместились влево, и индексы элементов {color=#f00}\"new\"{/color} и {color=#f00}\"values!\"{/color} изменились.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter04_02_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter04_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_02_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_02_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{color=#57f}{b}Списки (Lists): Что еще?{/b}{/color}\n\nДо сих пор мы добавляли в {font=monospace.ttf}{color=#57f}list{/color}{/font} только простые типы данных. Однако список может содержать совершенно любые данные, включая другие списки {font=monospace.ttf}{color=#57f}list{/color}{/font}! В Python абсолютно законно создавать список списков (и список списков списков, и так далее)!\n\nНапример, следующий код создает список ({font=monospace.ttf}{color=#888}parent{/color}{/font}), содержащий внутри себя три других списка:\n\n{font=monospace.ttf}    parent {color=#0f0}={/color} {color=#57f}list{/color}()\n    parent.{color=#57f}append{/color}([[{color=#f00}1{/color}, {color=#f00}2{/color}, {color=#f00}3{/color}])\n    parent.{color=#57f}append{/color}([[{color=#f00}4{/color}, {color=#f00}5{/color}, {color=#f00}6{/color}])\n    parent.{color=#57f}append{/color}([[{color=#f00}7{/color}, {color=#f00}8{/color}, {color=#f00}9{/color}]){/font}\n\nРанее мы визуализировали простые списки как одномерные таблицы. Точно так же списки списков можно представить как двухмерную матрицу/сетку. Каждый элемент внешнего списка ({font=monospace.ttf}{color=#888}parent{/color}{/font}) представляет собой одну строку таблицы:\n\n{font=monospace.ttf}                    parent[[?][[{color=#f00}0{/color}]  parent[[?][[{color=#f00}1{/color}]  parent[[?][[{color=#f00}2{/color}]\n                  -------------------------------------------\n    parent[[{color=#f00}0{/color}] --> |      {color=#f00}1{/color}      |      {color=#f00}2{/color}      |      {color=#f00}3{/color}      |\n                  -------------------------------------------\n    parent[[{color=#f00}1{/color}] --> |      {color=#f00}4{/color}      |      {color=#f00}5{/color}      |      {color=#f00}6{/color}      |\n                  -------------------------------------------\n    parent[[{color=#f00}2{/color}] --> |      {color=#f00}7{/color}      |      {color=#f00}8{/color}      |      {color=#f00}9{/color}      |\n                  -------------------------------------------{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 7
screen chapter04_02_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter04_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_02_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{font=monospace.ttf}                    parent[[?][[{color=#f00}0{/color}]  parent[[?][[{color=#f00}1{/color}]  parent[[?][[{color=#f00}2{/color}]\n                  -------------------------------------------\n    parent[[{color=#f00}0{/color}] --> |      {color=#f00}1{/color}      |      {color=#f00}2{/color}      |      {color=#f00}3{/color}      |\n                  -------------------------------------------\n    parent[[{color=#f00}1{/color}] --> |      {color=#f00}4{/color}      |      {color=#f00}5{/color}      |      {color=#f00}6{/color}      |\n                  -------------------------------------------\n    parent[[{color=#f00}2{/color}] --> |      {color=#f00}7{/color}      |      {color=#f00}8{/color}      |      {color=#f00}9{/color}      |\n                  -------------------------------------------{/font}\n\nМы можем получить вложенный список, применив оператор индексации к внешнему списку. Например, этот код сохранит список {font=monospace.ttf}{color=#888}[[{/color}{color=#f00}4{/color}{color=#888},{/color} {color=#f00}5{/color}{color=#888},{/color} {color=#f00}6{/color}{color=#888}]{/color}{/font} в переменную {font=monospace.ttf}{color=#888}second_row{/color}{/font}:\n\n{font=monospace.ttf}    second_row {color=#0f0}={/color} parent[[{color=#f00}1{/color}]{/font}\n\nАналогично, мы можем обратиться к отдельному числу внутри вложенного списка, применив оператор индексации {b}{i}дважды{/i}{/b}. Первый индекс выбирает строку (подсписок), а второй — элемент внутри этой строки. Например, этот код запишет значение {font=monospace.ttf}{color=#f00}6{/color}{/font} в {font=monospace.ttf}{color=#888}second_row_third_col{/color}{/font}:\n\n{font=monospace.ttf}    second_row_third_col {color=#0f0}={/color} parent[[{color=#f00}1{/color}][[{color=#f00}2{/color}]{/font}\n\nНа этом мы завершаем знакомство со списками {font=monospace.ttf}{color=#57f}list{/color}{/font}. Еще больше подробностей вы найдете в {a=https://docs.python.org/3/tutorial/datastructures.html#more-on-lists}официальной документации Python по спискам{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
