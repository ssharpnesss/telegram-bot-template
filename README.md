# Telegram Bot Template

![Telegram](https://img.shields.io/badge/Telegram-26A5E4?logo=telegram&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram-3.x-2CA5E0?logo=python&logoColor=white)
![aiogram-dialog](https://img.shields.io/badge/aiogram--dialog-2.x-4CAF50?logo=python&logoColor=white)

Стартовый шаблон Telegram-бота на Python, aiogram и Redis. Содержит базовую структуру приложения без пользовательских моделей и интеграций.

## Требования

- Python 3.12–3.14
- Poetry
- Redis

## Установка

```bash
git clone https://github.com/ssharpnesss/telegram-bot-template.git
cd telegram-bot-template
poetry install
```

## Настройка

Скопируйте пример конфигурации:

```bash
cp config.toml.example config.toml
```

Создайте `.env` в корне проекта:

```env
BOT_TOKEN=your-telegram-bot-token
```

Укажите параметры Redis в `config.toml`. Секрет бота берётся из `BOT_TOKEN`, а не из TOML. Не коммитьте `.env` и личные конфиги.

## Запуск

```bash
poetry run python -m app
```

Можно передать путь к TOML:

```bash
poetry run python -m app --config path/to/config.toml
```

Redis должен быть запущен и доступен по адресу из конфигурации.

## Структура

```text
app/
├── dialogs/
├── filters/
├── handlers/
│   ├── admin/
│   └── user/
├── middlewares/
├── config.py
├── arguments.py
└── __main__.py
```

Добавьте собственные обработчики, модели, миграции и интеграции по мере необходимости.

## Лицензия

Смотрите [LICENSE](LICENSE) и замените поле copyright holder на своё имя или организацию.
