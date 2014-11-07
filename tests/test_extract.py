import opendatagovlt

def test_read_downloaded_pages(path):
    pages = opendatagovlt.read_downloaded_pages(None)
    assert len(pages) == 16

def test_get_table_from_html(html):
    table = opendatagovlt.get_table_from_html('tests', 'fixtures/search_results.html')
    assert table == None #list of lists?

## Alternative flow
def test_scrap_singular(path):
    scraped_singular = opendatagovlt.scrap_singular('test path')
    assert scrap_singular == None

def test_merge_singulars(list_of_lists):
    merged_singulars = opendatagovlt.merge_singulars('tests', 'list of lists')
    assert merged_singulars == None

def test_filter_entries(entries):
    filtered_entries = opendatagovlt.filter_entries('tests', 'entries')
    assert filtered_entries == None

def test_to_list_of_dicts(some_list):
    list_of_dicts = opendatagovlt.to_list_of_dicts('tests', 'some_list')
    assert list_of_dicts == None # How to test for list of dicts?


# Maybe this one is too big?
def test_alternative_flow():
    opendatagovlt.alternative_flow()