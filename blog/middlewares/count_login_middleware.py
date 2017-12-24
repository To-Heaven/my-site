class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class CountLoginMiddle(MiddlewareMixin):
    """ 用于记录网站主页访问数量

    """

    def process_request(self, request):
        from blog import models
        from django.db.models import F
        from re import match

        current_path = request.path_info
        obj = models.Site.objects.all().first()
        if current_path == '/':
            if not request.COOKIES.get('has_counted') == 'OK':
                obj.access_count = F('access_count') + 1
                obj.save()
                return None
        elif current_path == '/blog/':
            if not request.COOKIES.get('has_counted') == 'OK':
                obj.access_count = F('access_count') + 1
                obj.save()
                return None
        elif match(pattern=r'/blog/*', string=current_path):
            if not request.COOKIES.get('has_counted') == 'OK':
                obj.access_count = F('access_count') + 1
                obj.save()
                return None
