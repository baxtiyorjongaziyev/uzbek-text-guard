from uzbek_text_guard import find_violations


def test_detects_ascii_apostrophe_in_uzbek_word():
    assert len(find_violations('msg = "qo'ng'iroq"')) == 1


def test_allows_proper_uzbek_and_english_apostrophes():
    assert find_violations('msg = "qoʻngʻiroq va maʼno"') == []
    assert find_violations("msg = "don't stop"") == []
