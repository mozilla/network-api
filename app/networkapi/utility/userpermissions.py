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
    setting is_staff permissions when a user logs in from a 
    known-to-be mozilla account.
    """

    if user.email and ismoz(user.email):
        if user.is_staff == False:
            user.is_staff = True
            user.save()
