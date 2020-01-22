from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm

# Create your views here.

# def index(request):
#     return render(request, 'forum_app/index.html')


def postlist(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    return render (request, "forum_app/index.html",{'postlist': queryset})


# def post_detail(request, slug):
#     model = Post
#
#     return render(request,"forum_app/post_detail.html", {'model': model, 'slug': slug })


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'forum_app/post_detail.html'


def post_detail(request, slug):
    model = Post
    template_name = 'forum_app/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # print("aaaaaaaa", request.user)

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user   #this way you dont need to add the user field request.user
            # new_comment.active = True
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'model': model})