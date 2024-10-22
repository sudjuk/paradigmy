def field(items, *args):
    assert len(args) > 0
    for item in items:
        result = {}
        for arg in args:
            if item.get(arg) is not None:
                result[arg] = item[arg]
        if len(result) > 0:
            yield result
        elif len(args) == 1:
            yield item.get(args[0])