from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request,'post_list.html')
def post_create(request):
    return render(request,'create_post.html')
def post_edit(request):
    return render(request,'edit_post.html')
def post_read(request):
    return render(request,'read_post.html')