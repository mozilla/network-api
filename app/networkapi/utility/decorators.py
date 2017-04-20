import logging

from threading import Timer
from django.utils import timezone

logger = logging.getLogger(__name__)


def debounce_and_throttle(debounce_seconds, throttle_seconds):
    """
    A Decorator for debouncing and throttling a function's execution
    the original debounce strategy was found here:
    https://gist.github.com/walkermatt/2871026
    """
    def decorator(fn):
        def debounced_and_throttled(*args, **kwargs):
            def call_fn():
                now = timezone.now()
                try:
                    time_delta = now - debounced_and_throttled.last_called
                    if time_delta.seconds < throttle_seconds:
                        return logger.info(
                            'Can\'t build for {} more seconds'
                            .format(throttle_seconds - time_delta.seconds)
                        )
                except(AttributeError):
                    pass

                debounced_and_throttled.last_called = timezone.now()
                fn(*args, **kwargs)

            try:
                debounced_and_throttled.t.cancel()
            except(AttributeError):
                pass

            logger.info(
                'debouncing a build for {} seconds from now'
                .format(debounce_seconds)
            )
            debounced_and_throttled.t = Timer(debounce_seconds, call_fn)
            debounced_and_throttled.t.start()

        return debounced_and_throttled
    return decorator
