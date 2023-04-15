import asyncio,aiohttp
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup,CallbackQuery
from aiogram.types import Message
from aiogram.utils import executor
import sqlite3
import random
import logging
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from registration import FSMContext, State, StatesGroup, MemoryStorage, Phone
import Buttons
BOT_TOKEN = '5615273583:AAE56__6E2qo7YDX5VcX2hSMQubax9GiRuA' 
loop = asyncio.get_event_loop()
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop) 
admins=[2115654447,5243034955]
models=["Samsung","Iphone","Mi","Vivo","Oppo","Infinix"]
tel_mod=[]
tel_xar=[]
tel_link=[]
tel_narx=[]
tel_id=[]
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE telefonlar
#                    (id INTEGER PRIMARY KEY,tel_model TEXT,tele_name TEXT, xarakter TEXT, ras_link TEXT, prinse INTEGER)''')

@dp.message_handler(commands=['start'])
async def start(message:Message):
    user_id=message.from_user.id
    if user_id in admins :
        await message.answer("Assalomu Aleykum Botga xush kelibsiz! Botdan foydalanish rolini tanlang:",reply_markup=Buttons.EnterRoll())
    else:
        await message.answer("Assalomu alaykum gurlan tumanidagi volmer dokoning botiga hush kelibsiz")
        await message.answer("O'zingizga kerakli bolimni tanlang:",reply_markup=Buttons.Usermenu())
        
                
        #await message.answer(" admin menyusiga kirdiz",reply_markup=Buttons.AdminBtn())
    
        #await message.reply("Assalomu alaykum Volmir dokonining botiga xush kelibsiz",reply_markup=klent_but)
@dp.message_handler(Text(equals='👨‍💻 Admin', ignore_case=True))
async def entry_admin(message: types.Message) :
      user_id=message.from_user.id
      if user_id not in admins :
          return
      await message.delete()
      await message.answer("Kerakli buyruqni tanlang:",reply_markup=Buttons.AdminBtn())
@dp.message_handler(Text(equals='👤 User', ignore_case=True))
async def entry_admin(message: types.Message) :
    user_id=message.from_user.id
    if user_id not in admins :
          
          return
    await message.delete()
    await message.answer("O'zingizga kerakli bolimni tanlang:",reply_markup=Buttons.Usermenu())
@dp.message_handler(content_types=['text'])
async def entry_user(message: types.Message):
    if message.text in models:
        
        

# malumotlarni ekranga chiqarish
        global tel_mod,tel_xar,tel_link,tel_narx
   
         
        cursor.execute("SELECT tele_name FROM telefonlar WHERE tel_model LIKE '%"+message.text+"%' ")

# malumotlarni ekranga chiqarish
        telmod = cursor.fetchall()   
 
        
        cursor.execute("SELECT xarakter FROM telefonlar WHERE tel_model LIKE '%"+message.text+"%' ")
        telxar=cursor.fetchall()
              
        cursor.execute("SELECT ras_link FROM telefonlar WHERE tel_model LIKE '%"+message.text+"%' ")
        telras=cursor.fetchall()
               
        cursor.execute("SELECT prinse FROM telefonlar WHERE tel_model LIKE '%"+message.text+"%' ")
        price=cursor.fetchall()
        
        
        for x in range(len(price)):
            l=telras[x][0]
            await bot.send_photo(message.chat.id,photo=l,caption=f"📱 {message.text} {telmod[x][0]}\n📊 {telxar[x][0]}\n💰 Narxi:{price[x][0]}")
        
    
    
    
      

@dp.callback_query_handler(lambda c: c.data == 'add')
async def one(call: types.CallbackQuery, state: FSMContext):
    await call.answer("")
    await call.message.delete()
    await bot.send_message(call.from_user.id,"Telefon turini belgilang:",reply_markup=Buttons.Companies())
    await Phone.name.set()

@dp.callback_query_handler(state=Phone.name)
async def getName(call: types.CallbackQuery, state: FSMContext):
    await call.answer("")
    await call.message.delete()
    await call.message.answer(call.data)
    async with state.proxy() as data :
        data['name']=call.data
    await call.message.answer("Mod nomini kiriting:")
    await Phone.next()

@dp.message_handler(content_types=['text'], state=Phone.model)
async def setModel(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data :
        data['model']=message.text
    await message.answer("Telefon harakteristikasi:")
    await Phone.next()
     
@dp.message_handler(content_types=['text'], state=Phone.character)
async def setCharacter(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data :
        data['character']=message.text
    await message.answer("Telefon rasmini yuboring:")
    await Phone.next()

@dp.message_handler(content_types=['photo'], state=Phone.photo)
async def setCharacter(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data :
        data['photo']=message.photo[0].file_id
    await message.answer("Telefon narxini kiriting:")
    await Phone.next()

@dp.message_handler(content_types=['text'], state=Phone.price)
async def setCharacter(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data :
        data['price']=message.text
    await message.answer("Kiritilgan ma'lumotlar:")
    msg="ℹ️ Komaniya:"+data['name']+"\n"
    msg+="📱 Model:"+data['model']+"\n"
    msg+="📊 Harakteristikasi:"+data['character']+"\n"
    msg+="💰 Narxi:"+data['price']
    await bot.send_photo(message.chat.id,photo=data['photo'],caption=msg,reply_markup=Buttons.Agree())
    await Phone.next()
    
@dp.callback_query_handler(lambda c: c.data=='save', state=Phone.status)
async def savephone(call: types.callback_query,state: FSMContext):
    await call.answer("")
    await bot.send_message(call.from_user.id,"saqlandi")
    async with state.proxy() as data :
        data['status']=call.data
    cursor.execute("INSERT INTO telefonlar (tel_model,tele_name, xarakter, ras_link, prinse) VALUES (?, ?, ?, ?, ?)",
               (data['name'],data['model'],data['character'],data['photo'],data['price']))
    await call.message.answer("O'zingizga kerakli bolimni tanlang:",reply_markup=Buttons.AdminBtn())
    await state.finish()
    conn.commit()
    

@dp.callback_query_handler(lambda c: c.data=='cancel', state=Phone.status)
async def savephone(call: types.callback_query,state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer("Kerakli buyruqni tanlang:",reply_markup=Buttons.AdminBtn())

@dp.callback_query_handler(lambda c: c.data=='delate')
async def deletephone(call:types.callback_query):
    await call.answer("")
    cursor.execute("SELECT * FROM `telefonlar`")
    phones=cursor.fetchall()
    await call.message.answer("o'chirmoqchi bolgan telefon modelini tanlang:",reply_markup=Buttons.PhonesList(phones))
    

@dp.callback_query_handler(lambda c: c.data.isdigit())
async def editphone(call:types.callback_query):
    
    await call.answer(str(call.data))
    msg=call.message.text
    cursor.execute('DELETE FROM `telefonlar` WHERE `id`=?',(call.data,))
    cursor.execute("SELECT * FROM `telefonlar`")
    phones=cursor.fetchall()
    await call.message.edit_text(msg,reply_markup=Buttons.PhonesList(phones))
    conn.commit()

    
    
        
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True) 