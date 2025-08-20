from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review

# Create your views here.

def review(request):
    if request.method == "POST":
        # can also update entries by passing "instance = existing_entry" to below ReviewForm (using Reviews.objects.get(pk=1)) 
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            # review = Review(username= form.cleaned_data['username'],
            #                 review_text= form.cleaned_data['review_text'],
            #                 rating= form.cleaned_data['rating'])
            # review.save()
            form.save()     # since it is a ModelForm now
            return HttpResponseRedirect('/thanks')
    else:
        form = ReviewForm()
    
    return render(request, "reviews/review.html",{
        'form': form
    })

def thanks(request):
    return render(request, 'reviews/thanks.html')