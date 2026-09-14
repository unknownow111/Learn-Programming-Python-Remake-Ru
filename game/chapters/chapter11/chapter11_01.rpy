# chapter and lesson labels
label chapter11_01_01:
    $ COMPLETED.add("chapter11_01_01"); save_game()
    call screen chapter11_01_01_screen
label chapter11_01_02:
    $ COMPLETED.add("chapter11_01_02"); save_game()
    call screen chapter11_01_02_screen
label chapter11_01:
    jump chapter11_01_01
    jump chapter_select

# page 1
screen chapter11_01_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter11_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter11"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter11_01_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 11{/i}{/b}{/size}\n\n{b}{i}{color=#57f}Эпилог{/color}{/i}{/b}\n\n{b}{color=#0f0}Sabeel Mansuri{/color}{/b}\n\n{size=-10}{i}\"Ты выживешь и поймешь, что человек не должен быть столь глуп. Два года назад здесь, на этом самом месте, мне тоже снился один и тот же сон. Мне снилось, что я должен отправиться в Испанию и отыскать там разрушенную церковь, где ночуют пастухи со своими овцами.\nВ моем сне прямо из ризницы рос платан, и мне было сказано, что если я раскопаю его корни, то найду скрытое сокровище. Но я же не настолько глуп, чтобы пересекать целую пустыню только из-за повторяющегося сна.\"\n\nПастух с трудом поднялся на ноги и еще раз посмотрел на Пирамиды.\nКазалось, они насмехались над ним, и он рассмеялся в ответ, а его сердце переполняла радость.\n\nПотому что теперь он точно знал, где спрятано его сокровище.{/i}\n\n — Пауло Коэльо, {i}Алхимик{/i}{/size}\n\n\n{b}{color=#0f0}Niema Moshiri{/color}{/b}\n\n{size=-10}{i}\"Герои этих историй часто могли повернуть назад, но не повернули. Они шли вперед.\nПотому что они держались за что-то.\"\n\n\"А за что держимся мы, Сэм?\"\n\n\"За то, что в этом мире есть добро, мистер Фродо. И за него стоит бороться.\"{/i}\n\n — Дж. Р. Р. Толкин, {i}Властелин колец: Две крепости{/i}{/size}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 2
screen chapter11_01_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter11_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter11_01_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "В меню" action Jump("chapter11"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "Это было потрясающее путешествие, и мы искренне гордимся тем, что вы прошли весь этот путь! Обучение программированию может показаться сложной задачей, и мы благодарны, что вы решили сделать шаг навстречу новому и присоединились к нам в изучении магии Python. Даже если вы изначально начали этот курс в учебных целях, мы призываем вас подумать о том, как применить полученные знания во всех сферах вашей жизни.\n\n    – {b}{i}Любите играть с друзьями в настольные игры?{/i}{/b}\n        – Напишите программу на Python для автоматизации рутины (например, бросков костей), чтобы сделать игру еще веселее!\n\n    – {b}{i}Вы заядлый книголюб?{/i}{/b}\n        – Напишите программу на Python для каталогизации вашей библиотеки!\n        – Какие книги у вас есть, какие хотите прочитать, что находится в списке желаемого и т. д.\n\n    – {b}{i}Увлекаетесь видеоиграми?{/i}{/b}\n        – Создайте собственную видеоигру на Python (например, с помощью {a=https://www.pygame.org/}PyGame{/a})!":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "thanks.png":
        xsize 1800
        ysize 714
        xalign 0.5
        yalign .95
