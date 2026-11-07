from collections.abc import Iterator
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Button:
    id: str
    label: str


@dataclass(frozen=True)
class IncomingMessage:
    user_id: str
    text: str


@dataclass(frozen=True)
class IssuedKey:
    value: str


class MessageGateway(Protocol):
    def poll_events(self) -> Iterator[IncomingMessage]: ...
    def send_text(self, user_id: str, text: str, buttons: list[Button] | None = None) -> None: ...
    def send_image(self, user_id: str, image: bytes, caption: str = "") -> None: ...


class KeyProvider(Protocol):
    def issue_key(self, user_ref: str) -> IssuedKey: ...


class QrRenderer(Protocol):
    def render(self, payload: str) -> bytes: ...
