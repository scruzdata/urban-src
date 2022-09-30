from rest_framework import pagination
from rest_framework.response import Response


class Custom20Pagination(pagination.PageNumberPagination):

    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):

        page_size_param = int(self.request.GET.get('page_size', self.page_size))
        results_total = self.page.paginator.count
        self.page_size = page_size_param if page_size_param < results_total else results_total

        return Response({
            'pagination': {
                'num_results':  self.page.paginator.count,
                'num_pages':    self.page.paginator.num_pages,
                'page_current': self.page.number,
                'page_size':    self.page_size,
                'next':         self.get_next_link(),
                'previous':     self.get_previous_link()
            },
            'results': data
        })
