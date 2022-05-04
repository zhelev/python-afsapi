import typing as t
import xml.etree.ElementTree as ET


def unpack_xml(root: t.Optional[ET.Element], key: str) -> t.Optional[str]:
    if root:
        element = root.find(key)

        if element is not None and hasattr(element, "text"):
            if element.text is not None:
                return str(element.text)

    return None


A = t.TypeVar("A")
B = t.TypeVar("B")


def maybe(
    val: t.Optional[A], fn: t.Union[t.Callable[[A], B], t.Type[B]]
) -> t.Optional[B]:
    if val is not None:
        return fn(val)  # type: ignore
    return None
