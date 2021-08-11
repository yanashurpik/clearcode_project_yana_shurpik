import time


class RequestTimeout:
    __last_request = time.time()
    __timeout = None

    @staticmethod
    def request_timer(timeout=1):
        RequestTimeout.__timeout = timeout

        def request_timer_decor(request_method):
            def wrapper(*args, **kwargs):
                if time.time() - RequestTimeout.__last_request < RequestTimeout.__timeout:
                    time.sleep(RequestTimeout.__timeout - (time.time() - RequestTimeout.__last_request))
                RequestTimeout.__last_request = time.time()
                return request_method(*args, **kwargs)

            return wrapper

        return request_timer_decor
