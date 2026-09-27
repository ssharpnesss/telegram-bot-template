import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
from redis.asyncio import Redis

from app.arguments import parse_arguments
from app.config import parse_config
from app.handlers import get_handlers
from app.middlewares import register_middlewares


async def main() -> None:
    arguments = parse_arguments()
    config = parse_config(arguments.config)

    redis = Redis(
        host=config.settings.redis_host,
        port=config.settings.redis_port,
        username=config.settings.redis_username,
        password=(
            config.settings.redis_password.get_secret_value()
            if config.settings.redis_password
            else None
        ),
    )
    storage = RedisStorage(
        redis=redis,
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )

    bot = Bot(
        token=config.bot.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode="HTML"),
    )
    dispatcher = Dispatcher(storage=storage)
    register_middlewares(dispatcher, config)
    dispatcher.include_router(get_handlers())

    try:
        await bot.delete_webhook(drop_pending_updates=config.settings.drop_pending_updates)
        await dispatcher.start_polling(bot, config=config)
    finally:
        await redis.aclose()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
