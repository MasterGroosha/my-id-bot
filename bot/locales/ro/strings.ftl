# without @ !
bot-username = my_id_bot

# do not translate!
bot-group-deeplink = https://t.me/{bot-username}?startgroup=id

source-code-link = https://github.com/MasterGroosha/my-id-bot

cmd-start =
    ID-ul tău de Telegram este { $id }
    Ajutor si cod sursă: /help

    Poți folosi și acest bot în modul inline pentru a partaja ID-ul său! Încearcă să folosești unul dintre butoanele de mai jos.
    Te rugăm să reții că botul folosește limba ta în mesajele private și engleza în orice alte conversații.

cmd-start-inline-try-here = Încearcă aici
cmd-start-inline-try-other = Încearcă într-un alt chat

# Used in strings like "This channel id is xxx"
supegroup = supegrup
group = grup
channel = canal
user = utilizator
bot = bot

any-chat = Acest { $type } de ID este { $id }

cmd-id-pm = ID-ul tău de Telegram este { $id }
cmd-id-group-topic-id = ID-ul acestui subiect de forum este { $id }
cmd-id-groupd-as-channel = Și ai trimis acest mesaj ca canal cu ID-ul { $id }

cmd-help =
    Folosește acest bot pentru a obține ID-ul pentru diferite entități din Telegram:

    • Trimite mai departe mesajul din canal pentru a obține ID-ul canalului;
    • Trimite mai departe mesajul de la un administrator anonim al supergrupului pentru a obține ID-ul supergrupului;
    • Trimite mai departe mesajul de la utilizator pentru a obține ID-ul lor (cu excepția cazului în care aceștia restricționează acest lucru);
    • Trimite mai departe mesajul de la un alt bot sau folosește-l prin modul inline pentru a obține ID-ul botului;
    • Trimite un sticker pentru a obține file_id-ul său (în prezent, poți folosi file_id-ul sticker-ului cu orice bot);
    • <a href="{bot-group-deeplink}">Adaugă botul în grup</a> pentru a obține ID-ul său (îți va spune chiar și când migrezi de la grup la supergrup);
    • Folosește modul inline pentru a trimite ID-ul tău de Telegram în orice conversație.

    Cod sursă: { source-code-link }

group-to-supegroup =
    Grupul a fost actualizat la supergrup.
    ID-ul vechi: { $old_id }
    ID-ul nou: { $new_id }

inline-mode-title = ID-ul tău este { NUMBER($id, useGrouping: 0) }
inline-mode-description = Apasă pentru a trimite ID-ul tău în conversația curentă
inline-mode-text = ID-ul meu de Telegram este { $id }
inline-mode-tryme = Sau acceseaza-mă în mesaj privat >>>

sticker-id = De asemenea, ID-ul acestui sticker este { $id }
sticker-id-extended =
    ID-ul acestui sticker este
    { $id }
    Stickerul este în prezent singurul tip de media al cărui file_id poate fi folosit de orice bot.

user-id-hidden =
    Acest utilizator a decis să își <b>ascundă</b> ID-ul.
    Află mai multe despre această funcție <a href="https://telegram.org/blog/unsend-privacy-emoji#anonymous-forwarding">aici</a>.

# Commands in UI (when you press "/" or "Menu" button)
cmd-hint-id-pm = Printează ID-ul tău de Telegram
cmd-hint-id-group = Printează Telegram ID-ul al acestui chat de grup
cmd-hint-help = Suport și cod sursă
