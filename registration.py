from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

class Phone(StatesGroup) :
    name=State()
    model=State()
    character=State()
    photo=State()
    price=State()
    status=State()

