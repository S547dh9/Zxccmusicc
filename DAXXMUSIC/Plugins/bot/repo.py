from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωεℓ¢σмє ƒσя 𝚍𝚊𝚡𝚡 яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗚𝗥𝗢𝗨𝗣", url="https://t.me/ANIME_IMMORTAL"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Qweibie"),
          ],
               [
                InlineKeyboardButton("𝗕𝗢𝗧𝗦", url="https://t.me/FleX_Bots_News"),

],
[
              InlineKeyboardButton("𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬", url=f"https://t.me/EMXES_COMMUNITY"),
              InlineKeyboardButton("︎𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url=f"https://t.me/Flex_Support_Chat"),
              ],
              [
              InlineKeyboardButton("︎𝗪𝗔𝗜𝗙𝗨 𝗕𝗢 https://t.me/Grabbing_Your_Waifu_Bot", url=f""),
InlineKeyboardButton("𝗛𝗨𝗦𝗕𝗔𝗡𝗗𝗢 𝗕𝗢𝗧 ", url=f"https://t.me/Grabbing_Your_Husbando_Bot"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡G 𝗕𝗜𝗧", url=f""),
InlineKeyboardButton("𝗖𝗛𝗔𝗧𝗚𝗣𝗧", url=f"https://github.com/DAXXTEAM/DAXXCHATGPT"),
],
[
              InlineKeyboardButton("𝗔𝗡𝗜𝗠𝗘", url=f"https://t.me/Ongoing_Anime_Barlow"),
              InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘︎", url=f"https://github.com/DAXXTEAM/DAXXMOVIEBOT"),
              ],
              [
              InlineKeyboardButton("︎𝗘𝗠𝗫 𝗡𝗘𝗧𝗪𝗢𝗥𝗞", url=f"https://t.me/EMXES_NETWORK"),
InlineKeyboardButton("𝗞𝗔𝗠𝗨𝗜 𝗡𝗘𝗧𝗪𝗢𝗥𝗞", url=f"https://t.me/KAMUI_NETWORK"),
],
[
InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧 𝗕𝗢𝗧 ", url=f""),
InlineKeyboardButton("𝗦𝗘𝗔𝗥𝗖𝗛𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/SEARCH_BOT"),
],
[
InlineKeyboardButton("𝗖𝗖 𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/CC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/faa1f3ad7116e33d9f402.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/DAXXTEAM/DAXXMUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/DAXXTEAM/DAXXMUSIC) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/HEROKUFREECC)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


