def log(debug):
    def _log(f):
        def wrap(a, b):
            if debug:
                print('valor a:', a)
                print('valor b:', b)

            return  f(a, b)
        return wrap

    return _log

@log(debug=True)
def suma(a, b):
    return a + b

print(suma(1,2))