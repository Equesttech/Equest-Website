from django.shortcuts import render
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from hitcount.views import HitCountDetailView
from django.views import generic
from .models import Post


def category_list(request):

    categories = Category.objects.all()
    return render(request, 'classroom/blog-home.html', {'categories': categories})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'classroom/blog-home.html.html', {'category': category})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # count_hit = True
    template_name = 'classroom/blog-home.html'
    paginate_by = 3


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'


# Comment posted

# def post_detail(request, slug, ):
#     template_name = 'classroom/blog-single.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True, parent__isnull=True)
#     new_comment = None
#     parent_obj = None
#
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             parent_obj = None
#             # get parent comment id from hidden input
#             try:
#                 # id integer e.g. 15
#                 parent_id = int(request.POST.get('parent_id'))
#             except:
#                 parent_id = None
#             # if parent_id has been submitted get parent_obj id
#             if parent_id:
#                 parent_obj = Comment.objects.get(id=parent_id)
#                 # if parent object exist
#                 if parent_obj:
#                     # create replay comment object
#                     reply_comment = comment_form.save(commit=False)
#                     # assign parent_obj to replay comment
#                     reply_comment.parent = parent_obj
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#             return HttpResponseRedirect(post.get_absolute_url())
#
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})


def post_detail(request, slug):
    template_name = 'classroom/blog-single.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})