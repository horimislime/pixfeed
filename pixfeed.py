from flask import Flask,make_response
from pyzuri import pyzuri
import datetime

DATE_FORMAT="%Y-%m-%dT%H:%M:%SZ"

app=Flask(__name__)
#app.debug=True
pixiv=pyzuri("id","password")


@app.route('/')
def index():
    return "hello"

@app.route('/favorites')
def feed_favuser_works():
    favuser_works=pixiv.getFavUserWorks()
    feed = '<?xml version="1.0" encoding="UTF-8"?>\n'
    feed += '<feed xmlns="http://www.w3.org/2005/Atom">\n'
    feed += '<title>Pixiv Favorite User\'s RSS</title>\n'
    feed += '<link href="http://www.pixiv.net/bookmark_new_illust.php" rel="alternate"></link>\n'
    feed += '<id>http://www.pixiv.net/bookmark_new_illust.php</id>\n'

    feed += '<updated>' + str(datetime.datetime.now().strftime(DATE_FORMAT)) + '</updated>\n'
#    feed += '<author><name>horimislime</name></author>\n'
    for illus in favuser_works:
        pass
    return feed

@app.route('/daily')
def feed_daily_rss():

    daily_ranking=pixiv.getDailyRanking()
    feed = '<?xml version="1.0" encoding="UTF-8"?>\n'
    feed += '<feed xmlns="http://www.w3.org/2005/Atom">\n'
    feed += '<title>Pixiv Daily Ranking RSS</title>\n'
    feed += '<link href="http://www.pixiv.net/ranking.php?mode=daily" rel="alternate"></link>\n'
    feed += '<id>pixiv.net/ranking.php?mode=daily</id>\n'

    feed += '<updated>' + str(datetime.datetime.now().strftime(DATE_FORMAT)) + '</updated>\n'
    feed += '<author><name>horimislime</name></author>\n'

    for illust in daily_ranking:
        feed+='<entry>\n'
        feed+='<title>'+illust["title"]+'</title>\n'
        feed+='<link href="'+illust["illust_url"]+'" rel="alternate"></link>\n'
        feed += '<updated>' + str(datetime.datetime.now().strftime(DATE_FORMAT)) + '</updated>\n'
        feed += '<id>'+illust["illust_url"]+'</id>\n'
        feed+='<summary type="html"><a href="'+illust["illust_url"]+'"><img src="'+illust["thumb_url"]+'"/></a></summary>\n'
#        feed+='<summary type="html">hogehoge</summary>\n'
        feed+='</entry>\n'
    feed+='</feed>'
    
    resp=make_response(feed)
    resp.headers['Content-Type']='application/atom+xml'
    return resp

"""
@app.route('favorites')
def feed_favuser_works():
    return "hello"
"""
if __name__=='__main__':
    app.run()
