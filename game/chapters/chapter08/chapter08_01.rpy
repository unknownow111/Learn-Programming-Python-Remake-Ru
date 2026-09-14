# chapter and lesson labels
label chapter08_01_01:
    $ COMPLETED.add("chapter08_01_01"); save_game()
    call screen chapter08_01_01_screen
label chapter08_01:
    jump chapter08_01_01
    jump chapter_select

# page 1
screen chapter08_01_01_screen:
    text "1 / " + str(persistent.NUM_PAGES["chapter08_01"]):
        color gui.accent_color
        xpos persistent.PAGENUM_XPOS
        ypos persistent.PAGENUM_YPOS
    textbutton "Назад" action Jump("chapter08"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    textbutton "Назад" action Jump("chapter08"):
        xpos persistent.NAV_BUTTON_NEXT_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    text "{size=+20}{b}{i}Глава 8{/i}{/b}{/size}\n\n{color=#57f}{b}{i}\"Нельзя потерять то, чего у тебя никогда не было\"\n    — Тот самый парень из 6-го класса{/i}{/b}{/color}\n\nВаш \"друг\" аппетитно хрустит вашей любимой пачкой чипсов с халапеньо. Вы просите поделиться. Друг запускает руку в пачку, съедает последний чипс, протягивает вам пустой пакет и с улыбкой говорит: {color=#57f}{i}\"Угощайся!\"{/i}{/color}\n\n{b}{color=#f00}ОСТАНОВИСЬ и подумай:{/color}{/b} Можете ли вы \"угоститься\"?\n\nКак невозможно достать чипс из пустой пачки, так и в Python есть действия, которые физически невозможно выполнить. Например, нельзя обратиться к несуществующей переменной, взять элемент по несуществующему индексу списка и так далее. Такую особую категорию непредвиденных ситуаций называют {b}{i}исключениями{/i}{/b} ({b}{i}exceptions{/i}{/b}).\n\nЛюбой программист стремится писать код без исключений. Однако ошибки неизбежны. Когда программа предназначена для реальных пользователей, мы должны грамотно перехватывать и обрабатывать любые ошибки (исключения), не допуская аварийного завершения программы.":
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
    add "chips.png":
        xsize 800
        ysize 633
        xalign 0.5
        yalign .96
