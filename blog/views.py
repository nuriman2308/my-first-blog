from django.shortcuts import render

# "logic" of our application

def post_list(request):
    return render(request, 'blog/post_list.html', {})
