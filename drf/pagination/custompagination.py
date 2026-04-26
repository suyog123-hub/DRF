from rest_framework.pagination import PageNumberPagination


class DetailsPagination(PageNumberPagination):
    page_size = 3
    # this is for the next page and previous page in the url
    page_query_param = 'newpage'
    # this is for the client to specify the page size in the url
    page_size_query_param = 'page_size'
    # this is for the maximum page size in the url that the client can specify
    max_page_size = 100