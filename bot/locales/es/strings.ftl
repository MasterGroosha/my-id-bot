# without @ !
bot-username = my_id_bot

# do not translate!
bot-group-deeplink = https://t.me/{bot-username}?startgroup=id

source-code-link = https://github.com/MasterGroosha/my-id-bot

cmd-start =
    Tu ID de Telegram es { $id }.
    Ayuda y código fuente: /help

    También puedes usar este bot en modo inline para compartir la ID! Prueba usando lso botones de abajo.
    Por favor, ten en cuenta que el bot usa tu idioma en privado y en inglés en cualquier otro chat.

cmd-start-inline-try-here = Intenta aquí
cmd-start-inline-try-other = Intenta en otro chat

# Used in strings like "This channel id is xxx"
supergroup = supergrupo
group = grupo
channel = canal
user = usuario
bot = bot

any-chat = Esta { $type } ID es { $id }

cmd-id-pm = Tu ID de Telegram es { $id }.
cmd-id-group-topic-id = La ID de este grupo es { $id }.
cmd-id-group-as-channel = Y has envido este mensaje de  un canal con ID { $id }.

cmd-help =
    Usa este bot para obtener la ID de diferentes entidades en Telegram:

    • Reenvía un mensaje de un canal para obtener la ID del canal;
    • Reenvía un mensaje de un admin de supergrupo anónimo para obtener la ID del supergrupo;
    • Reenvía un mensaje de un usuario para obtener su ID (Solo si no tiene activada la protección);
    • Reenvía un mensaje de otro bot o usa el modo inline para obtener la ID de este;
    • Envía un sticker para obtener su file_id (Puedes usar el file_id de sticker con cualquier bot);
    • <a href="{bot-group-deeplink}">Añade el bot a un grupo</a> para obtener su ID (incluso te dirá cuando pases de grupo a supergrupo);
    • Usa el modo inline para enviar tu ID de Telegram a otros chats.

    Source code: { source-code-link }

group-to-supergroup =
    El grupo se ha convertido en supergroup.
    Antigua ID: { $old_id }
    Nueva ID: { $new_id }

inline-mode-title = Tu ID es { NUMBER($id, useGrouping: 0) }
inline-mode-description = has click para mandar tu ID al chat actual.
inline-mode-text = Mi ID de Telegram es { $id }.
inline-mode-tryme = O prueba el bot en PM >>>

sticker-id = Ademas, la ID del sticker es { $id }.
sticker-id-extended =
    La ID del sticker es
    { $id }
    El sticker es actualmente el único tipo de datos cuya file_ids pueden usar los bots.

user-id-hidden =
    Este usuario ha decidido <b>ocultar</b> su ID.
    Puedes leer más sobre este cambio <a href="https://telegram.org/blog/unsend-privacy-emoji#anonymous-forwarding">aquí</a>.

# Commands in UI (when you press "/" or "Menu" button)
cmd-hint-id-pm = Muestra tu ID de Telegram.
cmd-hint-id-group = Muestra la ID de Telegram de este chat de grupo.
cmd-hint-help = Ayuda y código fuente.
