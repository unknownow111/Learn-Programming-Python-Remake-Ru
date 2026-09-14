# compute progress strings
init python:
    def compute_progress_strings():
        num_complete = compute_num_complete(); lessons = dict(); out = list()
        for lesson in persistent.NUM_PAGES:
            chapter = lesson.split('_')[0]
            if chapter not in lessons:
                lessons[chapter] = set()
            lessons[chapter].add(lesson)
        for chapter in sorted(lessons.keys()):
            chapter_num = int(chapter.lstrip("chapter"))
            chapter_str = "{b}Глава %d:{/b}" % chapter_num
            chapter_fin = False
            if num_complete[chapter] == sum(persistent.NUM_PAGES[v] for v in lessons[chapter]):
                chapter_fin = True
            elif num_complete[chapter] != 0:
                chapter_str = "{color=#ff0}%s{/color}" % chapter_str
            lesson_strs = list()
            for lesson in sorted(lessons[chapter]):
                lesson_str = "%d.%d (%d/%d)" % (chapter_num, int(lesson.split("_")[-1]), num_complete[lesson], persistent.NUM_PAGES[lesson])
                if not chapter_fin:
                    if num_complete[lesson] == persistent.NUM_PAGES[lesson]:
                        lesson_str = "{color=#0f0}%s{/color}" % lesson_str
                    elif num_complete[lesson] != 0:
                        lesson_str = "{color=#ff0}%s{/color}" % lesson_str
                lesson_strs.append(lesson_str)
            chapter_str = "%s %s" % (chapter_str, ', '.join(lesson_strs))
            if chapter_fin:
                chapter_str = "{color=#0f0}%s{/color}" % chapter_str
            out.append(chapter_str)
        return out

# progress screen
label progress:
    call screen progress_screen
    jump chapter_select
screen progress_screen:
    text "Прогресс":
        size gui.title_text_size
        color gui.accent_color
        xalign persistent.TITLE_XALIGN
        ypos persistent.TITLE_YPOS
    textbutton "Назад" action Jump("chapter_select"):
        xpos persistent.NAV_BUTTON_PREV_XPOS
        ypos persistent.NAV_BUTTON_YPOS
    vbox:
        xpos persistent.CONTENT_XPOS
        ypos persistent.CONTENT_YPOS
        xsize persistent.CONTENT_XSIZE
        for chapter_str in compute_progress_strings():
            text chapter_str
            text ""
