from telegram import InlineKeyboardButton

country_tag = ["fa" ,"en","ar","ru","fr","it","zh-CN","de","es"]
country_name = ["فارسي-🇮🇷","انگليسي-🏴󠁧󠁢󠁥󠁮󠁧󠁿","عربي-🇦🇪","روسيه-🇷🇺","فرانسوي-🇫🇷","ايتاليايي-🇮🇹","چيني-🇨🇳","آلماني-🇩🇪","اسپانيايي-🇪🇸"]
    

dict_msg = {
  
    "change_trans_to":" زبان ترجمه به {} تغيير كرد ",
    "user_msg" : "",
    "user_msg_id":0,
    "user_chat_id":0,
    "user_to_lang" : "en",
    "start_msg" : """👋سلام{}عزیز
\n
به ربات مترجم سريع خوش اومدي🥳
.""" ,
    "menu":"🆎 ————————————> 🈯️",
 
    "start_msg4" : """“({})زبان ترجمه فعلی\n  زبان مورد نظر خود را انتخاب کنید""",
   
    "start_msg2":"متن خود را وارد کنید:",
    "info_msg" : """⚙️            بخش تنظيمات              ⚙️
\n
در اين بخش شما ميتوانيد زبان ترجمه مورد نياز خود را انتخاب كنيد.            
(به صورت پيش فرض انگليسي ميباشد)
\n
       🆎             بخش ترجمه                🈯️
\n
در اين بخش شما متن خود را ارسال كرده و به سادگي آن را ترجمه شده دريافت ميكنيد 😎
\n 
                       ⚠️توجه ⚠️
\n
اين ربات اپن سورس ميباشد و سورس كد در گيت هاب بارگزاري شده است .""",

    "settings_btn" : [[
    InlineKeyboardButton("بازگشت", callback_data="back")
    ,InlineKeyboardButton("راهنما",callback_data="info")],
    [InlineKeyboardButton(country_name[0],callback_data="fa")] ,
    [InlineKeyboardButton(country_name[1],callback_data="en")],
    [InlineKeyboardButton(country_name[2],callback_data="ar")],
    [InlineKeyboardButton(country_name[3],callback_data="ru")],
    [InlineKeyboardButton(country_name[4],callback_data="fr")],
    [InlineKeyboardButton(country_name[5],callback_data="it")],
    [InlineKeyboardButton(country_name[6],callback_data="zh-CN")],
    [InlineKeyboardButton(country_name[7],callback_data="de")],
    [InlineKeyboardButton(country_name[8],callback_data="es")]],
    
}
