import telebot
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

def hello(message):
    msg_box = ['привет', 'хай', 'дарова', 'привки', 'здарова', 'прив']
    for i in msg_box:
        if i in message.text.lower():
            return True

def good_bye(message):
    msg_box = ['пока', 'бай бай', 'бб', 'поки', 'гуд бай', 'гуд бай', 'бай']
    for i in msg_box:
        if i in message.text.lower():
            return True

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я рекламный бот игры «๖ۣۜOrion» и его дискорд сервера. Пропиши /help, чтобы поссмотреть список команд.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/about - об «๖ۣۜOrion»\n"
                                      "/discord - ссылка на дискорд сервер\n"
                                      "/vk - ссылка на вк\n"
                                      "/ad_on_us - скриншот рекламы на наш сервер, с группы Ориона, где 150_000 подписчиков\n")

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, """Приветствую тебя, друг или подруга. Мы рекомендуем посетить замечательный сервер в Discord, посвященный игре «Орион». Орион – это игра, совмещающая элементы из Terraria и Minecraft.
Игра была создана в 2014 году и сначала получила популярность благодаря роликам на канале «1st1» в социальной сети ВКонтакте. Изначально игра была доступна в ВКонтакте и Одноклассниках, но в 2016 году разработчик продал игру компании Y8, а в 2018 году сервера были полностью удалены из ВКонтакте. Далее игра стала доступна только через переработанную версию «Orion Sandbox» от Y8, где не было онлайн-режима, и постепенно игра потеряла популярность. 
Однако появилось сообщество, возглавляемое Дмитрием Зиминым, который возродил игру. Он перевел «Orion Sandbox» с английского на русский язык и смог перенести игру на компьютер. Новое сообщество орионовцев начало набирать обороты, 
и в декабре 2023 года количество участников на Discord сервере перевалило за 1000 человек. Это стало возможным благодаря ютуберу по террарии «Svorob» (https://www.youtube.com/@Svorob), 
который создал короткий ролик о истории данной игры (он собрал: 150 тысяч просмотров, 15 тысяч лайков и 250 комментариев), с ссылкой на наш сервер в Discord (https://www.youtube.com/shorts/mHPwSehjPdo). 
Мы не останавливаемся на достигнутом и продолжаем набирать обороты, чтобы стать сильнее. Присоединяйтесь к нам – на сервере есть сама игра Орион. Также игра переписывается с ActionScript на JavaScript, что позволит добавить мультиплеер,
чего раньше в игре не было. На сервере царит приятная атмосфера, установлены нормальные правила, здесь веселые люди, доброжелательная администрация и модерация. Мы ждем всех вас, ведь вместе мы сила! Орионовцы, присоединяйтесь!\n

Создатели игры «Hide Online» - это команды разработчиков, и он связан с Русланом и Егором Блиновыми, которые создали Орион.

/discord - ссылка на дискорд сервер

/vk - ссылка на вк""")

@bot.message_handler(commands=['discord'])
def discord(message):
    bot.send_message(message.chat.id, "Наш ДС: https://discord.gg/JNkx2Q7473 (нас там свыше 1000 участников)")
    bot.send_photo(message.chat.id, photo=open('Наш ДС сервер по Ориону.png', 'rb'))

@bot.message_handler(commands=['vk'])
def vk(message):
    bot.send_message(message.chat.id, "Наша группа ВК: https://vk.com/alor418294")
    bot.send_photo(message.chat.id, photo=open('Группа ВК по Ориону.png', 'rb'))

@bot.message_handler(commands=['ad_on_us'])
def ad_on_us(message):
    bot.send_message(message.chat.id, "А вот и скриншот рекламы на нас, в группе по ориону, где свыше 150_000 подписчиков")
    bot.send_photo(message.chat.id, photo=open('Скриншот рекламы на нас.png', 'rb'))

@bot.message_handler(content_types=['text'], func=hello)
def hello(message):
    bot.send_message(message.chat.id,f"Приветики, {message.from_user.first_name} ❤️")

@bot.message_handler(content_types=['text'], func=good_bye)
def good_bye(message):
    bot.send_message(message.chat.id,"Покасики, пупс 😘")

@bot.message_handler(content_types=['text'])
def unknown command(message):
    bot.send_message(message.chat.id,"Прости, бро, я ещё не научился разговаривать полноценно 😞. Рассмотри список команд /help")

@bot.message_handler(content_types=['photo'])
def good_photo(message):
    bot.send_message(message.chat.id,"Хорошее фото 🥰")

bot.polling()