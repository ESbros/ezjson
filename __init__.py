from os.path import dirname, join

from textx import language, metamodel_from_file

@language("ezjson", "*.ezjson")
def ezjson():
    "A language for creating JSON files easier."
    return metamodel_from_file(join(dirname(__file__), "ezjson.tx"))