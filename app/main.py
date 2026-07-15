import asyncio
from aiogram import Bot, Dispatcher
from loguru import logger

from app.config import settings
from app.handlers.start import router as start_router
from app.handlers.evaluate import router as evaluate_router

async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(evaluate_router)

    logger.info("🚀 Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
