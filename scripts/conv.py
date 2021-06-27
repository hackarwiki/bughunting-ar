import re,sys

# made with ❤️ by @knassar702
# usage: cat file.md | python3 conv.py
class arMarkdown:
    def __init__(self,data):
        self.data = data
    def header(self):
        c = self.data.split(' ')[0].count('#')
        if c == 0 or c > 6:
            return self.data
        else:
            v = f'<h{c} dir="rtl" align="right">{"".join(self.data.split(" ")[1:])}</h{c}>'
            self.data = v
            return v
    def comment(self):
        c = self.data.split(' ')[0].count('>')
        if c > 0 :
            f = f"<blackqoute dir='rtl' align='right'>{''.join(self.data.split(' ')[1:])}</blackqoute>"
            self.data = f
            return f
        return self.data
    def image(self):
        txt = self.data
        sub = ''
        r = re.search(r'!\[[^\]]*\](.*?)\s*("(?:.*[^"])")?\s*\)',txt)
        if r:
            c = r.group()
            alt = re.findall(r'!\[(.*?)\](|. .)[(].*[)]',c)
            link = re.findall(r'[(].*[)]',c)[0]
            link = link.replace(link[0],'').replace(link[-1],'')
            sub += f"<img src='{link}' alt='{alt[0][0]}' style='float: right;' />"
            self.data = sub
        return self.data
    def links(self):
        txt = self.data
        sub = ''
        r = re.search(r'\[[^\]]*\](.*?)\s*("(?:.*[^"])")?\s*\)',txt)
        if r:
            c = r.group()
            # get the content of []
            name = re.findall(r'!\[(.*?)\](|. .)[(].*[)]',c)
            # get the content of ()
            link = re.findall(r'[(].*[)]',c)[0]
            link = link.replace(link[0],'').replace(link[-1],'')
            # add the link and name
            sub += f'<a style="float:right" href="{link}">{name}</a>'
            self.data = sub
        return txt
    def start(self):
        self.image()
        self.header()
        self.comment()
        self.links()
        print(self.data)
for data in sys.stdin:
    data = data.rstrip()
    c = arMarkdown(data)
    c.start()
