import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.forms.models import model_to_dict
from goods.models import Goods


# class GoodsListView(View):
#     """
#     django的view实现
#     """
#     def get(self, request):
#         json_list = []
#         goods = Goods.objects.all()
#         for good in goods:
#
#             json_dict = dict(name=good.name, category=good.category.name, market_price=good.market_price)
#             json_list.append(json_dict)
#
#         return HttpResponse(json.dumps(json_list), content_type='application/json')


# class GoodsListView(View):
#     """
#     django model_to_dict
#     """
#     def get(self, request):
#         json_list = []
#         goods = Goods.objects.all()
#         for good in goods:
#             json_dict = model_to_dict(good)
#             json_list.append(json_dict)
#         return HttpResponse(json.dumps(json_list), content_type='application/json')

class GoodsListView(View):
    """
    django serializer
    """
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()

        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)

        return JsonResponse(json_data, safe=False)





