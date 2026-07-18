def normalize(article):
    return {'title':article.get('title','').strip(),'source':article.get('source','unknown'),'timestamp':article.get('timestamp'),'content':article.get('content','')}
