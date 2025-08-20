from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Enter your name", max_length=100, error_messages={
#         "required": "Bhai naam to daalo",
#         "max_length": "only add Chinna Swami of Chinna swami mutuswami vengopal iyer..."
#     })
    
#     review_text = forms.CharField(label="Enter your review", widget=forms.Textarea, max_length=500)

#     rating = forms.IntegerField(label="Enter your rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text', 'rating']
        # fields = __all__
        labels = {
            'username': 'Your Name',
            'review_text': 'Your Review',
            'rating': 'Your Rating'
        }
        exclude = ['owner_comment']        
        error_messages = {
            "username":{
                "required":"Bhai naam to daalo",
                "max_length": "only add Chinna Swami of Chinna swami mutuswami vengopal iyer..."
            }
        }