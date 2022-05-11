if 3/2 == 1:
    from urllib import URLopener
else:
    from urllib.request import URLopener

langs = ['af', 'az', 'id', 'ms', 'bi', 'bs', 'ca', 'ny', 'da', 'de', 'et', 'na', 'en', 'es', 'to', 'mg', 'fr', 'sm', 'hr', 'it', 'mh', 'kl', 'rn', 'rw', 'sw', 'ht', 'lv', 'lt', 'lb', 'hu', 'mt', 'nl', 'no', 'uz', 'pl', 'pt', 'pt-br', 'ro', 'qu', 'st', 'tn', 'sq', 'ss', 'sk', 'sl', 'so', 'fi', 'sv', 'tl', 'vi', 'tr', 'tk', 'fj', 'wo', 'yo', 'is', 'cs', 'el', 'be', 'ky', 'mo', 'mn', 'ru', 'sr', 'tg', 'uk', 'bg', 'kk', 'hy', 'he', 'ur', 'ar', 'fa', 'dv', 'ne', 'hi', 'bn', 'ta', 'th', 'lo', 'dz', 'my', 'ka', 'ti', 'am', 'km', 'zh-cn', 'zh', 'ja', 'ko']

downloader = URLopener()
for lang in langs:
    downloader.retrieve('http://www.transformice.com/langues/tfm-{}.gz?d=6'.format(lang), 'langues/tfm-{}.gz'.format(lang))