from networkapi.utility.decorators import debounce_and_throttle


@debounce_and_throttle(5, 15)
def build_static_site(sender, instance, **kwargs):
    print("Calling post_save_callback for {sender}".format(sender=sender))
