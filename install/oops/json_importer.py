from oops.json_types import JsonView

def sample_function(x: JsonView) -> bool:
    return isinstance(x, dict)
