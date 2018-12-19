def decor(asterisco):
    def _decor(func):
        def wrap():
            if asterisco:
                print("*" * 12)
            else:
                print("=" * 12)

            func()

            if asterisco:
                print("*" * 12)
            else:
                print("=" * 12)

        return wrap

    return _decor


@decor(asterisco=False)
def print_text():
    print('Hola mundo')

print_text()