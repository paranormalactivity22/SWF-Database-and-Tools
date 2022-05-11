import os, asyncio, aiohttp, aiofiles, json

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                towrite = await resp.read()
                _path = url.split('.')[2:]
                _path = '.'.join(_path)
                dirs = _path.split('/')
                dirs[0] = 'TFM_IMAGES'
                _path = '/'.join(dirs)
                if os.path.exists(_path):
                    async with aiofiles.open(_path, mode='rb') as f:
                        content = await f.read()
                        if content == towrite:
                            print(f'[!] File \'{_path}\' is already exists, skipping.')
                            return
                path = ''
                for dir in dirs:
                    if '?' in dir:
                        dir = dir.split('?')[0]
                    if dir.split('.')[-1] in ['png', 'jpg', 'gif', 'swf', 'mp3', 'jpeg', 'ico'] or 'tfz_' in dir:
                        continue
                    path += dir
                    if not os.path.exists(path):
                        print(f'[+] Creating \'{path}/\' directory.')
                        os.mkdir(path)
                    path += '/'
                file_name = dirs.pop()
                if '?' in file_name:
                    file_name = file_name.split('?')[0]
                if '?' in _path:
                    _path = _path.split('?')[0]
                async with aiofiles.open(_path, mode='wb') as f:
                    print(f'[+] Saving \'{file_name}\' to \'{"/".join(dirs)}/\' directory.')
                    await f.write(towrite)

async def start():
    print('[+] Transformice image parser')
    print('[+] Tool by Depwesso')
    print()
    urls = []
    async with aiohttp.ClientSession() as session:
        for html in ['images', 'ar', 'godspaw', 'share', 'woot', 'wp-admin', 'wp-content', 'wp-includes']:
            async with session.get(f"http://derpolino.alwaysdata.net/imagetfm/getFiles.php?n={html}%2F&mode=tfm") as resp:
                urls.extend(map(lambda url: 'https://www.transformice.com/' + url, json.loads((await resp.read()).decode()).values()))

    for url in urls:
        await download(url)

    for binary in ["x_fourrures", "x_fourrures2", "x_fourrures3", "x_fourrures4", "x_meli_costumes", "x_pictos_editeur"]:
        await download(f'http://transformice.com/images/x_bibliotheques/{binary}.swf')
    for langue in ['en', 'fr', 'br', 'es', 'cn', 'tr', 'vk', 'pl', 'hu', 'nl', 'ro', 'id', 'de', 'e2', 'ar', 'ph', 'lt', 'jp', 'ch', 'fi', 'cz', 'sk', 'hr', 'bu', 'lv', 'he', 'it', 'et', 'az', 'pt']:
        await download(f'http://transformice.com/langues/tfz_{langue}')
    for music in range(4):
        await download(f'http://transformice.com/images/musiques/tfm_{music}.mp3')
    print('Finished')
    os.system('pause')

loop = asyncio.get_event_loop()
loop.run_until_complete(start())