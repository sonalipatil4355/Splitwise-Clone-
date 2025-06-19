from rest_framework import routers
from .views import UserViewSet, GroupViewSet, ExpenseViewSet, SplitViewSet

from django.urls import path
from .views import group_list,chatbot,create_expense,create_group, add_expense, group_balances

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'splits', SplitViewSet)

urlpatterns = router.urls



urlpatterns = [
    path('groups/', group_list, name='group-list'),
    path('chatbot/', chatbot, name='chatbot'),
    path('expenses/add/', create_expense, name='create-expense'),
    path('groups/create/', create_group, name='create-group'),
    path('expenses/add/', add_expense, name='add-expense'),
    path('groups/<int:group_id>/balances/', group_balances, name='group-balances'),
]



