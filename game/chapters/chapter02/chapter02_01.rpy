# chapter and lesson labels
label chapter02_01_01:
    $ COMPLETED.add("chapter02_01_01"); save_game()
    call screen chapter02_01_01_screen
label chapter02_01:
    jump chapter02_01_01
    jump chapter_select

# page 1
screen chapter02_01_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter02_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter02"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter02"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 2{/i}{/b}{/size}\n\n{color=#57f}{b}{i}Хотите мороженого?{/i}{/b}{/color}\n\nПредставим, что вы придерживаетесь разумного питания и делаете осознанный выбор (в чем мы ни секунды не сомневаемся, это лишь вводные условия). Как бы вы ответили на этот вопрос?\n\nСкорее всего, ваш ответ будет зависеть от обстоятельств! Если вы только что проснулись и собираетесь позавтракать, ответ (ведь вы следите за здоровьем) — однозначно нет. Но если вы только что вкусно поужинали, шарик-другой десерта будет очень кстати.\n\nГоворя формальным языком, ваш ответ является {b}{i}условным (conditional){/i}{/b}. То есть решение меняется в зависимости от контекста и условий. Те инструменты, которые мы изучили ранее, не позволяли ветвить логику программы.\n\nДавайте это исправим!":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "ice_cream.png":
        xsize 340
        ysize 800
        xalign 0.5
        yalign .95
