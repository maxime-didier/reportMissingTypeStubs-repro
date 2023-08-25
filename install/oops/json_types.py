from typing import Union, Any
from collections.abc import Sequence, Mapping

# JsonView = Union[None, int, float, str, 'JsonArrayView', 'JsonObjectView']
# JsonArrayView = Sequence[JsonView]
# JsonObjectView = Mapping[str, JsonView]

# Apparently, this is enough, a non-recursive type "works" too
JsonView = Union[None, int, float, str, Sequence[Any], Mapping[str, Any]]
