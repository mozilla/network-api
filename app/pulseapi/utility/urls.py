from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, get_user_model
from django.urls import reverse


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

    # make sure to clear the current auth for the user, if authed
    user = request.user
    if user.is_authenticated:
        logout(request)

    # Get the real login URL from the social-auth system
    login_url = reverse("social:begin", args=["google-oauth2"])

    # Make sure to redirect to the post-login local proxy route
    login_url = login_url + '?next=' + reverse('proxy-post-login')
    
    # Which can then forward the client to the original url
    original_url = request.GET.get('original_url', '/admin')
    login_url = login_url + + '?original_url=' + original_url

    request.session['original_url'] = original_url

    return redirect(login_url)


def post_login_redirect(request):
    """
    This extra step is necessary because gauth doesn't like
    doing external redirects. So we have a local proxy route
    that can be called, with the caveat that the original url
    gets cached in the session object and the original url that
    was passed in prior to authentication has to match the
    url that is found when finalising login.
    """
    original_url = request.GET.get('original_url', '/admin')
    session_original_url = request.session['original_url']

    request.session['original_url'] = False

    if original_url == session_original_url:
        return redirect(original_url)

    return redirect('/admin')


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
    url(r'^login/', login_redirect, name="proxy-login"),
    url(r'^postlogin/', post_login_redirect, name="proxy-post-login"),
    url(r'^logout/', force_logout, name="proxy-logout"),
    url(r'^nonce/', nonce, name="get a new nonce value"),
    url(r'^userstatus/', userstatus, name="get current user information"),
]
