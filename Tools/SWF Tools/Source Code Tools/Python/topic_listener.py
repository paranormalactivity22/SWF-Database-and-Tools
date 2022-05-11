import requests
import re
from bs4 import BeautifulSoup

class topic_lister:
    def __init__(self, section):
        self.url = 'https://atelier801.com/section?{0}'.format(section)
        self.current_page = 1
        self.left_pages = 1
        self.section = {
            'name': 'undefined',
            'tags': {},
            'topics': {},
            'unique_authors': {},
            'pages': 0
        }

    def generate_result(self, file_name, tag_only = False):
        final_text = u'[size=13][size=17][color=#2ecf73]{0}[/color][/size]\n[b]Topic tags ({4}):[/b] {1}\n\n[b]Topic authors ({5}):[/b] {2}\n\n[b]Total topics:[/b] {3}[/size]'

        tags_text = u''
        for tag in sorted(iter(self.section['tags'].keys()), key=lambda k: len(self.section['tags'][k]), reverse=True):
            tag_data =  self.section['tags'][tag]
            tags_text += u', {0} ({1})'.format(tag, len(tag_data))
        tags_text = u'[font=Monospace]{0}[/font]'.format(tags_text[2:])

        authors_text = u''
        for author in sorted(iter(self.section['unique_authors'].keys()), key=lambda k: len(self.section['unique_authors'][k]), reverse=True):
            author_data = self.section['unique_authors'][author]
            authors_text += u', {0} ({1})'.format(author, len(author_data))
        authors_text = u'[font=Monospace]{0}[/font]'.format(authors_text[2:])

        topics_text = u'\n\n[size=12][font=Monospace][table]'
        cel_normalizer = u'-' * 32
        cel_normalizer = u'[color=#1c3c41]'+cel_normalizer+u'[/color]'
        for topic in sorted(iter(self.section['topics'].keys())):
            topic_data = self.section['topics'][topic]
            t_url_title = re.findall('\d+', topic_data['url'])[1]
            topics_text += u'[row]\n\t[cel]{0}[/cel]\n\t[cel]{1}[/cel]\n\t[cel]{2}[/cel]\n\t[cel][url=https://atelier801.com/{3}]T-{4}[/url][/cel]\n[/row]\n'.format(topic_data['title'], topic_data['author'], topic_data['tagged'], topic_data['url'], t_url_title)

        final_text = final_text.format(self.section['name'], tags_text, authors_text, len(self.section['topics']), len(self.section['tags']), len(self.section['unique_authors']))
        final_text += topics_text+u'[/table][/font][/size]'

        file_stream = open(file_name, 'a', encoding="utf-8")
        file_stream.write(final_text)
        file_stream.close()

    def load_section(self):
        formatted_url = '{0}&p={1}'.format(self.url, self.current_page)
        print(u'({0}/{1}) Requisitando página [{2}]'.format(self.current_page, self.left_pages, formatted_url))
        request = requests.get(formatted_url)
        html_page = request.text
        self.search_topics(html_page)
        self.get_left_pages(html_page)

        if (self.current_page < self.left_pages):
            self.current_page += 1
            self.load_section()

    def get_left_pages(self, content):
        html = BeautifulSoup(content, 'html.parser')
        navigation_div = html.find(attrs = {
            'class': 'cadre-pagination'
        }).find('a').text
        total_pages = re.match('\d+ / (\d+)', navigation_div)
        if (total_pages):
            self.left_pages = int(total_pages.group(1))

    def search_topics(self, content):
        html = BeautifulSoup(content, 'html.parser')
        self.section['name'] = html.title.string
        topics = html.find_all(attrs = {
            'class': 'cadre-sujet'
        })
        for topic in topics:
            topic_title = topic.find(attrs = {
                'class': 'cadre-sujet-titre'
            })
            topic_name = topic_title.text.strip()
            topic_tag = re.match('\[(.*?)\]', topic_name)
            topic_tag = topic_tag and topic_tag.group(1) or 'none'
            if (not topic_tag in self.section['tags']):
                self.section['tags'][topic_tag] = []
            topic_url = topic_title.get('href')
            self.section['tags'][topic_tag].append(topic_url)
            topic_name = topic_name#.replace(u'['+topic_tag+u']', '').strip().title()

            topic_sujet = topic.find(attrs = {
                'class': 'element-sujet'
            })
            topic_author = topic.find(attrs = {
                'class': 'cadre-sujet-infos'
            }).find('span', attrs = {
                'class': re.compile('cadre-type-auteur-(.*?)')
            }).text
            if (not topic_author in self.section['unique_authors']):
                self.section['unique_authors'][topic_author] = []
            self.section['unique_authors'][topic_author].append(topic_url)

            topic_date = int(topic_sujet.find('span').text)/1e3
            self.section['topics'][topic_name] = {
                'title': topic_name,
                'tagged': topic_tag.lower(),
                'author': topic_author,
                'created': topic_date,
                'url': topic_url
            }


topicHandler = topic_lister('f=5&s=2')
topicHandler.load_section()
topicHandler.generate_result(u'editor_de_mapas.txt') # arquivo para salvar o bbcode