# without @ !
bot-username = my_id_bot

# do not translate!
bot-group-deeplink = https://t.me/{bot-username}?startgroup=id

source-code-link = https://github.com/MasterGroosha/my-id-bot

cmd-start =
    Ваш Telegram ID: { $id }
    Допомога та вихідний код: /help

    Ви також можете використовувати цього бота в інлайн-режимі! Спробуйте одну з кнопок нижче.
    Врахуйте, що бот відповідає на вашій мові лише в особистих повідомленнях і на англійській у всіх інших чатах.

cmd-start-inline-try-here = Спробувати тут
cmd-start-inline-try-other = Спробувати в іншому чаті

# Used in strings like "This channel id is xxx"
supergroup = супергрупа
group = група
channel = канал
user = користувач
bot = бот

any-chat = Це { $type } з ID { $id }

cmd-id-pm = Ваш Telegram ID: { $id }
cmd-id-group-topic-id = Це топік з ID { $id }
cmd-id-group-as-channel = І ви відправили це повідомлення від імені каналу з ID { $id }

cmd-help =
    Цей бот призначений для отримання ID різних об'єктів у Telegram:

    • Перешліть повідомлення з каналу, щоб дізнатися його ID;
    • Перешліть повідомлення від анонімного адміністратора супергрупи, щоб дізнатися ID цієї супергрупи;
    • Перешліть повідомлення від юзера, щоб дізнатися його/її ID (якщо вони не заборонили це);
    • Перешліть повідомлення від іншого бота або використайте його в інлайн-режимі, щоб дізнатись ID бота;
    • Відправте стікер, щоб дізнатись його file_id (надалі, цей file_id можна використовувати у будь-яких ботах);
    • <a href="{bot-group-deeplink}">Додайте бота до групи</a>, щоб дізнатись її ID (бот також повідомить про міграцію групи у супергрупу);
    • Спробуйте бота в інлайн-режимі, щоб надіслати свій Telegram ID у будь-який чат.

    Вихідний код бота: { source-code-link }

group-to-supergroup =
    Група перетворена у супергрупу.
    Старий ID: { $old_id }
    Новий ID: { $new_id }

inline-mode-title = Ваш ID { NUMBER($id, useGrouping: 0) }
inline-mode-description = Натисніть, щоб надіслати його у поточний чат
inline-mode-text = Мій Telegram ID { $id }
inline-mode-tryme = Спробуйте мене в особистих повідомленнях >>>

sticker-id = ID этого стикера: { $id }
sticker-id-extended =
    ID цього стікера
    { $id }
    У даний момент тільки айді стікерів можна використовувати у будь-яких ботах.

user-id-hidden =
    Цей користувач <b>приховав</b> свій айді при пересиланні.
    <a href="https://telegram.org/blog/unsend-privacy-emoji#anonymous-forwarding">Детальніше про цю фічу</a>.

# Commands in UI (when you press "/" or "Menu" button)
cmd-hint-id-pm = Дізнатись свій ID
cmd-hint-id-group = Дізнатись ID цієї групи
cmd-hint-help = Допомога ти вихідний код
