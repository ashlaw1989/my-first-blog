from django.shortcuts import render

# Create your views here.

# views always take in a request, and they almost always render and return a response
def post_list(request):
    # when rendering a webpage we return a render of the request, athe html page we want to load, and any data we want to pass to that webpage (usually in the form of a db query)
    return render(request, "blog/post_list.html", {})