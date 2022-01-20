import typing as t
import xml.etree.ElementTree as ET


def unpack_xml(root: ET.Element | None, key: str) -> str | None:
    if root:
        element = root.find(key)

        if element is not None and hasattr(element, "text"):
            if element.text is not None:
                return str(element.text)

    return None


A = t.TypeVar("A")
B = t.TypeVar("B")


def maybe(val: A | None, fn: t.Union[t.Callable[[A], B], t.Type[B]]) -> B | None:
    if val is not None:
        return fn(val)  # type: ignore
    return None
