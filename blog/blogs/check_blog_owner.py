from django.http import Http404


def check_blog_owner(blog, request):
    """Checks the owner of the topic and return error 404 if not correct user."""
    if blog.owner != request.user:
        raise Http404
