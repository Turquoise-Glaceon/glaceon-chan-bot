import discord
import random
from PIL import Image
from PIL import ImageFont, ImageDraw
import os
import shutil

TOKEN = 'TOKEN'
mint = "<@mint>"

CHANNEL_ID = CHANNEL_ID

hand = ":raised_hand:"
DRAzzz = [0,0,1,1,1,1,2,2,2,2,2,3,3,4,"SQ","SQ","SQ"]
DRASQ = ["2v2","2v2","2v2","3v3","3v3","4v4","66","66"]
DRAf = ["FFA","FFA","FFA","FFA","FFA","FFA","FFA","FFA","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","3v3","3v3","3v3","3v3","3v3","3v3","3v3","3v3","3v3","3v3","4"]
DRA4 = ["4v4","4v4","4v4","4v4","6v6"]
Track = ["none", "MKS", "WP", "SSC", "TR", "MC", "TH", "TM", "SGF", "SA", "DS", "Ed", "MW", "CC", "BDD", "BC", "RR", "rMMM", "rMC", "rCCB", "rTT", "rDDD", "rDP3", "rRRy", "rDKJ", "rWS", "rSL", "rMP", "rYV", "rTTC", "rPPS", "rGV", "rRRd", "dYC", "dEA", "dDD", "dMC", "dWGM", "dRR", "dIIO", "dHC", "dBP", "dCL", "dWW", "dAC", "dNBC", "dRiR", "dSBS", "dBB", "bPP", "bTC", "bCMo", "bCMa", "bTB", "bSR", "bSG", "bNH", "bNYM", "bMC3", "bKD", "bWP", "bSS", "bSL", "bMG", "bSHS"]
rTrack = ["MKS", "WP", "SSC", "TR", "MC", "TH", "TM", "SGF", "SA", "DS", "Ed", "MW", "CC", "BDD", "BC", "RR", "rMMM", "rMC", "rCCB", "rTT", "rDDD", "rDP3", "rRRy", "rDKJ", "rWS", "rSL", "rMP", "rYV", "rTTC", "rPPS", "rGV", "rRRd", "dYC", "dEA", "dDD", "dMC", "dWGM", "dRR", "dIIO", "dHC", "dBP", "dCL", "dWW", "dAC", "dNBC", "dRiR", "dSBS", "dBB", "bPP", "bTC", "bCMo", "bCMa", "bTB", "bSR", "bSG", "bNH", "bNYM", "bMC3", "bKD", "bWP", "bSS", "bSL", "bMG", "bSHS"]
sae = ["毎度" + hand + "必勝法でござうるす♪" , "毎度" + hand + "必勝法だなも♪" , "毎度" + hand + "勝つ勝つござうるす♪" , "がんばる必勝法だなも♪" , "がんばるだなも必勝法♪" , "勝つ勝つだなもでござうるすの必勝法♪" , "おはおはメモメモござうるす♪" , "にこにこメモメモござうるす♪" , "にこにこメモメモござうるす♪" , "コロすゾ立ち回り ( *ᵔ ᵕ ᵔ *)" , "しばくゾ立ち回り ( *ᵔ ᵕ ᵔ *)" , "秘密の必勝法だなも♪" , "必勝法のメモメモだなも♪" , "にこにこれっつごー必勝法♪" , "だなも！！"]
oha = "毎度" + hand + "おはおはござうるす♪"

client = discord.Client()

async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.purge()
    await channel.send(oha)
    
@client.event 
async def on_ready():
    print('ログインしました')
    await greet()
    #await client.change_presence(activity=discord.Game(name=f"TEST{len(client.guilds)}"))

@client.event
async def on_message(message):
    
    none = ["none","NONE","CLEAR"]
    MKS = ["MKS","マリオカートスタジアム","マリカス","まりかす"]
    WP = ["WP","ウォーターパーク","ウォタパ","うぉたぱ"]
    SSC = ["SSC","スイーツキャニオン","スイキャニ","すいきゃに"]
    TR = ["TR","ドッスンいせき","ドッスン","ドッスン遺跡","どっすん"]
    MC = ["MC","マリオサーキット","新マリサ","しんマリサ","新まりさ","しんまりさ"]
    TH = ["TH","キノピオハーバー","ハーバー","はーばー"]
    TM = ["TM","ねじれマンション","ねじマン","ねじれ"]
    SGF = ["SGF","ヘイホーこうざん","ヘイこう","ヘイホー","ヘイホー高山","ヘイホー鉱山","へいこう","へいほー"]
    SA = ["SA","サンシャインくうこう","サンシャイン空港","くうこう","空港"]
    DS = ["DS","ドルフィンみさき","ドルみ","ドルミ","みさき","ドルフィン","ドルフィン岬","岬","どるみ"]
    Ed = ["Ed","ED","エレクトロドリーム","エレドリ","えれどり","エレド","えれど"]
    MW = ["MW","ワリオスノーマウンテン","ワリスノ","雪山","わりすの"]
    CC = ["CC","スカイガーデン","スカガ","すかが"]
    BDD = ["BDD","ホネホネさばく","ホネホネ","ほねほね","ほねさば","骨骨","骨さば","骨サバ","骨鯖"]
    BC = ["BC","クッパキャッスル","クパキャ","くぱきゃ"]
    RR = ["RR","レインボーロード","新虹","しんにじ","にじ"]
    rMMM = ["rMMM","RMMM","MMM","モーモーカントリー","モモカン","ももかん"]
    rMC = ["rMC","RMC","GBA","GBAマリオサーキット","グバ","ぐば","GBAマリサ","グバマリ","ぐばマリ","グバまり","ぐばまり"]
    rCCB = ["rCCB","RCCB","CCB","プクプクビーチ","プクビ","ぷくび"]
    rTT = ["rTT","RTT","TT","キノピオハイウェイ","ハイウェイ","はいうぇい"]
    rDDD = ["rDDD","RDDD","カラカラさばく","カラカラ砂漠","カラサバ","からさば"]
    rDP3 = ["rDP3","RDP3","RDP","DP3","DP","ドーナツへいや","ドーナツ平野","平野","へいや"]
    rRRy = ["rRRy","RRRY","RRY","ピーチサーキット","ピチサ","ぴちさ"]
    rDKJ = ["rDKJ","RDKJ","DKJ","DK","RDK","DKジャングル","ジャングル","じゃんぐる"]
    rWS = ["rWS","RWS","WS","ワリオスタジアム","ワリスタ","わりすた"]
    rSL = ["rSL","RSL","SL","シャーベットランド","シャベラン","しゃべらん"]
    rMP = ["rMP","RMP","MP","ミュージックパーク","ミューパ","みゅーぱ"]
    rYV = ["rYV","RYV","YV","ヨッシーバレー","ヨシバ","よしば"]
    rTTC = ["rTTC","RTTC","TTC","チクタクロック","チクタク","ちくたく"]
    rPPS = ["rPPS","RPPS","PPS","パックンスライダー","パクスラ","ぱくすら"]
    rGV = ["rGV","RGV","GV","グラグラかざん","グラグラ","ぐらぐら","火山","かざん","ぐらかざ","グラかざ"]
    rRRd = ["rRRd","RRRD","RRD","64レインボーロード","64虹","64にじ"]
    dYC = ["dYC","DYC","YC","ヨッシーサーキット","ヨシサ","よしさ"]
    dEA = ["dEA","DEA","EA","エキサイトバイク","エキバ","えきば"]
    dDD = ["dDD","DDD","DD","ドラゴンロード","ドラロ","どらろ"]
    dMC = ["dMC","DMC","ミュートシティ","ミュート","みゅーと"]
    dWGM = ["dWGM","DWGM","WGM","ワリオこうざん","ワリオ鉱山","わりこう","ワリこう","ワリコウ"]
    dRR = ["dRR","DRR","SFCレインボーロード","SFC虹","SFCにじ"]
    dIIO = ["dIIO","DIIO","IIO","ツルツルツイスター","ツツツ","つつつ","つるつる","ツルツル"]
    dHC = ["dHC","DHC","HC","ハイラルサーキット","ハイラル","はいらる"]
    dBP = ["dBP","DBP","BP","ベビィパーク","ベビパ","べびぱ"]
    dCL = ["dCL","DCL","CL","チーズランド","チーズ","ちーず","チズラン","ちずらん"]
    dWW = ["dWW","DWW","WW","ネイチャーロード","ネイチャー","ねいちゃー"]
    dAC = ["dAC","DAC","AC","どうぶつの森","どうぶつのもり","どう森","どうもり"]
    dNBC = ["dNBC","DNBC","NBC","ネオクッパシティ","ネオパ","ねおぱ","ネオクッパ","ねおくっぱ"]
    dRiR = ["dRiR","DRIR","RIR","リボンロード","リボン","りぼん"]
    dSBS = ["dSBS","DSBS","SBS","リンリンメトロ","リンメト","りんめと","リンリン","りんりん"]
    dBB = ["dBB","DBB","BB","ビッグブルー","びっぐぶるー"]
    bPP = ["bPP","BPP","PP","パリプロムナード","パリ","ぱり","パリプロ","ぱりぷろ"]
    bTC = ["bTC","BTC","TC","キノピオサーキット","キノサ","きのさ"]
    bCMo = ["bCMo","BCMO","CMO","チョコマウンテン","チョコ","ちょこ","チョコ山","ちょこ山","チョコやま","ちょこやま"]
    bCMa = ["bCMa","BCMA","CMA","ココナッツモール","ココモ","ここも"]
    bTB = ["bTB","BTB","TB","トーキョースクランブル","トースク","とーすく","トーキョー","とーきょー","東京"]
    bSR = ["bSR","BSR","SR","キノコリッジウェイ","キノリ","きのり","キコリ","きこり"]
    bSG = ["bSG","BSG","SG","GBAスカイガーデン","GBAスカ","GBAすか","グバスカ","ぐばスカ","グバすか","ぐばすか"]
    bNH = ["bNH","BNH","NH","ニンニンドージョー","ニンニン","にんにん"]
    bNYM = ["bNYM","BNYM","NYM"]
    bMC3 = ["bMC3","BMC3","BMC","MC3"]
    bKD = ["bKD","BKD","KD"]
    bWP = ["bWP","BWP"]
    bSS = ["bSS","BSS","SS"]
    bSL = ["bSL","BSL"]
    bMG = ["bMG","BMG","MG"]
    bSHS = ["bSHS","BSHS","SHS"]
    
    Trackzzz = [none, MKS, WP, SSC, TR, MC, TH, TM, SGF, SA, DS, Ed, MW, CC, BDD, BC, RR, rMMM, rMC, rCCB, rTT, rDDD, rDP3, rRRy, rDKJ, rWS, rSL, rMP, rYV, rTTC, rPPS, rGV, rRRd, dYC, dEA, dDD, dMC, dWGM, dRR, dIIO, dHC, dBP, dCL, dWW, dAC, dNBC, dRiR, dSBS, dBB, bPP, bTC, bCMo, bCMa, bTB, bSR, bSG, bNH, bNYM, bMC3, bKD, bWP, bSS, bSL, bMG, bSHS]


    xMx = message.content
    
    zMz = xMx.upper()

    def aaa():
        for i in Trackzzz:
            if zMz in i:
                txt = str(i[0])
                return(txt)

    Mx = aaa()
    Ux = message.author.id
    Cx = message.channel.id
    U = str(Ux)
    C = str(Cx)
    path1 = "User"
    path2 = U
    path3 = "input.py"
    path4 = "channel"
    path5 = C+".py"
    path7 = "output.png"
    path8 = os.path.join("minimap","image")
    path9 = str(Mx)+".png"
    pathU = os.path.join(path1,path2)
    pathUc = os.path.join(pathU,path3)
    pathC = os.path.join(path4,path5)
    UF = os.path.isfile(pathUc)
    CF = os.path.isfile(pathC)
    rpathr = random.choice(rTrack)
    rpath1 = "rTrack"
    rpath2 = "Table"
    rpath3 = rpathr
    rpath4 ="minimap.png"
    rTpath = os.path.join(os.path.join(os.path.join(rpath1,rpath2),rpath3),rpath4)
    rpathC = os.path.join(rpath1,path4,path5)
    rCF = os.path.isfile(rpathC)
    mention = "<@" + U + ">"
    mkb = "http://japan-mk.blog.jp/mk8dx.info-4"
    glaurl = "url"
    
    co4 = message.content[4:]
    co5 = message.content[5:]
    
    if message.author.bot:
        return
    if Mx != None:
        print(xMx + "→" + zMz + "→" + Mx)
    if message.content[:5] == 'g.みんと':
        if co5 == "":
            await message.channel.send(mint + "\n" + "ラウンジやれ")
            await message.channel.send(glaurl + "mintloungeyare.mp3")
        elif str(co5.isdigit()) == "True":
            for i in range(int(co5)):
                await message.channel.send(mint + "\n" + "ラウンジやれ")
            await message.channel.send(glaurl + "mintloungeyare.mp3")
        else:
            await message.channel.send("error")
    if message.content == 'みんと':
            await message.channel.send(mint + "\n" + "ラウンジやれ")
    if message.content == 'ドラゴン':
        
        zzz = random.choice(DRAzzz)
        
        if zzz == "SQ":
            title = "ラウンジSQ "
            SQ = random.choice(DRASQ)
            
            if SQ == "66":
                draunge = "ラウンジ 66SQ"
            else:
                draunge = title + SQ

        else:
            title = "ラウンジ"
            
            def loungedra():
                fg = random.choice(DRAf)
                if fg == "4":
                    fg = random.choice(DRA4)
                return (fg)
            
            draunge = title + loungedra()

            for i in range(zzz):
                
                fg = loungedra()
                
                draunge += "→" + fg

        await message.channel.send(draunge)

    if message.content == 'たんたんたいむ':
        await message.channel.send("https://www.maruchan.co.jp/products/search/maruchanseimencup_umakaratantanmen.html")
        await message.channel.send("https://www.amazon.co.jp/dp/B09CY8RY5D/ref=cm_sw_r_cp_api_i_7EZPEPRC3R86TG6YD9WB?_encoding=UTF8&psc=1")
    if message.content == 'めぅ':
        await message.channel.send("(˶ᵔᵕᵔ˶)")
    if message.content == 'きせのん':
        Xenon = ["イケメン","強い","学校いけ","きせのんうんこ","きせのんばか"]
        await message.channel.send(random.choice(Xenon))
    if message.content == 'ぶれす':
        await message.channel.send("合格！！")
    if message.content == "chocolate":
        latechoco = ["回線弱者","回線強者","回線強者","回線強者","回線強者"]
        await message.channel.send("チョコは"+random.choice(latechoco))
    if message.content == 'すえ':
        await message.channel.send("あ？貴様赤投げたろかこら")
    if message.content == 'マリンピア日本海': 
        await message.channel.send("スカイガーデン")
    if message.content == 'よし':
        await message.channel.send("お前らのマリオカートへのモチベーションはこんなものか！！！！学校、会社、冠婚葬祭全てを投げ出してこのゲームをやれ！！！" + "\n" + "すみません悪い妖精さんがでてきてしまいました、、")
    #if message.content == 'おはよう':
        #await message.channel.send(oha)
    if message.content == 'めぅめぅ':
        await message.channel.send("めめめめめめめ めうめうーっ！(」ﾟﾛﾟ)」めめめ めうめうーっ！(」ﾟﾛﾟ)」ﾟﾛﾟ)」ぺーったんぺったんぺったんぺったん だいすき～っ☆⌒ヽ('､＾)" + "\n" + "めめめめめめめ めうめうーっ！(」ﾟﾛﾟ)」めめめ めうめうーっ！(」ﾟﾛﾟ)」ﾟﾛﾟ)」ぺーったんぺったんぺったんぺったん だいすき～っ☆⌒ヽ('､＾)" + "\n" +"あいことばは" + "\n" + "もえおこし" + "\n" + "もえおこし" + "\n" + "M (/ ^∇^)/ O (^O^ ) K (/ ^O^)/ S (^∇^ )" + "\n" + "M (/ ^ω^)/ O (⁰▿⁰ ) K (/ ^0^)/ S (^ω^ )" + "\n" + "ぺたっとぺたっとぺたりこー!! わふー!!" + "\n" + "(˶ᵔᵕᵔ˶)(˶ᵔᵕᵔ˶)(˶ᵔᵕᵔ˶)(˶ᵔᵕᵔ˶)(˶ᵔᵕᵔ˶)")
    if Mx:
        """patha = path8
        pathb = message.content+".png"
        original_image_name = os.path.join(patha,pathb)
        
        copied_image_name = r"minimap/output.png"

        im = Image.open(original_image_name)

        copy_im = im.copy()
        draw = ImageDraw.Draw(copy_im)

        copy_im.save(copied_image_name)"""

        if CF:
            with open(pathC) as f:
                data = f.read()
                if data != "":
                    with open(pathC) as f:
                        for line in f:
                            pathl = str(line[:len(line)-1])
                            original_image_name = os.path.join(path8,path9)
        
                            copied_image_name = os.path.join(path1,pathl,path7)

                            im = Image.open(original_image_name)

                            copy_im = im.copy()
                            
                            draw = ImageDraw.Draw(copy_im)

                            copy_im.save(copied_image_name)
                    
                    await message.add_reaction("\N{ballot box with check}")

        if rCF and Mx != "none":
            with open(rpathC, "r") as f:
                data = f.readlines()[1]
            with open(rpathC, "r") as f:
                datalast = f.readlines()[-1]
            with open(rpathC, "r") as f:
                datahow = f.readlines()[0]
                datamany = datahow[5:]
                datatimes = str(int(datamany)-1)
            if data[:2] != "無し":
                if Mx+"\n" == data:
                    await message.channel.send("正解！")
                    if int(datamany) == 1:
                        await message.channel.send("おしまい！")
                        f = open(rpathC, 'w')

                        f.write("Track0" + "\n" + "無し" + "\n" +"回数")

                        f.close()

                    else:
                        await message.channel.send("あと"+datatimes+"問！")
                        f = open(rpathC, 'w')

                        f.write("Track" + datatimes + "\n" + rpathr + "\n" +"回数")

                        f.close()

                        await message.channel.send(file=discord.File(rTpath))
                        
                else:
                    if datalast == "4":
                        await message.channel.send("不正解")
                        await message.channel.send("正解は...")
                        await message.channel.send(data)
                        if int(datamany) == 1:
                            await message.channel.send("おしまい！")
                            f = open(rpathC, 'w')

                            f.write("Track0" + "\n" + "無し" + "\n" +"回数")

                            f.close()

                        else:
                            f = open(rpathC, 'w')

                            f.write("Track" + datatimes + "\n" + rpathr)

                            f.close()

                            await message.channel.send("あと" + datatimes + "問！")
                            await message.channel.send(file=discord.File(rTpath))

                    else:
                        if str(datalast.isdigit()) == "True":
                            f = open(rpathC, 'a')

                            f.write("\n" + str(int(datalast)+1))

                            f.close()

                        else:
                            f = open(rpathC, 'a')

                            f.write("\n"+str(1))

                            f.close()

                        await message.channel.send("不正解")

                                                          
    if message.content == "g.it":
        if UF:
            print(pathU+"は存在します")
        else:
            original = "UserID"
            shutil.copytree(original,pathU)

            f = open(pathUc, 'w')

            f.write(C)

            f.close()
               
            print(pathU+"を作成しました")
                
        if CF:
            print(pathC+"は存在します")
        else:
            f = open(pathC,"w")
            f.close()
            
            print(pathC+"を作成しました")
            
        with open(pathUc) as f:
            data = f.readlines()[0]
            if data == C:
                print("同じです")
                
            else:
                file_name = os.path.join(path4,data)+".py"

                with open(file_name) as f:
                    data_lines = f.read()

                data_lines = data_lines.replace(U+"\n","")

                with open(file_name,"w") as f:
                    f.write(data_lines)

                with open(pathC, 'a') as f:
                    print(Ux,file=f)

                f = open(pathUc, 'w')

                f.write(C)

                f.close()
                
                print("変更しました")
                        
        embed = discord.Embed(color=0x06e7ff)
        embed.add_field(name = "URL(" + mention + ")",value=glaurl + U + "/index.html")
        embed.set_footer(text="元画像:" + mkb)

        #await message.channel.send(f"{message.author.mention}",embed=embed)
        await message.channel.send(embed=embed)
        
    if message.content[:4] == "r.it":
        
        async def randomtrack():
            await message.channel.send(mkb)
            await message.channel.send(file=discord.File(rTpath))
        
        if co4 == ".stop":
            f = open(rpathC, 'w')

            f.write("Track0" + "\n" + "無し")

            f.close()

            await message.channel.send("終了しました")

        elif message.content == "r.it":
            f = open(rpathC, 'w')

            f.write("Track1" + "\n" + rpathr + "\n" +"回数")

            f.close()
            
            await randomtrack()

        elif str(co4.isdigit()) == "True":
            f = open(rpathC, 'w')

            f.write("Track0" + co4 + "\n" + rpathr + "\n" +"回数")

            f.close()
                    
            await randomtrack()
            
        else:
            await message.channel.send("error")

    if message.content == "おやすみ" and Cx == CHANNEL_ID:
        channel = client.get_channel(CHANNEL_ID)
        await channel.purge()
        await message.channel.send("おやすみ")

    if message.content == "チャンネル教えて":
        if UF:
            with open(pathUc) as f:
                data = f.readlines()[0]

            await message.channel.send("<#" + data + ">")

        else:
            await message.channel.send("g.itしてないよ")
            
    if message.content == "相談があるんだなも":
        danamo = random.choice(sae)
        if danamo == "だなも！！":
            if danamo == "だなも！！":
                zaurusu = "勝つ勝つメモメモみんなで食べるよ♪" + "\n" + "ツルツルテカテカ明日も晴れるかな♪"
            else:
                zaurusu = danamo
        else:
            zaurusu = danamo
        await message.channel.send(zaurusu)
        
    if message.content[:4] == "g.sq":
        xMx = xMx.replace("g.lt","").replace("`","")

        comsg = xMx.count(" MMR)\n")

        delgo = xMx[:xMx.find("Table:")]

        mem = delgo[delgo.find("\n1."):]

        for i in range(1,comsg+1):
            mem = mem.replace(str(i)+". ","")
            mmrst = mem.find("(")
            mmrgo = mem.find(" MMR)")
            mmr = mem[:mmrgo][mmrst+1:]
            mem = mem.replace(" ("+mmr+" MMR)\n",", ")

        score = "!submit "+str(int(12/comsg))+" sq"

        mem = mem.replace(", "," 0\n")

        submit = score + mem
        
        await message.channel.send(submit)

        
client.run(TOKEN)
