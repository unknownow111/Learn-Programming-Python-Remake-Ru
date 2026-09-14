# chapter and lesson labels
label chapter05_02_01:
    $ COMPLETED.add("chapter05_02_01"); save_game()
    call screen chapter05_02_01_screen
label chapter05_02_02:
    $ COMPLETED.add("chapter05_02_02"); save_game()
    call screen chapter05_02_02_screen
label chapter05_02_03:
    $ COMPLETED.add("chapter05_02_03"); save_game()
    call screen chapter05_02_03_screen
label chapter05_02_04:
    $ COMPLETED.add("chapter05_02_04"); save_game()
    call screen chapter05_02_04_screen
label chapter05_02_05:
    $ COMPLETED.add("chapter05_02_05"); save_game()
    call screen chapter05_02_05_screen
label chapter05_02_06:
    $ COMPLETED.add("chapter05_02_06"); save_game()
    call screen chapter05_02_06_screen
label chapter05_02_07:
    $ COMPLETED.add("chapter05_02_07"); save_game()
    call screen chapter05_02_07_screen
label chapter05_02:
    jump chapter05_02_01
    jump chapter_select

# page 1
screen chapter05_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter05_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{b}{i}Функция{/i}{/b} — это блок кода, который может быть вызван из другого места программы. У функции есть 3 основные части:\n\n    1. {b}Имя (Name):{/b} как называется функция; по этому имени другой код обращается к ней\n    2. {b}Параметры (Parameters):{/b} данные, передаваемые внутрь функции для работы\n    3. {b}Тело (Body):{/b} непосредственно код и логика, исполняемые функцией\n\nОбщая структура функции выглядит так:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}function_name{/color}(param_1, param_2):\n        {color=#f0f}# тело функции (function_body){/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "function.png":
        xsize 1122
        ysize 1073
        xalign 0.6
        yalign 0.9

# page 2
screen chapter05_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter05_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_02_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Как только функция объявлена, мы можем ее {b}{i}вызвать{/i}{/b}. Вызов функции приостанавливает текущее выполнение, переходит к коду функции, выполняет ее {b}{i}тело{/i}{/b}, а затем возвращается к тому месту, откуда был сделан вызов. Вы уже умеете вызывать встроенные функции (например, {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font}), и вызов собственных функций работает абсолютно так же:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}meep{/color}(word):\n        {color=#57f}print{/color}({color=#f00}\"meep\" {color=#0f0}+{/color} word)\n\n    {color=#57f}print{/color}({color=#f00}\"jeep\"{/color})\n    {color=#57f}meep{/color}({color=#f00}\"beep\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"keep\"{/color}){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Что выведет приведенный выше код?\n\nКогда мы передаем данные в функцию (например, строку {font=monospace.ttf}{color=#f00}\"beep\"{/color}{/font}), мы связываем эти данные с соответствующими параметрами из списка параметров. Передаваемые данные называются {b}{i}аргументами{/i}{/b} ({b}{i}arguments{/i}{/b}).":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter05_02_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter05_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_02_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_02_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Давайте разберем наглядный пример того, как (и зачем) использовать функции. Взгляните на эту программу:\n\n{font=monospace.ttf}    user_data {color=#0f0}={/color} {color=#57f}input{/color}().{color=#57f}split{/color}()\n    {color=#ff0}for{/color} s {color=#0f0}in{/color} user_data:\n        count {color=#0f0}={/color} {color=#f00}0{/color}\n        {color=#ff0}for{/color} c {color=#0f0}in{/color} s:\n            {color=#ff0}if{/color} c {color=#0f0}in{/color} {{{color=#f00}\"a\"{/color}, {color=#f00}\"e\"{/color}, {color=#f00}\"i\"{/color}, {color=#f00}\"o\"{/color}, {color=#f00}\"u\"{/color}}:\n                count {color=#0f0}+={/color} {color=#f00}1{/color}\n        {color=#57f}print{/color}(s {color=#0f0}+{/color} {color=#f00}\" \" {color=#0f0}+{/color} {color=#57f}str{/color}(count)){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Что делает эта программа?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter05_02_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter05_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_02_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_02_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Хотя за пару минут внимательного анализа вы наверняка поймете смысл программы, согласитесь, это требует усилий. А теперь взгляните на ту же самую логику, оформленную с помощью функций:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}get_user_data{/color}():\n        {color=#ff0}return{/color} {color=#57f}input{/color}().{color=#57f}split{/color}()\n\n    {color=#ff0}def{/color} {color=#57f}count_vowels{/color}(data):\n        count {color=#0f0}={/color} {color=#f00}0{/color}\n        {color=#ff0}for{/color} c {color=#0f0}in{/color} data:\n            {color=#ff0}if{/color} c {color=#0f0}in{/color} {{{color=#f00}\"a\"{/color}, {color=#f00}\"e\"{/color}, {color=#f00}\"i\"{/color}, {color=#f00}\"o\"{/color}, {color=#f00}\"u\"{/color}}:\n                count {color=#0f0}+={/color} {color=#f00}1{/color}\n        {color=#ff0}return{/color} count\n\n    user_data {color=#0f0}={/color} {color=#57f}get_user_data{/color}()\n    {color=#ff0}for{/color} s {color=#0f0}in{/color} user_data:\n        {color=#57f}print{/color}(s + {color=#f00}\" \" + {color=#57f}str{/color}({color=#57f}count_vowels{/color}(s))){/font}\n\nТеперь назначение кода очевидно сразу: получаем данные от пользователя и выводим каждое слово с количеством гласных! Благодаря функциям мы добились двух вещей:\n\n    1. Написали {b}{i}гораздо более читаемый код{/i}{/b}\n    2. {b}{i}Разделили ответственность (декомпозировали задачу){/i}{/b}\n\nВы наверняка заметили ключевое слово {font=monospace.ttf}{color=#ff0}return{/color}{/font}. Функции могут не только совершать действия, но и возвращать результат своей работы обратно в вызывающий код. {b}{i}Возвращаемое значение{/i}{/b} можно присвоить любой переменной. В Python {i}все{/i} функции что-то возвращают: если оператор {font=monospace.ttf}{color=#ff0}return{/color}{/font} не указан явно, функция автоматически возвращает значение {font=monospace.ttf}{color=#f00}None{/color}{/font}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
screen chapter05_02_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter05_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_02_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_02_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Поговорим подробнее о модульности и разделении кода — золотом стандарте в разработке ПО.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Почему деление кода на модули и функции так полезно?\n\nПредставьте, что вы написали программу подсчета гласных, но в ней закрался баг: {i}программа считает гласные только для первых пяти слов, а дальше ломается.{/i} Где искать ошибку?\n\nЕсли код написан сплошным полотном, найти причину тяжело: сломаться могла {b}{i}любая{/i}{/b} строка. Но если код разбит на функции, вы можете протестировать каждую функцию изолированно и сразу найти виновника! Не нужно перечитывать весь проект — достаточно проверить маленькие кирпичики по отдельности.\n\nЭта практика лежит в основе {b}{i}модульного тестирования (unit-testing){/i}{/b}, когда каждая отдельная единица (unit) тестируется независимо.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter05_02_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter05_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_02_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter05_02_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Вспомните: при первом знакомстве с {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} мы сказали, что это встроенная функция, к деталям которой мы еще вернемся. Действительно, {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font} — это функция, принимающая данные и выводящая их в стандартный вывод программы.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Как может выглядеть тело функции {font=monospace.ttf}{color=#57f}print{/color}{color=#888}(){/color}{/font}?\n\nЕсли вы не знаете точного ответа — не переживайте! Никто не ждет от вас знания низкоуровневых механизмов вывода на экран, и Python тоже этого не требует. В этом и заключается вся суть. Главная мощь функций — принцип {b}{i}черного ящика (black-boxing){/i}{/b}: вы можете эффективно использовать функцию, совершенно не зная, как именно она реализована изнутри. Вам достаточно знать лишь то, что подать ей на вход и что она отдаст на выходе.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "box.png":
        xsize 1000
        ysize 885
        xalign 0.45
        yalign 0.85

# page 7
screen chapter05_02_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter05_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter05_02_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Помимо объявления функций через ключевое слово {font=monospace.ttf}{color=#f00}def{/color}{/font}, можно создавать компактные безымянные функции — {b}{i}лямбда-функции (lambda functions){/i}{/b}. Их удобно использовать в выражениях или передавать в качестве аргументов другим функциям. Синтаксис лямбда-функции:\n\n{font=monospace.ttf}    {color=#ff0}lambda{/color} arguments : expression{/font}\n\nК примеру, функция возведения числа в квадрат:\n\n{font=monospace.ttf}    {color=#ff0}def{/color} {color=#57f}square{/color}(x):\n        {color=#ff0}return{/color} x{color=#0f0}**{/color}{color=#f00}2{/color}{/font}\n\nЕе можно записать в виде лямбда-выражения:\n\n{font=monospace.ttf}    square {color=#0f0}={/color} {color=#ff0}lambda{/color} x: x{color=#0f0}**{/color}{color=#f00}2{/color}{/font}\n\n    – Аргумент (над чем выполняется операция) — {font=monospace.ttf}{color=#888}x{/color}{/font}\n    – Выражение (что функция возвращает) — {font=monospace.ttf}{color=#888}x{/color}{color=#0f0}**{/color}{color=#f00}2{/color}{/font}\n    – Ключевое слово {font=monospace.ttf}{color=#ff0}lambda{/color}{/font} возвращает сам объект функции, который мы сохраняем в {font=monospace.ttf}{color=#888}square{/color}{/font}\n\nВызов в обоих случаях выглядит одинаково:\n\n{font=monospace.ttf}    {color=#57f}square{/color}({color=#f00}4{/color}){/font}\n\nМы не будем подробно углубляться в лямбда-функции в этом курсе, так как они считаются продвинутой темой, но если вам интересно узнать о них больше — ознакомьтесь с {a=https://realpython.com/python-lambda/}этим руководством{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
