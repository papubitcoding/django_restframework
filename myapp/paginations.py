from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size=5
    page_size_query_param='records'
    
    
    
class MyLimitPagination(LimitOffsetPagination):
    pass