import discord
import random
from PIL import Image
from PIL import ImageFont, ImageDraw
import os
import shutil
import time


TOKEN = 'TOKEN'

CHANNEL_ID = xxx

DRAzzz = ["1","1","2","2","2","2","3","3","3","3","3","4","4","5","SQ","SQ","SQ"]
DRASQ = ["2v2","2v2","2v2","3v3","3v3","4v4","66","66"]
DRAf = ["FFA","FFA","FFA","FFA","FFA","FFA","FFA","FFA","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","2v2","3v3","3v3","3v3","3v3","3v3","3v3","3v3","3v3","3v3","3v3","4"]
DRA4 = ["4v4","4v4","4v4","4v4","6v6"]
Track = ["none", "MKS", "WP", "SSC", "TR", "MC", "TH", "TM", "SGF", "SA", "DS", "Ed", "MW", "CC", "BDD", "BC", "RR", "rMMM", "rMC", "rCCB", "rTT", "rDDD", "rDP3", "rRRy", "rDKJ", "rWS", "rSL", "rMP", "rYV", "rTTC", "rPPS", "rGV", "rRRd", "dYC", "dEA", "dDD", "dMC", "dWGM", "dRR", "dIIO", "dHC", "dBP", "dCL", "dWW", "dAC", "dNBC", "dRiR", "dSBS", "dBB", "bPP", "bTC", "bCMo", "bCMa", "bTB", "bSR", "bSG", "bNH"]
rTrack = ["MKS", "WP", "SSC", "TR", "MC", "TH", "TM", "SGF", "SA", "DS", "Ed", "MW", "CC", "BDD", "BC", "RR", "rMMM", "rMC", "rCCB", "rTT", "rDDD", "rDP3", "rRRy", "rDKJ", "rWS", "rSL", "rMP", "rYV", "rTTC", "rPPS", "rGV", "rRRd", "dYC", "dEA", "dDD", "dMC", "dWGM", "dRR", "dIIO", "dHC", "dBP", "dCL", "dWW", "dAC", "dNBC", "dRiR", "dSBS", "dBB", "bPP", "bTC", "bCMo", "bCMa", "bTB", "bSR", "bSG", "bNH"]

client = discord.Client()

async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("毎度 :raised_hand: おはおはござうるす♪")

@client.event
async def on_ready():
    print('ログインしました')
    await greet()

@client.event
async def on_message(message):
    Mx = message.content
    Ux = message.author.id
    Cx = message.channel.id
    M = str(Mx)
    U = str(Ux)
    C = str(Cx)
    path1 = "User"
    path2 = U
    path3 = "input.py"
    path4 = "channel"
    path5 = C+".py"
    path6 = "User"
    path7 = "output.png"
    path8 = "minimap\image"
    path9 = message.content+".png"
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
    pathD = "DRAlounge.py"
    
    if message.author.bot:
        return
    if message.content[:5] == 'g.みんと':
        if message.content[5:] == "":
            await message.channel.send("<@734030898177245195>" + "\n" + "ラウンジやれ")
        else:
            if str(message.content[5:].isdigit()) == "True":
                for i in range(int(message.content[5:])):
                    await message.channel.send("<@734030898177245195>" + "\n" + "ラウンジやれ")

    if message.content == 'みんと':
            await message.channel.send("<@734030898177245195>" + "\n" + "ラウンジやれ")
    if message.content == 'ドラゴン':
        zzz = random.choice(DRAzzz)
        if zzz == "SQ":
            title = "ラウンジSQ "
            SQ = random.choice(DRASQ)
            if SQ == "66":
                copy = "ラウンジ 66SQ"
            else:
                copy = title + SQ

            await message.channel.send(copy)
        else:
            title = "ラウンジ"
            fg = random.choice(DRAf)
            if fg == "4":
                fz = randomchoice(DRA4)
            else:
                fz = fg

            f = open(pathD, 'w')

            f.write(title + fz)

            f.close()

            for i in range(int(zzz)-1):

                with open(pathD) as f:
                    data = f.readlines()[0]

                fg = random.choice(DRAf)
                if fg == "4":
                    fz = randomchoice(DRA4)
                else:
                    fz = fg
                
                f = open(pathD, 'w')

                f.write(data + "→" + fz)

                f.close()

            with open(pathD) as f:
                data = f.readlines()[0]

            await message.channel.send(data)

    if message.content == 'たんたんたいむ':
        await message.channel.send("https://www.maruchan.co.jp/products/search/maruchanseimencup_umakaratantanmen.html")
        await message.channel.send("https://www.amazon.co.jp/dp/B09CY8RY5D/ref=cm_sw_r_cp_api_i_7EZPEPRC3R86TG6YD9WB?_encoding=UTF8&psc=1")
    if message.content == 'めぅ':
        await message.channel.send("(˶ᵔᵕᵔ˶)")
    if message.content == 'きせのん':
        Xenon = ["イケメン","強い","学校いけ","きせのんうんこ"]
        await message.channel.send(random.choice(Xenon))
    if message.content == 'ぶれす':
        await message.channel.send("合格！！")
    if message.content == "チョコ":
        kuji = ["回線弱者","回線強者","回線強者","回線強者","回線強者"]
        await message.channel.send("チョコは"+random.choice(kuji))
    if message.content == 'すえ':
        await message.channel.send("あ？貴様赤投げたろかこら")
    if message.content == 'マリンピア日本海': 
        await message.channel.send("スカイガーデン")
    if message.content == 'よし':
        await message.channel.send("お前らのマリオカートへのモチベーションはこんなものか！！！！学校、会社、冠婚葬祭全てを投げ出してこのゲームをやれ！！！" + "\n" + "すみません悪い妖精さんがでてきてしまいました、、")
    if message.content == 'おはよう':
        await message.channel.send('毎度 :raised_hand: おはおはござうるす♪')
    if message.content == 'めぅめぅ':
        await message.channel.send("めめめめめめめ めうめうーっ！(」ﾟﾛﾟ)」めめめ めうめうーっ！(」ﾟﾛﾟ)」ﾟﾛﾟ)」ぺーったんぺったんぺったんぺったん だいすき～っ☆⌒ヽ('､＾)" + "\n" + "めめめめめめめ めうめうーっ！(」ﾟﾛﾟ)」めめめ めうめうーっ！(」ﾟﾛﾟ)」ﾟﾛﾟ)」ぺーったんぺったんぺったんぺったん だいすき～っ☆⌒ヽ('､＾)" + "\n" +"あいことばは" + "\n" + "もえおこし" + "\n" + "もえおこし" + "\n" + "M (/ ^∇^)/ O (^O^ ) K (/ ^O^)/ S (^∇^ )" + "\n" + "M (/ ^ω^)/ O (⁰▿⁰ ) K (/ ^0^)/ S (^ω^ )" + "\n" + "ぺたっとぺたっとぺたりこー!! わふー!!" + "\n" + "(˶ᵔᵕᵔ˶)(˶ᵔᵕᵔ˶)(˶ᵔᵕᵔ˶)(˶ᵔᵕᵔ˶)(˶ᵔᵕᵔ˶)")
    if message.content in Track:
        print("コース名を確認しました")
        patha = "minimap\image"
        pathb = message.content+".png"
        original_image_name = os.path.join(patha,pathb)
        
        copied_image_name = r"minimap\output.png"

        im = Image.open(original_image_name)

        copy_im = im.copy()
        draw = ImageDraw.Draw(copy_im)

        copy_im.save(copied_image_name)

        if CF:
                with open(pathC) as f:
                    for line in f:
                        pathl = str(line[:18])
                        original_image_name = os.path.join(path8,path9)
        
                        copied_image_name = os.path.join(path6,pathl,path7)

                        im = Image.open(original_image_name)

                        copy_im = im.copy()
                        draw = ImageDraw.Draw(copy_im)

                        copy_im.save(copied_image_name)

        if rCF:
            if message.content != "none":
                with open(rpathC) as f:
                    data = f.readlines()[1]
                with open(rpathC, 'r') as f:
                    datalast = f.readlines()[-1]
                with open(rpathC, 'r') as f:
                    datahow = f.readlines()[0]
                    datamany = datahow[5:]
                    datatimes = str(int(datamany)-1)
                if data[:2] != "無し":
                    if message.content+"\n" == data:
                        await message.channel.send("正解！")
                        if int(datamany) == 1:                            
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
                            print(data)
                            await message.channel.send("不正解")
                            await message.channel.send("正解は...")
                            await message.channel.send(data)
                            if int(datamany) == 1:                               
                                f = open(rpathC, 'w')

                                f.write("Track0" + "\n" + "無し" + "\n" +"回数")

                                f.close()

                            else:
                                print(datahow)
                                print(datamany)
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
            original = "channelid.py"
            shutil.copy(original,pathC)
            print(pathC+"を作成しました")
            
            
        with open(pathUc) as f:
            data = f.readlines()[0]
            if data == C:
                print("同じです")
                with open(pathC, 'a') as f:
                    print(Ux,file=f)
            else:
                print("変更しました")
                file_name = os.path.join(path4,data)+".py"

                with open(file_name, encoding="cp932") as f:
                    data_lines = f.read()

                data_lines = data_lines.replace(U+"\n","")

                with open(file_name, mode="w", encoding="cp932") as f:
                    f.write(data_lines)

                with open(pathC, 'a') as f:
                    print(Ux,file=f)

                f = open(pathUc, 'w')

                f.write(C)

                f.close()
    if message.content[:4] == "r.it":
        if message.content[4:] == ".stop":
            f = open(rpathC, 'w')

            f.write("Track0" + "\n" + "無し")

            f.close()

            await message.channel.send("終了しました")

        else:
            await message.channel.send("http://japan-mk.blog.jp/mk8dx.info-4")
            
            if message.content == "r.it":
                f = open(rpathC, 'w')

                f.write("Track1" + "\n" + rpathr + "\n" +"回数")

                f.close()

            else:
                if str(message.content[4:].isdigit()) == "True":
                    f = open(rpathC, 'w')

                    f.write("Track0" + str(message.content[4:]) + "\n" + rpathr + "\n" +"回数")

                    f.close()
                
            await message.channel.send(file=discord.File(rTpath))
        
        
client.run(TOKEN)
