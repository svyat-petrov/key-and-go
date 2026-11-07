import time
from dataclasses import dataclass, field

MAX_FAILS = 3
COOLDOWN_SECONDS = 10 * 60
SESSION_TTL_SECONDS = 24 * 60 * 60

NEW = "NEW"
AUTHED = "AUTHED"


@dataclass
class Session:
    user_id: str
    state: str = NEW
    fails: int = 0
    last_activity: float = field(default_factory=time.monotonic)
    cooldown_until: float | None = None


class SessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, Session] = {}

    def _get(self, user_id: str) -> Session:
        session = self._sessions.get(user_id)
        if session is None:
            return Session(user_id)
        if time.monotonic() - session.last_activity > SESSION_TTL_SECONDS:
            return Session(user_id)
        return session

    def get_or_create(self, user_id: str) -> Session:
        session = self._get(user_id)
        session.last_activity = time.monotonic()
        self._sessions[user_id] = session
        return session

    def authorize(self, user_id: str) -> None:
        session = self._sessions[user_id]
        session.state = AUTHED
        session.fails = 0
        session.cooldown_until = None

    def register_fail(self, user_id: str) -> int:
        session = self._sessions[user_id]
        session.fails += 1
        if session.fails >= MAX_FAILS:
            session.cooldown_until = time.monotonic() + COOLDOWN_SECONDS
            return 0
        return MAX_FAILS - session.fails

    def is_blocked(self, user_id: str) -> bool:
        session = self._sessions.get(user_id)
        if session is None or session.cooldown_until is None:
            return False
        if time.monotonic() >= session.cooldown_until:
            session.cooldown_until = None
            session.fails = 0
            return False
        return True

    def reset(self, user_id: str) -> Session:
        session = Session(user_id)
        self._sessions[user_id] = session
        return session
