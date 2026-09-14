# chapter and lesson labels
label chapter04_06_01:
    $ COMPLETED.add("chapter04_06_01"); save_game()
    call screen chapter04_06_01_screen
label chapter04_06_02:
    $ COMPLETED.add("chapter04_06_02"); save_game()
    call screen chapter04_06_02_screen
label chapter04_06_03:
    $ COMPLETED.add("chapter04_06_03"); save_game()
    call screen chapter04_06_03_screen
label chapter04_06_04:
    $ COMPLETED.add("chapter04_06_04"); save_game()
    call screen chapter04_06_04_screen
label chapter04_06_05:
    $ COMPLETED.add("chapter04_06_05"); save_game()
    call screen chapter04_06_05_screen
label chapter04_06_06:
    $ COMPLETED.add("chapter04_06_06"); save_game()
    call screen chapter04_06_06_screen
label chapter04_06_07:
    $ COMPLETED.add("chapter04_06_07"); save_game()
    call screen chapter04_06_07_screen
label chapter04_06_08:
    $ COMPLETED.add("chapter04_06_08"); save_game()
    call screen chapter04_06_08_screen
label chapter04_06_09:
    $ COMPLETED.add("chapter04_06_09"); save_game()
    call screen chapter04_06_09_screen
label chapter04_06:
    jump chapter04_06_01
    jump chapter_select

# page 1
screen chapter04_06_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter04_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_06_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Мы познакомились со стандартными структурами данных Python и рассмотрели сценарии их использования. На практике вам очень часто будет требоваться последовательно наполнять структуру данными. Например, представьте, что вам нужен {font=monospace.ttf}{color=#57f}list{/color}{/font}, содержащий квадраты целых чисел от {font=monospace.ttf}{color=#f00}0{/color}{/font} до некоего целого числа {font=monospace.ttf}{color=#888}n{/color}{/font} (включительно):\n\n{font=monospace.ttf}    squares {color=#0f0}={/color} [[{color=#f00}0{/color}, {color=#f00}1{/color}, {color=#f00}4{/color}, {color=#f00}9{/color}, ..., n{color=#0f0}**{/color}{color=#f00}2{/color}]{/font}\n\nИсходя из уже пройденного материала, ход ваших мыслей был бы следующим:\n\n    1. Создать пустой список с помощью функции {font=monospace.ttf}{color=#57f}list{/color}{color=#888}(){/color}{/font}\n    2. Пройтись по числам {font=monospace.ttf}{color=#f00}0{/color}{/font}, {font=monospace.ttf}{color=#f00}1{/color}{/font}, {font=monospace.ttf}{color=#f00}2{/color}{/font} и т.д. с помощью функции {font=monospace.ttf}{color=#57f}range{/color}{color=#888}(){/color}{/font}\n    3. На каждой итерации добавлять квадрат числа в список с помощью метода {font=monospace.ttf}{color=#888}.{/color}{color=#57f}append{/color}{color=#888}(){/color}{/font}\n\nОбъединив все вместе в коде на Python, вы бы получили нечто подобное:\n\n{font=monospace.ttf}    squares {color=#0f0}={/color} {color=#57f}list{/color}()\n    {color=#ff0}for{/color} x {color=#0f0}in{/color} {color=#57f}range{/color}(n{color=#0f0}+{/color}{color=#f00}1{/color}):\n        squares.{color=#57f}append{/color}(x{color=#0f0}**{/color}{color=#f00}2{/color}){/font}\n\nЭтот фрагмент отлично работает, но для реализации довольно простой идеи потребовалось 3 строчки кода. Можно ли сделать это лучше и элегантнее?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "thinking.png":
        xsize 440
        ysize 400
        xalign 0.5
        yalign .95

# page 2
screen chapter04_06_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter04_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_06_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_06_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "В Python генераторы ({b}{i}comprehensions{/i}{/b}) предоставляют компактный способ одновременно создавать {i}и{/i} наполнять структуры данных. Вспомним наш предыдущий пример:\n\n{font=monospace.ttf}    squares {color=#0f0}={/color} {color=#57f}list{/color}()\n    {color=#ff0}for{/color} x {color=#0f0}in{/color} {color=#57f}range{/color}(n{color=#0f0}+{/color}{color=#f00}1{/color}):\n        squares.{color=#57f}append{/color}(x{color=#0f0}**{/color}{color=#f00}2{/color}){/font}\n\nМы можем использовать {b}{i}генератор списков{/i}{/b} ({b}{i}list comprehension{/i}{/b}), чтобы поместить цикл for прямо {i}внутрь{/i} объявления списка. Синтаксис будет следующим (помним, что списки задаются квадратными скобками):\n\n{font=monospace.ttf}    squares {color=#0f0}={/color} [[x{color=#0f0}**{/color}{color=#f00}2{/color} {color=#ff0}for{/color} x {color=#0f0}in{/color} {color=#57f}range{/color}(n{color=#0f0}+{/color}{color=#f00}1{/color})]{/font}\n\nЕсли сформулировать это простыми словами: \"Создать {font=monospace.ttf}{color=#57f}list{/color}{/font}, содержащий значение {font=monospace.ttf}{color=#888}x{/color}{color=#f00}²{/color}{/font} для каждого целого числа {font=monospace.ttf}{color=#888}x{/color}{/font} в диапазоне {font=monospace.ttf}{color=#f00}0{/color} ≤ {color=#888}x{/color} ≤ {color=#888}n{/color}{/font}, и сохранить полученный список в переменную {font=monospace.ttf}{color=#888}squares{/color}{/font}.\"":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter04_06_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter04_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_06_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_06_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Хотя генераторы списков ({font=monospace.ttf}{color=#57f}list{/color}{/font} comprehensions) — самый частый случай, мы можем использовать генераторы и для компактного построения других структур! Например, следующий код аналогичен предыдущему, но сохраняет квадраты чисел в {font=monospace.ttf}{color=#57f}set{/color}{/font} (множество):\n\n{font=monospace.ttf}    squares {color=#0f0}={/color} {color=#57f}set{/color}()\n    {color=#ff0}for{/color} x {color=#0f0}in{/color} {color=#57f}range{/color}(n{color=#0f0}+{/color}{color=#f00}1{/color}):\n        squares.{color=#57f}add{/color}(x{color=#0f0}**{/color}{color=#f00}2{/color}){/font}\n\nКак и прежде, мы можем применить {b}{i}генератор множеств{/i}{/b} ({b}{i}set comprehension{/i}{/b}) с фигурными скобками:\n\n{font=monospace.ttf}    squares {color=#0f0}={/color} {{x{color=#0f0}**{/color}{color=#f00}2{/color} {color=#ff0}for{/color} x {color=#0f0}in{/color} {color=#57f}range{/color}(n{color=#0f0}+{/color}{color=#f00}1{/color})}{/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Что произойдет, если в генераторе множеств встретятся повторяющиеся значения?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter04_06_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter04_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_06_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_06_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Пойдем еще дальше: используем генераторы для создания словарей {font=monospace.ttf}{color=#57f}dict{/color}{/font}! Представим ситуацию, когда у нас есть список имен студентов и список их оценок, где оценка по индексу {font=monospace.ttf}{color=#888}i{/color}{/font} в {font=monospace.ttf}{color=#888}grades{/color}{/font} принадлежит студенту по индексу {font=monospace.ttf}{color=#888}i{/color}{/font} в {font=monospace.ttf}{color=#888}names{/color}{/font}:\n\n{font=monospace.ttf}    names  {color=#0f0}={/color} [[{color=#f00}\"Niema Moshiri\"{/color}, {color=#f00}\"Sabeel Mansuri\"{/color}, ...]\n    grades {color=#0f0}={/color} [[{color=#f00}\"A+\"{/color},            {color=#f00}\"A\"{/color},              ...]{/font}\n\nЧто если мы хотим создать словарь {font=monospace.ttf}{color=#57f}dict{/color}{/font}, где ключами будут имена студентов, а значениями — их оценки?\n\n{font=monospace.ttf}    grades {color=#0f0}={/color} {{{color=#f00}\"Niema Moshiri\"{/color}: {color=#f00}\"A+\"{/color}, {color=#f00}\"Sabeel Mansuri\"{/color}: {color=#f00}\"A\"{/color}, ...}{/font}\n\nМы могли бы создать пустой словарь, обойти индексы списков и добавлять пары ключ-значение на каждой итерации цикла:\n\n{font=monospace.ttf}    name_to_grade {color=#0f0}={/color} {color=#57f}dict{/color}()\n    {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}({color=#57f}len{/color}(names)):\n        name_to_grade[[names[[i]] {color=#0f0}={/color} grades[[i]{/font}\n\nЭто работает, но с помощью {b}{i}генератора словарей{/i}{/b} ({b}{i}dict comprehension{/i}{/b}) мы запишем это в одну строчку:\n\n{font=monospace.ttf}    name_to_grade = {{names[[i]: grades[[i] {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}({color=#57f}len{/color}(names))}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 5
screen chapter04_06_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter04_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_06_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_06_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Мы научились собирать структуру данных в одну строчку, но во всех предыдущих примерах в результат попадали {b}{i}все{/i}{/b} элементы цикла. А что если мы хотим {b}{i}отфильтровать{/i}{/b} значения по условию? Например, в вычислении квадратов чисел мы хотим оставить только четные квадраты. Обычный цикл с условием {b}{i}if{/i}{/b} выглядел бы так:\n\n{font=monospace.ttf}    squares {color=#0f0}={/color} {color=#57f}list{/color}()\n    {color=#ff0}for{/color} x {color=#0f0}in{/color} {color=#57f}range{/color}(n{color=#0f0}+{/color}{color=#f00}1{/color}):\n        {color=#ff0}if{/color} x{color=#0f0}**{/color}{color=#f00}2{/color} {color=#0f0}%{/color} {color=#f00}2{/color} {color=#0f0}=={/color} {color=#f00}0{/color}: {color=#f0f}# если x**2 четное{/color}\n            squares.{color=#57f}append{/color}(x**{color=#f00}2{/color}){/font}\n\nОказывается, условия if можно использовать прямо внутри генераторов!\n\n{font=monospace.ttf}    squares {color=#0f0}={/color} [[x**{color=#f00}2{/color} {color=#ff0}for{/color} x {color=#0f0}in{/color} {color=#57f}range{/color}(n{color=#0f0}+{/color}{color=#f00}1{/color}) {color=#ff0}if{/color} x{color=#0f0}**{/color}{color=#f00}2{/color} {color=#0f0}%{/color} {color=#f00}2{/color} {color=#0f0}=={/color} {color=#f00}0{/color}]{/font}\n\nСмысл: \"Создать список, содержащий {font=monospace.ttf}{color=#888}x{/color}{color=#f00}²{/color}{/font} для каждого {font=monospace.ttf}{color=#888}x{/color}{/font} от {font=monospace.ttf}{color=#f00}0{/color} до {color=#888}n{/color}{/font}, но только если {font=monospace.ttf}{color=#888}x{/color}{color=#f00}²{/color}{/font} делится на 2 без остатка\". Результатом будет список, из которого отброшены все неподходящие значения:\n\n{font=monospace.ttf}    [[{color=#f00}0{/color}, {color=#f00}4{/color}, {color=#f00}16{/color}, ...]{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter04_06_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter04_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_06_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_06_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "В предыдущем примере мы использовали блок if внутри генератора для {b}{i}фильтрации{/i}{/b} (отсеивания) элементов. А что если вместо выбрасывания элемента мы хотим использовать ветку {b}{i}else{/i}{/b} с {b}{i}альтернативным{/i}{/b} значением? Например, у нас есть список чисел {font=monospace.ttf}{color=#888}nums{/color}{/font}, и мы хотим получить новый список {font=monospace.ttf}{color=#888}even_or_odd{/color}{/font}, где на месте каждого числа будет стоять строка {font=monospace.ttf}{color=#f00}\"even\"{/color}{/font}, если число четное, или {font=monospace.ttf}{color=#f00}\"odd\"{/color}{/font}, если нечетное:\n\n{font=monospace.ttf}    nums        {color=#0f0}={/color} [[{color=#f00}0{/color},      {color=#f00}1{/color},     {color=#f00}1{/color},     {color=#f00}2{/color},      {color=#f00}3{/color},     {color=#f00}5{/color},     {color=#f00}8{/color},      {color=#f00}13{/color},    ...]\n    even_or_odd {color=#0f0}={/color} [[{color=#f00}\"even\"{/color}, {color=#f00}\"odd\"{/color}, {color=#f00}\"odd\"{/color}, {color=#f00}\"even\"{/color}, {color=#f00}\"odd\"{/color}, {color=#f00}\"odd\"{/color}, {color=#f00}\"even\"{/color}, {color=#f00}\"odd\"{/color}, ...]{/font}\n\nОбычный код занял бы 6 строк:\n\n{font=monospace.ttf}    even_or_odd {color=#0f0}={/color} {color=#57f}list{/color}()\n    {color=#ff0}for{/color} num {color=#0f0}in{/color} nums:\n        {color=#ff0}if{/color} num {color=#0f0}%{/color} {color=#f00}2{/color} {color=#0f0}=={/color} {color=#f00}0{/color}:\n            even_or_odd.{color=#57f}append{/color}({color=#f00}\"even\"{/color})\n        {color=#ff0}else{/color}:\n            even_or_odd.{color=#57f}append{/color}({color=#f00}\"odd\"{/color}){/font}\n\nКак записать это через генератор списков?\n\n{font=monospace.ttf}    even_or_odd {color=#0f0}={/color} [[{color=#f00}\"even\"{/color} {color=#ff0}if{/color} num {color=#0f0}%{/color} {color=#f00}2{/color} {color=#0f0}=={/color} {color=#f00}0{/color} {color=#ff0}else{/color} {color=#f00}\"odd\"{/color} {color=#ff0}for{/color} num {color=#0f0}in{/color} nums]{/font}\n\nРазберем по частям: берется {font=monospace.ttf}{color=#f00}\"even\"{/color}{/font}, если условие истинно, иначе {font=monospace.ttf}{color=#f00}\"odd\"{/color}{/font} — и так для каждого числа в {font=monospace.ttf}{color=#888}nums{/color}{/font}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 7
screen chapter04_06_07_screen:
    text "7 / " + str(persistent.NUM_PAGES["chapter04_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_06_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_06_08"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Генераторы могут быть даже {b}{i}вложенными{/i}{/b}! Допустим, вы хотите сформировать матрицу в виде списка списков кортежей:\n\n{font=monospace.ttf}    -------------------------\n    | ({color=#f00}0{/color},{color=#f00}0{/color}) | ({color=#f00}0{/color},{color=#f00}1{/color}) | ({color=#f00}0{/color},{color=#f00}2{/color}) |\n    -------------------------\n    | ({color=#f00}1{/color},{color=#f00}0{/color}) | ({color=#f00}1{/color},{color=#f00}1{/color}) | ({color=#f00}1{/color},{color=#f00}2{/color}) |\n    -------------------------{/font}\n\nС помощью обычных вложенных циклов это выглядело бы так:\n\n{font=monospace.ttf}    matrix {color=#0f0}={/color} {color=#57f}list{/color}()\n    {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}2{/color}):\n        row {color=#0f0}={/color} {color=#57f}list{/color}()\n        {color=#ff0}for{/color} j {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}3{/color}):\n            row.{color=#57f}append{/color}((i,j))\n        matrix.{color=#57f}append{/color}(row){/font}\n\nЗдесь не только много строк, но и легко ошибиться (например, забыть добавить {font=monospace.ttf}{color=#888}row{/color}{/font} в {font=monospace.ttf}{color=#888}matrix{/color}{/font} после завершения внутреннего цикла). Как лаконично выразить это через генераторы?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 8
screen chapter04_06_08_screen:
    text "8 / " + str(persistent.NUM_PAGES["chapter04_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_06_07"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter04_06_09"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Начнем с внутреннего цикла for:\n\n{font=monospace.ttf}    row {color=#0f0}={/color} {color=#57f}list{/color}()\n    {color=#ff0}for{/color} j {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}3{/color}):\n        row.{color=#57f}append{/color}((i,j)){/font}\n\nПревратим его в генератор списка:\n\n{font=monospace.ttf}    row {color=#0f0}={/color} [[(i,j) {color=#ff0}for{/color} j {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}3{/color})]{/font}\n\nТеперь подставим это во внешний цикл, заменив {font=monospace.ttf}{color=#888}row{/color}{/font}:\n\n{font=monospace.ttf}    matrix {color=#0f0}={/color} {color=#57f}list{/color}()\n    {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}2{/color}):\n        matrix.{color=#57f}append{/color}([[(i,j) {color=#ff0}for{/color} j {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}3{/color})]){/font}\n\nИ наконец, свернем и внешний цикл тоже:\n\n{font=monospace.ttf}    matrix {color=#0f0}={/color} [[[[(i,j) {color=#ff0}for{/color} j {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}3{/color})] {color=#ff0}for{/color} i {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}2{/color})]{/font}\n\nГотово! Длинный блок превратился в одну выразительную строчку.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} А что если вместо 2-мерного списка нам понадобился бы 3-мерный? Можно ли построить его аналогичным образом?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 9
screen chapter04_06_09_screen:
    text "9 / " + str(persistent.NUM_PAGES["chapter04_06"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter04_06_08"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "О генераторах можно рассказывать бесконечно, но для вводного курса этой базы более чем достаточно. Подведем ключевые итоги:\n\nГенераторы позволяют выразить инициализацию и фильтрацию структур данных значительно компактнее. В ряде случаев это делает код легче для восприятия и уменьшает количество мест для случайных опечаток. Более того, создание коллекций через генераторы выполняется в Python {b}{i}немного быстрее{/i}{/b} обычных циклов со списками.\n\nОднако помните важное правило: чересчур сложные вложенные генераторы в одну строчку могут стать {b}{i}крайне{/i}{/b} трудными для чтения и отладки. Главный принцип чистого кода — понятность для человека. Не гонитесь за записью всего приложения в одну строчку: если генератор перестает быть понятным с первого взгляда, лучше расписать его обычным циклом!":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
