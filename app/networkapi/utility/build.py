from networkapi.utility.debounce import debounce


@debounce(10)
def build_static_site(sender, instance, **kwargs):
    print("Calling post_save_callback for {sender}".format(sender=sender))
