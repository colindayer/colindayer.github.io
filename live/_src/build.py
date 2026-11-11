# Builds live/index.html (en), live/fr/, live/de/ and each language's more/ page from the templates.  python3 build.py
import os, re
H = os.path.dirname(os.path.abspath(__file__)); L = os.path.dirname(H)
T = open(os.path.join(H, 'template.html')).read(); M = open(os.path.join(H, 'more.html')).read()
S = {
 'en': dict(title="Colin Dayer, piano", meta="Pianist in Bern. Solo piano or the duo Laguna Breeze for hotels, bars and restaurants. Free from December 2026.",
   nav_clip="Clip", nav_facts="Practical", nav_contact="Contact", h1_sub="piano",
   lead="I'm a pianist in Bern. This winter I'm looking for a regular evening in a hotel bar, a restaurant or a lounge — in Valais, Vaud or around Bern. Alone at the piano, or with Quincy Freysinger as the duo Laguna Breeze.",
   photo_alt="Colin Dayer at the piano", clip_h="Forty seconds", clip_p="Recorded live at HKB Bern in August. Four songs, cut short.",
   facts_h="The practical side",
   f1k="When", f1v="From 1 December 2026, for the winter season. One fixed evening a week is what I'd like most; single evenings and private events work too.",
   f2k="Where", f2v="Valais, Vaud and Bern first. Further for a residency.",
   f3k="Sets", f3v="Two or three sets of 45 minutes, from aperitif into dinner. Volume to suit the room — people can talk over it, or listen.",
   f4k="Piano", f4v="Yours, grand or upright. If there isn't one, I bring a stage piano and a small amp.",
   f5k="Music", f5v="Jazz standards, bossa nova, soul, a few of my own pieces. Requests welcome, including the ones you're tired of.",
   f6k="Duo", f6v="With Quincy on voice and guitar it gets warmer and a bit louder. Good for bars, après-ski and parties.",
   f7k="Fee", f7v="Depends on the place and the number of evenings. Ask and I'll give you a figure the same day.",
   console_alt="Colin Dayer in the studio", console_cap="HKB Bern",
   songs_h="Two whole songs", solo_cap="Solo · Joseph Kosma", duo_cap="Laguna Breeze · Antônio Carlos Jobim",
   more_lead="There are", more_link="six full recordings", venues_lead="And two evenings filmed in venues:", **{'and': "and"},
   rep_h="Some of what I play", own="Colin Dayer", rep_more="and whatever you ask for",
   mailsubj="Live%20piano%20%E2%80%93%20winter%202026%2F27", note="I answer in English, French or German, usually the same day."),
 'fr': dict(title="Colin Dayer, piano", meta="Pianiste à Berne. Piano solo ou duo Laguna Breeze pour hôtels, bars et restaurants. Disponible dès décembre 2026.",
   nav_clip="Clip", nav_facts="Pratique", nav_contact="Contact", h1_sub="piano",
   lead="Je suis pianiste à Berne. Cet hiver, je cherche une soirée régulière dans un bar d'hôtel, un restaurant ou un lounge — en Valais, dans le canton de Vaud ou autour de Berne. Seul au piano, ou avec Quincy Freysinger en duo, Laguna Breeze.",
   photo_alt="Colin Dayer au piano", clip_h="Quarante secondes", clip_p="Enregistré en live à la HKB de Berne en août. Quatre morceaux, coupés court.",
   facts_h="Côté pratique",
   f1k="Quand", f1v="Dès le 1er décembre 2026, pour la saison d'hiver. Une soirée fixe par semaine, c'est ce que je préfère ; les soirées ponctuelles et les événements privés marchent aussi.",
   f2k="Où", f2v="Valais, Vaud et Berne d'abord. Plus loin pour une résidence.",
   f3k="Sets", f3v="Deux ou trois sets de 45 minutes, de l'apéritif au dîner. Le volume s'adapte à la salle — on peut parler par-dessus, ou écouter.",
   f4k="Piano", f4v="Le vôtre, à queue ou droit. S'il n'y en a pas, j'apporte un piano de scène et un petit ampli.",
   f5k="Musique", f5v="Standards de jazz, bossa nova, soul, quelques compositions à moi. Les demandes sont bienvenues, même celles dont vous êtes lassés.",
   f6k="Duo", f6v="Avec Quincy au chant et à la guitare, c'est plus chaleureux et un peu plus fort. Bien pour les bars, l'après-ski et les fêtes.",
   f7k="Tarif", f7v="Selon le lieu et le nombre de soirées. Demandez, je vous donne un chiffre le jour même.",
   console_alt="Colin Dayer en studio", console_cap="HKB Berne",
   songs_h="Deux morceaux entiers", solo_cap="Solo · Joseph Kosma", duo_cap="Laguna Breeze · Antônio Carlos Jobim",
   more_lead="Il y a", more_link="six enregistrements complets", venues_lead="Et deux soirées filmées en situation :", **{'and': "et"},
   rep_h="Un peu de ce que je joue", own="Colin Dayer", rep_more="et ce que vous demanderez",
   mailsubj="Piano%20live%20%E2%80%93%20hiver%202026%2F27", note="Je réponds en français, en allemand ou en anglais, en général le jour même."),
 'de': dict(title="Colin Dayer, Piano", meta="Pianist in Bern. Solo-Piano oder das Duo Laguna Breeze für Hotels, Bars und Restaurants. Frei ab Dezember 2026.",
   nav_clip="Clip", nav_facts="Praktisches", nav_contact="Kontakt", h1_sub="Piano",
   lead="Ich bin Pianist in Bern. Diesen Winter suche ich einen festen Abend in einer Hotelbar, einem Restaurant oder einer Lounge — im Wallis, in der Waadt oder rund um Bern. Allein am Flügel, oder mit Quincy Freysinger als Duo Laguna Breeze.",
   photo_alt="Colin Dayer am Piano", clip_h="Vierzig Sekunden", clip_p="Live aufgenommen an der HKB Bern im August. Vier Stücke, kurz geschnitten.",
   facts_h="Das Praktische",
   f1k="Wann", f1v="Ab 1. Dezember 2026, für die Wintersaison. Am liebsten ein fester Abend pro Woche; einzelne Abende und private Anlässe gehen auch.",
   f2k="Wo", f2v="Wallis, Waadt und Bern zuerst. Weiter weg für eine Residenz.",
   f3k="Sets", f3v="Zwei oder drei Sets à 45 Minuten, vom Apéro bis ins Dinner. Die Lautstärke passt sich dem Raum an — man kann darüber reden oder zuhören.",
   f4k="Piano", f4v="Ihres, Flügel oder Klavier. Wenn keines da ist, bringe ich ein Stage-Piano und einen kleinen Verstärker mit.",
   f5k="Musik", f5v="Jazz-Standards, Bossa Nova, Soul, ein paar eigene Stücke. Wünsche willkommen, auch die, die Sie nicht mehr hören können.",
   f6k="Duo", f6v="Mit Quincy an Gesang und Gitarre wird es wärmer und etwas lauter. Gut für Bars, Après-Ski und Feste.",
   f7k="Gage", f7v="Je nach Ort und Anzahl Abende. Fragen Sie, ich nenne Ihnen noch am selben Tag eine Zahl.",
   console_alt="Colin Dayer im Studio", console_cap="HKB Bern",
   songs_h="Zwei ganze Stücke", solo_cap="Solo · Joseph Kosma", duo_cap="Laguna Breeze · Antônio Carlos Jobim",
   more_lead="Es gibt", more_link="sechs vollständige Aufnahmen", venues_lead="Und zwei gefilmte Abende vor Ort:", **{'and': "und"},
   rep_h="Ein Teil von dem, was ich spiele", own="Colin Dayer", rep_more="und was Sie sich wünschen",
   mailsubj="Live-Piano%20%E2%80%93%20Winter%202026%2F27", note="Ich antworte auf Deutsch, Französisch oder Englisch, meist noch am selben Tag."),
}
MORE = {
 'en': dict(more_title="All recordings", more_p="Three solo pieces, three with Laguna Breeze, two evenings filmed in venues, and the longer reel.", m_solo="Solo piano", m_rooms="In venues", m_reel="Longer reel (72 s)", pianobar="Piano bar", own="Own composition"),
 'fr': dict(more_title="Tous les enregistrements", more_p="Trois morceaux en solo, trois avec Laguna Breeze, deux soirées filmées en situation, et le reel plus long.", m_solo="Piano solo", m_rooms="En situation", m_reel="Reel plus long (72 s)", pianobar="Piano-bar", own="Composition"),
 'de': dict(more_title="Alle Aufnahmen", more_p="Drei Solo-Stücke, drei mit Laguna Breeze, zwei gefilmte Abende vor Ort und das längere Reel.", m_solo="Solo-Piano", m_rooms="Vor Ort", m_reel="Längeres Reel (72 s)", pianobar="Piano-Bar", own="Eigene Komposition"),
}
for lang, d in S.items():
    sub = lang != 'en'; root = '../' if sub else ''
    links = {'en': root, 'fr': root + 'fr/', 'de': root + 'de/'}
    nav = ' <span style="margin-left:22px">' + ' · '.join(f'<a class="{"on" if k == lang else ""}" href="{"#" if k == lang else links[k]}">{k}</a>' for k in ('en', 'fr', 'de')) + '</span>'
    d = dict(d, lang=lang, root=root, home=root or '#', langnav=nav, more_dir='more/')
    path = os.path.join(L, lang if sub else '', 'index.html'); os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(re.sub(r'\{\{(\w+)\}\}', lambda m: d[m.group(1)], T)); print(lang, path)
    dm = dict(d, **MORE[lang], r=root + '../', back='../')
    mp = os.path.join(os.path.dirname(path), 'more', 'index.html'); os.makedirs(os.path.dirname(mp), exist_ok=True)
    open(mp, 'w').write(re.sub(r'\{\{(\w+)\}\}', lambda m: dm[m.group(1)], M))
