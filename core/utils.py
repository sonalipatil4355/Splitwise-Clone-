from .models import Expense, Split

def calculate_balances(group_id):
    balances = {}
    expenses = Expense.objects.filter(group_id=group_id)
    for expense in expenses:
        paid_by = expense.paid_by.id
        balances[paid_by] = balances.get(paid_by, 0) + expense.amount
        splits = Split.objects.filter(expense=expense)
        for split in splits:
            balances[split.user.id] = balances.get(split.user.id, 0) - split.amount_owed
    return balances
