from rest_framework.pagination import PageNumberPagination


class ResultSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'items'
    max_page_size = 20
