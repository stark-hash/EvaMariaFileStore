class script(object):
    START_TXT = """ðð¨..ðð¨..Êá´ÊÊá´ {} ð, Éª'á´ á´á´á´¡á´Êê°á´Ê á´á´á´á´-ê°ÉªÊá´á´Ê Êá´á´ Êá´á´ á´á´É´ á´sá´ á´á´ á´s á´ á´á´á´á´-ê°ÉªÊá´á´Ê ÉªÉ´ Êá´á´Ê É¢Êá´á´á´ ....

Éªá´'s á´á´sÊ á´á´ á´sá´ á´á´; á´á´sá´ á´á´á´ á´á´ á´á´ Êá´á´Ê É¢Êá´á´á´ á´s á´á´á´ÉªÉ´, á´Êá´á´s á´ÊÊ, Éª á´¡ÉªÊÊ á´Êá´á´ Éªá´á´ á´á´á´ Éªá´s á´Êá´Êá´...ð¤

â ï¸á´á´Êá´ Êá´Êá´ á´Êá´á´á´ Êá´Êá´ Êá´á´á´á´É´ Êá´Êá´á´¡

Â©ï¸ðððððððððð ðð  <a href=https://t.me/HadidTG>Êá´á´Éªá´</a>"""
    HELP_TXT = """ð·ð´ð {}
ð·ð´ðð´ ð¸ð ðð·ð´ ð·ð´ð»ð¿ ðµð¾ð ð¼ð ð²ð¾ð¼ð¼ð°ð½ð³ð."""
    ABOUT_TXT = """ 
ððð¢ð¨ð§ ð ð¦ð
âµâµâµâµâµâµâµâµâµâµâµâµâµâµâµâµâµâµâµâµ
ââââââ° êªá¥êª®êªð½ êªð´á§ â±âââ±âÛªÛª
ââ­ââââââââââââââââ£ 
ââ£âª¼ ðð ðð¼ðð - <a href="https://t.me/AnAutoFilterBot"> á´Ê sá´Êá´É´É¢á´ </a>
ââ£âª¼ â¹ï¸âºï¸âï¸ - <a href="https://t.me/HadidTG"> Êá´á´Éªá´ </a>
ââ£âª¼ ðð²ð«ð»ðªð»ð»ð - ð¿ððð¾ð¶ðð°ð¼
ââ£âª¼ ððªð·ð°ð¾ðªð°ð® - ð¿ððð·ð¾ð½ ð¹
ââ£âª¼ ððªð½ðª ððªð¼ð® - ð¼ð¾ð½ð¶ð¾ ð³ð±
ââ£âª¼ ðð¸ð½ ð¼ð®ð»ð¿ð®ð» -  ð·ð´ðð¾ðºð
ââ£âª¼ ðð¾ð²ðµð­ ð¢ð½ðªð½ð¾ð¼ - v2.0.1 [ ð±ð´ðð° ]
ââ°ââââââââââââââââ£ âââââââââââââââââââââ±âÛªÛª"""
    SOURCE_TXT = """<b>NOTE:</b> 
- Source - https://t.me/ippokittumennthonunnu/4 

<b>DEVS:</b>
- <a href=https://t.me/HadidTG>Êá´á´Éªá´</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and á´Ê sá´Êá´É´É¢á´ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. á´Ê sá´Êá´É´É¢á´ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- á´Ê sá´Êá´É´É¢á´ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. á´Ê sá´Êá´É´É¢á´ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/TG_PaulBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    FILESTORE_TXT = """<b>ð File Store</b>

A Module To Get Sharable Link For Any Telegram Media 

ð Avaible Commands:

â /link :- Reply To Any Telegram Media"""
    INFO_TXT = """<b>ð¤ User Information</b>

A Module To Fetch Telegram User Info

ð Avaible Commands:

â /info :- To Get User Information

â /id :- To Get Telegram User ID

â ï¸ Note : This Commands Be Used In PM's And Groups"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of á´Ê sá´Êá´É´É¢á´

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specified user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â ðð¾ðð°ð» ðµð¸ð»ð´ð: <code>{}</code>

â ðð¾ðð°ð» ððð´ðð: <code>{}</code>

â ðð¾ðð°ð» ð²ð·ð°ðð: <code>{}</code>

â ððð´ð³ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±

â ðµðð´ð´ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±"""
    LOG_TEXT_G = """#NewSá´Êá´É´É¢á´Group
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewSá´Êá´É´É¢á´User
ID - <code>{}</code>
Name - {}
"""
