from threading import Timer

def debounce(wait):
    """
    A Decorator for debouncing a function's execution
    Original code was found here: https://gist.github.com/walkermatt/2871026
    """
    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_fn():
                fn(*args, **kwargs)
            try:
                debounced.t.cancel()
            except(AttributeError):
                pass
            debounced.t = Timer(wait, call_fn)
            debounced.t.start()
        return debounced
    return decorator
