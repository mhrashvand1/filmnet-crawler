import re


def remove_js_comments(text):
    # Define regular expression pattern for matching JS comments
    pattern = r'<!--(.*?)-->'

    # Use re.sub() to remove JS comments from the text
    cleaned_text = re.sub(pattern, '', text)

    return cleaned_text


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
            'body':remove_js_comments(g['body'])
        })
    
    return result
