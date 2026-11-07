# Идентификаторы кнопок: приходят в IncomingMessage.text при нажатии
KEY_TEXT = "key_text"
KEY_QR = "key_qr"
KEY_CONFIG = "key_config"
SUPPORT = "support"

# Подписи кнопок для клавиатуры
KEY_TEXT_LABEL = "Получить ключ текстом"
KEY_QR_LABEL = "Получить QR-код"
KEY_CONFIG_LABEL = "Получить конфиг"
SUPPORT_LABEL = "У меня лапки 😔"

# Тексты диалога; {плейсхолдеры} заполняет flow
START_PROMPT = "Напишите тайное слово:"
AUTH_OK = "Угадали! Выберите кнопку:"
WRONG_SECRET = "Упс, промах. Осталось попыток: {left}"
RATE_LIMITED = "Слишком много промахов. Приходите позже."
NEED_AUTH = "Так не получится. Сначала тайное слово."
KEY_TEXT_TEMPLATE = "Ура, ваш ключ:\n{key}"
QR_CAPTION = "Сканируйте QR-код"
CONFIG_CAPTION = "Скачайте файл и импортируйте в приложении"
SUPPORT_TEMPLATE = "Напишите в поддержку: {contact}"
ERROR_TEMPLATE = "Не получилось. Попробуйте позже или напишите {contact}"
