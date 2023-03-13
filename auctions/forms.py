from django.forms import ModelForm
from .models import Auction


class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ['title', 'description', 'price', 'starting_bid']
