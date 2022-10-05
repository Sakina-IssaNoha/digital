import imp
from django.urls import path 
from .views import account_list, account_profile, card_list, card_profile, currency_list, customer_profile, customer_profile, edit_account, edit_card, edit_profile, edit_receipt, edit_transaction, edit_wallet, loan_list, notification_list, receipt_list, receipt_profile, register_currency, register_customer, register_transaction, reward_list, thirdparty_list, transaction_list, transaction_profile, wallet_list, wallet_profile
from .views import register_wallet
from .views import register_currency
from .views import register_account
from .views import register_transaction
from .views import register_card
from .views import register_thirdparty
from .views import register_notification
from .views import register_receipt
from .views import register_loan
from .views import register_reward
from .views import list_customers
from .views import wallet_list
from .views import currency_list
from .views import account_list
from .views import transaction_list
from .views import card_list
from .views import thirdparty_list
from .views import notification_list
from .views import receipt_list
from .views import loan_list
from .views import reward_list
from .views import customer_profile

urlpatterns = [
    path("register/",register_customer,name="registation"),
    path("wallet/",register_wallet,name="registation"),
    path("currency/",register_currency,name="registation"),
    path("account/",register_account,name="registation"),
    path("transaction/",register_transaction,name="registation"),
    path("card/",register_card,name="registation"),
    path("thirdparty/",register_thirdparty,name="registation"),
    path("notification/",register_notification,name="registation"),
    path("receipt/",register_receipt,name="registation"),
    path("loan/",register_loan,name="registation"),
    path("reward/",register_reward,name="registation"),
    
    
    path("customers/",list_customers,name="customers"),
    path("wallets/",wallet_list,name="wallets"),
    path("currencys/",currency_list,name="currencys"),
    path("accounts/",account_list,name="accounts"),
    path("transactions/",transaction_list,name="transactions"),
    path("cards/",card_list,name="cards"),
    path("thirdpartys/",thirdparty_list,name="thirdpartys"),
    path("notifications/",notification_list,name="notifications"),
    path("receipts/",receipt_list,name="receipts"),
    path("loans/",loan_list,name="loans"),
    path("rewards/",reward_list,name="rewards"),
    
    # !----display single customer profile-----!
    
    path("customers/<int:id>/",customer_profile,name="customer_profile"),
    path("wallets/<int:id>/", wallet_profile,name="wallet_profile"),
    path("accounts/<int:id>/",account_profile,name="account_profile"),
    path("cards/<int:id>/",card_profile,name="card_profile"),
    path("transactions/<int:id>/",transaction_profile,name="transaction_profile"),
    path("receipts/<int:id>/",receipt_profile,name="receipt_profile"),
   
    # !-----edit profile information-----!
    
    path("customers/edit/<int:id/",edit_profile,name="edit_profile"),
    path("wallets/edit/<int:id/",edit_wallet,name="edit_wallet"),
    path("accounts/edit/<int:id/",edit_account,name="edit_account"),
    path("cards/edit/<int:id/",edit_card,name="edit_card"),
    path("transactions/edit/<int:id/",edit_transaction,name="edit_transaction"),
    path("receipts/edit/<int:id/",edit_receipt,name="edit_receipt"),
    
    

]
