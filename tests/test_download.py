import httmock
import pkg_resources as pres
import opendatagovlt


@httmock.all_requests
def response_content(url, request):
    return pres.resource_string('tests', 'fixtures/search_results.html') #kas čia yra ir kaip tai veikia? Ar to paties reikia prie kitų testų?


@httmock.with_httmock(response_content)
def test_download():
    opendatagovlt.download_pages()


def test_download_page_alt0(number):
    opendatagovlt.download_alt0()
