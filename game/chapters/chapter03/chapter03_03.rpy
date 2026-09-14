# chapter and lesson labels
label chapter03_03_01:
    $ COMPLETED.add("chapter03_03_01"); save_game()
    call screen chapter03_03_01_screen
label chapter03_03_02:
    $ COMPLETED.add("chapter03_03_02"); save_game()
    call screen chapter03_03_02_screen
label chapter03_03:
    jump chapter03_03_01
    jump chapter_select

# page 1
screen chapter03_03_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter03_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter03_03_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Вам могло показаться, что обход строки с помощью while выглядит громоздко: нужно вручную объявлять счетчик, составлять условие с len() и не забывать прибавлять единицу. Нам же хочется просто сказать компьютеру: \"для каждого символа в строке\". Именно для этого предназначен {b}{i}цикл for{/i}{/b}!\n\nЦикл for автоматически перебирает каждый элемент коллекции. Его базовая структура:\n\n{font=monospace.ttf}    {color=#f0f}# код до цикла for{/color}\n\n    {color=#ff0}for{/color} iterator_var {color=#0f0}in{/color} data:\n        {color=#f0f}# код тела цикла{/color}\n\n    {color=#f0f}# код после цикла for{/color}{/font}\n\nЭто избавляет нас от индексов, ручного инкремента и вызовов len():\n\n{font=monospace.ttf}    var {color=#0f0}={/color} {color=#f00}\"apple\"{/color}\n    {color=#ff0}for{/color} i {color=#0f0}in{/color} var:\n        {color=#57f}print{/color}(i){/font}\n\nХотя имя {font=monospace.ttf}{color=#888}i{/color}{/font} часто используют по привычке, хорошим стилем считается называть переменную так, чтобы она отражала суть элемента (например, {font=monospace.ttf}{color=#888}char{/color}{/font} при переборе символов):\n\n{font=monospace.ttf}    var {color=#0f0}={/color} {color=#f00}\"apple\"{/color}\n    {color=#ff0}for{/color} char {color=#0f0}in{/color} var:\n        {color=#57f}print{/color}(char){/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "apple.png":
        xsize 300
        ysize 415
        xalign 0.8
        yalign .99

# page 2
screen chapter03_03_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter03_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03_03_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Автоматический перебор элементов очень удобен, но как быть, если нужно перебрать лишь первые {font=monospace.ttf}{color=#888}n{/color}{/font} элементов?\n\nЦикл for сам по себе идет до самого конца последовательности. Но мы можем сгенерировать нужный диапазон чисел с помощью встроенной функции {font=monospace.ttf}{color=#57f}range{/color}{color=#888}(){/color}{/font}.\n\nФункция {font=monospace.ttf}{color=#57f}range{/color}{color=#888}(){/color}{/font} принимает параметры {font=monospace.ttf}{color=#888}start{/color}{/font} и {font=monospace.ttf}{color=#888}end{/color}{/font}, возвращая последовательность целых чисел от {font=monospace.ttf}{color=#888}start{/color}{/font} (включительно) до {font=monospace.ttf}{color=#888}end{/color}{/font} (не включая). Например, {font=monospace.ttf}{color=#57f}range{/color}{color=#888}({/color}{color=#f00}1{/color}{color=#888},{/color} {color=#f00}4{/color}{color=#888}){/color}{/font} генерирует числа: {font=monospace.ttf}{color=#f00}1{/color}{/font}, {font=monospace.ttf}{color=#f00}2{/color}{/font}, {font=monospace.ttf}{color=#f00}3{/color}{/font}. Если параметр {font=monospace.ttf}{color=#888}start{/color}{/font} опущен, отсчет по умолчанию начинается с 0: {font=monospace.ttf}{color=#57f}range{/color}{color=#888}({color=#f00}4{/color}){/color}{/font} вернет: {font=monospace.ttf}{color=#f00}0{/color}{/font}, {font=monospace.ttf}{color=#f00}1{/color}{/font}, {font=monospace.ttf}{color=#f00}2{/color}{/font}, {font=monospace.ttf}{color=#f00}3{/color}{/font}.\n\nС помощью {font=monospace.ttf}{color=#57f}range{/color}{color=#888}(){/color}{/font} мы можем перебирать индексы:\n\n{font=monospace.ttf}    var {color=#0f0}={/color} {color=#f00}\"apple\"{/color}\n    {color=#ff0}for{/color} index {color=#0f0}in{/color} {color=#57f}range{/color}({color=#f00}3{/color}):\n        {color=#57f}print{/color}(var[[index]){/font}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Что напечатает приведенный выше код?\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Можно ли было добиться того же результата с помощью среза строки?":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
