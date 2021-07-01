from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor
from Skyline import Skyline
import matplotlib.pyplot as plt
import pickle
import os


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="SkylineBot!\nBenvingut %s!" % update.effective_chat.first_name)


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="/start: inicia la conversa amb el Bot.\n"
             "/help: contesta amb una llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús.\n"
             "/author: escriu el nom complet de l'autor del projecte i el seu correu electrònic oficial de la facultat.\n"
             "/lst: mostra els identificadors definits i la seva corresponent àrea.\n"
             "/clean: esborra tots els identificadors definits.\n"
             "/save id: guarda un skyline definit amb el nom id.sky.\n"
             "/load id: carrega un skyline de l'arxiu id.sky.")


def author(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="SkylineBot!\n@ Àlex Núñez Rodríguez (alex.nunez.rodriguez@est.fib.upc.edu), 2020")


def lst(update, context):
    if 'skyline' in context.user_data and len(context.user_data['skyline'].identifiers) > 0:
        msg = ''
        for identifier in context.user_data['skyline'].identifiers:
            msg += '%s, area: %d\n' % (identifier, context.user_data['skyline'].identifiers[identifier].area)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=msg)
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='No hi ha identificadors definits.')


def clean(update, context):
    if 'skyline' in context.user_data and len(context.user_data['skyline'].identifiers) > 0:
        context.user_data['skyline'] = EvalVisitor()
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='S\'han esborrat tots els identificadors definits.')
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='No hi ha identificadors definits.')


def save(update, context):
    if 'skyline' in context.user_data and len(context.user_data['skyline'].identifiers) > 0:
        fullname = (update.effective_chat.first_name + update.effective_chat.last_name).replace(' ', '')
        if not os.path.exists(fullname):
            os.makedirs(fullname)
        file = open(os.path.join(fullname, context.args[0] + '.sky'), 'wb')
        pickle.dump(context.user_data['skyline'].identifiers[context.args[0]], file)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='S\'ha guardat l\'identificador definit a l\'arxiu %s.sky.' % context.args[0])
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='No hi ha identificadors definits.')


def load(update, context):
    fullname = (update.effective_chat.first_name + update.effective_chat.last_name).replace(' ', '')
    file = open(os.path.join(fullname, context.args[0] + '.sky'), 'rb')
    context.user_data['skyline'].identifiers[context.args[0]] = pickle.load(file)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='S\'ha carregat l\'identificador definit a l\'arxiu %s.sky.' % context.args[0])


def skyline(update, context):
    input_stream = InputStream(update.message.text)

    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()

    if 'skyline' not in context.user_data:
        context.user_data['skyline'] = EvalVisitor()
    try:
        result = context.user_data['skyline'].visit(tree)
    except ValueError:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Error: Valor incorrecte")

    x = []
    bins = []
    for i in range(len(result.buildings) - 1):
        x += [result.buildings[i][0]]*result.buildings[i][1]
        bins += [result.buildings[i][0]]
    bins += [result.buildings[len(result.buildings) - 1][0]]
    plt.hist(x, bins, color='r')
    locs, labels = plt.xticks()
    new_locs = []
    for i in range(1, len(locs) - 1):
        if locs[i].is_integer():
            new_locs.append(int(locs[i]))
    plt.xticks(new_locs)
    locs, labels = plt.yticks()
    new_locs = []
    for i in range(0, len(locs) - 1):
        if locs[i].is_integer():
            new_locs.append(int(locs[i]))
    plt.yticks(new_locs)
    plt.savefig('skyline.png')
    plt.clf()
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open('skyline.png', 'rb'))
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="area: %d\nalçada: %d" % (result.area, result.height))


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(MessageHandler(Filters.text, skyline))

updater.start_polling()
