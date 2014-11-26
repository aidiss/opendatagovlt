import opendatagovlt


def test_extract_links(html):
    scraped_singular = opendatagovlt.extract_links(
        'tests',
        'fixtures/singular_html_empty.html')
    assert scraped_singular


def test_store_links(html, path):
    opendatagovlt.store_links(html, path)
    assert html == 'html'
    assert open(path) == True


def test_filter_links(html):
    #kam sito reikia? Juk jau turim extract links.
    pass


def test_detect_encoding():
    #turi testuoti keleta puslapiu, kiekvienam is ju nustato encoding
    assert opendatagovlt.detect_encoding('tests', 'fixtures/utf8.html') == 'utf8'
    assert opendatagovlt.detect_encoding('tests', 'fixtures/utf16.html') == 'utf16'
    assert opendatagovlt.detect_encoding('tests', 'fixtures/ascii.html') == 'ascii'
    assert opendatagovlt.detect_encoding('tests', 'fixtures/iso1600.html') == 'iso1600'


def test_download_page():
    #todo atkelti is kitur
    assert


def test_manage_downloaded_page():
    # per plati kategorija.
    # todo skaldyti
    assert
