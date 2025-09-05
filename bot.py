import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Configura o logging para ver erros
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Pega o token de uma variável de ambiente (mais seguro!)
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("A variável de ambiente BOT_TOKEN não foi configurada!")

# Função para o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Olá! Eu sou um bot. Me mande uma mensagem e eu vou repeti-la!"
    )

# Função para repetir mensagens
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Você disse: {update.message.text}"
    )

if __name__ == '__main__':
    # Cria a aplicação do bot
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Adiciona os handlers (comandos e mensagens)
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    # Inicia o bot
    print("Bot iniciado e rodando...")
    application.run_polling()