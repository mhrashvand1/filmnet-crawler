import re
from w3lib.html import remove_comments, remove_tags


def remove_nbsp(value):
    return value.replace('&nbsp;', '')


def get_genres(value):
    
    """ 
    Getting list of the categories and return list of the genres
    """
    
    genres = [c for c in value if c['type']=='genre'][0]['items']
    
    result = []
    for g in genres:
        result.append({
            'id':g['id'],
            'short_id':g['short_id'],
            'slug':g['slug'],
            'title':g['title'],
            'body':remove_comments(remove_tags(remove_nbsp(g['body'])))
        })
    
    return result

