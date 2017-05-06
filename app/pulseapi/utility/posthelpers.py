from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model


# API ROUTE: /nonce
def nonce(request):
    """
    set a new random nonce to act as form post identifier
    and inform the user what this value is so they can use
    it for signing their POST for a new entry.
    """
    if not request.user.is_authenticated():
        return HttpResponse('Not authorized', status=403)

    request.session['nonce'] = get_user_model().objects.make_random_password()

    return render(request, 'users/nonce.json', {
        'nonce': request.session['nonce']
    }, content_type="application/json")


# API ROUTE: /userstatus
def userstatus(request):
    """
    Get the login status associated with a session. If the
    status is "logged in", also include the user name and
    user email. NOTE: these values should never be persistently
    cached by applications, for obvious reasons.
    """
    username = False
    email = False
    loggedin = request.user.is_authenticated()

    if loggedin:
        username = request.user.username
        email = request.user.email

    return render(request, 'users/userstatus.json', {
        'username': username,
        'email': email,
        'loggedin': loggedin
    }, content_type="application/json")
