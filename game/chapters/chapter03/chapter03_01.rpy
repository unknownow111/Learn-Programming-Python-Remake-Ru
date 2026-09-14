# chapter and lesson labels
label chapter03_01_01:
    $ COMPLETED.add("chapter03_01_01"); save_game()
    call screen chapter03_01_01_screen
label chapter03_01:
    jump chapter03_01_01
    jump chapter_select

# page 1
screen chapter03_01_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter03_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter03"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter03"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 3{/i}{/b}{/size}\n\n{color=#57f}{b}{i}Что вы ели вчера? А позавчера? А за день до этого?{/i}{/b}{/color}\n\nКаждый день вы (надеемся) завтракаете, обедаете и ужинаете. А значит, ваш ответ на каждый из трех вопросов будет практически одинаковым.\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Как выглядел бы код, выводящий ответы на эти три вопроса?\n\nСкорее всего, вы представили нечто подобное:\n\n{font=monospace.ttf}    {color=#57f}print{/color}({color=#f00}\"Breakfast\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Lunch\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Dinner\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Breakfast\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Lunch\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Dinner\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Breakfast\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Lunch\"{/color})\n    {color=#57f}print{/color}({color=#f00}\"Dinner\"{/color}){/font}\n\nУжас, какая пустая трата места и сил! Мы повторяем одно и то же действие снова и снова. Наверняка должен быть более элегантный способ повторного выполнения инструкций (в программировании это известно как {b}{i}принцип DRY — Don't Repeat Yourself / Не повторяйся{/i}{/b}). И такой способ действительно есть: {b}{i}циклы{/i}{/b}, позволяющие автоматизировать любые рутинные повторения.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "burger_meal.png":
        xsize 1152
        ysize 657
        xalign 0.93
        yalign .62
