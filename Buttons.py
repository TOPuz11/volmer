from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup,CallbackQuery


def EnterRoll() :
    btn=ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=KeyboardButton("👨‍💻 Admin")
    btn2=KeyboardButton("👤 User")
    btn.add(btn1,btn2)
    return btn
def Usermenu():
    btn=ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=KeyboardButton("Samsung")
    btn2=KeyboardButton("Iphone")
    btn3=KeyboardButton("Mi")
    btn4=KeyboardButton("Vivo")
    btn5=KeyboardButton("Oppo")
    btn6=KeyboardButton("Infinix")
    btn.add(btn1,btn2)
    btn.add(btn3,btn4)
    btn.add(btn5,btn6)
    return btn
    
    

def AdminBtn() :
    btn=InlineKeyboardMarkup()
    btn1=InlineKeyboardButton(text="➕ Qo'shish",callback_data="add")  
    btn2=InlineKeyboardButton(text="🗑 O'chirish",callback_data="delate")  
    btn.add(btn1,btn2)
    return btn
def Companies() :
    btn=InlineKeyboardMarkup(width=3)
    sam=InlineKeyboardButton(text="Samsung",callback_data="Samsung")
    iph=InlineKeyboardButton(text="Iphone",callback_data="Iphone")
    opp=InlineKeyboardButton(text="Oppo",callback_data="Oppo")
    mi1=InlineKeyboardButton(text="MI/Redmi",callback_data="Mi")
    vvo=InlineKeyboardButton(text="Vivo",callback_data="Vivo")
    inf=InlineKeyboardButton(text="Infinix",callback_data="Infinix")
    btn.add(sam,iph,opp)
    btn.add(mi1,vvo,inf)
    return btn
def Agree():
    btn=InlineKeyboardMarkup(width=2)
    sam=InlineKeyboardButton(text="✅ Saqlash",callback_data="save")
    iph=InlineKeyboardButton(text="❌ Bekor qilish",callback_data="cancel")
    btn.add(sam,iph)
    return btn
def PhonesList(phones) :
    btn=InlineKeyboardMarkup()
    for row in phones:
        btn.add(InlineKeyboardButton(text="📱 "+str(row[1])+" "+str(row[2]),callback_data=row[0]))
    return btn