from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from recipes.models import Recipes, Review
from recipes.utils import average_rating
from .forms import BookMediaForm,EmpImageDisplay #поменяла ReviewForm SearchForm на эти два  



def home(request):
    theme = request.COOKIES.get('theme', 'light')
    context = {'theme': theme}
    response = render(request, 'recipes/main.html', context)
    response.set_cookie('theme', theme)
    return response


def set_theme(request):
    theme = request.GET.get('theme', 'light')
    response = HttpResponse()
    response.set_cookie('theme', theme)
    return response    

def payment(request):
    return render(request, 'recipes/payment_success.html')    

def services(request):
    return render(request, "recipes/salePage.html")

def index(request):

    return render(request, 'recipes/main.html')


def recipes(request):
    recipes = Recipes.objects.all()

    sort_by = request.GET.get('sort_by')  # get the value of the sorting parameter from the URL query string

    if sort_by == 'difficulty':
        recipes = sorted(recipes, key=lambda recipe: recipe.level)  # sort by difficulty level
    else:
        recipes = recipes.order_by('-rating')
   
    context = {
        'recipes': recipes
    }
    return render(request,'recipes/recipes.html',{'recipes': recipes})


def recipe_detail(request, pk):
    if pk is not None:
        recipe = get_object_or_404(Recipes, pk=pk)
    else:
        recipe = None
    reviews = recipe.review_set.all()
    if reviews:
        rating = average_rating([review.rating for review in reviews])
        context = {"recipe": recipe, "rating": rating, "reviews": reviews}
    else:
        context = {"recipe": recipe, "rating": None, "reviews": None}

    return render(request, 'recipes/detail.html', context)




def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Error logging! Try again.")
            return redirect('login')
    else:
        return render(request, 'recipes/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')

def search(request):
    # search = request.GET.get("search", "")
    # form = SearchForm(request.GET)
    # recipe = set()
    # if form.is_valid() and form.cleaned_data["search"]:
    #     search = form.cleaned_data["search"]
    #     search_in = form.cleaned_data.get("search_in") or "title"
    #     if search_in == "title":
    #         recipe = Recipes.objects.filter(title__contains=search)
    #     else:
    #         fname_contributors = Contributor.objects.filter(first_names__contains=search)
    #         for contributor in fname_contributors:
    #             for book in contributor.book_set.all():
    #                 recipe.add(book)
    #         lname_contributors = Contributor.objects.filter(last_names__contains=search)
    #         for contributor in lname_contributors:
    #             for book in contributor.book_set.all():
    #                 recipe.add(book)

    return render(request, 'recipes/search.html', {'form':form,'search': search, 'recipe': recipe})


def review_edit(request, recipe_pk, review_pk=None):
    recipe = get_object_or_404(Recipes, pk=recipe_pk)
    if review_pk is not None:
        review = get_object_or_404(Review, recipe_id=recipe_pk, pk=review_pk)
    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            updated_review = form.save(False)
            updated_review.recipe = recipe

            if review is None:
                messages.success(request, "Review for \"{}\" created.".format(recipe))
            else:
                updated_review.date_edited = timezone.now()
                messages.success(request, "Review for \"{}\" updated.".format(recipe))
                return redirect(recipe_detail, recipe.pk)
            updated_review.save()
    else:
        form = ReviewForm(instance=review)

    return render(request, "recipes/instance-form.html", {"form": form, "instance": review, "model_type": "Review", "related_instance": recipe, "related_model_type": "Book"})


def myprofile(request):
    return render(request, "recipes/myprofile.html")
