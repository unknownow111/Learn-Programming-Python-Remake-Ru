# chapter and lesson labels
label chapter01_03_01:
    $ COMPLETED.add("chapter01_03_01"); save_game()
    call screen chapter01_03_01_screen
label chapter01_03_02:
    $ COMPLETED.add("chapter01_03_02"); save_game()
    call screen chapter01_03_02_screen
label chapter01_03_03:
    $ COMPLETED.add("chapter01_03_03"); save_game()
    call screen chapter01_03_03_screen
label chapter01_03_04:
    $ COMPLETED.add("chapter01_03_04"); save_game()
    call screen chapter01_03_04_screen
label chapter01_03_05:
    $ COMPLETED.add("chapter01_03_05"); save_game()
    call screen chapter01_03_05_screen
label chapter01_03_06:
    $ COMPLETED.add("chapter01_03_06"); save_game()
    call screen chapter01_03_06_screen
label chapter01_03_07:
    call screen chapter01_03_07_screen
label chapter01_03:
    jump chapter01_03_01
    jump chapter_select

# page 1
screen chapter01_03_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter01_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_03_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Начнем с передачи компьютеру базовой информации в виде {b}{i}данных{/i}{/b}. Мы будем работать с четырьмя основными {b}{i}типами данных{/i}{/b}: {font=monospace.ttf}{color=#57f}int{/color}{/font}, {font=monospace.ttf}{color=#57f}float{/color}{/font}, {font=monospace.ttf}{color=#57f}bool{/color}{/font} и {font=monospace.ttf}{color=#57f}str{/color}{/font}. Они послужат фундаментальными строительными блоками в программировании.\n\n    – {font=monospace.ttf}{color=#57f}int{/color}{/font} — хранит любое целое число (сокращение от integer).\n        – Примеры: {font=monospace.ttf}{color=#f00}0{/color}{/font}, {font=monospace.ttf}{color=#f00}-5{/color}{/font}, {font=monospace.ttf}{color=#f00}37{/color}{/font}, {font=monospace.ttf}{color=#f00}-8142{/color}{/font}\n\n    – {font=monospace.ttf}{color=#57f}float{/color}{/font} — хранит вещественное число с дробной частью (число с плавающей точкой).\n        – Примеры: {font=monospace.ttf}{color=#f00}0.0{/color}{/font}, {font=monospace.ttf}{color=#f00}5.2{/color}{/font}, {font=monospace.ttf}{color=#f00}-12.332{/color}{/font}\n\n    – {font=monospace.ttf}{color=#57f}bool{/color}{/font} — логический тип, хранит либо {font=monospace.ttf}{color=#f00}True{/color}{/font} (истина), либо {font=monospace.ttf}{color=#f00}False{/color}{/font} (ложь) (сокращение от boolean).\n\n    – {font=monospace.ttf}{color=#57f}str{/color}{/font} — хранит строку из одного или более символов, обычно обрамляется одинарными или двойными кавычками*.\n        – Примеры: {font=monospace.ttf}{color=#f00}\"good morning\"{/color}{/font}, {font=monospace.ttf}{color=#f00}' '{/color}{/font}, {font=monospace.ttf}{color=#f00}'_/x|'{/color}{/font}\n\n{i}*Хотя официальное имя типа — {font=monospace.ttf}{color=#57f}str{/color}{/font}, обычно их называют просто \"строками\". В этом учебнике мы часто будем говорить \"строка\", имея в виду значение типа {font=monospace.ttf}{color=#57f}str{/color}{/font}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "analytics.png":
        xsize 1440
        ysize 810
        xalign 0.75
        yalign 0.99

# page 2
screen chapter01_03_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter01_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_03_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_03_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Чтобы передавать и сохранять данные в компьютере, мы используем {b}{i}переменные{/i}{/b}. Переменные работают в точности так же, как в математике: мы присваиваем переменной значение и подставляем ее в выражения. Эту операцию мы называем {b}{i}присваиванием переменной{/i}{/b}:\n\n    1. {b}{i}Имя{/i}{/b} переменной*\n    2. {b}{i}Оператор присваивания{/i}{/b} ({font=monospace.ttf}{color=#0f0}={/color}{/font})\n    3. {b}{i}Значение{/i}{/b} переменной\n\nК примеру, присвоим значение {font=monospace.ttf}{color=#57f}int{/color}{/font}, равное {font=monospace.ttf}{color=#f00}9{/color}{/font}, переменной с именем {font=monospace.ttf}foo{/font}:\n\n{font=monospace.ttf}    foo {color=#0f0}={/color} {color=#f00}9{/color}{/font}\n\nАналогично можно присваивать значения типов {font=monospace.ttf}{color=#57f}float{/color}{/font}, {font=monospace.ttf}{color=#57f}str{/color}{/font} и {font=monospace.ttf}{color=#57f}bool{/color}{/font}:\n\n{font=monospace.ttf}    bar {color=#0f0}={/color} {color=#f00}-4.1{/color}\n    baz {color=#0f0}={/color} {color=#f00}\"This is a string.\"{/color}\n    qux {color=#0f0}={/color} {color=#f00}False{/color}{/font}\n\nPython также поддерживает множественное присваивание в одну строку:\n\n{font=monospace.ttf}    bar, baz, qux {color=#0f0}={/color} {color=#57f}-4.1{/color}, {color=#57f}\"This is a string.\"{/color}, {color=#57f}False{/color}{/font}\n\n{i}*Не всякое имя допустимо. Имена могут состоять только из латинских букв (a-z, A-Z), цифр (0-9) и знака подчеркивания (_). Имя не может начинаться с цифры и не должно совпадать с зарезервированными ключевыми словами Python: {font=monospace.ttf}{color=#f00}and  as  assert  async  await  break  class  continue  def  del  elif  else  except  False  finally  for  from  global  if  import  in  is  lambda  None  nonlocal  not  or  pass  raise  return  True  try  while  with  yield{/color}{/font}{/i}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter01_03_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter01_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_03_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_03_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "В примерах выше мы ставили пробелы с обеих сторон от оператора присваивания:\n\n{font=monospace.ttf}    foo {color=#0f0}={/color} {color=#f00}9{/color}{/font}\n\nВ Python между частями выражения можно ставить сколько угодно пробелов. Например, можно написать вообще без пробелов:\n\n{font=monospace.ttf}    foo{color=#0f0}={/color}{color=#f00}9{/color}{/font}\n\nИли с большим количеством пробелов:\n\n{font=monospace.ttf}    foo          {color=#0f0}={/color}          {color=#f00}9{/color}{/font}\n\nВсе эти варианты работают совершенно одинаково. Возникает вопрос: какой вариант лучше? Главная цель программиста — писать код, который легко читать человеку. Общепринятым стандартом считается ставить по одному пробелу вокруг оператора присваивания — именно первый вариант признан эталонным стилем.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter01_03_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter01_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_03_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_03_05"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Людям приятно, когда элементы вокруг выдержаны в едином стиле. Например, если у вас несколько пар обуви, вы наверняка наденете одинаковые ботинки, а не разные. То же самое касается и имен переменных: хорошим тоном считается называть переменные единообразно.\n\nВ языках программирования преобладают два стиля именования: {a=https://en.wikipedia.org/wiki/Snake_case}Snake Case{/a} (стиль {font=monospace.ttf}{color=#888}snake_case{/color}{/font}) и {a=https://en.wikipedia.org/wiki/Camel_case}Camel Case{/a} (стиль {font=monospace.ttf}{color=#888}camelCase{/color}{/font}). В стиле {font=monospace.ttf}{color=#888}snake_case{/color}{/font} слова разделяются нижним подчеркиванием ({font=monospace.ttf}{color=#888}_{/color}{/font}), а все буквы строчные. В стиле {font=monospace.ttf}{color=#888}camelCase{/color}{/font} каждое новое слово начинается с заглавной буквы (кроме первого), без знаков разделения.\n\n{font=monospace.ttf}    my_snake_case_variable {color=#0f0}={/color} {color=#f00}42{/color}\n    myCamelCaseVariable {color=#0f0}={/color} {color=#f00}42{/color}{/font}\n\nПри написании кода на Python рекомендуется использовать {font=monospace.ttf}{color=#888}snake_case{/color}{/font}, как предписано в официальном руководстве по стилю {a=https://www.python.org/dev/peps/pep-0008/#naming-conventions}PEP 8{/a}.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "mismatched_shoes.png":
        xsize 1067
        ysize 754
        xalign 0.5
        yalign 0.97

# page 5
screen chapter01_03_05_screen:
    text "5 / " + str(persistent.NUM_PAGES["chapter01_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_03_04"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_03_06"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "С технической точки зрения код выполнится одинаково независимо от выбранных имен, однако соблюдение {b}{i}единого стиля{/i}{/b} делает код опрятным и понятным. Кроме того, имена переменных должны быть {b}{i}говорящими (осмысленными){/i}{/b}: любой читатель должен сразу понимать, за что отвечает переменная.\n\nНапример, неинформативные имена затрудняют чтение:\n\n{font=monospace.ttf}    t {color=#0f0}={/color} {color=#f00}\"The Fast and the Furious\"{/color}\n    y {color=#0f0}={/color} {color=#f00}2001{/color}{/font}\n\nСледующие имена информативны, но не согласованы по стилю (слова разделены по-разному):\n\n{font=monospace.ttf}    movie_title {color=#0f0}={/color} {color=#f00}\"The Fast and the Furious\"{/color}\n    releaseYear {color=#0f0}={/color} {color=#f00}2001{/color}{/font}\n\nА вот здесь имена и осмысленные, и оформлены в едином стиле:\n\n{font=monospace.ttf}    movie_title {color=#0f0}={/color} {color=#f00}\"The Fast and the Furious\"{/color}\n    release_year {color=#0f0}={/color} {color=#f00}2001{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 6
screen chapter01_03_06_screen:
    text "6 / " + str(persistent.NUM_PAGES["chapter01_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_03_05"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_03_07"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Существует еще один особый базовый тип данных, о котором важно знать: {font=monospace.ttf}{color=#57f}NoneType{/color}{/font}. Значение типа {font=monospace.ttf}{color=#57f}NoneType{/color}{/font} используется тогда, когда данных в переменной еще нет или значение отсутствует; в этом случае переменной присваивают {font=monospace.ttf}{color=#f00}None{/color}{/font}.\n\nПредставьте, что вы пишете программу, угадывающую любимое число пользователя по серии вопросов. В начале программы вы объявляете переменную {font=monospace.ttf}{color=#888}fav_num{/color}{/font}, в которую позже запишете результат отгадки.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Чему должна быть равна переменная {font=monospace.ttf}{color=#888}fav_num{/color}{/font} на данном начальном этапе?\n\nОтвета у программы еще нет, пока опрос не завершен. Поэтому логичным решением является инициализировать ее значением {font=monospace.ttf}{color=#f00}None{/color}{/font}:\n\n{font=monospace.ttf}    fav_num {color=#0f0}={/color} {color=#f00}None{/color}{/font}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 7
define persistent.chapter01_03_07_correct = {"a": True,  "b": False, "c": True,  "d": False, "e": False}
default chapter01_03_07_student = {k: False for k in persistent.chapter01_03_07_correct}
define persistent.chapter01_03_07_options = {
    "a": "{font=monospace.ttf}{color=#f00}None{/color} {color=#0f0}={/color} {color=#f00}\" \"{/color}{/font}",
    "b": "{font=monospace.ttf}four {color=#0f0}={/color} {color=#f00}5{/color}{/font}",
    "c": "{font=monospace.ttf}1_plus_2 {color=#0f0}={/color} {color=#f00}\"three\"{/color}{/font}",
    "d": "{font=monospace.ttf}false {color=#0f0}={/color} {color=#f00}True{/color}{/font}",
    "e": "Ни один из вышеперечисленных",
}
screen chapter01_03_07_screen:
    if "chapter01_03_07" in COMPLETED:
        text persistent.CHALLENGE_SOLVED_TEXT:
            size gui.title_text_size
            color persistent.CHALLENGE_SOLVED_COLOR
            xalign persistent.TITLE_XALIGN
            ypos persistent.TITLE_YPOS
    elif "chapter01_03_07" in INCORRECT:
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
    text "7 / " + str(persistent.NUM_PAGES["chapter01_03"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_03_06"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        spacing persistent.EXERCISE_SPACING
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        text "{b}{color=#f0f}Упражнение:{/color}{/b} Какие из следующих объявлений переменных недопустимы в Python? (Выберите все подходящие варианты)"
        for ol in sorted(persistent.chapter01_03_07_options.keys()):
            if "chapter01_03_07" in COMPLETED:
                if persistent.chapter01_03_07_correct[ol]:
                    textbutton _("{b}{color=#0f0}(%s){/color}{/b} %s" % (ol, persistent.chapter01_03_07_options[ol])) action NullAction()
                else:
                    textbutton _("(%s) %s" % (ol, persistent.chapter01_03_07_options[ol])) action NullAction()
            else:
                textbutton _("(%s) %s" % (ol, persistent.chapter01_03_07_options[ol])) action ToggleDict(chapter01_03_07_student, ol)
        if "chapter01_03_07" not in COMPLETED:
            hbox:
                textbutton _("{b}{color=#0f0}Ответить{/font}{/b}") action Function(grade_challenge, "chapter01_03_07", persistent.chapter01_03_07_correct, chapter01_03_07_student)
                text "   "
                textbutton _("{b}Очистить{/b}") action Function(set_all, chapter01_03_07_student, False, from_label="chapter01_03_07")
