from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()
bot = Bot(token='5491402580:AAEL906KeUMTaSf7XQ6PSHvLAfeMGBfKEsg')
dp = Dispatcher(bot,storage=storage)
