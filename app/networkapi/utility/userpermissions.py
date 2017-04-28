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


def set_user_permissions(backend, user, response, *args, **kwargs):
    """
    This is a social-auth pipeline function for automatically
    setting is_superuser permissions when a user logs in from a
    known-to-be mozilla account.
    """

    attrs = vars(user)
    print(', '.join("%s: %s" % item for item in attrs.items()))

    if user.email and ismoz(user.email):
        user.is_staff = True

        # For some reason just is_staff is not enough to get
        # access to the admin view right now, and the 
        # is_superuser flag needs to also be set to True...
        user.is_superuser = True

        user.save()
