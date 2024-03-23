from slugify import slugify

def slug(string, separator='-'):
    return slugify(string, separator=separator)

def unslug(slug_str, separator='-'):
    return slug_str.replace(separator, ' ')
