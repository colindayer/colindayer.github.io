# Builds live/index.html (en), live/fr/index.html, live/de/index.html from template.html.  python3 build.py
import os, re
H = os.path.dirname(os.path.abspath(__file__)); L = os.path.dirname(H)
T = open(os.path.join(H, 'template.html')).read()
S = {
 'en': dict(title="Colin Dayer, piano", meta="Live piano for hotels, bars and restaurants in Switzerland. Solo, or as the duo Laguna Breeze with voice and guitar. Winter 2026/27.",
   runner="Colin Dayer · piano · winter 2026/27", nav_reel="Clip", nav_songs="Two songs", nav_contact="Contact", s2_h="Two songs", s2_p="One alone, one with Quincy. Both recorded live at HKB Bern, August 2026.", solo_cap="Solo piano · Joseph Kosma", duo_cap="Laguna Breeze · Antônio Carlos Jobim", more_lead="More:", more_link="six full recordings", more_title="All recordings", more_p="Everything in one place: three solo pieces, three with Laguna Breeze, two evenings filmed in venues, and the longer reel.", m_solo="Solo piano", m_rooms="In the room", m_reel="Longer reel (72 s)",
   h1_sub="piano", lead="I play piano in hotels, bars and restaurants. On my own, or with Quincy Freysinger as <em>Laguna Breeze</em>.",
   photo_alt="Colin Dayer at the piano", photo_cap="HKB Bern, August 2026",
   s1_h="A minute and a bit", s1_p="Recorded and filmed live at HKB Bern, August 2026.", pianobar="Piano bar",
   s3_h="Solo piano", s3_p="Standards, bossa nova and a few of my own pieces. Leaves is one of them.", own="Own composition",
   s4_p="Quincy sings and plays guitar, I play piano. Mostly Brazilian songs and soul, and now and then a Pink Floyd tune taken very slowly.",
   s5_h="This winter", s5_p="Free from December, in Valais, Vaud and Bern. Ideally a regular evening each week; single evenings and private events are also welcome.",
   console_alt="Colin Dayer in the studio", solo="Solo", solo_p="On your piano, grand or upright, or I bring a stage piano. Usually two or three sets of 45 minutes, from aperitif through dinner.",
   duo="Duo", duo_p="Piano, voice and guitar. Right for bars, après-ski and parties, where a little more energy helps.",
   s6_h="Programme", s6_p="A selection. Requests welcome.", bookings="Bookings", mailsubj="Live%20piano%20%E2%80%93%20winter%202026%2F27",
   langs_note="I reply in English, French or German"),
 'fr': dict(title="Colin Dayer, piano", meta="Piano live pour hôtels, bars et restaurants en Suisse. En solo, ou en duo Laguna Breeze avec chant et guitare. Hiver 2026/27.",
   runner="Colin Dayer · piano · hiver 2026/27", nav_reel="Clip", nav_songs="Deux morceaux", nav_contact="Contact", s2_h="Deux morceaux", s2_p="Un en solo, un avec Quincy. Tous deux enregistrés en live à la HKB de Berne, août 2026.", solo_cap="Piano solo · Joseph Kosma", duo_cap="Laguna Breeze · Antônio Carlos Jobim", more_lead="Plus :", more_link="six enregistrements complets", more_title="Tous les enregistrements", more_p="Tout au même endroit : trois morceaux en solo, trois avec Laguna Breeze, deux soirées filmées en situation, et le reel plus long.", m_solo="Piano solo", m_rooms="En situation", m_reel="Reel plus long (72 s)",
   h1_sub="piano", lead="Je joue du piano dans les hôtels, les bars et les restaurants. Seul, ou avec Quincy Freysinger en duo, <em>Laguna Breeze</em>.",
   photo_alt="Colin Dayer au piano", photo_cap="HKB Berne, août 2026",
   s1_h="Un peu plus d'une minute", s1_p="Enregistré et filmé en live à la HKB de Berne, août 2026.", pianobar="Piano-bar",
   s3_h="Piano solo", s3_p="Standards, bossa nova et quelques compositions personnelles, dont Leaves.", own="Composition",
   s4_p="Quincy chante et joue de la guitare, je suis au piano. Surtout des chansons brésiliennes et de la soul, et de temps en temps un Pink Floyd pris très lentement.",
   s5_h="Cet hiver", s5_p="Disponible dès décembre, en Valais, dans le canton de Vaud et à Berne. Idéalement une soirée fixe par semaine ; soirées ponctuelles et événements privés bienvenus.",
   console_alt="Colin Dayer en studio", solo="Solo", solo_p="Sur votre piano, à queue ou droit, ou j'apporte un piano de scène. En général deux ou trois sets de 45 minutes, de l'apéritif au dîner.",
   duo="Duo", duo_p="Piano, chant et guitare. Pour les bars, l'après-ski et les fêtes, quand un peu plus d'énergie fait du bien.",
   s6_h="Programme", s6_p="Une sélection. Demandes bienvenues.", bookings="Réservations", mailsubj="Piano%20live%20%E2%80%93%20hiver%202026%2F27",
   langs_note="Je réponds en français, allemand ou anglais"),
 'de': dict(title="Colin Dayer, Piano", meta="Live-Piano für Hotels, Bars und Restaurants in der Schweiz. Solo oder als Duo Laguna Breeze mit Gesang und Gitarre. Winter 2026/27.",
   runner="Colin Dayer · Piano · Winter 2026/27", nav_reel="Clip", nav_songs="Zwei Stücke", nav_contact="Kontakt", s2_h="Zwei Stücke", s2_p="Eines allein, eines mit Quincy. Beide live aufgenommen an der HKB Bern, August 2026.", solo_cap="Solo-Piano · Joseph Kosma", duo_cap="Laguna Breeze · Antônio Carlos Jobim", more_lead="Mehr:", more_link="sechs vollständige Aufnahmen", more_title="Alle Aufnahmen", more_p="Alles an einem Ort: drei Solo-Stücke, drei mit Laguna Breeze, zwei gefilmte Abende vor Ort und das längere Reel.", m_solo="Solo-Piano", m_rooms="Vor Ort", m_reel="Längeres Reel (72 s)",
   h1_sub="Piano", lead="Ich spiele Piano in Hotels, Bars und Restaurants. Allein, oder mit Quincy Freysinger als Duo <em>Laguna Breeze</em>.",
   photo_alt="Colin Dayer am Piano", photo_cap="HKB Bern, August 2026",
   s1_h="Gut eine Minute", s1_p="Live aufgenommen und gefilmt an der HKB Bern, August 2026.", pianobar="Piano-Bar",
   s3_h="Solo-Piano", s3_p="Jazz-Standards, Bossa Nova und einige eigene Stücke, darunter Leaves.", own="Eigene Komposition",
   s4_p="Quincy singt und spielt Gitarre, ich spiele Piano. Vor allem brasilianische Songs und Soul, und ab und zu ein sehr langsamer Pink Floyd.",
   s5_h="Diesen Winter", s5_p="Ab Dezember frei, im Wallis, in der Waadt und in Bern. Am liebsten ein fester Abend pro Woche; einzelne Abende und private Anlässe sind ebenso willkommen.",
   console_alt="Colin Dayer im Studio", solo="Solo", solo_p="Auf Ihrem Flügel oder Klavier, oder ich bringe ein Stage-Piano mit. Meist zwei oder drei Sets à 45 Minuten, vom Apéro bis ins Dinner.",
   duo="Duo", duo_p="Piano, Gesang und Gitarre. Passt in Bars, zum Après-Ski und an Feste, wo etwas mehr Energie gefragt ist.",
   s6_h="Programm", s6_p="Eine Auswahl. Wünsche willkommen.", bookings="Buchungen", mailsubj="Live-Piano%20%E2%80%93%20Winter%202026%2F27",
   langs_note="Ich antworte auf Deutsch, Französisch oder Englisch"),
}
for lang, d in S.items():
    sub = lang != 'en'; root = '../' if sub else ''
    links = {'en': root + ('' if sub else '#'), 'fr': root + 'fr/', 'de': root + 'de/'}
    nav = ' <span style="margin-left:26px">' + ' · '.join(f'<a class="{"on" if k == lang else ""}" href="{links[k] if k != lang else "#"}">{k}</a>' for k in ('en', 'fr', 'de')) + '</span>'
    d = dict(d, lang=lang, root=root, home=root or '#', langnav=nav)
    path = os.path.join(L, lang if sub else '', 'index.html'); os.makedirs(os.path.dirname(path), exist_ok=True)
    d['more_dir']='more/'
    out = re.sub(r'\{\{(\w+)\}\}', lambda m: d[m.group(1)], T)
    open(path, 'w').write(out); print(lang, path)
    M = open(os.path.join(H, 'more.html')).read()
    dm = dict(d, r=root + '../', back='../')
    mp = os.path.join(os.path.dirname(path), 'more', 'index.html'); os.makedirs(os.path.dirname(mp), exist_ok=True)
    open(mp, 'w').write(re.sub(r'\{\{(\w+)\}\}', lambda m: dm[m.group(1)], M))
