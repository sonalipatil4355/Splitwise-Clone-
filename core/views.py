from rest_framework import viewsets
from .models import User, Group, Expense, Split
from .serializers import UserSerializer, GroupSerializer, ExpenseSerializer, SplitSerializer

from .models import Group

from django.shortcuts import render, redirect
from .forms import ExpenseForm,GroupForm

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class SplitViewSet(viewsets.ModelViewSet):
    queryset = Split.objects.all()
    serializer_class = SplitSerializer

    




def group_list(request):
    groups = Group.objects.prefetch_related('users').all()
    return render(request, 'groups.html', {'groups': groups})


from django.http import JsonResponse
from .utils import calculate_balances

def group_balances(request, group_id):
    return JsonResponse(calculate_balances(group_id))




from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chatbot(request):
    response = None
    if request.method == 'POST':
        query = request.POST.get('query')
        # MOCK: replace with OpenAI or HuggingFace logic
        if "Alice" in query:
            response = "Alice owes ₹500 in the Goa Trip group."
        else:
            response = "I couldn't understand. Try another query."
    return render(request, 'chatbot.html', {'response': response})



def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group-list')  # Change to your desired redirect
    else:
        form = ExpenseForm()
    return render(request, 'create_expense.html', {'form': form})


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group-list')
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form})


from .utils import calculate_balances

def group_balances(request, group_id):
    group = Group.objects.get(id=group_id)
    balances = calculate_balances(group_id)
    return render(request, 'balances.html', {'balances': balances, 'group': group})



def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group-list') 
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})
