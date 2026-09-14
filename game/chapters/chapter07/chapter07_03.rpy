# chapter and lesson labels
label chapter07_03_01:
    $ COMPLETED.add("chapter07_03_01"); save_game()
    call screen chapter07_03_01_screen
label chapter07_03_02:
    $ COMPLETED.add("chapter07_03_02"); save_game()
    call screen chapter07_03_02_screen
label chapter07_03_03:
    $ COMPLETED.add("chapter07_03_03"); save_game()
    call screen chapter07_03_03_screen
label chapter07_03_04:
    call screen chapter07_03_04_screen
label chapter07_03_05:
    $ COMPLETED.add("chapter07_03_05"); save_game()
    call screen chapter07_03_05_screen
label chapter07_03_06:
    $ COMPLETED.add("chapter07_03_06"); save_game()
    call screen chapter07_03_06_screen
label chapter07_03_07:
    $ COMPLETED.add("chapter07_03_07"); save_game()
    call screen chapter07_03_07_screen
label chapter07_03_08:
    $ COMPLETED.add("chapter07_03_08"); save_game()
    call screen chapter07_03_08_screen
label chapter07_03_09:
    $ COMPLETED.add("chapter07_03_09"); save_game()
    call screen chapter07_03_09_screen
label chapter07_03_10:
    call screen chapter07_03_10_screen
label chapter07_03:
    jump chapter07_03_01
    jump chapter_select

# page 1
screen chapter07_03_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter07_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_03_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Теперь, когда мы умеем создавать свои {b}{i}{color=#57f}классы{/color}{/i}{/b}, мы перейдем к созданию {b}{i}экземпляров{/i}{/b} этих классов — самих {b}{i}{color=#f00}объектов{/color}{/i}{/b}.\n\nВспомним метод {font=monospace.ttf}{color=#57f}__init__{/color}{color=#888}(){/color}{/font} в классе {b}{color=#57f}Burger{/color}{/b}. Он неявно вызывается при создании объекта следующим синтаксисом:\n\n{font=monospace.ttf}    my_burger {color=#0f0}={/color} {color=#57f}Burger{/color}(){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Строка выше вызовет ошибку. Каких данных здесь не хватает?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "factory.png":
        xsize 1900
        ysize 1225
        xalign 0.5
        yalign .99

# page 2
screen chapter07_03_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter07_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_03_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_03_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Поскольку наш метод {font=monospace.ttf}{color=#57f}__init__{/color}{color=#888}(){/color}{/font} принимает 7 обязательных параметров (не считая {font=monospace.ttf}{color=#888}self{/color}{/font}), мы обязаны передать их при создании объекта:\n\n{font=monospace.ttf}    my_burger {color=#0f0}={/color} {color=#57f}Burger{/color}({color=#f00}\"brioche\"{/color}, {color=#f00}\"pepperjack\"{/color}, {color=#f00}\"veggie\"{/color}, {color=#f00}\"ketchup\"{/color}, {color=#f00}False{/color}, {color=#f00}False{/color}, {color=#f00}2{/color}){/font}\n\nСоздав {font=monospace.ttf}{color=#888}my_burger{/color}{/font}, мы обращаемся к его атрибутам и методам через оператор точки ({font=monospace.ttf}{color=#ff0}.{/color}{/font}):\n\n{font=monospace.ttf}    {color=#57f}print{/color}(my_burger.sauce)\n    {color=#57f}print{/color}(my_burger.num_pickles)\n\n    my_burger.{color=#57f}add_pickles{/color}({color=#f00}2{/color})\n    my_burger.{color=#57f}describe_burger{/color}(){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Что напечатает приведенный код?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter07_03_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter07_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_03_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_03_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Собственные объекты можно использовать точно так же, как и встроенные: передавать в функции, сохранять в списки и словари. Но особенно мощный прием — {b}{i}использование одних объектов в качестве атрибутов других объектов (композиция){/i}{/b}.\n\nСоздадим класс {font=monospace.ttf}{color=#57f}Lunch{/color}{/font} (Обед), состоящий из бургера ({font=monospace.ttf}{color=#57f}Burger{/color}{/font}), картошки фри ({font=monospace.ttf}{color=#57f}Fries{/color}{/font}) и напитка ({font=monospace.ttf}{color=#57f}Drink{/color}{/font}):\n\n{font=monospace.ttf}{size=-5}    {color=#ff0}class{/color} {color=#57f}Drink{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, flavor, milliliters):\n            self.flavor {color=#0f0}={/color} flavor\n            self.milliliters {color=#0f0}={/color} milliliters\n\n    {color=#ff0}class{/color} {color=#57f}Fries{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, flavor, salted):\n            self.flavor {color=#0f0}={/color} flavor\n            self.salted {color=#0f0}={/color} salted\n\n    {color=#ff0}class{/color} {color=#57f}Lunch{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, drink, burger, fries):\n            self.drink {color=#0f0}={/color} drink\n            self.burger {color=#0f0}={/color} burger\n            self.fries {color=#0f0}={/color} fries{/size}{/font}\n\nИ соберем их воедино:\n\n{font=monospace.ttf}{size=-5}    my_drink {color=#0f0}={/color} {color=#57f}Drink{/color}({color=#f00}\"water\"{/color}, {color=#f00}500{/color})\n    my_burger {color=#0f0}={/color} {color=#57f}Burger{/color}({color=#f00}\"brioche\"{/color}, {color=#f00}\"pepperjack\"{/color}, {color=#f00}\"veggie\"{/color}, {color=#f00}\"ketchup\"{/color}, {color=#f00}False{/color}, {color=#f00}False{/color}, {color=#f00}2{/color})\n    my_fries {color=#0f0}={/color} {color=#57f}Fries{/color}({color=#f00}\"sweet potato\"{/color}, {color=#f00}False{/color})\n    my_lunch {color=#0f0}={/color} {color=#57f}Lunch{/color}({color=#f00}my_drink{/color}, {color=#f00}my_burger{/color}, {color=#f00}my_fries{/color}){/size}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
define persistent.chapter07_03_04_correct = {"a": False,  "b": False, "c": True,  "d": True}
default chapter07_03_04_student = {k: False for k in persistent.chapter07_03_04_correct}
define persistent.chapter07_03_04_options_v2 = {
    "a": "Узнать тип напитка можно так: {font=monospace.ttf}your_lunch.water{/font}",
    "b": "Узнать вид котлеты можно так: {font=monospace.ttf}your_lunch.patty{/font}",
    "c": "Узнать вкус картошки можно так: {font=monospace.ttf}your_lunch.fries.flavor{/font}",
    "d": "Получить объект {font=monospace.ttf}{color=#57f}Drink{/color}{/font} вашего обеда можно так: {font=monospace.ttf}your_lunch.drink{/font}",
}
screen chapter07_03_04_screen:
    if "chapter07_03_04" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter07_03_04" in INCORRECT:
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
    text "4 / " + str(persistent.NUM_PAGES["chapter07_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_03_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_03_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Выберите все верные утверждения о следующей программе:\n\n{font=monospace.ttf}{size=-5}    {color=#ff0}class{/color} {color=#57f}Drink{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, flavor, milliliters):\n            ...\n    {color=#ff0}class{/color} {color=#57f}Burger{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, bun, cheese, patty, sauce, lettuce, tomato, num_pickles):\n            ...\n    {color=#ff0}class{/color} {color=#57f}Fries{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, flavor, salted):\n            ...\n    {color=#ff0}class{/color} {color=#57f}Lunch{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, drink, burger, fries):\n            ...\n    your_drink {color=#0f0}={/color} {color=#57f}Drink{/color}({color=#f00}\"water\"{/color}, {color=#f00}500{/color})\n    your_burger {color=#0f0}={/color} {color=#57f}Burger{/color}({color=#f00}\"brioche\"{/color}, {color=#f00}\"pepperjack\"{/color}, {color=#f00}\"veggie\"{/color}, {color=#f00}\"ketchup\"{/color}, {color=#f00}False{/color}, {color=#f00}False{/color}, {color=#f00}2{/color})\n    your_fries {color=#0f0}={/color} {color=#57f}Fries{/color}({color=#f00}\"sweet potato\"{/color}, {color=#f00}False{/color})\n    your_lunch {color=#0f0}={/color} {color=#57f}Lunch{/color}(your_drink, your_burger, your_fries){/size}{/font}"
        for ol in sorted(persistent.chapter07_03_04_options_v2.keys()):
            if "chapter07_03_04" in COMPLETED:
                if persistent.chapter07_03_04_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter07_03_04_options_v2[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter07_03_04_options_v2[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter07_03_04_options_v2[ol])) action ToggleDict(chapter07_03_04_student, ol)
        if "chapter07_03_04" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter07_03_04", persistent.chapter07_03_04_correct, chapter07_03_04_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter07_03_04_student, False, from_label="chapter07_03_04")

# page 5
screen chapter07_03_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter07_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_03_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_03_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Допустим, мы с вами заказали абсолютно одинаковый обед:\n\n{font=monospace.ttf}    my_drink {color=#0f0}={/color} {color=#57f}Drink{/color}({color=#f00}\"water\"{/color}, {color=#f00}500{/color})\n    my_burger {color=#0f0}={/color} {color=#57f}Burger{/color}({color=#f00}\"brioche\"{/color}, {color=#f00}\"pepperjack\"{/color}, {color=#f00}\"veggie\"{/color}, {color=#f00}\"ketchup\"{/color}, {color=#f00}False{/color}, {color=#f00}False{/color}, {color=#f00}2{/color})\n    my_fries {color=#0f0}={/color} {color=#57f}Fries{/color}({color=#f00}\"sweet potato\"{/color}, {color=#f00}False{/color})\n    my_lunch {color=#0f0}={/color} {color=#57f}Lunch{/color}(my_drink, my_burger, my_fries)\n\n    your_drink {color=#0f0}={/color} {color=#57f}Drink{/color}({color=#f00}\"water\"{/color}, {color=#f00}500{/color})\n    your_burger {color=#0f0}={/color} {color=#57f}Burger{/color}({color=#f00}\"brioche\"{/color}, {color=#f00}\"pepperjack\"{/color}, {color=#f00}\"veggie\"{/color}, {color=#f00}\"ketchup\"{/color}, {color=#f00}False{/color}, {color=#f00}False{/color}, {color=#f00}2{/color})\n    your_fries {color=#0f0}={/color} {color=#57f}Fries{/color}({color=#f00}\"sweet potato\"{/color}, {color=#f00}False{/color})\n    your_lunch {color=#0f0}={/color} {color=#57f}Lunch{/color}(my_drink, my_burger, my_fries){/font}\n\nЧто произойдет, если спросить Python, равны ли наши обеды?\n\n{font=monospace.ttf}    {color=#57f}print{/color}(my_lunch {color=#0f0}=={/color} your_lunch){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Что напечатает эта строчка?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter07_03_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter07_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_03_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_03_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Удивительно, но ответ — {font=monospace.ttf}{color=#f00}False{/color}{/font}! Чтобы понять почему, напечатаем сами объекты:\n\n{font=monospace.ttf}    {color=#57f}print{/color}(my_lunch)\n    {color=#57f}print{/color}(your_lunch){/font}\n\nВывод будет примерно следующим:\n\n{font=monospace.ttf}    <{color=#57f}__main__{/color}.{color=#57f}Lunch{/color} object at {color=#f00}0x10b695320{/color}>\n    <{color=#57f}__main__{/color}.{color=#57f}Lunch{/color} object at {color=#f00}0x10b695400{/color}>{/font}\n\nШестнадцатеричные числа после {font=monospace.ttf}{color=#f00}0x{/color}{/font} — это конкретные адреса в {b}{i}оперативной памяти{/i}{/b}. Адреса различаются, а значит, перед нами два разных, независимых объекта, у которых просто случайно совпало содержимое.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "burger_meal.png":
        xsize 1152
        ysize 657
        xalign 0.2
        yalign .9
    add "burger_meal.png":
        xsize 1152
        ysize 657
        xalign 0.8
        yalign .9

# page 7
screen chapter07_03_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter07_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_03_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_03_08"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Однако в реальной жизни мы скажем: {color=#57f}{i}\"У нас одинаковые обеды!\"{/i}{/color}\n\nPython позволяет переопределить логику сравнения объектов через специальный метод {font=monospace.ttf}{color=#57f}__eq__{/color}{color=#888}(){/color}{/font} (для знака ==):\n\n{font=monospace.ttf}    {color=#ff0}class{/color} {color=#57f}Lunch{/color}:\n        {color=#ff0}def{/color} {color=#57f}__init__{/color}(self, drink, burger, fries):\n            self.drink {color=#0f0}={/color} drink\n            self.burger {color=#0f0}={/color} burger\n            self.fries {color=#0f0}={/color} fries\n\n        {color=#ff0}def{/color} {color=#57f}__eq__{/color}(self, other):\n            same_drink {color=#0f0}={/color} (self.drink {color=#0f0}=={/color} other.drink)\n            same_burger {color=#0f0}={/color} (self.burger {color=#0f0}=={/color} other.burger)\n            same_fries {color=#0f0}={/color} (self.fries {color=#0f0}=={/color} other.fries)\n            {color=#ff0}return{/color} same_drink {color=#0f0}and{/color} same_burger {color=#0f0}and{/color} same_fries{/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} От чего зависит работа этого метода?\n\nЕсли классы {font=monospace.ttf}{color=#57f}Drink{/color}{/font}, {font=monospace.ttf}{color=#57f}Burger{/color}{/font} и {font=monospace.ttf}{color=#57f}Fries{/color}{/font} не переопределят свой собственный {font=monospace.ttf}{color=#57f}__eq__{/color}{color=#888}(){/color}{/font}, они будут сравниваться по адресам памяти. Для полноценного сравнения каждый вложенный класс тоже должен реализовать {font=monospace.ttf}{color=#57f}__eq__{/color}{color=#888}(){/color}{/font}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 8
screen chapter07_03_08_screen:
    text "8 / " + str(persistent.NUM_PAGES["chapter07_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_03_07"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_03_09"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Переопределение {font=monospace.ttf}{color=#57f}__eq__{/color}{color=#888}(){/color}{/font} кажется отличной идеей, но порождает тонкий вопрос:\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Какую возможность мы теряем, переопределяя метод {font=monospace.ttf}{color=#57f}__eq__{/color}{color=#888}(){/color}{/font}?\n\nСнова представим, что мы заказали одинаковые блюда, и все классы корректно реализуют сравнение по значению. Теперь выражение вернет {font=monospace.ttf}{color=#f00}True{/color}{/font}:\n\n{font=monospace.ttf}    {color=#57f}print{/color}(my_lunch {color=#0f0}=={/color} your_lunch){/font}\n\nНо представьте, что кто-то спрашивает: \"Ели ли вы из одной тарелки (делили ли один и тот же обед)?\". Мы не делили один бургер пополам — у каждого была своя порция! Однако теперь оператор == больше не может сказать нам, один ли это и тот же физический объект в памяти.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 9
screen chapter07_03_09_screen:
    text "9 / " + str(persistent.NUM_PAGES["chapter07_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_03_08"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter07_03_10"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Эта разница обусловлена двумя видами равенства. Представьте близнецов: они похожи во всем (равенство по {b}{i}значению{/i}{/b}), но это два разных человека (не равны по {b}{i}идентичности{/i}{/b}).\n\n    1. {b}Равенство по значению (Equality of Value):{/b} объекты логически эквивалентны по содержимому\n    2. {b}Равенство по идентичности (Equality of Identity):{/b} это в точности один и тот же объект в памяти\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Проверяет ли {font=monospace.ttf}{color=#57f}__eq__{/color}{color=#888}(){/color}{/font} равенство по {b}{i}значению{/i}{/b} или по {b}{i}идентичности{/i}{/b}?\n\nОтвет: зависит от реализации! По умолчанию в Python метод {font=monospace.ttf}{color=#57f}__eq__{/color}{color=#888}(){/color}{/font} сравнивает {b}{i}идентичность{/i}{/b} (адреса). Когда разработчик переопределяет его, он обычно настраивает сравнение по {b}{i}значению{/i}{/b}.\n\nА как проверить идентичность объектов в памяти, даже если {font=monospace.ttf}{color=#57f}__eq__{/color}{color=#888}(){/color}{/font} переопределен? Для этого в Python существует оператор {font=monospace.ttf}{color=#ff0}is{/color}{/font}! Он возвращает {font=monospace.ttf}{color=#f00}True{/color}{/font} только в том случае, если обе переменные ссылаются на один и тот же участок памяти.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 10
define persistent.chapter07_03_10_correct = {"a": True,  "b": False, "c": False,  "d": False}
default chapter07_03_10_student = {k: False for k in persistent.chapter07_03_10_correct}
define persistent.chapter07_03_10_options = {
    "a": "True True",
    "b": "True False",
    "c": "False True",
    "d": "False False",
}
screen chapter07_03_10_screen:
    if "chapter07_03_10" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter07_03_10" in INCORRECT:
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
    text "10 / " + str(persistent.NUM_PAGES["chapter07_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter07_03_09"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Что напечатает следующий код? Предположим, что метод {font=monospace.ttf}{color=#57f}__eq__{/color}{color=#888}(){/color}{/font} корректно реализован для всех классов.\n\n{font=monospace.ttf}    my_drink {color=#0f0}={/color} {color=#57f}Drink{/color}({color=#f00}\"water\"{/color}, {color=#f00}500{/color})\n    my_burger {color=#0f0}={/color} {color=#57f}Burger{/color}({color=#f00}\"brioche\"{/color}, {color=#f00}\"pepperjack\"{/color}, {color=#f00}\"veggie\"{/color}, {color=#f00}\"ketchup\"{/color}, {color=#f00}False{/color}, {color=#f00}False{/color}, {color=#f00}2{/color})\n    my_fries {color=#0f0}={/color} {color=#57f}Fries{/color}({color=#f00}\"sweet potato\"{/color}, {color=#f00}False{/color})\n    my_lunch {color=#0f0}={/color} {color=#57f}Lunch{/color}(my_drink, my_burger, my_fries)\n\n    your_lunch {color=#0f0}={/color} my_lunch\n    your_lunch.drink.flavor {color=#0f0}={/color} {color=#f00}\"soda\"{/color}\n\n    {color=#57f}print{/color}(your_lunch {color=#0f0}=={/color} my_lunch, your_lunch {color=#0f0}is{/color} my_lunch){/font}"
        for ol in sorted(persistent.chapter07_03_10_options.keys()):
            if "chapter07_03_10" in COMPLETED:
                if persistent.chapter07_03_10_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter07_03_10_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter07_03_10_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter07_03_10_options[ol])) action [Function(set_all, chapter07_03_10_student, False, from_label="chapter07_03_10"), ToggleDict(chapter07_03_10_student, ol)]
        if "chapter07_03_10" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter07_03_10", persistent.chapter07_03_10_correct, chapter07_03_10_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter07_03_10_student, False, from_label="chapter07_03_10")
