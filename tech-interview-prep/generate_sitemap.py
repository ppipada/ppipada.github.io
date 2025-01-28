import datetime
import os

url = 'https://pankajpipada.com/tech-interview-prep/#'
file_path = "./sitemap.xml"
exclude_files = [
    'coverpage', 'navbar', 'README', 'sidebar', '_sidebar', 'all', 'CHANGELOG', "_pending", "all-problems/README", 'all-tags/README', 'algorithms/README'
]


def create_sitemap():
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for path, dirs, files in os.walk("./"):
        for file in files:
            if not file.endswith('.md'):
                continue
            try:
                if not path.endswith('/'):
                    path += '/'
                new_path = (path.replace('\\', '/') + file)[2:-3]
                if new_path in exclude_files:
                    continue
                print(new_path)
                xml += '  <url>\n'
                xml += f'    <loc>{url}/{new_path}</loc>\n'
                lastmod = datetime.datetime.utcfromtimestamp(os.path.getmtime(path + file)).strftime('%Y-%m-%d')
                xml += f'    <lastmod>{lastmod}</lastmod>\n'
                xml += '  </url>\n'
            except Exception as e:
                print(path, file, e)
                break
    xml += f'</urlset>\n'

    with open(file_path, 'w', encoding='utf-8') as sitemap:
        sitemap.write(xml)


if __name__ == '__main__':
    create_sitemap()