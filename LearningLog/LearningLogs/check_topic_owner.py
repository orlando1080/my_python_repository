from django.http import Http404


def check_topic_owner(topic, request):
    """Checks the owner of the topic and return error 404 if not correct user."""
    if topic.owner != request.user:
        raise Http404
