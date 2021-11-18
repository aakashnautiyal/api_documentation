def docstring_parameter(*args, **kwargs):
    """
    Docstring function to append Host URL to Swagger docstring
    :param args: any blank {} to be appended
    :param kwargs: any keys to be appended
    :return: updated doc-string
    """
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*args, **kwargs)
        return obj

    return dec
