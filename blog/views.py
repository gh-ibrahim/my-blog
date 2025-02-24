from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
# This is the simplest view possible in Django.
# To create a view, we created a function (def) called post_list that takes request and will return the value it gets from calling another function render that will render (put together) our template blog/post_list.html.
