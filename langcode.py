# see: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

iso639_codes = ["sv"]

def is_valid_langcode(raw):
    return raw in iso639_codes

# pytest for above function

def test_is_valid_langcode():
    assert is_valid_langcode("sv") == True
