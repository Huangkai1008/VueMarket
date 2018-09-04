import json

from django.http import HttpResponse
from django.views.generic import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()
        for good in goods:
            json_dict = dict(name=good.name, category=good.category.name, market_price=good.market_price)
            json_list.append(json_dict)

        return HttpResponse(json.dumps(json_list), content_type='application/json')
