# chapter and lesson labels
label chapter07_02_01:
    $ COMPLETED.add("chapter07_02_01"); save_game()
    call screen chapter07_02_01_screen
label chapter07_02_02:
    $ COMPLETED.add("chapter07_02_02"); save_game()
    call screen chapter07_02_02_screen
label chapter07_02_03:
    $ COMPLETED.add("chapter07_02_03"); save_game()
    call screen chapter07_02_03_screen
label chapter07_02_04:
    $ COMPLETED.add("chapter07_02_04"); save_game()
    call screen chapter07_02_04_screen
label chapter07_02_05:
    $ COMPLETED.add("chapter07_02_05"); save_game()
    call screen chapter07_02_05_screen
label chapter07_02_06:
    $ COMPLETED.add("chapter07_02_06"); save_game()
    call screen chapter07_02_06_screen
label chapter07_02_07:
    $ COMPLETED.add("chapter07_02_07"); save_game()
    call screen chapter07_02_07_screen
label chapter07_02_08:
    $ COMPLETED.add("chapter07_02_08"); save_game()
    call screen chapter07_02_08_screen
label chapter07_02_09:
    $ COMPLETED.add("chapter07_02_09"); save_game()
    call screen chapter07_02_09_screen
label chapter07_02_10:
    $ COMPLETED.add("chapter07_02_10"); save_game()
    call screen chapter07_02_10_screen
label chapter07_02_11:
    $ COMPLETED.add("chapter07_02_11"); save_game()
    call screen chapter07_02_11_screen
label chapter07_02:
    jump chapter07_02_01
    jump chapter_select

# page 1
screen chapter07_02_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_02_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Чтобы научить компьютер понимать мир, нам придется изменить взгляд на данные. Для простейших задач было достаточно примитивных типов: {font=monospace.ttf}{color=#57f}int{/color}{/font}, {font=monospace.ttf}{color=#57f}str{/color}{/font}, {font=monospace.ttf}{color=#57f}float{/color}{/font} и {font=monospace.ttf}{color=#57f}bool{/color}{/font}. Однако реальный мир вокруг нас люди воспринимают как набор предметов и объектов, а не россыпь разрозненных байтов и чисел.\n\nДавайте научим этому восприятию наш компьютер.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "bedroom.jpg":
        xsize 1920
        ysize 1280
        xalign 0.5
        yalign .9

# page 2
screen chapter07_02_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_02_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_02_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Но так ли новы для нас объекты на самом деле? Мы работали не только с простыми числами, но и со сложными типами данных: {font=monospace.ttf}{color=#57f}list{/color}{/font}, {font=monospace.ttf}{color=#57f}set{/color}{/font}, {font=monospace.ttf}{color=#57f}tuple{/color}{/font} и {font=monospace.ttf}{color=#57f}dict{/color}{/font}! Все типы данных в Python, включая примитивные числа — {b}{i}это и есть объекты{/i}{/b}! Это встроенные типы объектов, предоставляемые языком.\n\nВ Python при использовании оператора присваивания ({font=monospace.ttf}{color=#0f0}={/color}{/font}) переменная всего лишь {b}{i}ссылается{/i}{/b} (указывает) на определенный объект в оперативной памяти компьютера. Например:\n\n{font=monospace.ttf}    x {color=#0f0}={/color} {color=#f00}7{/color} {color=#f0f}# создаем переменную x, указывающую на объект int 7{/color}\n    y {color=#0f0}={/color} x {color=#f0f}# создаем переменную y, указывающую на тот же объект{/color}\n    x {color=#0f0}={/color} {color=#f00}0{/color} {color=#f0f}# направляем x на объект int 0{/color}{/font}\n\nЗдесь {font=monospace.ttf}{color=#888}x{/color}{/font} и {font=monospace.ttf}{color=#888}y{/color}{/font} не связаны жестко между собой: когда {font=monospace.ttf}{color=#888}x{/color}{/font} стал указывать на 0, {font=monospace.ttf}{color=#888}y{/color}{/font} по-прежнему ссылается на 7.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter07_02_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_02_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_02_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "В предыдущем примере переменные указывали на неизменяемые базовые типы. Но если две переменные ссылаются на один и тот же {b}{i}изменяемый{/i}{/b} ({b}{i}mutable{/i}{/b}) объект, изменение объекта через одну переменную отразится и во второй (потому что меняется сам {b}{i}объект{/i}{/b}, на который они {b}{i}обе{/i}{/b} ссылаются):\n\n{font=monospace.ttf}    x {color=#0f0}={/color} [[{color=#f00}1{/color}, {color=#f00}2{/color}]  {color=#f0f}# x ссылается на список [[1, 2]{/color}\n    y {color=#0f0}={/color} x       {color=#f0f}# y теперь ссылается на тот же список{/color}\n    x.{color=#57f}append{/color}({color=#f00}3{/color}) {color=#f0f}# добавляем 3 в список по ссылке x{/color}{/font}\n\nЗдесь {font=monospace.ttf}{color=#888}x{/color}{/font} и {font=monospace.ttf}{color=#888}y{/color}{/font} указывают на один и тот же список в памяти. Вызов {font=monospace.ttf}{color=#888}x.{/color}{color=#57f}append{/color}{color=#888}({/color}{color=#f00}3{/color}{color=#888}){/color}{/font} модифицирует общий список, поэтому {font=monospace.ttf}{color=#888}y{/color}{/font} также увидит изменения.\n\nТеперь мы готовы конструировать собственные объекты.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter07_02_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_02_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_02_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "В качестве сквозного примера смоделируем реальный предмет: {b}{i}бургер{/i}{/b}. Мы хотим, чтобы компьютер мог полноценно описать бургер как объект.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Как описать конкретный бургер? Из чего он состоит?\n\nДля точной модели нужно зафиксировать набор характеристик. В программировании они называются {b}{i}переменными экземпляра{/i}{/b} ({b}{i}instance variables{/i}{/b}) или {b}{i}атрибутами{/i}{/b}. Для простоты выделим 7 характеристик:\n\n    – Тип булочки\n    – Сорт сыра\n    – Вид котлеты\n    – Вид соуса\n    – Есть ли салат (да/нет)\n    – Есть ли помидоры (да/нет)\n    – Количество соленых огурчиков\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Какими базовыми типами данных можно представить каждую из этих характеристик?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "burger.png":
        xsize 577
        ysize 500
        xalign 0.5
        yalign .5

# page 5
screen chapter07_02_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_02_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_02_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Подберем базовые типы, наилучшим образом описывающие каждое свойство:\n\n{font=monospace.ttf}    -------------------------------------------------------\n    | {color=#0f0}Характеристика{/color}    | {color=#0f0}Тип данных{/color} | {color=#0f0}Пример значения{/color}       |\n    -------------------------------------------------------\n    | Булочка (bun)     |    {color=#57f}str{/color}    | bun {color=#0f0}={/color} {color=#f00}\"brioche\"{/color}     |\n    -------------------------------------------------------\n    | Сыр (cheese)      |    {color=#57f}str{/color}    | cheese {color=#0f0}={/color} {color=#f00}\"american\"{/color} |\n    -------------------------------------------------------\n    | Котлета (patty)   |    {color=#57f}str{/color}    | patty {color=#0f0}={/color} {color=#f00}\"chicken\"{/color}   |\n    -------------------------------------------------------\n    | Соус (sauce)      |    {color=#57f}str{/color}    | sauce {color=#0f0}={/color} {color=#f00}\"mayo\"{/color}      |\n    -------------------------------------------------------\n    | Салат?            |    {color=#57f}bool{/color}   | lettuce {color=#0f0}={/color} {color=#f00}False{/color}     |\n    -------------------------------------------------------\n    | Помидор?          |    {color=#57f}bool{/color}   | tomato {color=#0f0}={/color} {color=#f00}True{/color}       |\n    -------------------------------------------------------\n    | Огурчики (кол-во) |    {color=#57f}int{/color}    | num_pickles {color=#0f0}={/color} {color=#f00}2{/color}     |\n    -------------------------------------------------------{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter07_02_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_02_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_02_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь уточним терминологию. В программировании используется понятие {b}{i}класса{/i}{/b} ({b}{i}class{/i}{/b}) для обозначения общего чертежа или шаблона объекта. Например, общее понятие бургера (что бургер имеет {i}какую-то{/i} булку, {i}какую-то{/i} котлету) называется {b}{color=#57f}классом Burger{/color}{/b}. С другой стороны, конкретный физический бургер, который вы держите в руках (у которого булка — бриошь, а котлета — куриная), называется {b}{color=#f00}объектом (экземпляром) Burger{/color}{/b}.\n\nОписывая для Python бургер, мы описываем общий шаблон — {b}{color=#57f}класс Burger{/color}{/b}:\n\n{font=monospace.ttf}    {color=#ff0}class{/color} {color=#57f}Burger{/color}:{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 7
screen chapter07_02_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_02_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_02_08"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь добавим в класс атрибуты. Для этого внутри класса объявляется специальный метод* {font=monospace.ttf}{color=#57f}__init__{/color}{color=#888}(){/color}{/font}. Функции, объявленные внутри класса, называются {b}{i}методами экземпляра{/i}{/b}:\n\n{font=monospace.ttf}    {color=#ff0}class{/color} {color=#57f}Burger{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self):{/font}\n\nОбратите внимание на параметр {font=monospace.ttf}{color=#888}self{/color}{/font}. Первым параметром любого метода экземпляра всегда должен быть {font=monospace.ttf}{color=#888}self{/color}{/font} — он указывает на {b}{i}сам конкретный объект{/i}{/b}, для которого вызывается данный метод.\n\nНазначение метода {font=monospace.ttf}{color=#57f}__init__{/color}{color=#888}(){/color}{/font} (конструктора/инициализатора) — создание различных экземпляров бургеров по одному шаблону. Мы передаем в него параметры для каждого атрибута:\n\n{font=monospace.ttf}    {color=#ff0}class{/color} {color=#57f}Burger{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, bun, cheese, patty, sauce, lettuce, tomato, num_pickles):{/font}\n\n{i}*Такие методы с двойными подчеркиваниями называются {b}магическими или специальными методами (dunder methods){/b}. Python вызывает их автоматически при выполнении определенных действий (создание объекта, сравнение, преобразование в строку и т.д.).{/i}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 8
screen chapter07_02_08_screen:
    text "8 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_02_07"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_02_09"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь нужно сохранить переданные аргументы в сам создаваемый объект через ключевое слово {font=monospace.ttf}{color=#888}self{/color}{/font}:\n\n{font=monospace.ttf}    {color=#ff0}class{/color} {color=#57f}Burger{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, bun, cheese, patty, sauce, lettuce, tomato, num_pickles):\n            self.bun {color=#0f0}={/color} bun\n            self.cheese {color=#0f0}={/color} cheese\n            self.patty {color=#0f0}={/color} patty\n            self.sauce {color=#0f0}={/color} sauce\n            self.lettuce {color=#0f0}={/color} lettuce\n            self.tomato {color=#0f0}={/color} tomato\n            self.num_pickles {color=#0f0}={/color} num_pickles{/font}\n\nКаждое значение сохранено в переменную экземпляра (например, {font=monospace.ttf}{color=#888}self.bun{/color}{/font}) для дальнейшего использования.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 9
screen chapter07_02_09_screen:
    text "9 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_02_08"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_02_10"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Помимо {font=monospace.ttf}{color=#57f}__init__{/color}{color=#888}(){/color}{/font}, мы можем описывать любые собственные методы поведения! Например, метод {font=monospace.ttf}{color=#57f}add_pickles{/color}{color=#888}(){/color}{/font}, который принимает число {font=monospace.ttf}{color=#888}n{/color}{/font} и добавляет огурчики в бургер:\n\n{font=monospace.ttf}    {color=#ff0}class{/color} {color=#57f}Burger{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, bun, cheese, patty, sauce, lettuce, tomato, num_pickles):\n            self.bun {color=#0f0}={/color} bun\n            self.cheese {color=#0f0}={/color} cheese\n            self.patty {color=#0f0}={/color} patty\n            self.sauce {color=#0f0}={/color} sauce\n            self.lettuce {color=#0f0}={/color} lettuce\n            self.tomato {color=#0f0}={/color} tomato\n            self.num_pickles {color=#0f0}={/color} num_pickles\n\n        {color=#ff0}def{/color} {color=#57f}add_pickles{/color}(self, n):\n            self.num_pickles {color=#0f0}+={/color} n{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 10
screen chapter07_02_10_screen:
    text "10 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_02_09"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_02_11"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Мы также можем написать метод {font=monospace.ttf}{color=#57f}describe_burger{/color}{color=#888}(){/color}{/font}, распечатывающий аппетитное описание бургера:\n\n{font=monospace.ttf}    {color=#ff0}class{/color} {color=#57f}Burger{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, bun, cheese, patty, sauce, lettuce, tomato, num_pickles):\n            self.bun {color=#0f0}={/color} bun\n            self.cheese {color=#0f0}={/color} cheese\n            self.patty {color=#0f0}={/color} patty\n            self.sauce {color=#0f0}={/color} sauce\n            self.lettuce {color=#0f0}={/color} lettuce\n            self.tomato {color=#0f0}={/color} tomato\n            self.num_pickles {color=#0f0}={/color} num_pickles\n\n        {color=#ff0}def{/color} {color=#57f}add_pickles{/color}(self, n):\n            self.num_pickles {color=#0f0}+={/color} n\n\n        {color=#ff0}def{/color} describe_burger(self):\n            {color=#57f}print{/color}({color=#f00}\"This burger has a\"{/color}, self.bun, {color=#f00}\"bun with a\"{/color}, self.patty, {color=#f00}\"patty.\"{/color}, end{color=#0f0}={/color}{color=#f00}\" \"{/color})\n            {color=#57f}print{/color}({color=#f00}\"It's drizzled with a delicious\"{/color}, self.sauce, {color=#f00}\"sauce.\"{/color}, end{color=#0f0}={/color}{color=#f00}\" \"{/color})\n            {color=#ff0}if{/color} self.lettuce:\n                {color=#57f}print{/color}({color=#f00}\"There is a bed of lettuce.\"{/color}, end{color=#0f0}={/color}{color=#f00}\" \"{/color})\n            {color=#ff0}if{/color} self.tomato:\n                {color=#57f}print{/color}({color=#f00}\"There are fresh tomatoes.\"{/color}, end{color=#0f0}={/color}{color=#f00}\" \"{/color})\n            {color=#ff0}if{/color} self.num_pickles {color=#0f0}>{/color} {color=#f00}0{/color}:\n                {color=#57f}print{/color}({color=#f00}\"Also, there are exactly\"{/color}, self.num_pickles, {color=#f00}\"pickles.\"{/color}, end{color=#0f0}={/color}{color=#f00}\" \"{/color}){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 11
screen chapter07_02_11_screen:
    text "11 / " + str(persistent.NUM_PAGES["chapter07_02"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_02_10"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Естественно, {font=monospace.ttf}{color=#57f}__init__{/color}{color=#888}(){/color}{/font} — не единственный магический метод. Их множество (см. {a=https://docs.python.org/3/reference/datamodel.html#basic-customization}официальную документацию Python{/a}). Например, метод {font=monospace.ttf}{color=#57f}__str__{/color}{color=#888}(){/color}{/font} определяет, как объект будет выглядеть при выводе через print(). По умолчанию вывод объекта печатает лишь его адрес в памяти. Реализовав {font=monospace.ttf}{color=#57f}__str__{/color}{color=#888}(){/color}{/font}, мы задаем понятное человекочитаемое строковое представление:\n\n{font=monospace.ttf}{size=-5}    {color=#ff0}class{/color} {color=#57f}Burger{/color}:\n        ...\n        {color=#ff0}def{/color} {color=#57f}__str__{/color}(self):\n            {color=#ff0}return{/color} {color=#f00}\"Bun: \"{/color} + self.bun + {color=#f00}\" Patty: \"{/color} + self.patty + {color=#f00}\" Sauce: \"{/color} + self.sauce{/size}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
