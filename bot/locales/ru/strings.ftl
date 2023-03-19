# without @ !
bot-username = my_id_bot

# do not translate!
bot-group-deeplink = https://t.me/{bot-username}?startgroup=id

source-code-link = https://github.com/MasterGroosha/my-id-bot

cmd-start =
    Ваш Telegram ID: { $id }
    Помощь и исходники: /help

# Used in strings like "This channel id is xxx"
supergroup = супергруппа
group = группа
channel = канал
user = пользователь
bot = бот

any-chat = Это { $type } с ID { $id }

cmd-id-pm = Ваш Telegram ID: { $id }
cmd-id-group-topic-id = Это топик с ID { $id }
cmd-id-group-as-channel = И вы отправили это сообщение от имени канала с ID { $id }

cmd-help =
    Этот бот предназначен для получения ID разных сущностей в Telegram:

    • Перешлите сообщение из канала, чтобы узнать его ID;
    • Перешлите сообщение от анонимного администратора супергруппы, чтобы узнать ID этой супергруппы;
    • Перешлите сообщение от юзера, чтобы узнать его/её ID (если они не запретили это);
    • Перешлите сообщение от бота, чтобы узнать его ID;
    • Отправьте стикер, чтобы узнать его file_id (их можно использовать с любыми ботами);
    • <a href="{bot-group-deeplink}">Добавьте бота в группу</a>, чтобы узнать её ID (бот также сообщит о миграции группы в супергруппу);
    • Попробуйте бота в инлайн-режиме, чтобы отправить свой Telegram ID в любой чат.

    Исходники бота: { source-code-link }

group-to-supergroup =
    Группа обновлена до супергруппы.
    Старый ID: { $old_id }
    Новый ID: { $new_id }

inline-mode-title = Ваш ID { NUMBER($id, useGrouping: 0) }
inline-mode-description = Нажмите, чтобы отправить его в текущий чат
inline-mode-text = Мой Telegram ID { $id }
inline-mode-tryme = Попробуйте меня в ЛС >>>

sticker-id = ID этого стикера: { $id }
sticker-id-extended =
    ID этого стикера
    { $id }
    В настоящий момент только айди стикеров можно использовать любыми ботами.

user-id-hidden =
    Этот пользователь <b>скрыл</b> свой айди при пересылке.
    <a href="https://telegram.org/blog/unsend-privacy-emoji#anonymous-forwarding">Подробнее об этой фиче</a>.

# Commands in UI (when you press "/" or "Menu" button)
cmd-hint-id-pm = Узнать свой ID
cmd-hint-id-group = Узнать ID этой группы
cmd-hint-help = Справка и исходники
