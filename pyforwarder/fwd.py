import inspect

def forwarder(attr, methods=None, target_class=None):
    assert methods or target_class, "At least one of 'methods' or 'target_class' must be specified"
    if not methods:
        methods = [name for name, value in inspect.getmembers(target_class)
                   if not name.startswith("_") and inspect.ismethod(value) or inspect.isfunction(value)]

    def decorator(cls):

        def create_forwarder(methodname):
            def replacement_method(self, *args, **kwargs):
                underlying_class = getattr(self, attr)
                underlying_method = getattr(underlying_class, methodname)
                return underlying_method(*args, **kwargs)
            return replacement_method

        for methodname in methods:
            f = create_forwarder(methodname)
            f.__name__ = methodname
            if target_class:
                underlying_method = getattr(target_class, methodname)
                if hasattr(inspect, 'signature'):
                    sig = inspect.signature(underlying_method)
                else:
                    argspec = inspect.getargspec(underlying_method)
                    sig = inspect.formatargspec(*argspec)
                f.__doc__ = "Arguments: " + str(sig) + "\n\n" + inspect.getdoc(underlying_method)
            setattr(cls, methodname, f)

        return cls
    return decorator
