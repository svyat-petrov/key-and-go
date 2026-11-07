import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    vk_api_token: str
    vk_group_id: str
    vk_api_version: str
    access_secret_word: str
    support_contact: str
    log_level: str


def read_settings() -> Settings:
    required = [
        "VK_API_TOKEN",
        "VK_GROUP_ID",
        "VK_API_VERSION",
        "ACCESS_SECRET_WORD",
        "SUPPORT_CONTACT",
    ]
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        raise RuntimeError(f"Отсутствуют переменные окружения: {', '.join(missing)}")

    return Settings(
        vk_api_token=os.environ["VK_API_TOKEN"],
        vk_group_id=os.environ["VK_GROUP_ID"],
        vk_api_version=os.environ["VK_API_VERSION"],
        access_secret_word=os.environ["ACCESS_SECRET_WORD"],
        support_contact=os.environ["SUPPORT_CONTACT"],
        log_level=os.environ.get("LOG_LEVEL") or "INFO",
    )
