class script(object):
    START_TXT = """𝐘𝐨..𝐘𝐨..ʜᴇʟʟᴏ {} 🙋, ɪ'ᴍ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ-ꜰɪʟᴛᴇʀ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴀs ᴀ ᴀᴜᴛᴏ-ꜰɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ....

ɪᴛ's ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴍᴇ; ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ, ᴛʜᴀᴛs ᴀʟʟ, ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴛʜᴇʀᴇ...🤓

⚠️ᴍᴏʀᴇ ʜᴇʟᴘ ᴄʜᴇᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ

©️𝐌𝐀𝐈𝐍𝐓𝐀𝐈𝐍𝐄𝐃 𝐁𝐘  <a href=https://t.me/HadidTG>ʜᴀᴅɪᴅ</a>"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """ 
𝗔𝗕𝗢𝗨𝗧 𝗠𝗦𝗚
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰ ꪖ᥇ꪮꪊ𝓽 ꪑ𝘴ᧁ ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ 𝙈𝙔 𝙉𝘼𝙈𝙀 - <a href="https://t.me/AnAutoFilterBot"> ᴅʀ sᴛʀᴀɴɢᴇ </a>
║┣⪼ Ⓓ︎Ⓔ︎Ⓥ︎ - <a href="https://t.me/HadidTG"> ʜᴀᴅɪᴅ </a>
║┣⪼ 𝓛𝓲𝓫𝓻𝓪𝓻𝓻𝔂 - 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
║┣⪼ 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮 - 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
║┣⪼ 𝓓𝓪𝓽𝓪 𝓑𝓪𝓼𝓮 - 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
║┣⪼ 𝓑𝓸𝓽 𝓼𝓮𝓻𝓿𝓮𝓻 -  𝙷𝙴𝚁𝙾𝙺𝚄
║┣⪼ 𝓑𝓾𝓲𝓵𝓭 𝓢𝓽𝓪𝓽𝓾𝓼 - v2.0.1 [ 𝙱𝙴𝚃𝙰 ]
║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍⊱❁۪۪"""
    SOURCE_TXT = """<b>NOTE:</b> 
- Source - https://t.me/ippokittumennthonunnu/4 

<b>DEVS:</b>
- <a href=https://t.me/HadidTG>ʜᴀᴅɪᴅ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ᴅʀ sᴛʀᴀɴɢᴇ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ᴅʀ sᴛʀᴀɴɢᴇ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- ᴅʀ sᴛʀᴀɴɢᴇ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ᴅʀ sᴛʀᴀɴɢᴇ supports buttons with any telegram media type.
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
    FILESTORE_TXT = """<b>📁 File Store</b>

A Module To Get Sharable Link For Any Telegram Media 

📚 Avaible Commands:

◉ /link :- Reply To Any Telegram Media"""
    INFO_TXT = """<b>👤 User Information</b>

A Module To Fetch Telegram User Info

📚 Avaible Commands:

◉ /info :- To Get User Information

◉ /id :- To Get Telegram User ID

⚠️ Note : This Commands Be Used In PM's And Groups"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ᴅʀ sᴛʀᴀɴɢᴇ

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>

★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>

★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>

★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱

★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewSᴛʀᴀɴɢᴇGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewSᴛʀᴀɴɢᴇUser
ID - <code>{}</code>
Name - {}
"""
