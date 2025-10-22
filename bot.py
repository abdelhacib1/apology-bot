from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio
import os  # ضروري لإحضار التوكن من البيئة

# ===== رسائل الاعتذار =====
messages = [
    "Hey habit nqolek haja b hada lbot teichi aqray w afhmini",
    "First qbel kolch eandi 3ans doka w ana nhabek kont nchofk daymen fihom bla matkoni elabalk 3asitk kter mn ay bnadem mais jamais drt fi bali nkon meak wla kan eandi courage bach nji l eandk ejbtini bzf w mahabitch ndiy3k mais daymen kont nhes bli mafihach maelabalich so raht eand rebi pcq hiwa kan éspoir lwahid taei bach nkon meak…",
    "Ki kont nchof fik f hado 3ans erft bzf swalh elik w habitek bzf bzf konti tefla perfect w hayla fi eini chaba sportive w khatiha lmachakil w lhaja important mrabya kont nchofk w elabali bli nti nas mlah malgré wach kano yhdro elik mais khayert mnsamaech l nas w kont daymen ndifondi elik malgré makontich terfini aslan konti jozi eliya mais nbqa chad kolch w mnqder ndir walo",
    "So elabali bli qstek b hadrti w ljeste taei hadak nhar pcq drt haja grv eiyana mais machi qasdii wlh machi maenaha manich mqadrek wla manich mdayer fik confiance smhili ela wach ja mni kont f moment eiyan ghltt fih meak w nesta3ref b lghata taeii",
    "Mais wlh nhabek bzf bzf w ndir fik confiance w qimtek ghalya eandi eziza eliya bzf bzf rani ferhan li habitini w drtili qima f hyatek w nkreh ki nza3fek wla nqisk bzf rahi ghaydtni rohi doka w rani hechman mnk",
    "So ida habiti jawzili hadi lghalta w khalina nkamlo pcq i need u in my life hab nkon meak nti brk pcq siw kem i hemmlegh grv hayla nti",
    "Lukan marakich eziza eliya mandirch hada gae bach tsmhili mais testahli kter wlh smhili luna",
    "smhili rah nkon ممتن لوجودك w nrigliw hadi la situation binatna"
]

# ===== أوامر البوت =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("نكمل", callback_data="msg_0")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(messages[0], reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    if data.startswith("msg_"):
        index = int(data.split("_")[1]) + 1
        if index < len(messages):
            keyboard = [[InlineKeyboardButton("واصل", callback_data=f"msg_{index}")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await asyncio.sleep(1)
            await query.edit_message_text(messages[index], reply_markup=reply_markup)
        else:
            keyboard = [[InlineKeyboardButton("راسل إسلام", url="https://t.me/abdelhacib")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await asyncio.sleep(1)
            await query.edit_message_text(messages[-1], reply_markup=reply_markup)

# ===== تشغيل التطبيق =====
def main():
    TOKEN = os.getenv("BOT_TOKEN")  # 🔥 اجلب التوكن من Environment Variables
    if not TOKEN:
        raise ValueError("⚠️ BOT_TOKEN not found in environment variables.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("✅ Bot started successfully...")
    app.run_polling()

if __name__ == "__main__":
    main()
