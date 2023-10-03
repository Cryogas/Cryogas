from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("AEIOU") == ""
    assert shorten("123") == "123"
    assert shorten("?!") == "?!"

