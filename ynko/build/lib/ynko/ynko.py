def func2():
    print('puripuri')
    # Script2.py executed as script
    # do something

def bot():
    import os
    print(os.getcwd())
    import subprocess
    import os
    print(os.getcwd())
    import time
    import discord
    import random
    import asyncio
    import requests, bs4
    import sys
    from ynko.ynko import ynko

    ynko.func2()

    # 自分のBotのアクセストークンに置き換えてください
    # 読込むファイルのパスを宣言する
    file_name = "./token.txt"
    data = None
    try:
        file = open(file_name)
        data = file.read()
        print(data)
        file.close()
    except Exception as e:
        print(e)

    # 接続に必要なオブジェクトを生成
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    # 起動時に動作する処理
    @client.event
    async def on_ready():
        # 起動したらターミナルにログイン通知が表示される
        print('----------------')
        print('ログインしました')
        print('----------------')
        print('')
        print('BOT表示名：', client.user.name)  # Botの名前
        print('BOTのID：', client.user.id)  # ID
        print('Dicord.pyのバージョン：', discord.__version__)
        ch = client.get_channel(947469205538762812)
        print('')
        guild_count = len(client.guilds)
        game = discord.Game(f'ただいま起動しました')
        await client.change_presence(activity=discord.Game(name=str(game)))
        time.sleep(3)
        game = discord.Game(f'{guild_count} サーバーに導入されています')
        await client.change_presence(activity=discord.Game(name=str(game)))
        print('ログインしました {0.user}'.format(client))
        await ch.send("`BOTが起動しました！`")

    # メッセージ受信時に動作する処理
    @client.event
    async def on_message(message):
        guild_count = len(client.guilds)
        game = discord.Game(f'{guild_count} サーバーに導入されています')
        await client.change_presence(activity=discord.Game(name=str(game)))
        # メッセージ送信者がBotだった場合は無視する

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!boturl':
            print('メッセージを確認')
            embed = discord.Embed(title="BOT導入URL",
                                  description='`通常導入URL`' + '\n' + 'https://discord.com/api/oauth2/authorize?client_id=924945655414267934&permissions=536807472375&scope=bot%20applications.commands' + '\n' + '`BOTが正常に動作しない場合`' + '\n' + 'https://discord.com/api/oauth2/authorize?client_id=924945655414267934&permissions=8&scope=bot')
            await message.channel.send(embed=embed)
            print('メッセージを送りました')
            print(message.content)

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!help':
            print('メッセージを確認')
            msg = '`開発段階のコマンドのヘルプを表示`' + '\n' + 'spb!testhelp' + '\n' + '`サーバーの招待URL（LINK）を作成または取得`' + '\n' + 'spb!invitelink' + '\n' + '`今後の予定を表示`' + '\n' + 'spb!update' + '\n' + '`ヘルプを表示`' + '\n' + 'spb!help' + '\n' + '`BOTの導入URLを表示`' + '\n' + 'spb!boturl' + '\n' + '`グローバルチャット機能`' + '\n' + '[hrk_グローバルチャット] という名前のテキストチャンネルを作成してください' + '\n' + 'それだけでグローバルチャットが使えるようになります' + '\n' + 'ただしプライベートチャンネルに設定した際は権限設定でチャンネルを表示する権限をBOTに与えてください' + '\n' + '`チャットログ作成機能`' + '\n' + '[ログ_hrk] という名前のテキストチャンネルを作成してください' + '\n' + 'それだけでログ機能が使えるようになります' + '\n' + 'ただしプライベートチャンネルに設定した際は権限設定でチャンネルを表示する権限をBOTに与えてください '
            embed = discord.Embed(title="ボットコマンド", description=msg)
            await message.channel.send(embed=embed)

            print(message.content)
            print('メッセージを送りました')

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!re':
            setmsg = message.author.id
            print(setmsg)
            if setmsg == 812275752904163358:
                # 改良版
                ch = client.get_channel(947469205538762812)
                await ch.send("`BOTを再起動＆ボットを更新します`")
                game = discord.Game(f'再起動まで数秒お待ちください....')
                await client.change_presence(activity=discord.Game(name=str(game)))
                game = discord.Game(f'起動まで数分お待ちください....')
                channel = message.channel
                await channel.send(f'{message.author.mention}さん、コマンドを受け付けました！' + '\n' + '`ボットを再起動します`')
                time.sleep(15)
                await client.change_presence(activity=discord.Game(name=str(game)))
                proc = subprocess.Popen(['python3', '6.py'])
                proc.poll()
                await client.logout()
                exit()

                # 変更前
                guild_count = len(client.guilds)
                ch = client.get_channel(947469205538762812)
                await ch.send("`BOTを再起動＆ボットを更新します`")
                game = discord.Game(f'再起動中です....')
                await client.change_presence(activity=discord.Game(name=str(game)))
                proc = subprocess.Popen(['python3', '1.py'])
                await client.logout()
                proc.poll()
                exit()

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!down':
            setmsg = message.author.id
            print(setmsg)
            if setmsg == 812275752904163358:
                ch = client.get_channel(947469205538762812)
                await ch.send("`BOTをシャットダウンします`")
                game = discord.Game(f'BOTは停止中です、起動までお待ちください')
                await client.change_presence(activity=discord.Game(name=str(game)))
                channel = message.channel
                await channel.send(f'{message.author.mention}さん、コマンドを受け付けました！' + '\n' + '`ボットをシャットダウンします`')
                proc = subprocess.Popen(['python3', '停止中専用.py'])
                proc.poll()
                await client.logout()
                exit()

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!vr':
            msg = "バージョン 1.9.8 早期リリース"
            embed = discord.Embed(title="ベータ版コマンド：ボットバージョン", description=msg)
            await message.channel.send(embed=embed)

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!info':
            msg = (
                    '`バージョン`' + '\n' + 'バージョン 1.9.6 早期リリース' + '\n' + '`通常導入URL`' + '\n' + 'https://discord.com/api/oauth2/authorize?client_id=924945655414267934&permissions=536807472375&scope=bot%20applications.commands' + '\n' + '`BOTが正常に動作しない場合`' + '\n' + 'https://discord.com/api/oauth2/authorize?client_id=924945655414267934&permissions=8&scope=bot')
            embed = discord.Embed(title="ベータ版コマンド：ボットの詳細", description=msg)
            await message.channel.send(embed=embed)

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!spam':
            if message.author.guild_permissions.administrator:
                msg = "スパムをしようとしたやつは誰だ～ ＾_＾"
                embed = discord.Embed(title="スパムは禁止されています", description=msg)
                await message.channel.send(embed=embed)

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!update':
            msg = "`ボットの機能追加`" + "\n" + "JS版 / コマンドでのコマンド実装" + "\n" + "`バグ修正`" + "\n" + "極秘（アップデート後に通知します）"
            embed = discord.Embed(title="今後の予定", description=msg)
            await message.channel.send(embed=embed)

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!testhelp':
            print('メッセージを確認')
            msg = '`コマンドの使用方法を表示します`' + '\n' + 'spb!usecmdhelp' + '`指定した人をキックします`' + 'spb!kick' + '\n' + '`指定した人をBANをします`' + '\n' + 'spb!ban' + '\n' + '`指定した人にDMにメッセージを送ります`' + '\n' + 'spb!senddm' + '\n' + '`指定した人のBANを解除します`' + '\n' + 'spb!unban' + '\n' + '`GBANされている人をリスト形式で表示（開発者のみ）`' + '\n' + 'spb!gbanlist' + '\n' + '`BOTのコンソールのログをリセット（開発者のみ）`' + '\n' + 'spb!clear' + '\n' + '`サーバー認証機能（開発段階）`' + '\n' + 'spb!info' + '\n' + '`ボットの詳細を表示`' + '\n' + 'spb!verify' + '\n' + '`ボットを再起動（開発者のみ）`' + '\n' + 'spb!re' + '\n' + '`ボットをシャットダウン（開発者のみ）`' + '\n' + 'spb!down' + '\n' + '`ボットのバージョン情報`' + '\n' + 'spb!vr'
            embed = discord.Embed(title="ボット開発中＆開発者専用コマンド", description=msg)
            await message.channel.send(embed=embed)

            print(message.content)
            print('メッセージを送りました')

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!verify':

            passseta = random.randint(11111111, 9999999999)
            passsetb = random.randint(11111111, 9999999999)
            passsetc = random.randint(11111111, 9999999999)
            passsetd = random.randint(11111111, 9999999999)
            passsete = random.randint(11111111, 9999999999)
            print(passseta)
            print(passsetb)
            print(passsetc)
            print(passsetd)
            print(passsete)
            passlock = passseta * passsetb * passsetc - passsetd - passsete
            channel = message.channel
            await channel.send("認証コードを３０秒以内に送ってください")
            await channel.send(str('`認証コード : `') + str(passlock))
            file_nameaa = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(message.author.id)
            file12 = open(file_nameaa, 'w')
            file12.write(str(passlock))
            file12.close()
            file12 = open(file_nameaa)
            file12.close()

            # 待っているものに該当するかを確認する関数
            def check(m):
                # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                # コマンドを打ったチャンネルという条件
                path = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(message.author.id)
                file_name = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(message.author.id)
                f = open(path)
                file = open(file_name)
                data = file.read()
                print(data)
                file.close()
                file = open(file_name)
                file.close()
                return m.content == data and m.channel == channel

            try:
                # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                msg = await client.wait_for('message', check=check, timeout=30)
                # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

            # asyncio.TimeoutError が発生したらここに飛ぶ
            except asyncio.TimeoutError:
                await channel.send(f'{message.author.mention}さん、認証時間切れです')
            else:
                # メンション付きでメッセージを送信する。
                await channel.send(f'{msg.author.mention}さん、認証は成功しました')
        if message.author.bot:
            return
        if message.content == 'spb!BOTアクティベート':

            passseta = random.randint(11111111, 9999999999)
            passsetb = random.randint(11111111, 9999999999)
            passsetc = random.randint(11111111, 9999999999)
            passsetd = random.randint(11111111, 9999999999)
            passsete = random.randint(11111111, 9999999999)
            print(passseta)
            print(passsetb)
            print(passsetc)
            print(passsetd)
            print(passsete)
            passlock = passseta * passsetb * passsetc - passsetd - passsete
            channel = message.channel
            await channel.send("すべてのメッセージを３０秒以内に送ってください(`そうしないとタイムアウトします`)")
            await channel.send(str('`認証コード : `') + str(passlock))
            path = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(message.author.id)
            file_name = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(message.author.id)
            file = open(file_name, 'w')
            file.write(str(passlock))
            file.close()
            file = open(file_name)
            file.close()

            # 待っているものに該当するかを確認する関数
            def check(m):
                if not message.author.bot:
                    # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                    # コマンドを打ったチャンネルという条件
                    path = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(message.author.id)
                    file_name = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(
                        message.author.id)
                    f = open(path)
                    file = open(file_name)
                    data = file.read()
                    print(data)
                    file.close()
                    file = open(file_name)
                    file.close()
                    return m.content == data and m.channel == channel

            try:
                # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                msg = await client.wait_for('message', check=check, timeout=30)
                # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

            # asyncio.TimeoutError が発生したらここに飛ぶ
            except asyncio.TimeoutError:
                await channel.send(f'{message.author.mention}さん、認証時間切れです')
            else:
                # メンション付きでメッセージを送信する。
                await channel.send(f'{msg.author.mention}さん、認証は成功しました')
                await channel.send(f'`ユーザー名を入力してください`')

                # 待っているものに該当するかを確認する関数
                def check(m):
                    if not message.author.bot:
                        # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                        # コマンドを打ったチャンネルという条件
                        path = str('./アカウント/') + str(message.author.id)
                        file_name = str('./アカウント/') + str(message.author.id)
                        f = open(path)
                        file = open(file_name)
                        data = file.read()
                        print(data)
                        file.close()
                        file = open(file_name)
                        file.close()
                        return m.content == data and m.channel == channel

                try:
                    # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                    msg = await client.wait_for('message', check=check, timeout=30)
                    # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                    # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                    # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

                # asyncio.TimeoutError が発生したらここに飛ぶ
                except asyncio.TimeoutError:
                    await channel.send(f'{message.author.mention}さん、認証時間切れです')
                else:
                    # メンション付きでメッセージを送信する。

                    # 待っているものに該当するかを確認する関数
                    await channel.send(f'{msg.author.mention}さん、パスワードを入力してください')

                    def check(m):
                        if not message.author.bot:
                            # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                            # コマンドを打ったチャンネルという条件
                            path = str('./アカウント/パスワード/') + str(message.author.id)
                            file_name = str('./アカウント/パスワード/') + str(message.author.id)
                            f = open(path)
                            file = open(file_name)
                            data = file.read()
                            print(data)
                            file.close()
                            file = open(file_name)
                            file.close()
                            return m.content == data and m.channel == channel
                        return

                    try:
                        # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                        msg = await client.wait_for('message', check=check, timeout=30)
                        # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                        # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                        # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

                    # asyncio.TimeoutError が発生したらここに飛ぶ
                    except asyncio.TimeoutError:
                        await channel.send(f'{message.author.mention}さん、認証時間切れです')
                    else:
                        # メンション付きでメッセージを送信する。
                        await channel.send(f'{msg.author.mention}さん、ログインは成功しました')
                        res = requests.get('https://LicensSever6295ee.harumaki.repl.co')
                        res.raise_for_status()
                        soup = bs4.BeautifulSoup(res.text, "html.parser")
                        elems = soup.select('#list h2')
                        key = None
                        for elem in elems:
                            key = elem.getText()

                        res = requests.get(key)
                        res.raise_for_status()
                        soup = bs4.BeautifulSoup(res.text, "html.parser")
                        elems = soup.select('#list h2')
                        for elem in elems:
                            key = elem.getText()

                        res = requests.get(key)
                        res.raise_for_status()
                        soup = bs4.BeautifulSoup(res.text, "html.parser")
                        elems = soup.select('#list h2')
                        for elem in elems:
                            key = elem.getText()
                            await channel.send(f'`ライセンスキーを入力してください:`')

                            # 待っているものに該当するかを確認する関数
                            def check(m):
                                if not message.author.bot:
                                    # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                                    # コマンドを打ったチャンネルという条件
                                    new_dir_path_recursive = str('./ボット-データ/') + str(message.author.id)
                                    os.makedirs(new_dir_path_recursive, exist_ok=True)
                                    new_dir_path_recursive = str('./ボット-データ/') + str(message.author.id) + ('/カウント')
                                    os.makedirs(new_dir_path_recursive, exist_ok=True)

                                    path = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str('導入カウント')
                                    is_file = os.path.isfile(path)
                                    if is_file:
                                        file = "OK"
                                    else:
                                        # パスが存在しないかファイルではない
                                        path = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str(
                                            '導入カウント')
                                        f = open(path, 'w')
                                        f.write('0')  # 何も書き込まなくてファイルは作成されました
                                        f.close()

                                    path = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str('導入可能制限')
                                    is_file = os.path.isfile(path)
                                    if is_file:
                                        file = "0"
                                    else:
                                        # パスが存在しないかファイルではない
                                        path = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str(
                                            '導入可能制限')
                                        f = open(path, 'w')
                                        f.write('5')  # 何も書き込まなくてファイルは作成されました
                                        f.close()
                                    print(key)
                                    return m.channel == channel and key == m.content
                                return

                            try:
                                msg = await client.wait_for('message', check=check, timeout=30)
                                # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                                # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                                # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                                # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

                            # asyncio.TimeoutError が発生したらここに飛ぶ
                            except asyncio.TimeoutError:
                                await channel.send(f'{message.author.mention}さん、認証時間切れです')
                            else:
                                await channel.send(f'{msg.author.mention}さん、ライセンスキーの確認に成功しました')
                                await channel.send("`アクティベートするサーバーIDを教えてください`")

                                # 待っているものに該当するかを確認する関数
                                def check(m):
                                    if not message.author.bot:
                                        # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                                        # コマンドを打ったチャンネルという条件
                                        channel = message.channel

                                        new_dir_path_recursive = str('./一時フォルダ/') + str(message.author.id)
                                        os.makedirs(new_dir_path_recursive, exist_ok=True)

                                        path = str('./一時フォルダ/') + str(message.author.id) + ('/一時ファイル')
                                        is_file = os.path.isfile(path)
                                        if is_file:
                                            file = "OK"
                                        else:
                                            # パスが存在しないかファイルではない
                                            path = str('./一時フォルダ/') + str(message.author.id) + ('/一時ファイル')
                                            f = open(path, 'w')
                                            f.write('')  # 何も書き込まなくてファイルは作成されました
                                            f.close()

                                        path = str('./一時フォルダ/') + str(message.author.id) + ('/一時ファイル')
                                        f = open(path, 'w')
                                        f.write(m.content)  # 何も書き込まなくてファイルは作成されました
                                        f.close()
                                        if not message.author.bot:
                                            return m.channel == channel
                                    return

                                try:
                                    # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                                    msg = await client.wait_for('message', check=check, timeout=30)
                                    # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                                    # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                                    # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

                                # asyncio.TimeoutError が発生したらここに飛ぶ
                                except asyncio.TimeoutError:
                                    await channel.send(f'{message.author.mention}さん、認証時間切れです')
                                else:
                                    # メンション付きでメッセージを送信する。

                                    path = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str('導入カウント')
                                    file_name = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str(
                                        '導入カウント')
                                    f = open(path)
                                    file = open(file_name)
                                    count = file.read()
                                    print(count)
                                    file.close()

                                    path = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str('導入可能制限')
                                    file_name = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str(
                                        '導入可能制限')
                                    f = open(path)
                                    file = open(file_name)
                                    count2 = file.read()
                                    print(count2)
                                    file.close()

                                    path = str('./一時フォルダ/') + str(message.author.id) + ('/一時ファイル')
                                    file_name = str('./一時フォルダ/') + str(message.author.id) + ('/一時ファイル')
                                    f = open(path)
                                    file = open(file_name)
                                    count3 = file.read()
                                    print(count)
                                    file.close()

                                    path = str('./許可サーバーリスト/') + str(count3)
                                    is_file = os.path.isfile(path)
                                    if is_file:
                                        channel = message.channel
                                        await channel.send(f'{msg.author.mention}さん、そのサーバーのBOTはすでにアクティベートされています')
                                    else:
                                        # パスが存在しないかファイルではない
                                        if count <= count2 and not count == count2:
                                            passlock = str(message.author.id)
                                            channel = message.channel
                                            path = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str(
                                                '導入カウント')
                                            file_name = str('./ボット-データ/') + str(message.author.id) + str(
                                                '/カウント/') + str(
                                                '導入カウント')
                                            file = open(file_name, 'w')
                                            str1 = str(count)
                                            (str32e) = int(count) + int(1)
                                            file.write(str(str32e))
                                            file.close()
                                            file = open(file_name)
                                            file.close()

                                            passlock = str(message.author.id)
                                            channel = message.channel
                                            path = str('./許可サーバーリスト/') + str(count3)
                                            file_name = str('./許可サーバーリスト/') + str(count3)
                                            file = open(file_name, 'w')
                                            file.write(str(count3))
                                            file.close()
                                            file = open(file_name)
                                            file.close()

                                            passlock = str(message.author.id)
                                            channel = message.channel
                                            path = str('./ボット-データ/') + str(message.author.id) + str("/") + str(count3)
                                            file_name = str('./ボット-データ/') + str(message.author.id) + str("/") + str(
                                                count3)
                                            file = open(file_name, 'w')
                                            file.write(str(count3))
                                            file.close()
                                            file = open(file_name)
                                            file.close()
                                            await channel.send(
                                                f'{msg.author.mention}さん、サーバーID : ' + count3 + ' のサーバーをアクティベートしました')
                                            print("BOTのアクティベートが完了しました")
                                        else:
                                            await channel.send(
                                                f'{msg.author.mention}さん、BOTのアクティベートができません。' + '\n' + '導入制限の : ' + count2 + (
                                                    ' になっています。追加するにはプランを変更する、またはほかのサーバーのアクティベートを削除してください'))
                                            print("BOTのアクティベートができません")

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!BOTアンアクティベート':
            messagesenduser = message.author.id
            passseta = random.randint(11111111, 9999999999)
            passsetb = random.randint(11111111, 9999999999)
            passsetc = random.randint(11111111, 9999999999)
            passsetd = random.randint(11111111, 9999999999)
            passsete = random.randint(11111111, 9999999999)
            print(passseta)
            print(passsetb)
            print(passsetc)
            print(passsetd)
            print(passsete)
            passlock = passseta * passsetb * passsetc - passsetd - passsete
            channel = message.channel
            await channel.send("すべてのメッセージを３０秒以内に送ってください(`そうしないとタイムアウトします`)")
            await channel.send(str('`認証コード : `') + str(passlock))
            path = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(message.author.id)
            file_name = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(message.author.id)
            file = open(file_name, 'w')
            file.write(str(passlock))
            file.close()
            file = open(file_name)
            file.close()
            a89 = message.author.id

            # 待っているものに該当するかを確認する関数
            def check(m):
                if not message.author.bot and messagesenduser == m.author.id:
                    # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                    # コマンドを打ったチャンネルという条件
                    path = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(message.author.id)
                    file_name = str('./一時フォルダ/') + str(message.guild.id) + str(message.channel.id) + str(
                        message.author.id)
                    f = open(path)
                    file = open(file_name)
                    data = file.read()
                    print(data)
                    file.close()
                    file = open(file_name)
                    file.close()
                    return m.content == data and m.channel == channel
                return

            try:
                # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                msg = await client.wait_for('message', check=check, timeout=30)
                # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

            # asyncio.TimeoutError が発生したらここに飛ぶ
            except asyncio.TimeoutError:
                await channel.send(f'{message.author.mention}さん、認証時間切れです')
            else:
                # メンション付きでメッセージを送信する。
                await channel.send(f'{msg.author.mention}さん、認証は成功しました')
                await channel.send(f'`ユーザー名を入力してください`')

                # 待っているものに該当するかを確認する関数
                a89 = message.author.id

                # 待っているものに該当するかを確認する関数
                def check(m):
                    if not message.author.bot and messagesenduser == m.author.id:
                        # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                        # コマンドを打ったチャンネルという条件
                        path = str('./アカウント/') + str(message.author.id)
                        file_name = str('./アカウント/') + str(message.author.id)
                        f = open(path)
                        file = open(file_name)
                        data = file.read()
                        print(data)
                        file.close()
                        file = open(file_name)
                        file.close()
                        return m.content == data and m.channel == channel
                    return

                try:
                    # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                    msg = await client.wait_for('message', check=check, timeout=30)
                    # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                    # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                    # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

                # asyncio.TimeoutError が発生したらここに飛ぶ
                except asyncio.TimeoutError:
                    await channel.send(f'{message.author.mention}さん、認証時間切れです')
                else:
                    # メンション付きでメッセージを送信する。

                    # 待っているものに該当するかを確認する関数
                    await channel.send(f'{msg.author.mention}さん、パスワードを入力してください')

                    a89 = message.author.id

                    # 待っているものに該当するかを確認する関数
                    def check(m):
                        if not message.author.bot and messagesenduser == m.author.id:
                            # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                            # コマンドを打ったチャンネルという条件
                            path = str('./アカウント/パスワード/') + str(message.author.id)
                            file_name = str('./アカウント/パスワード/') + str(message.author.id)
                            f = open(path)
                            file = open(file_name)
                            data = file.read()
                            print(data)
                            file.close()
                            file = open(file_name)
                            file.close()
                            return m.content == data and m.channel == channel
                        return

                    try:
                        # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                        msg = await client.wait_for('message', check=check, timeout=30)
                        # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                        # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                        # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

                    # asyncio.TimeoutError が発生したらここに飛ぶ
                    except asyncio.TimeoutError:
                        await channel.send(f'{message.author.mention}さん、認証時間切れです')
                    else:
                        # メンション付きでメッセージを送信する。
                        await channel.send(f'{msg.author.mention}さん、ログインは成功しました')

                        await channel.send('`アンアクティベートするサーバーID`')

                        a89 = message.author.id

                        # 待っているものに該当するかを確認する関数
                        def check(m):
                            msgda = m.content
                            if not message.author.bot and messagesenduser == m.author.id:
                                # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                                # コマンドを打ったチャンネルという条件
                                path = (str('./ボット-データ/') + str(message.author.id) + str("/") + str(m.content))
                                print(path)
                                is_file = os.path.isfile(path)
                                msga = m.content
                                if is_file:
                                    # パスが存在しないかファイルではない
                                    path = str('./一時フォルダ/') + str(message.author.id) + ('/一時ファイル')
                                    f = open(path, 'w')
                                    f.write('ok')  # 何も書き込まなくてファイルは作成されました
                                    f.close()

                                    path = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str('導入カウント')
                                    file1_name = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str(
                                        '導入カウント')
                                    f = open(path)
                                    file1 = open(file1_name)
                                    count = str(file1.read())
                                    print(count)
                                    file1.close()
                                    file1 = open(file1_name)
                                    file1.close()
                                    # 必要に応じて有効化 by MCCbena
                                    #                                passlock = str(message.author.id)
                                    #                                channel = message.channel
                                    #                                path = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str('導入カウント')
                                    file_name = str('./ボット-データ/') + str(message.author.id) + str('/カウント/') + str(
                                        '導入カウント')
                                    file = open(file_name, 'w')
                                    (str32e) = int(count) - int(1)
                                    file.write(str(str32e))
                                    file.close()
                                    file = open(file_name)
                                    file.close()
                                    file.close()

                                    path1a = (str('./ボット-データ/') + str(message.author.id) + str("/") + str(msgda))
                                    os.remove(str('./ボット-データ/') + str(message.author.id) + str("/") + str(msgda))
                                    print("here" + path1a)

                                    path1a = (str('./許可サーバーリスト/') + str(msgda))
                                    os.remove(str('./許可サーバーリスト/') + str(msgda))
                                    print("here" + path1a)
                                else:
                                    path = str('./一時フォルダ/') + str(message.author.id) + ('/一時ファイル')
                                    f = open(path, 'w')
                                    f.write("ok12")  # 何も書き込まなくてファイルは作成されました
                                    f.close()

                            channel = message.channel
                            return not m.channel == channel

                        try:
                            # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                            msg = await client.wait_for('message', check=check, timeout=30)
                            # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                            # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

                        # asyncio.TimeoutError が発生したらここに飛ぶ
                        except asyncio.TimeoutError:
                            await channel.send(f'{msg.author.mention}さん、タイムアウトしました')
                        else:
                            # メンション付きでメッセージを送信する。
                            path = str('./一時フォルダ/') + str(message.author.id) + str('/一時ファイル')
                            file_name21 = str('./一時フォルダ/') + str(message.author.id) + '/一時ファイル'
                            f = open(path)
                            file1 = open(file_name21)
                            severid1 = file1.read()
                            print(severid1)
                            file1.close()
                            file1 = open(file_name21)
                            file1.close()
                            if severid1 == "ok":
                                await channel.send(f'{msg.author.mention}さん、そのサーバーをアンアクティベートしました')
                            else:
                                await channel.send(f'{msg.author.mention}さん、そのサーバーはアクティベートされていないか、あなたがアクティベートしていません')

        # メッセージ送信者がBotだった場合は無視する
        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!BOTアクティベートリスト':
            path = str("./ボット-データ/") + str(message.author.id)
            files = os.listdir(path)
            files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
            await message.channel.send(str("アクティベートしたサーバーIDリスト : ") + str("`") + str(files_file) + str("`"))

        if message.content.startswith('spb!senddm '):
            # DMに送るメッセージを取得
            channel = message.channel
            id = message.content.replace('spb!senddm ', '')

            await channel.send(f'{message.author.mention}さん、送るメッセージを送ってください')

            def check(m):
                if not message.author.bot and message.author.id == m.author.id:
                    # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
                    # コマンドを打ったチャンネルという条件
                    channel = message.channel
                    global msg12, temptxt
                    msg12 = m.content
                    return m.channel == channel
                msg12 = m.content
                return

            try:
                # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
                msg = await client.wait_for('message', check=check, timeout=300)
                # wait_forの1つ目のパラメータは、イベント名の on_がないもの
                # 2つ目は、待っているものに該当するかを確認する関数 (任意)
                # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

            # asyncio.TimeoutError が発生したらここに飛ぶ
            except asyncio.TimeoutError:
                await channel.send(f'{message.author.mention}さん、時間切れです')
            else:
                user = await client.fetch_user(id)
                await channel.send(f'{msg.author.mention}さん、`' + msg12 + "` を `" + str(user) + "` さんに送信しました")
                assert isinstance(id, object)
                user = await client.fetch_user(id)
                await user.send(msg12)

        if message.author.bot:
            return
        if isinstance(message.channel, discord.DMChannel):
            if message.content == "こんにちは":
                # 処理
                async with message.channel.typing():
                    await asyncio.sleep(1)
                    id = message.author.id
                    assert isinstance(id, object)
                    user = await client.fetch_user(id)
                    await user.send("こんにちは～")
            pass

        if message.author.bot:
            return
        if message.content == "spb!invitelink":
            ch = message.channel
            invites = await message.channel.invites()
            if discord.utils.get(invites, max_age=0):
                print(discord.utils.get(invites, max_age=0))
                msg = discord.utils.get(invites, max_age=0)
                await ch.send(msg)
            else:
                print(await message.channel.create_invite())
                msg = await message.channel.create_invite()
                await ch.send(msg)

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        setmsg1 = message.author.id
        if setmsg1 == 812275752904163358:
            if message.content == 'spb!clear':
                command = 'clear'
                if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
                    command = 'cls'
                os.system(command)
                channel = message.channel
                await channel.send(f'{message.author.mention}さん、コンソールをクリアしました')

        if message.author.bot:
            return
        setmsg = message.author.id
        runok = "禁止"
        if message.content.startswith("spb!run python3 "):
            if message.author.guild_permissions.administrator:
                if setmsg == 812275752904163358:
                    if runok == "OK":
                        userid = message.content.replace('spb!run python3 ', '')
                        print(userid)
                        proc = subprocess.Popen(['python3', userid])
                        proc.poll()
                        channel = message.channel
                        await channel.send(f'{message.author.mention}さん、`' + 'python3 ' + userid + '` をコンソールで実行しました')

        if message.author.bot:
            return
        setmsg = message.author.id
        runok = "禁止"
        if message.content.startswith("spb!run python "):
            if message.author.guild_permissions.administrator:
                if setmsg == 812275752904163358:
                    if runok == "OK":
                        userid = message.content.replace('spb!run python ', '')
                        print(userid)
                        proc = subprocess.Popen(['python', userid])
                        proc.poll()
                        channel = message.channel
                        await channel.send(f'{message.author.mention}さん、`' + 'python ' + userid + '` をコンソールで実行しました')

        # 最近追加
        if message.author.bot:
            return
        setmsg = message.author.id
        if message.content.startswith("spb!kick "):
            print("1")
            if message.author.guild_permissions.administrator:
                print("2")
                userid = message.content.replace('spb!kick ', '')
                print(userid)
                channel = message.channel
                user = await client.fetch_user(userid)
                embed = discord.Embed(title="キックが正常に実行されました", color=0xff0000)
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="対象", value=user, inline=False)
                embed.add_field(name="実行", value=message.author, inline=False)
                await message.channel.send(embed=embed)
                try:
                    await message.guild.kick(user)
                except:  # NameError 以外はここで処理
                    print('エラーを無視しました')

        if message.author.bot:
            return
        if isinstance(message.channel, discord.DMChannel):
            print("")
        else:
            if message.author.guild_permissions.administrator:
                if message.content.startswith("spb!ban "):
                    userid = message.content.replace('spb!ban ', '')
                    user = await client.fetch_user(userid)
                    embed = discord.Embed(title="BANが正常に実行されました", color=0xff0000)
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.add_field(name="対象", value=user, inline=False)
                    embed.add_field(name="実行", value=message.author, inline=False)
                    channel = message.channel
                    await message.channel.send(embed=embed)
                    banop = "コマンド利用者 : " + str(message.author)
                    await message.guild.ban(user, reason=banop)

        if message.author.bot:
            return
        if isinstance(message.channel, discord.DMChannel):
            if message.author.guild_permissions.administrator:
                if message.content.startswith("spb!unban"):
                    userid = message.content.replace('spb!unban ', '')
                    user = await client.fetch_user(userid)
                    embed = discord.Embed(title="BANを解除しました", color=0xff0000)
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.add_field(name="対象", value=user, inline=False)
                    embed.add_field(name="実行", value=message.author, inline=False)
                    await message.channel.send(embed=embed)
                    await message.guild.unban(user)

        if message.author.bot:
            return
        gbantemp = "0"
        if message.content == "spb!MyGBAN":
            # 処理
            if isinstance(message.channel, discord.DMChannel):
                gbantemp = "0"
                async with message.channel.typing():
                    f = open('./GBAN/GBANlist.txt')
                    gbanlist = f.read().split()
                    print(gbanlist)
                    f.close()
                    user = await client.fetch_user(message.author.id)
                    guildjoinuserid = "'" + str(message.author.id) + "'"
                    for gbanid in gbanlist:  # BOTが所属する全てのチャンネルをループ
                        gbanid = "'" + str(gbanid) + "'"
                        if gbanid == guildjoinuserid:  # グローバルチャット用のチャンネルが見つかったとき
                            print("GBAN USER 検知")
                            gbantemp = "BAN"
                        else:
                            print("GBAN USER ではない")
                            if not gbantemp == "BAN":
                                gbantemp = "NOBAN"
                            continue
            if gbantemp == "BAN":
                user = await client.fetch_user(message.author.id)
                embed = discord.Embed(title="GBANをされています", color=0xff0000)
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="GBAN対象", value=user, inline=False)
                embed.add_field(name="お問合せ先", value="@ふまれうか_HRK#9119", inline=False)
                await asyncio.sleep(1)
                id = message.author.id
                assert isinstance(id, object)
                await user.send(embed=embed)
            else:
                user = await client.fetch_user(message.author.id)
                embed = discord.Embed(title="GBANはされていません", color=0xff0000)
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="GBAN情報", value="GBAN対象ではない", inline=False)
                embed.add_field(name="お問合せ先", value="@ふまれうか_HRK#9119", inline=False)
                await asyncio.sleep(1)
                id = message.author.id
                assert isinstance(id, object)
                await user.send(embed=embed)

            pass

        if message.author.bot:
            return
        setmsg = message.author.id
        if message.content.startswith("spb!gban "):
            if setmsg == 812275752904163358:
                gbanid = message.content.replace('spb!gban ', '')
                name = await client.fetch_user(gbanid)
                f = open('./GBAN/GBANlist.txt')
                gbanlist = f.read()
                print(gbanlist)
                f.close()

                path = str('./GBAN/') + str("GBANlist.txt")
                f = open(path, 'w')
                f.write(str(gbanid) + " " + gbanlist)  # 何も書き込まなくてファイルは作成されました
                f.close()
                channel = message.channel
                await channel.send(
                    f'{message.author.mention}さん、' + str(name) + " ( " + str(name.id) + " ) をGBANに追加しました")

        if message.author.bot:
            return
        setmsg = message.author.id
        if setmsg == 812275752904163358:
            if message.content.startswith("spb!ungban "):
                gbanid = message.content.replace('spb!ungban ', '')
                name = await client.fetch_user(gbanid)
                f = open('./GBAN/GBANlist.txt')
                gbanlist = f.read()
                print(gbanlist)
                f.close()

                del21 = gbanid + " "
                temptxt = ""

                for x in range(len(del21)):
                    temptxt = del21.replace(del21, '')

                path = str('./GBAN/') + str("GBANlist.txt")
                f = open(path, 'w')
                f.write(str(temptxt))  # 何も書き込まなくてファイルは作成されました
                f.close()
                channel = message.channel
                await channel.send(
                    f'{message.author.mention}さん、' + str(name) + " ( " + str(name.id) + " ) をGBANから削除しました")

        if message.author.bot:
            return
        setmsg = message.author.id
        if message.content == 'spb!gbanlist':
            if setmsg == 812275752904163358:
                f = open('./GBAN/GBANlist.txt')
                gbanlist = f.read().split()
                print(gbanlist)
                f.close()
                channel = message.channel
                embed = discord.Embed(title="GBANリスト", color=0xff0000)
                for gbanid in gbanlist:  # BOTが所属する全てのチャンネルをループ
                    print(gbanid)
                    user = await client.fetch_user(int(gbanid))
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.add_field(name="GBAN対象", value=str(user), inline=False)
                if not isinstance(message.channel, discord.DMChannel):
                    await message.channel.send(embed=embed)

                else:
                    user = await client.fetch_user(int(message.author.id))
                    id = message.author.id
                    assert isinstance(id, object)
                    await user.send(embed=embed)

        # 開発段階
        if message.author.bot:
            return
        setmsg = message.author.id
        if setmsg == 812275752904163358 and message.content.startswith("spb!botname "):
            msg = message.content.replace('spb!botname ', '')
            channel = message.channel
            await channel.send(f'{message.author.mention}さん、 ' + msg + " に名前を変更しました（このコマンドはクールタイムが長いです）")
            await client.user.edit(username=msg)

        if message.author.bot:
            return
        # 「/neko」と発言したら「にゃーん」が返る処理
        if message.content == 'spb!usecmdhelp':
            print("")

    @client.event
    async def on_member_join(member):
        print("新規ユーザー検知")
        f = open('./GBAN/GBANlist.txt')
        gbanlist = f.read().split()
        print(gbanlist)
        f.close()
        guildjoinuserid = "'" + str(member.id) + "'"
        for gbanid in gbanlist:  # BOTが所属する全てのチャンネルをループ
            print(gbanid)
            print(guildjoinuserid)
            gbanid = "'" + str(gbanid) + "'"
            if gbanid == guildjoinuserid:  # グローバルチャット用のチャンネルが見つかったとき
                print("GBAN USER 検知")
                user = await client.fetch_user(member.id)
                embed = discord.Embed(title="GBANをされています", color=0xff0000)
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="GBAN対象", value=user, inline=False)
                embed.add_field(name="お問合せ先", value="@ふまれうか_HRK#9119", inline=False)
                await user.send(embed=embed)
                await member.guild.ban(user, reason="GBANされたユーザー")
            else:
                print("GBAN USER ではない")
                continue

    # Botの起動とDiscordサーバーへの接続
    client.run(data)

