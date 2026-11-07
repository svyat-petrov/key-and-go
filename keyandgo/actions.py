from dataclasses import dataclass

from keyandgo.interfaces import Button


@dataclass(frozen=True)
class SendText:
    user_id: str
    text: str
    buttons: list[Button] | None = None


@dataclass(frozen=True)
class SendImage:
    user_id: str
    image: bytes
    caption: str = ""


@dataclass(frozen=True)
class SendConfig:
    user_id: str
    file: bytes
    caption: str = ""


type Action = SendText | SendImage | SendConfig
