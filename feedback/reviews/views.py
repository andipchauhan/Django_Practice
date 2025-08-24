from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
# UpdateView and DeleteView also available
from .forms import ReviewForm
from .models import Review

# Create your views here.

class AddFavoriteView(View):
    def post(self,request):
        review_id = request.POST['review_id']
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/"+review_id)

class ReviewView(CreateView):
    # we don't even need the ReviewForm class in forms.py with CreateView, but we can use it also if we want custom labels and error messages
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thanks"
    # will auto save and we don't need a form_valid method

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thanks"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
        
        
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html",{
#             'form': form
#         })
        
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thanks')
#         return render(request, "reviews/review.html",{
#             'form': form
#         })



class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base = super().get_queryset()
    #     data = base.filter(rating__gt=3)
    #     return data
    
class ReviewDetailView(DetailView):
    template_name = 'reviews/review_detail.html'
    model = Review
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        fav_id = request.session.get("favorite_review")
        # use .get() instead of accessing like keys in dictionary ["favorite_review"] to avoid errors in case data hasn't been set before
        context["is_fav"] = fav_id == str(loaded_review.id)
        return context
    

class ThanksView(TemplateView):
    template_name = 'reviews/thanks.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['name'] = "Random name"
    #     return context


# class ThanksView(View):
#     def get(self, request):
#         return render(request, 'reviews/thanks.html')

    

# def review(request):
#     if request.method == "POST":
#         # can also update entries by passing "instance = existing_entry" to below ReviewForm (using Reviews.objects.get(pk=1)) 
#         form = ReviewForm(request.POST)
        
#         if form.is_valid():
#             # review = Review(username= form.cleaned_data['username'],
#             #                 review_text= form.cleaned_data['review_text'],
#             #                 rating= form.cleaned_data['rating'])
#             # review.save()
#             form.save()     # since it is a ModelForm now
#             return HttpResponseRedirect('/thanks')
#     else:
#         form = ReviewForm()
    
#     return render(request, "reviews/review.html",{
#         'form': form
#     })


# def thanks(request):
#     return render(request, 'reviews/thanks.html')