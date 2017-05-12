from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, get_user_model
from django.template import Template, Context


def set_random_value(request, propname):
    """
    Set up a random value for the session state,
    used in authentication validation.
    """

    request.session[propname] = get_user_model().objects.make_random_password()


def login_redirect(request):
    """
    Specific login call for logging in through another front-end
    """
    original_url = request.GET.get('original_url', False)

    if original_url is False:
        set_random_value(request, 'state')
        original_url = request.session['state']

    # Get the real login URL from the social-auth system
    login_path_template = Template('{% url "social:begin" "google-oauth2" %}')
    login_path = login_path_template.render(Context({}))
    login_url = login_path + '?next=' + original_url

    return redirect(login_url)


def force_logout(request):
    """
    An explicit logout route.
    """
    user = request.user

    if user.is_authenticated:
        logout(request)

    return HttpResponse("User is no longer logged in.")


def nonce(request):
    """
    set a new random nonce to act as form post identifier
    and inform the user what this value is so they can use
    it for signing their POST for a new entry.
    """
    if not request.user.is_authenticated():
        return HttpResponse('Not authorized', status=403)

    set_random_value(request, 'nonce')

    return render(request, 'users/nonce.json', {
        'nonce': request.session['nonce']
    }, content_type="application/json")


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


# And then, finally, the url patterns
urlpatterns = [
    url(r'^login/', login_redirect, name="A login proxy for off-site clients"),
    url(r'^logout/', force_logout, name="A logou proxy for off-site clients"),
    url(r'^nonce/', nonce, name="get a new nonce value"),
    url(r'^userstatus/', userstatus, name="get current user information"),
]
