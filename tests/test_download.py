import httmock
import pkg_resources as pres
import opendatagovlt


@httmock.all_requests
def response_content(url, request):
    return pres.resource_string('tests', 'fixtures/search_results.html')


@httmock.with_httmock(response_content)
def test_download():
    opendatagovlt.download_pages()
