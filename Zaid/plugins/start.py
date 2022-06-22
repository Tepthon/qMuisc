from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
اهلا! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
*** أنا بوت بسيط لإدارة الموسيقى والتليفزيون ** ** يمكنني تشغيل الأغاني بصوتك ** ** يمكنني منع كتم صوت كل مستخدمين ** ** لديّ جميع الميزات التي تحتاج إلى بوتقة موسيقية ** ** هذا الروبوت يعتمد على التليثون. يوفر المزيد من الاستقرار من الروبوتات الأخرى **! ** يمكنني القيام بأشياء أخرى مثل الدبابيس وغيرها **
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
X ** انقر على زر المساعدة لمزيد من المعلومات X **.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ اضفني إلى مجموعتك", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 كود السورس", "https://github.com/Tepthon/qMusic")],
        [Button.url("🗣️ كروب الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("المساعدة والأوامر", data="help")]])
       return

    if event.is_group:
       await event.reply("**مرحباً! ما زلت على قيد الحياة ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ اضفني إلى مجموعتك", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 كود السورس", "https://github.com/Tepthon/qMuisc")],
        [Button.url("🗣️ كروب المساعدة", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("المساعدة والأوامر", data="help")]])
       return
