# chapter and lesson labels
label chapter02_02_01:
    $ COMPLETED.add("chapter02_02_01"); save_game()
    call screen chapter02_02_01_screen
label chapter02_02_02:
    $ COMPLETED.add("chapter02_02_02"); save_game()
    call screen chapter02_02_02_screen
label chapter02_02_03:
    $ COMPLETED.add("chapter02_02_03"); save_game()
    call screen chapter02_02_03_screen
label chapter02_02_04:
    $ COMPLETED.add("chapter02_02_04"); save_game()
    call screen chapter02_02_04_screen
label chapter02_02_05:
    $ COMPLETED.add("chapter02_02_05"); save_game()
    call screen chapter02_02_05_screen
label chapter02_02_06:
    $ COMPLETED.add("chapter02_02_06"); save_game()
    call screen chapter02_02_06_screen
label chapter02_02_07:
    $ COMPLETED.add("chapter02_02_07"); save_game()
    call screen chapter02_02_07_screen
label chapter02_02_08:
    call screen chapter02_02_08_screen
label chapter02_02_09:
    call screen chapter02_02_09_screen
label chapter02_02_10:
    $ COMPLETED.add("chapter02_02_10"); save_game()
    call screen chapter02_02_10_screen
label chapter02_02_11:
    call screen chapter02_02_11_screen
label chapter02_02:
    jump chapter02_02_01
    jump chapter_select

# page 1
screen chapter02_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Прежде чем писать код с ветвлением, изучим тип данных, который мы пока обходили стороной: {font=monospace.ttf}{color=#57f}bool{/color}{/font}. Напомним, что переменные типа {font=monospace.ttf}{color=#57f}bool{/color}{/font} принимают одно из двух значений: {font=monospace.ttf}{color=#f00}True{/color}{/font} (истина) или {font=monospace.ttf}{color=#f00}False{/color}{/font} (ложь). Однако простое присвоение булевых констант само по себе мало что дает. Их подлинная мощь раскрывается в {b}{i}логических выражениях{/i}{/b}.\n\nЛогические выражения — это конструкции, сравнивающие данные и возвращающие {font=monospace.ttf}{color=#f00}True{/color}{/font} или {font=monospace.ttf}{color=#f00}False{/color}{/font} в зависимости от выполнения условий. Инструменты для построения таких утверждений называются {b}{i}логическими операторами{/i}{/b}. Ниже приведена таблица логических операторов в порядке убывания их приоритета*:\n\n{font=monospace.ttf}    -----------------------------------------------------------------------------\n    | {color=#57f}Приоритет{/color}        | {color=#57f}Оператор{/color}                   | {color=#57f}Действие{/color}                  |\n    -----------------------------------------------------------------------------\n    | Высший           | {color=#0f0}in{/color}, {color=#0f0}is{/color}, {color=#0f0}<{/color}, {color=#0f0}<={/color} {color=#0f0}>{/color}, {color=#0f0}>={/color} {color=#0f0}!={/color}, {color=#0f0}=={/color} | Вхождение и сравнение     |\n    -----------------------------------------------------------------------------\n    |                  | {color=#0f0}not{/color}                        | Логическое НЕ (NOT)       |\n    -----------------------------------------------------------------------------\n    |                  | {color=#0f0}and{/color}                        | Логическое И (AND)        |\n    -----------------------------------------------------------------------------\n    | Низший           | {color=#0f0}or{/color}                         | Логическое ИЛИ (OR)       |\n    -----------------------------------------------------------------------------{/font}\n\n{i}*Все логические операторы имеют {b}более низкий{/b} приоритет, чем арифметические (за исключением оператора присваивания {font=monospace.ttf}{color=#0f0}:={/color}{/font} / {font=monospace.ttf}{color=#0f0}={/color}{/font}).{/i}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "logic.png":
        xsize 1000
        ysize 332
        xalign 0.5
        yalign .95

# page 2
screen chapter02_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_02_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Сначала рассмотрим операторы {b}{i}сравнения{/i}{/b}. Они позволяют сопоставлять значения двух выражений. Операторы {b}{i}равенства{/i}{/b} ({font=monospace.ttf}{color=#0f0}=={/color}{/font}) и {b}{i}неравенства{/i}{/b} ({font=monospace.ttf}{color=#0f0}!={/color}{/font}):\n\n{font=monospace.ttf}    x {color=#0f0}=={/color} y {color=#f0f}# True, если x и y РАВНЫ (иначе False){/color}\n    x {color=#0f0}!={/color} y {color=#f0f}# True, если x и y НЕ РАВНЫ (иначе False){/color}{/font}\n\nОператоры {b}{i}меньше{/i}{/b} ({font=monospace.ttf}{color=#0f0}<{/color}{/font}) и {b}{i}больше{/i}{/b} ({font=monospace.ttf}{color=#0f0}>{/color}{/font}):\n\n{font=monospace.ttf}    x {color=#0f0}<{/color} y {color=#f0f}# True, если x МЕНЬШЕ y (иначе False){/color}\n    x {color=#0f0}>{/color} y {color=#f0f}# True, если x БОЛЬШЕ y (иначе False){/color}{/font}\n\nОператоры {b}{i}меньше либо равно{/i}{/b} ({font=monospace.ttf}{color=#0f0}<={/color}{/font}) и {b}{i}больше либо равно{/i}{/b} ({font=monospace.ttf}{color=#0f0}>={/color}{/font}):\n\n{font=monospace.ttf}    x {color=#0f0}<={/color} y {color=#f0f}# True, если x МЕНЬШЕ ЛИБО РАВЕН y (иначе False){/color}\n    x {color=#0f0}>={/color} y {color=#f0f}# True, если x БОЛЬШЕ ЛИБО РАВЕН y (иначе False){/color}{/font}\n\nТакже существуют операторы {b}{i}принадлежности (membership){/i}{/b}. Они проверяют, входит ли элемент в состав коллекции. Пока единственная знакомая нам коллекция — это строка. Для строк операторы принадлежности проверяют, является ли одна строка {b}{i}подстрокой{/i}{/b} другой:\n\n{font=monospace.ttf}    x {color=#0f0}in{/color} y     {color=#f0f}# True, если x ВХОДИТ в состав y (иначе False){/color}\n    x {color=#0f0}not in{/color} y {color=#f0f}# True, если x НЕ ВХОДИТ в y (иначе False){/color}{/font}\n\n{i}Оператор {font=monospace.ttf}{color=#0f0}is{/color}{/font} мы намеренно пока опускаем — о нем речь пойдет позже при изучении объектов.{/i}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter02_02_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_02_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_02_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь мы умеем получать булевы значения из переменных. Но что если требуется объединить несколько условий в единое сложное логическое выражение?\n\nВ Python есть три ключевых {b}{i}логических связки{/i}{/b}: {font=monospace.ttf}{color=#0f0}not{/color}{/font}, {font=monospace.ttf}{color=#0f0}and{/color}{/font} и {font=monospace.ttf}{color=#0f0}or{/color}{/font}. Их поведение наглядно описывают {b}{i}таблицы истинности{/i}{/b}, показывающие результат для всех возможных комбинаций аргументов.\n\nСамый простой оператор — {font=monospace.ttf}{color=#0f0}not{/color}{/font} (логическое отрицание). Для любой булевой переменной {font=monospace.ttf}{color=#888}x{/color}{/font} выражение {font=monospace.ttf}{color=#0f0}not{/color} {color=#888}x{/color}{/font} инвертирует ее значение:\n\n{font=monospace.ttf}    -----------------\n    |   {color=#888}x{/color}   | {color=#0f0}not{/color} {color=#888}x{/color} |\n    -----------------\n    | {i}{color=#f00}True{/color}{/i}  | {color=#f00}False{/color} |\n    -----------------\n    | {i}{color=#f00}False{/color}{/i} | {color=#f00}True{/color}  |\n    -----------------{/font}\n\nТо есть в коде:\n\n{font=monospace.ttf}    {color=#0f0}not{/color} {color=#f00}True{/color}  {color=#f0f}# False{/color}\n    {color=#0f0}not{/color} {color=#f00}False{/color} {color=#f0f}# True{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter02_02_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_02_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_02_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Следующий логический оператор — {font=monospace.ttf}{color=#0f0}and{/color}{/font} (логическое И, конъюнкция). Для двух булевых переменных {font=monospace.ttf}{color=#888}x{/color}{/font} и {font=monospace.ttf}{color=#888}y{/color}{/font} выражение {font=monospace.ttf}{color=#888}x{/color} {color=#0f0}and{/color} {color=#888}y{/color}{/font} вернет {font=monospace.ttf}{color=#f00}True{/color}{/font} {b}{i}только тогда, когда оба{/i}{/b} операнда ({font=monospace.ttf}{color=#888}x{/color}{/font} {b}{i}И{/i}{/b} {font=monospace.ttf}{color=#888}y{/color}{/font}) равны {font=monospace.ttf}{color=#f00}True{/color}{/font}. В любых других случаях возвращается {font=monospace.ttf}{color=#f00}False{/color}{/font}.\n\n{font=monospace.ttf}                      {color=#888}y{/color}\n              -----------------\n              | {i}{color=#f00}True{/color}{/i}  | {i}{color=#f00}False{/color}{/i} |\n      -------------------------\n      | {i}{color=#f00}True{/color}{/i}  | {color=#f00}True{/color}  | {color=#f00}False{/color} |\n    {color=#888}x{/color} -------------------------\n      | {i}{color=#f00}False{/color}{/i} | {color=#f00}False{/color} | {color=#f00}False{/color} |\n      -------------------------{/font}\n\nВ коде Python:\n\n{font=monospace.ttf}    {color=#f00}True{/color}  {color=#0f0}and{/color} {color=#f00}True{/color}  {color=#f0f}# True{/color}\n    {color=#f00}True{/color}  {color=#0f0}and{/color} {color=#f00}False{/color} {color=#f0f}# False{/color}\n    {color=#f00}False{/color} {color=#0f0}and{/color} {color=#f00}True{/color}  {color=#f0f}# False{/color}\n    {color=#f00}False{/color} {color=#0f0}and{/color} {color=#f00}False{/color} {color=#f0f}# False{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
screen chapter02_02_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_02_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_02_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Третий оператор — {font=monospace.ttf}{color=#0f0}or{/color}{/font} (логическое ИЛИ, дизъюнкция). Выражение {font=monospace.ttf}{color=#888}x{/color} {color=#0f0}or{/color} {color=#888}y{/color}{/font} возвращает {font=monospace.ttf}{color=#f00}True{/color}{/font}, если {b}{i}хотя бы один{/i}{/b} из операндов ({font=monospace.ttf}{color=#888}x{/color}{/font} {b}{i}ИЛИ{/i}{/b} {font=monospace.ttf}{color=#888}y{/color}{/font}) равен {font=monospace.ttf}{color=#f00}True{/color}{/font}. {font=monospace.ttf}{color=#f00}False{/color}{/font} возвращается только тогда, когда ложны оба операнда сразу.\n\n{font=monospace.ttf}                      {color=#888}y{/color}\n              -----------------\n              | {i}{color=#f00}True{/color}{/i}  | {i}{color=#f00}False{/color}{/i} |\n      -------------------------\n      | {i}{color=#f00}True{/color}{/i}  | {color=#f00}True{/color}  | {color=#f00}True{/color}  |\n    {color=#888}x{/color} -------------------------\n      | {i}{color=#f00}False{/color}{/i} | {color=#f00}True{/color}  | {color=#f00}False{/color} |\n      -------------------------{/font}\n\nВ коде Python:\n\n{font=monospace.ttf}    {color=#f00}True{/color}  {color=#0f0}or{/color} {color=#f00}True{/color}  {color=#f0f}# True{/color}\n    {color=#f00}True{/color}  {color=#0f0}or{/color} {color=#f00}False{/color} {color=#f0f}# True{/color}\n    {color=#f00}False{/color} {color=#0f0}or{/color} {color=#f00}True{/color}  {color=#f0f}# True{/color}\n    {color=#f00}False{/color} {color=#0f0}or{/color} {color=#f00}False{/color} {color=#f0f}# False{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter02_02_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_02_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_02_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Из школьного курса математики вы наверняка помните, что некоторые операторы сравнения являются взаимно противоположными (дополняющими). Например, операторы {font=monospace.ttf}{color=#0f0}<{/color}{/font} и {font=monospace.ttf}{color=#0f0}>={/color}{/font} взаимно дополняют друг друга, так как любое число попадает ровно в одну из этих двух категорий.\n\nЭто значит, что две записи ниже полностью идентичны. Встречая конструкции вида первой строки, вы можете (и должны!) упрощать их до более понятного второго варианта:\n\n{font=monospace.ttf}    {color=#0f0}not{/color} x {color=#0f0}>={/color} {color=#f00}7{/color}\n    x {color=#0f0}<{/color} {color=#f00}7{/color}{/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Какие еще пары операторов сравнения взаимно противоположны?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 7
screen chapter02_02_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_02_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_02_08"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Давайте составим собственные логические выражения. Следующий код напечатает {font=monospace.ttf}{color=#f00}True{/color}{/font}, если {font=monospace.ttf}{color=#888}x{/color}{/font} меньше {font=monospace.ttf}{color=#f00}5{/color}{/font} (и {font=monospace.ttf}{color=#f00}False{/color}{/font} в противном случае):\n\n{font=monospace.ttf}    {color=#57f}print{/color}(x {color=#0f0}<{/color} {color=#f00}5{/color}){/font}\n\nА этот код выведет {font=monospace.ttf}{color=#f00}True{/color}{/font}, если строка {font=monospace.ttf}{color=#888}y{/color}{/font} содержится внутри {font=monospace.ttf}{color=#f00}\"apple stems\"{/color}{/font}:\n\n{font=monospace.ttf}    {color=#57f}print{/color}(y {color=#0f0}in{/color} {color=#f00}\"apple stems\"{/color}){/font}\n\nЕсли нам необходимо выполнение {b}{i}обоих{/i}{/b} условий одновременно, связываем их оператором {font=monospace.ttf}{color=#0f0}and{/color}{/font}:\n\n{font=monospace.ttf}    {color=#57f}print{/color}(x {color=#0f0}<{/color} {color=#f00}5{/color} {color=#0f0}and{/color} y {color=#0f0}in{/color} {color=#f00}\"apple stems\"{/color}){/font}\n\nА если достаточно выполнения {b}{i}хотя бы одного{/i}{/b} из них, используем {font=monospace.ttf}{color=#0f0}or{/color}{/font}:\n\n{font=monospace.ttf}    {color=#57f}print{/color}(x {color=#0f0}<{/color} {color=#f00}5{/color} {color=#0f0}or{/color} y {color=#0f0}in{/color} {color=#f00}\"apple stems\"{/color}){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 8
define persistent.chapter02_02_08_correct = {"a": True,  "b": True, "c": False,  "d": True}
default chapter02_02_08_student = {k: False for k in persistent.chapter02_02_08_correct}
define persistent.chapter02_02_08_options = {
    "a": "{font=monospace.ttf}val {color=#0f0}={/color} {color=#f00}\"la\"{/color}{/font}",
    "b": "{font=monospace.ttf}val {color=#0f0}={/color} {color=#f00}\"3\"{/color}{/font}",
    "c": "{font=monospace.ttf}val {color=#0f0}={/color} {color=#f00}\"tab\"{/color}{/font}",
    "d": "{font=monospace.ttf}val {color=#0f0}={/color} {color=#f00}\"foof\"{/color}{/font}",
}
screen chapter02_02_08_screen:
    if "chapter02_02_08" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter02_02_08" in INCORRECT:
        text persistent.CHALLENGE_INCORRECT_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_INCORRECT_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    else:
        text persistent.EXERCISE_BREAK_TITLE:
            size gui.title_text_size
            color persistent.EXERCISE_BREAK_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    text "8 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_02_07"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_02_09"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} При каких значениях {font=monospace.ttf}{color=#888}val{/color}{/font} следующее выражение даст {font=monospace.ttf}{color=#f00}True{/color}{/font}? Выберите все подходящие варианты.\n\n{font=monospace.ttf}    val {color=#0f0}not in{/color} {color=#f00}\"glass table\"{/color} {color=#0f0}or{/color} val {color=#0f0}!={/color} {color=#f00}\"tab\"{/color}{/font}"
        for ol in sorted(persistent.chapter02_02_08_options.keys()):
            if "chapter02_02_08" in COMPLETED:
                if persistent.chapter02_02_08_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter02_02_08_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter02_02_08_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter02_02_08_options[ol])) action ToggleDict(chapter02_02_08_student, ol)
        if "chapter02_02_08" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter02_02_08", persistent.chapter02_02_08_correct, chapter02_02_08_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter02_02_08_student, False, from_label="chapter02_02_08")

# page 9
define persistent.chapter02_02_09_correct = {"a": False,  "b": False, "c": False,  "d": False, "e": True}
default chapter02_02_09_student = {k: False for k in persistent.chapter02_02_09_correct}
define persistent.chapter02_02_09_options = {
    "a": "{font=monospace.ttf}a {color=#0f0}={/color} {color=#f00}12{/color}, b {color=#0f0}={/color} любое положительное {color=#57f}int{/color}, c {color=#0f0}={/color} любое положительное {color=#57f}int{/color}{/font}",
    "b": "{font=monospace.ttf}a {color=#0f0}!={/color} {color=#f00}12{/color}, b {color=#0f0}={/color} любое положительное {color=#57f}int{/color}, c {color=#0f0}={/color} любое положительное {color=#57f}int{/color}{/font}",
    "c": "{font=monospace.ttf}a {color=#0f0}={/color} любое положительное {color=#57f}int{/color}, b {color=#0f0}={/color} {color=#f00}5{/color}, c {color=#0f0}={/color} любое положительное {color=#57f}int{/color}{/font}",
    "d": "{font=monospace.ttf}a {color=#0f0}={/color} любое положительное {color=#57f}int{/color}, b {color=#0f0}={/color} любое положительное {color=#57f}int{/color}, c {color=#0f0}={/color} {color=#f00}100{/color}{/font}",
    "e": "{font=monospace.ttf}a {color=#0f0}!={/color} {color=#f00}12{/color}, b {color=#0f0}={/color} любое положительное {color=#57f}int{/color}, c {color=#0f0}={/color} {color=#f00}12{/color}{/font}",
}
screen chapter02_02_09_screen:
    if "chapter02_02_09" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter02_02_09" in INCORRECT:
        text persistent.CHALLENGE_INCORRECT_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_INCORRECT_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    else:
        text persistent.EXERCISE_BREAK_TITLE:
            size gui.title_text_size
            color persistent.EXERCISE_BREAK_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    text "9 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_02_08"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_02_10"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Какие из условий {b}{i}гарантированно{/i}{/b} сделают результат выражения равным {font=monospace.ttf}{color=#f00}False{/color}{/font}? Учитывайте приоритет операторов.\n\n{font=monospace.ttf}    a {color=#0f0}=={/color} {color=#f00}12{/color} {color=#0f0}or{/color} b {color=#0f0}!={/color} {color=#f00}5{/color} {color=#0f0}and{/color} c {color=#0f0}<={/color} {color=#f00}10{/color}{/font}"
        for ol in sorted(persistent.chapter02_02_09_options.keys()):
            if "chapter02_02_09" in COMPLETED:
                if persistent.chapter02_02_09_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter02_02_09_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter02_02_09_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter02_02_09_options[ol])) action ToggleDict(chapter02_02_09_student, ol)
        if "chapter02_02_09" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter02_02_09", persistent.chapter02_02_09_correct, chapter02_02_09_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter02_02_09_student, False, from_label="chapter02_02_09")

# page 10
screen chapter02_02_10_screen:
    text "10 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_02_09"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter02_02_11"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Последняя тема булевой логики в этом разделе — {b}{i}законы Де Моргана{/i}{/b}. Они используются для раскрытия скобок и упрощения выражений с оператором отрицания {font=monospace.ttf}{color=#0f0}not{/color}{/font}:\n\n    1. {font=monospace.ttf}{color=#0f0}not{/color} ({color=#888}x{/color} {color=#0f0}and{/color} {color=#888}y{/color}){/font} эквивалентно {font=monospace.ttf}{color=#0f0}not{/color} {color=#888}x{/color} {color=#0f0}or not{/color} {color=#888}y{/color}{/font}\n    2. {font=monospace.ttf}{color=#0f0}not{/color} ({color=#888}x{/color} {color=#0f0}or{/color} {color=#888}y{/color}){/font} эквивалентно {font=monospace.ttf}{color=#0f0}not{/color} {color=#888}x{/color} {color=#0f0}and not{/color} {color=#888}y{/color}{/font}\n\nК примеру, два приведенных выражения абсолютно равносильны:\n\n{font=monospace.ttf}    {color=#0f0}not{/color} (num {color=#0f0}<={/color} {color=#f00}5{/color} {color=#0f0}or{/color} num {color=#0f0}>{/color} {color=#f00}4{/color})\n    num {color=#0f0}>{/color} {color=#f00}5{/color} {color=#0f0}and{/color} num {color=#0f0}<={/color} {color=#f00}4{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 11
define persistent.chapter02_02_11_correct = {"a": False,  "b": False, "c": False,  "d": False, "e": True}
default chapter02_02_11_student = {k: False for k in persistent.chapter02_02_11_correct}
define persistent.chapter02_02_11_options = {
    "a": "{font=monospace.ttf}a {color=#0f0}={/color} {font=monospace.ttf}{color=#f00}False{/color}{/font},   b {color=#0f0}={/color} {font=monospace.ttf}{color=#f00}False{/color}{/font}{/font}",
    "b": "{font=monospace.ttf}a {color=#0f0}={/color} {font=monospace.ttf}{color=#f00}False{/color}{/font},   b {color=#0f0}={/color} {font=monospace.ttf}{color=#f00}True{/color}{/font}{/font}",
    "c": "{font=monospace.ttf}a {color=#0f0}={/color} {font=monospace.ttf}{color=#f00}True{/color}{/font},    b {color=#0f0}={/color} {font=monospace.ttf}{color=#f00}False{/color}{/font}{/font}",
    "d": "{font=monospace.ttf}a {color=#0f0}={/color} {font=monospace.ttf}{color=#f00}True{/color}{/font},    b {color=#0f0}={/color} {font=monospace.ttf}{color=#f00}True{/color}{/font}{/font}",
    "e": "Выражение ни при каких условиях не может быть равно {font=monospace.ttf}{color=#f00}True{/color}{/font}",
}
screen chapter02_02_11_screen:
    if "chapter02_02_11" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter02_02_11" in INCORRECT:
        text persistent.CHALLENGE_INCORRECT_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_INCORRECT_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    else:
        text persistent.EXERCISE_BREAK_TITLE:
            size gui.title_text_size
            color persistent.EXERCISE_BREAK_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    text "11 / " + str(persistent.NUM_PAGES["chapter02_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02_02_10"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} При каких значениях {font=monospace.ttf}{color=#888}a{/color}{/font} и {font=monospace.ttf}{color=#888}b{/color}{/font} выражение ниже вернет {font=monospace.ttf}{color=#f00}True{/color}{/font}?\n\n{font=monospace.ttf}    a {color=#0f0}and not{/color} (b {color=#0f0}or{/color} a){/font}"
        for ol in sorted(persistent.chapter02_02_11_options.keys()):
            if "chapter02_02_11" in COMPLETED:
                if persistent.chapter02_02_11_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter02_02_11_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter02_02_11_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter02_02_11_options[ol])) action [Function(set_all, chapter02_02_11_student, False, from_label="chapter02_02_11"), ToggleDict(chapter02_02_11_student, ol)]
        if "chapter02_02_11" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter02_02_11", persistent.chapter02_02_11_correct, chapter02_02_11_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter02_02_11_student, False, from_label="chapter02_02_11")
