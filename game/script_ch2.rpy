label ch2:
    $ gotowangba = 0
    $ learned = 0
    stop music
    voice "voice/awei2-1.ogg"
    w "弱耶，拜托你很弱耶！你现在知道谁是老大了喔？哈！"
    "阿伟指着电脑说着，阿伟的阿嬤听到了，便从房间内走了出来。"
    scene awei ama
    voice "voice/ama2-1.ogg"
    am "阿伟你又在玩电动喔？休息一下吧？去看个书好不好？"
    if secondrun == 1:
        "阿伟应该怎么做？"
        menu:
            "休息一下，去看书。":
                jump kanshu
            "继续打电动。":
                jump jixu
    else:
        jump jixu
label kanshu:
    scene black
    with fade
    "阿伟起身，回房休息了。"
    "偶然间，他看到了一本书，标题是《男生在外如何保护自己》。"
    w "这是什么？"
    "阿伟翻开了书，阅读着。"
    $ learned = 1
    "阿伟嬤见阿伟在认真看书，便放心地离开了家。"
    pause 2
    "叮叮叮..."
    "手机响了。"
    "阿伟拿起手机。"
    bn "要不要一起去网吧打电动？"
    bn "我在台北XXX网吧等你。"
    menu:
        "去。":
            wn "好。"
            nvl clear
            "阿伟离开了家，前往了台北XXX网吧。"
            jump wangba
        "不去。":
            wn "算了，我还要看书呢。"
            bn "好吧。"
            nvl clear
            pause 2
            "阿伟躺在床上无所事事。"
            "他感觉家里的空气十分闷热，便前往了公园散心。"
            jump gongyuan
label jixu:
        w "烦耶。"
        am "我在跟你讲话你有没有听到？"
        w "你不要烦好不好！"
        am "我才讲你两句你就说我烦？我只希望你能够好好用功读书，整天只看到你在这边打电动！"
        w "吼！死了啦，都你害的啦，拜托。"
        scene ama
        "阿伟生气着冲出了家门。"
        if secondrun == 0:
            w "（那天，我只是因为受不了阿嬷啰嗦，就冲出去，谁知道，竟然......）"
        jump wangba
label wangba:
        scene wangba
        with fade
        "网吧。"
        if gotowangba == 1:
            b "你不是说不用来了吗？怎么又过来了？"
            w "不是，我和你说啊..."
            b "快点过来！帮我打他！"
            w "不是，听我说..."
            b "快点！"
            "阿伟被彬彬强拉到座位上，打起了电动。"
            scene jiege kanyiyan
            "一旁的男子看了他们一眼。"
            "..."
            jump wuwai
        else:
            w "他超废的耶！"
            b "我知道啊。之前我就干掉他过。"
            w "二班那个啊！他每次都被我洗战绩耶。"
            b "他就嫩啊。"
            w "快点啦！"
            b "我看到了。"
            w "左边左边！"
            b "好了。"
            w "上面上面上面上面！"
            scene jiege kanyiyan
            "阿伟和彬彬打着电动。一旁的男子转过身来，看了他们一眼。"
            b "放了放了。"
            w "左边左边！"
            b "你不会放喔。"
            w "快点快点快点。"
            w "我死了啦，快点放！"
            w "复活复活。"
            b "诶，来救我，快点快点。"
            w "来来来，来了。"
            scene wab wangba
            b "我死了，我不要玩了。"
            w "欸，干嘛啦，你不要每次都这样好不好？"
            b "不想玩了啦。"
            pause 1.9
            w "你还有没有钱啊？我肚子好饿。"
            b "没了啦，今天都花光了。"
            scene jiege kanyiyan
            "一旁的男子再次转过身看了他们一眼。"
            w "我刚不是叫你多带一点吗？"
            b "你干嘛自己不多带。"
            w "诶，不要每次都这样好不好。"
            "那男子起身，走出了网吧。"
            b "好啦，时间也差不多了，也该回家了。"
            w "不要，我要再玩一下。"
            "......"
            jump wuwai
label gongyuan:
    scene gongyuan
    with fade
    play music "audio/bird.ogg"
    "公园。"
    "阿伟坐在了一棵树的旁边。旁边是坐在长椅上的美雪。"
    "淑惠走了过来。"
    s "嗨，美雪。"
    x "嗨，淑惠。"
    "美雪旁边的小女孩哭闹不停。"
    x "唉，真拿你没办法。去那边玩吧。"
    "小女孩跑向了不远处的健身轮。"
    scene jinlunfawang
    x "唉，小孩子，真的是有得玩都疯了。"
    pause 2
    scene gongyuan
    "淑惠一直看着两个玩健身轮的小孩。"
    x "不用再看了啦，这里没有坏人。"
    s "不是啦，最近有很多新闻报道诱骗儿童性侵的案件。"
    s "而且被诱骗的大多数是男生。弄得我神经兮兮的。"
    x "性侵男生...？"
    s "是啊。而且，作案分子大都在网吧和KTV附近诱拐男孩子。"
    "阿伟听到这句话，想到了约自己在网吧打电动的彬彬。"
    play sound "audio/runaway.ogg"
    "于是，他慌忙向网吧跑去。"
    stop music
    $ gotowangba = 1
    jump wangba
label wuwai:
    scene wuwai
    with fade
    "两人走出了网吧。"
    w "彬彬，我好饿喔。我们两个都没钱了。"
    b "没有钱我们就只能回家。"
    w "拜托！我才不要回家咧，我阿嬷超凶的耶，去住你家啦。"
    b "不行啦。"
    w "为什么不行？"
    b "喔，我自己都自身难保了。"
    w "哪有。"
    b "而且我爸会揍我。"
    w "真的假的。"
    voice "voice/jiege1.ogg"
    unk "不好意思...我刚听到你们两个说肚子饿，我这里刚好有块面包，我还不饿，请你们吃。"
    "那男子向两人搭话，并递给了他们一块面包。"
    w "先吃先吃。"
    "两人接过面包，迫不及待地撕下面包，吃了起来。"
    unk "对了，我叫阿杰，我也常来这里玩，嗯，他们都叫我杰哥。"
    "阿伟&彬彬" "杰哥好。"
    w "先吃啦..."
    "两人抬起了头，互相看了几眼，便慌忙向杰哥鞠了躬，便再次拿起面包吃了起来。"
    scene jiege chujian
    j "诶，你们好。我一个人住，我的房子还蛮大的，欢迎你们来我家玩。玩累了就...直接睡觉，没问题的。"
    scene wab huaiyi
    w "你觉得呢？"
    b "我觉得，他怪怪的。"
    w "看起来就是个很奇怪的人啊！不要理他。"
    "阿伟&彬彬" "不要去不要去。"
    scene jiege chujian
    j "诶诶...我常常帮助一些翘家的人，如果你们不要来的话，也没有关系。如果要来的话，我等一下可以带你们去超商，买一些好吃的喔。"
    scene wab huaiyi
    w "有东西可以吃耶！要不要去啊？"
    "彬彬犹豫了一会。但他无法抵御食物的诱惑，便决定和和杰哥一起去。"
    b "好啦，不然去好了。"
    w "去一下好了啦。"
    scene jiege chujian
    "杰哥露出了笑容。"
    scene wab huaiyi
    w "那杰哥！我和我朋友今天就去住你家咯！"
    scene jiege chujian
    j "好啊，没问题啊！那走啊！我们现在就去超商买一些吃的！"
    w "好啊！"
    j "走走走走走。"
    scene chaoshang
    w "你去那边，你去那边。"
    b "泡面。"
    w "小泡芙耶！"
    j "都可以拿。"
    w "谢谢杰哥！"
    w "好多饮料喔！"
    w "有酒耶！"
    b "不要看酒了啦，先买饮料啦。"
    b "什么都可以拿吗，杰哥？"
    j "都可以拿。"
    b "真的假的？"
    j "随便拿，你们随便拿。"
    w "真的可以吗？"
    j "可以拿，都拿。"
    w "谢谢杰哥！"
    "三人一起去了超商，买了很多吃的和饮料。"
    "杰哥并不吝啬自己的钱包，任由二人买东西。"
    "杰哥拿起了货架上的一些啤酒，看了几眼..."
    "又将目光投向了挑选饮料的二人。"
    "杰哥露出了笑容，再在货架上拿了一些啤酒。"
    scene wanshang
    with fade
    "晚上，杰哥家。"
    scene jiegejia
    with fade
    voice "voice/b2-1.ogg"
    b "快哉啊——————！快哉，快————哉————啊！"
    "彬彬瘫倒在沙发上，两臂拍打着沙发。"
    voice "voice/jiege2-1.ogg"
    j "你看，你看这个彬彬，才喝几罐，就醉了！真的太逊了！"
    voice "voice/awei3-1.ogg"
    w "这个彬彬就是逊啦！"
    voice "voice/jiege2-2.ogg"
    j "嗯？听你这么说，你很勇哦？"
    voice "voice/awei3-2.ogg"
    w "开玩笑，我超勇的好不好！我超会喝的啦！"
    "杰哥把手放在了阿伟的腿上。"
    voice "voice/jiege2-3.ogg"
    j "超会喝，很勇嘛？身材不错哦，蛮结实的啊？"
    w "杰哥，你干嘛啊？"
    j "都几岁了，还那么害羞？我看你完全是不懂喔？"
    w "懂，懂什么啊？"
    j "你想懂，我房里有一些好康的。"
    w "好康？是新游戏喔？"
    j "什么新游戏，比游戏还刺激！还可以教你......转大人。"
    w "转大人？"
    j "对啊。来啊，来看就知道了！"
    "阿伟被杰哥拉向了卧室，一旁的彬彬仍醉倒在沙发上，此时的他，完全不知道，后来发生了什么......。"
    scene woshi
    with fade
    w "杰哥，你有好多A片喔。"
    j "哎呦，那没什么，来看这个好康的！"
    "杰哥点击了电脑，屏幕上显示出一个画面......"
    "阿伟靠近了看，似乎不知道这是什么内容，但他的脸出卖了他。"
    w "杰哥，这是什么啊？"
    pause 1
    j "哎呦，你脸红啦？来，让我看看。"
    w "不要啦！"
    j "让我看看。"
    w "不要啦！杰哥，你干嘛啊？"
    j "让我看看你发育正不正常啊！"
    "杰哥突然做出可疑的举动。"
    if learned = 1:
        "阿伟想起淑惠在公园说的话，又想起了那本书......"
        "他抄起酒罐，往杰哥的太阳穴砸去。"
        j "你...你..."
        "杰哥倒在地上。"
        "阿伟慌忙跑出房间，背起大醉的彬彬跑出了杰哥家。"
        scene black
        with fade
        play music "audio/beishang.ogg"
        voice "voice/b2-1.ogg"
        b "快哉啊——————！快哉，快————哉————啊！"
        "彬彬拍打着阿伟的肩膀。"
        "阿伟在街道上，不知所措。"
        "虽然那街道他已老马识途，但因为杰哥在房间做出的种种举动，使他冷汗不止。"
        "此时的他，只能逃脱，却不知逃向何处。"
        pause 2
        "他的腿麻了。"
        "他想倒在地上，但他的求生欲让他坚持回到了自己家。"
        pause 2
        scene ama
        with fade
        am "阿伟你怎么了？怎么背着一个人？是你同学吗？"
        "阿伟把彬彬放在自己卧室的床上，然后锁上了家门，和彬彬一起躺在了床上。"
        b "快哉...快哉......"
        stop music
        jump xuexiao
    w "杰哥，不要啦！"
    "阿伟推开了杰哥。"
    scene jiege zhaijing
    with fade
    "杰哥摘下了眼镜，放在桌子上。"
    pause 2
    j "听话......"
    j "让我看看！"
    scene awei buyao
    w "不要！"
    scene jiege quantou
    "杰哥突然一拳打在阿伟的头部，打倒了阿伟，便立刻袭击阿伟，强行脱下了他的衣服。"
    w "杰哥不要啦，杰哥不要——！"
    scene awei luo
    w "杰哥......."
    w "杰哥不要————！杰哥————！杰哥不要！"
    scene awei shihou
    with fade
    $ renpy.movie_cutscene("awei_shihou.mp4")
    "阿伟蜷缩在墙角，抱着枕头，遮着自己的身体。"
    scene jiege shihou
    pause 2
    j "这件事是我们两个之间的秘密。"
    j "你最好不要给我告诉任何人。"
    j "如果你要说出去。"
    j "你就给我小心一点。"
    j "我知道你学校在哪里。"
    j "也知道你读哪一班。"
    j "你最好给我好好记住，懂吗！"
    scene awei and bar
    "阿伟说不出话。"
    "他低下了头，颤抖着，哭泣着......"
    $ renpy.movie_cutscene("ed.mp4")
    scene xuexiao
    with fade
    play music "audio/bird.ogg"
    "过了几天..."
    "阿伟走向了学校大门。彬彬见到了阿伟，立刻跑向了阿伟。"
    b "诶，阿伟，阿伟。"
    b "你这几天去哪里。"
    scene awei and binbin
    "阿伟看着别处，沉默起来。"
    b "你知道吗？"
    b "你阿嬤被学校约谈了耶。"
    "彬彬拍了一下阿伟。"
    b "你不能再翘课啦。"
    w "哦。"
    b "什么哦？"
    b "这几天都找不到你。"
    b "电话也不接。"
    b "发生什么事了？"
    w "（有人会相信我吗？）"
    w "（为什么他要对我那样？）"
    w "（我可以跟彬彬说... 我和杰哥的事情吗？）"
    "阿伟转向头，看向另一边。"
    w "没，没事啦。"
    b "什么没事。"
    b "你整个人阴阳怪气的。"
    w "彬彬，你可不可以不要管我啊！"
    scene xuexiao
    "阿伟撒开彬彬的手，跑走了。"
    b "诶！阿伟！"
    stop music
    play music "audio/beishang.ogg"
    scene shangdian
    with fade
    "阿伟郁闷地走在商店里。"
    "突然，手机响了。"
    "阿伟从口袋拿出了手机。"
    w "（...！）"
    scene awei shouji
    j "（好想你，再来我们家住一晚吧！）"
    j "（记住，这是我们之间的秘密。）"
    j "（不可以告诉任何人，否则......）"
    scene tingzi
    with fade
    stop music
    play music "audio/bird.ogg"
    w "淑慧阿姨，他就是这样，一直一直骚扰我。"
    s "阿伟，真难为你了，这阵子你一定过得很痛苦。"
    w "那我刚刚说的，你相信我吗？"
    s "我当然相信你啊，而且我还处理过类似的情形。"
    w "真的吗，那我该怎么办？"
    w "我好怕杰哥会到学校找我喔。"
    s "不用担心，这种情形一定要求救，一定要说出来。"
    s "如果你跟第一个大人说，他没有办法帮助你，你就赶快去找第二个大人。"
    w "喔。"
    s "那你家里还有谁啊？"
    w "我阿嬷。"
    s "阿嬷，那我先陪你回去找你阿嬷。"
    s "然后我们再去报警。"
    w "报—— 报警，为什么要报警啊？"
    s "因为这已经是性侵的行为啦，最好去报警，要不然他就会再伤害其他的人。"
    s "然后要做好相关的验伤检查，最后要找老师，来帮你做心理辅导。"
    "阿伟点了点头。"
    scene black
    with fade
    "......"
    "阿伟报了警，杰哥被绳之以法。"
    "但那痛苦的遭遇，始终刻在阿伟心灵的一角，永远不可磨灭......"
    "Normal End"
    $ persistent.passed = True
label xuexiao:
    scene xuexiao
    with fade
    "第二天，早上。"
    "阿伟和彬彬一起去了学校。"
    with fade
    "放学后。"
    "淑惠走向了阿伟。"
    s "你阿嬷跟我说，你和彬彬在一床睡觉？这是怎么回事呢？"
    "阿伟想起昨天早上，在公园听到的话。"
    w "我...我好像差点被性骚扰了......"
    s "性骚扰？"
    w "对......我该怎么办？"
    s "我们应该去报警。然后要做好相关的验伤检查，最后要找老师，来帮你做心理辅导。"
    "阿伟点了点头。"
    scene black
    with fade
    "......"
    "阿伟报了警，杰哥被绳之以法。"
    "之后，学校举行了隆重的表彰大会。"
    "阿伟获得了“正义标兵”的表彰。"
    "虽然那经历始终刻在阿伟心灵的一角，但经历了之后，他反而更加乐观了。"
    "阿伟也不在生阿嬷的气，更能心平气和地对待他人。"
    "True End"
return
