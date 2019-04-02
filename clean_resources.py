def load_words(_file_path=""):
    if _file_path == "":
        return []
    _file = open(_file_path, 'rb')
    _text = _file.read()
    _file.close()
    return _text.lower().split()


def write_words(_file_path="", _words=[]):
    if _file_path == "":
        return
    _output_file = open(_file_path, 'wb')

    for _word in _words:
        _output_file.write(_word + "\n")
    _output_file.close()


name_file_path = "resource/human_names.txt"
names = load_words(name_file_path)
set_names = set(names)
uniqe_sorted_names = sorted(set_names)
write_words(name_file_path, uniqe_sorted_names)

cites_file_path = "resource/common_cities_state_countries_names.txt"
cites = load_words(cites_file_path)
set_cites = set(cites)
uniqe_sorted_cites = sorted(set_cites)
write_words(cites_file_path, uniqe_sorted_cites)
