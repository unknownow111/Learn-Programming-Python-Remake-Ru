# chapter and lesson labels
label chapter01_01_01:
    $ COMPLETED.add("chapter01_01_01"); save_game()
    call screen chapter01_01_01_screen
label chapter01_01_02:
    $ COMPLETED.add("chapter01_01_02"); save_game()
    call screen chapter01_01_02_screen
label chapter01_01_03:
    $ COMPLETED.add("chapter01_01_03"); save_game()
    call screen chapter01_01_03_screen
label chapter01_01_04:
    $ COMPLETED.add("chapter01_01_04"); save_game()
    call screen chapter01_01_04_screen
label chapter01_01:
    jump chapter01_01_01
    jump chapter_select

# page 1
screen chapter01_01_01_screen:
    add "gui/main_menu.png"
    text "1 / " + str(persistent.NUM_PAGES["chapter01_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_01_02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS

# page 2
screen chapter01_01_02_screen:
    text "2 / " + str(persistent.NUM_PAGES["chapter01_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_01_01"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_01_03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Добро пожаловать на курс!{/i}{/b}{/size}\n\nЭтот интерактивный учебник создан для того, чтобы познакомить новичков с удивительным миром компьютерных наук (Computer Science)! Курс не требует никаких предварительных знаний. Мы надеемся, что к его завершению вы научитесь мыслить алгоритмически, писать программы на Python и проектировать классы, используя принципы объектно-ориентированного программирования (ООП).\n\nВ учебнике используется подход активного обучения (Active Learning): материал насыщен разнообразными практическими заданиями, которые стимулируют мышление и закрепляют пройденное. Вам встретятся вопросы формата {b}{color=#f00}ОСТАНОВИСЬ и подумай{/color}{/b}, помогающие осмыслить тему, а также {b}{color=#f0f}Упражнения{/color}{/b}, проверяющие понимание ключевых концепций.\n\nПриятного обучения!\n\n{a=https://sabeelmansuri.com/}Sabeel Mansuri{/a} и {a=https://niema.net/}Niema Moshiri{/a}":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 3
screen chapter01_01_03_screen:
    text "3 / " + str(persistent.NUM_PAGES["chapter01_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_01_02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Далее" action Jump("chapter01_01_04"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Об авторах{/i}{/b}{/size}\n\n{a=https://sabeelmansuri.com/}Сабил Мансури (Sabeel Mansuri){/a} (бакалавр Калифорнийского университета в Сан-Диего, 2020) — инженер-программист и биоинформатик, специализирующийся на передовых методиках обучения. Его опыт охватывает full-stack веб-разработку, создание учебных курсов, исследования в вычислительной биологии и проектирование высоконагруженных распределенных сетевых систем в Amazon Web Services (AWS).\n\n{a=https://niema.net/}Нима Мошири (Niema Moshiri){/a} (Ph.D., Калифорнийский университет в Сан-Диего, 2019) — доцент кафедры компьютерных наук и инженерии (CSE) в Калифорнийском университете в Сан-Диего. Специализируется в области биоинформатики, объединяющей Computer Science (с фокусом на разработке алгоритмов) и молекулярную биологию. Его исследования посвящены созданию вычислительных методов анализа вирусной филогенетики и эпидемиологии.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE

# page 4
screen chapter01_01_04_screen:
    text "4 / " + str(persistent.NUM_PAGES["chapter01_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter01_01_03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter01"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Благодарности{/i}{/b}{/size}\n\nМы выражаем благодарность {a=https://www.linkedin.com/in/savannah-collyer/}Savannah Collyer{/a} и {a=https://www.linkedin.com/in/jaz-gill/}Jaz Gill{/a} за вклад в проектирование учебной программы курса.\n\nТакже благодарим {a=http://compeau.cbd.cmu.edu/}Phillip Compeau{/a} и {a=http://cseweb.ucsd.edu/~ppevzner/}Pavel Pevzner{/a}, чей учебник ({a=http://bioinformaticsalgorithms.com/}Bioinformatics Algorithms: An Active Learning Approach{/a}) послужил источником вдохновения для стиля изложения и педагогического подхода.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
