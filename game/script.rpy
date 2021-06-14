label start:
    define w = Character("阿伟")
    define j = Character("杰哥")
    define b = Character("彬彬") 
    define m = Character("美琪")
    define s = Character("淑惠")
    define sm = Character("淑惠&美琪")
    define am = Character("阿伟嬤")
    define unk = Character("？？？")
    define bn = Character("彬彬", kind=nvl)
    define wn = Character("阿伟", kind=nvl)
    define x = Character("美雪")
    if not persistent.passed:
        call ch1
    if persistent.passed == True:
        with fade
        unk "何必如此。"
        unk "阿伟和彬彬的结局，难道只能这样吗？"
        unk "你依然要坐以待毙吗？"
        menu:
            "是。":
                unk "好吧。"
                unk "那么，继续如往常运行。"
                call ch1
            "否。":
                unk "那么，由你改写两人的命运。"
                $ secondrun = 1
                with fade
                window hide
                scene title
                play sound "audio/start.ogg"
                pause 9.5
                window show
                scene awei diandong
                with fade
                call ch2
return