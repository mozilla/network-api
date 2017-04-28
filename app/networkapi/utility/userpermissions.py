from django.contrib.sites.models import Site
from mezzanine.core.models import SitePermission


def ismoz(email):
    """
    This function determines whether a particular email address is a
    mozilla address or not. We strictly control mozilla.com and
    mozillafoundation.org addresses, and so filtering on the email
    domain section using exact string matching is acceptable.
    """
    if email is None:
        return False

    parts = email.split('@')
    domain = parts[1]

    if domain == 'mozilla.com':
        return True

    if domain == 'mozillafoundation.org':
        return True

    return False


def add_user_to_main_site(user):
    """
    make sure a user has permissions to look at the main site.
    """

    sites = Site.objects.all()
    main_site = sites[0]

    permissions = False

    try:
        siteperms = SitePermission.objects.filter(user=user)
        permissions = siteperms[0]
    except:
        permissions = SitePermission.objects.create(user=user)

    permissions.sites.add(main_site)


def set_user_permissions(backend, user, response, *args, **kwargs):
    """
    This is a social-auth pipeline function for automatically
    setting is_superuser permissions when a user logs in from a
    known-to-be mozilla account.
    """

    if user.email and ismoz(user.email) and user.is_staff is False:
        user.is_staff = True
        user.save()
        add_user_to_main_site(user)
