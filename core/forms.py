from django import forms
from .models import Expense, Group, User

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'paid_by', 'group', 'split_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['split_type'].widget = forms.Select(choices=[('equal', 'Equal'), ('percentage', 'Percentage')])


from django import forms
from .models import Group, User

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'users']
        widgets = {
            'users': forms.CheckboxSelectMultiple
        }
