from collections import defaultdict

from rest_framework import viewsets
from rest_framework import views
from rest_framework import response

from diet.models import Diet
from diet.serializers import DietSerializer

from shopping.models import ShoppingList
from shopping.models import ListItem
from shopping.serializers import ShoppingListSerializer


class DietViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer


class GenerateShoppingListView(views.APIView):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
    serializer_class_return = ShoppingListSerializer

    def post(self, request, *args, **kwargs):
        diet = self.queryset.filter(pk=kwargs['pk']).first()
        weekdays = request.data['weekdays']
        diet_days = diet.dietday_set.filter(weekday__in=weekdays)
        shopping_list = ShoppingList.objects.create(diet=diet)
        for day in diet_days:
            shopping_list.weekdays.add(day)
        shopping_list.save()
        self.generate_shoping_items(shopping_list, diet_days)
        serializer = self.serializer_class_return(shopping_list)
        return response.Response(serializer.data, status=201)

    def generate_shoping_items(self, shopping_list, diet_days):
        items = defaultdict(float)
        for day in diet_days:
            for meal in day.meal_set.all():
                for meal_item in meal.mealitem_set.all():
                    items[meal_item.product] += meal_item.amount

        for product, amount in items.items():
            ListItem.objects.create(
                shopping_list=shopping_list,
                category=product.category,
                product=product,
                amount=amount)
