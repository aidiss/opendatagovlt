import opendatagovlt


def test_read_downloaded_pages():
    pages = opendatagovlt.read_downloaded_pages()
    assert len(pages) == 16
