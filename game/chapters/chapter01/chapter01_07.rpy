# chapter and lesson labels
label chapter01_07_01:
    $ COMPLETED.add("chapter01_07_01"); save_game()
    call screen chapter01_07_01_screen
label chapter01_07_02:
    $ COMPLETED.add("chapter01_07_02"); save_game()
    call screen chapter01_07_02_screen
label chapter01_07_03:
    $ COMPLETED.add("chapter01_07_03"); save_game()
    call screen chapter01_07_03_screen
label chapter01_07_04:
    call screen chapter01_07_04_screen
label chapter01_07_05:
    $ COMPLETED.add("chapter01_07_05"); save_game()
    call screen chapter01_07_05_screen
label chapter01_07_06:
    $ COMPLETED.add("chapter01_07_06"); save_game()
    call screen chapter01_07_06_screen
label chapter01_07_07:
    $ COMPLETED.add("chapter01_07_07"); save_game()
    call screen chapter01_07_07_screen
label chapter01_07:
    jump chapter01_07_01
    jump chapter_select

# page 1
screen chapter01_07_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter01_07"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_07_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "По мере изучения возможностей Python ваш код будет становиться всё сложнее. На самом деле вы уже способны понимать довольно замысловатые конструкции:\n\n{font=monospace.ttf}    x, y, z {color=#0f0}={/color} {color=#f00}2{/color}, {color=#f00}5{/color}, {color=#f00}7{/color}\n    {color=#57f}print{/color}({color=#57f}str{/color}(x {color=#0f0}+{/color} y {color=#0f0}*{/color} z) {color=#0f0}+{/color} {color=#f00}\" is not the same as \"{/color} {color=#0f0}+{/color} {color=#57f}str{/color}((x {color=#0f0}+{/color} y) {color=#0f0}*{/color} z))\n    {color=#57f}print{/color}({color=#57f}str{/color}({color=#57f}float{/color}(x)) {color=#0f0}+{/color} {color=#f00}\" is not the same as \"{/color} {color=#0f0}+{/color} {color=#57f}str{/color}(x)){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Что делает приведенный фрагмент кода?\n\nОдна из главных задач программиста — сделать код легко читаемым для других разработчиков. Это кардинально повышает качество проекта, что жизненно важно при работе в команде или возвращении к собственному коду спустя пару месяцев (вы удивитесь, насколько легко запутаться в собственном коде!).\n\nНо в коде, подобном примеру выше, логика не очевидна с первого взгляда. Нужен способ добавлять текстовые пояснения прямо в код, объясняющие читателю, что здесь происходит. Для этого созданы {b}{i}комментарии{/i}{/b}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "speech_bubble.png":
        xsize 776
        ysize 687
        xalign 0.7
        yalign .95

# page 2
screen chapter01_07_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter01_07"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_07_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_07_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Комментарии позволяют вставлять текстовые пояснения на человеческом языке прямо в код программы. При запуске Python полностью игнорирует комментарии — они предназначены исключительно для людей.\n\nБывает два вида комментариев: {b}{i}однострочные{/i}{/b} и {b}{i}многострочные{/i}{/b}. Ниже показан пример того, как они делают наш предыдущий код понятным:\n\n{font=monospace.ttf}    {color=#f00}'''\n    Показываем, как приоритет операторов и приведение типов меняют вывод\n    '''{/color}\n    x, y, z = {color=#f00}2{/color}, {color=#f00}5{/color}, {color=#f00}7{/color}\n    {color=#57f}print{/color}({color=#57f}str{/color}(x {color=#0f0}+{/color} y {color=#0f0}*{/color} z) {color=#0f0}+{/color} {color=#f00}\" is not the same as \"{/color} {color=#0f0}+{/color} {color=#57f}str{/color}((x {color=#0f0}+{/color} y) {color=#0f0}*{/color} z))  {color=#f0f}# Приоритет операторов{/color}\n    {color=#57f}print{/color}({color=#57f}str{/color}({color=#57f}float{/color}(x)) {color=#0f0}+{/color} {color=#f00}\" is not the same as \"{/color} {color=#0f0}+{/color} {color=#57f}str{/color}(x))             {color=#f0f}# float против int{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter01_07_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter01_07"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_07_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_07_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{b}{i}Однострочный комментарий{/i}{/b} занимает одну строку. Он идеально подходит для краткого описания небольшого фрагмента кода (до 10 строк). Чтобы создать его, достаточно поставить символ решётки ({font=monospace.ttf}{color=#f0f}#{/color}{/font}) — всё, что идет после него до конца строки, станет комментарием.\n\nЕсли комментарий относится к нескольким последующим строкам, его ставят на отдельной строке непосредственно перед ними:\n\n{font=monospace.ttf}    {color=#f0f}# Выводим числа от 1 до 3, каждое с новой строки{/color}\n    {color=#57f}print{/color}({color=#f00}1{/color})\n    {color=#57f}print{/color}({color=#f00}2{/color})\n    {color=#57f}print{/color}({color=#f00}3{/color}){/font}\n\nЕсли комментарий поясняет одну конкретную строку, его можно разместить как над ней, так и справа на той же строке:\n\n{font=monospace.ttf}    {color=#f0f}# Выводим последнюю цифру числа num{/color}\n    {color=#57f}print{/color}(num {color=#0f0}%{/color} {color=#f00}10{/color}){/font}\n\nИли в конце строки с кодом:\n\n{font=monospace.ttf}    {color=#57f}print{/color}(num {color=#0f0}%{/color} {color=#f00}10{/color}) {color=#f0f}# Выводим последнюю цифру числа num{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
init python:
    def chapter01_07_04_check(x):
        return x.strip().startswith("#")
default chapter01_07_04_student = ""
screen chapter01_07_04_screen:
    if "chapter01_07_04" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter01_07_04" in INCORRECT:
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
    text "4 / " + str(persistent.NUM_PAGES["chapter01_07"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_07_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_07_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Напишите любой однострочный комментарий в поле ниже.\n\nЕсли нужно вдохновение, напишите комментарий к строке кода:\n\n{font=monospace.ttf}    {color=#57f}print{/color}(message){/font}"
        hbox:
            text persistent.INPUT_LABEL_TEXT
            text " "
            if "chapter01_07_04" in COMPLETED:
                text "{b}{color=#0f0}" + str(chapter01_07_04_student) + "{/color}"
            else:
                frame:
                    background persistent.INPUT_BACKGROUND_COLOR
                    input:
                        value VariableInputValue("chapter01_07_04_student")
        if "chapter01_07_04" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter01_07_04", persistent.chapter01_07_04_correct, chapter01_07_04_student, check=chapter01_07_04_check)
                text "   "
                textbutton _("{b}Очистить{/b}") action [SetVariable("chapter01_07_04_student",""), RemoveFromSet(INCORRECT,"chapter01_07_04")]

# page 5
screen chapter01_07_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter01_07"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_07_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_07_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{b}{i}Многострочный комментарий{/i}{/b} может занимать сколько угодно строк. Его часто используют для общего описания больших логических блоков кода. Он начинается с трех одинарных кавычек* ({font=monospace.ttf}{color=#f00}'''{/color}{/font}) и завершается также тремя одинарными кавычками ({font=monospace.ttf}{color=#f00}'''{/color}{/font}). Заметили сходство? По сути, многострочный комментарий — это просто многострочная строка, не присвоенная ни одной переменной!\n\nМногострочные комментарии обычно размещают перед большими смысловыми блоками программы:\n\n{font=monospace.ttf}    {color=#f00}'''\n    Проверяем равенство многострочной строки и однострочной\n    '''{/color}\n    mls {color=#0f0}={/color} {color=#f00}\"Hello, \"{/color} \\\n          {color=#f00}\"how are you?\"{/color}\n    sls {color=#0f0}={/color} {color=#f00}\"Hello, how are you?\"{/color}\n    {color=#57f}print{/color}(mls {color=#0f0}=={/color} sls){/font}\n\n\n{i}*Можно использовать и тройные двойные кавычки (\"\"\"), но среди разработчиков традиционно популярнее одинарные.{/i}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter01_07_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter01_07"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_07_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_07_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Многострочные комментарии часто сочетают с однострочными для структурированного описания работы модуля. Например, в коде ниже многострочный комментарий описывает общую цель скрипта, а однострочные поясняют конкретные подзадачи:\n\n{font=monospace.ttf}    {color=#f00}'''\n    Вычисляем процент стены, покрытый новыми обоями\n    '''{/color}\n    {color=#f0f}# Считаем общую площадь стен{/color}\n    height {color=#0f0}={/color} {color=#f00}8{/color}\n    long_wall {color=#0f0}={/color} {color=#f00}13{/color}\n    short_wall {color=#0f0}={/color} {color=#f00}10.5{/color}\n    total_wall {color=#0f0}={/color} (height {color=#0f0}*{/color} (long_wall {color=#0f0}+{/color} short_wall))\n\n    {color=#f0f}# Считаем площадь наклеенных обоев{/color}\n    height_covered {color=#0f0}={/color} {color=#f00}5{/color}\n    l_w_covered {color=#0f0}={/color} {color=#f00}8{/color}\n    s_w_covered {color=#0f0}={/color} {color=#f00}7{/color}\n    total_covered {color=#0f0}={/color} height_covered {color=#0f0}*{/color} (l_w_covered {color=#0f0}+{/color} s_w_covered)\n\n    {color=#f0f}# Выводим покрытие в процентах{/color}\n    {color=#57f}print{/color}({color=#f00}\"Coverage: \"{/color} + {color=#57f}str{/color}(total_covered {color=#0f0}/{/color} total_wall)){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 7
screen chapter01_07_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter01_07"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_07_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "В завершение предостережем вас от {b}{i}избыточного комментирования (over-commenting){/i}{/b}: когда комментариев так много, что код становится захламленным и трудночитаемым. Например, бессмысленно комментировать каждую элементарную строку, действие которой и так очевидно:\n\n{font=monospace.ttf}    greeting {color=#0f0}={/color} {color=#f00}\"Welcome to this program!\"{/color}                             {color=#f0f}# Объявляем greeting{/color}\n    work_in_progress {color=#0f0}={/color} {color=#f00}\"We are almost ready to release this program.\"{/color} {color=#f0f}# Объявляем статус{/color}\n    closing {color=#0f0}={/color} {color=#f00}\"Hope to see you back soon!\"{/color}                            {color=#f0f}# Объявляем closing{/color}\n\n    {color=#57f}print{/color}(greeting)         {color=#f0f}# Печатаем greeting{/color}\n    {color=#57f}print{/color}(work_in_progress) {color=#f0f}# Печатаем статус{/color}\n    {color=#57f}print{/color}(closing)          {color=#f0f}# Печатаем closing{/color}{/font}\n\nВместо этого лучше сгруппировать действия логически:\n\n{font=monospace.ttf}    {color=#f0f}# Подготавливаем сообщения для пользователя{/color}\n    greeting {color=#0f0}={/color} {color=#f00}\"Welcome to this program!\"{/color}\n    work_in_progress {color=#0f0}={/color} {color=#f00}\"We are almost ready to release this program.\"{/color}\n    closing {color=#0f0}={/color} {color=#f00}\"Hope to see you back soon!\"{/color}\n\n    {color=#f0f}# Выводим сообщения в стандартный поток{/color}\n    {color=#57f}print{/color}(greeting)\n    {color=#57f}print{/color}(work_in_progress)\n    {color=#57f}print{/color}(closing){/font}\n\nОдним словом... {b}{i}Комментируйте с умом и заботой!{/i}{/b} Вы будущий скажете себе огромное спасибо!":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
