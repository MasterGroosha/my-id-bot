# without @ !
bot-username = my_id_bot

# do not translate!
bot-group-deeplink = https://t.me/{bot-username}?startgroup=id

source-code-link = https://github.com/MasterGroosha/my-id-bot

cmd-start =
    Your Telegram ID is { $id }
    Help and source code: /help

# Used in strings like "This channel id is xxx"
supergroup = supergroup
group = group
channel = channel
user = user
bot = bot

any-chat = This { $type } ID is { $id }

cmd-id-pm = Your Telegram ID is { $id }
cmd-id-group-topic-id = This forum topic ID is { $id }
cmd-id-group-as-channel = And you've sent this message as channel with ID { $id }

cmd-help =
    Use this bot to get ID for different entities across Telegram:

    • Forward message from channel to get channel ID;
    • Forward message from anonymous supergroup admin to get supergroup ID;
    • Forward message from user to get their ID (unless they restrict from doing so);
    • Send a sticker to get its file_id (currently you can use the sticker's file_id with any bot);
    • <a href="{bot-group-deeplink}">Add bot to group</a> to get its ID (it will even tell you when you migrate from group to supergroup);
    • Use inline mode to send your Telegram ID to any chat.

    Source code: { source-code-link }

group-to-supergroup =
    Group upgraded to supergroup.
    Old ID: { $old_id }
    New ID: { $new_id }

inline-mode-title = Your ID is { NUMBER($id, useGrouping: 0) }
inline-mode-description = Tap to send your ID to current chat
inline-mode-text = My Telegram ID is { $id }
inline-mode-tryme = Or try me in PM >>>

sticker-id = Also this sticker's ID is { $id }
sticker-id-extended =
    This sticker ID is
    { $id }
    Sticker is currently the only media type which file_ids can be used by any bot.

user-id-hidden =
    This user decided to <b>hide</b> their ID.
    Learn more about this feature <a href="https://telegram.org/blog/unsend-privacy-emoji#anonymous-forwarding">here</a>.

# Commands in UI (when you press "/" or "Menu" button)
cmd-hint-id-pm = Print your Telegram ID
cmd-hint-id-group = Print Telegram ID of this group chat
cmd-hint-help = Help and source code
