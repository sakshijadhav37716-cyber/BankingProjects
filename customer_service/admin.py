from django.contrib import admin
from .models import Card

admin.site.register(Card)
from .models import (
    BankAccount,
    Transaction,
    LoanApplication,
    Card,
    NetBanking,
    CustomerServiceRequest,
    CardTransaction
)

admin.site.register(BankAccount)
admin.site.register(Transaction)
admin.site.register(LoanApplication)
admin.site.register(Card)
admin.site.register(NetBanking)
admin.site.register(CustomerServiceRequest)
admin.site.register(CardTransaction)