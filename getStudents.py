from bs4 import BeautifulSoup
import requests

f = open("students.txt", "w")

for aasta in range(2010, 2023):
    print("parseing ", aasta)
    url = f'https://www.htg.tartu.ee/d7/lennud_d.php?aasta={aasta}'

    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object with the website's HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all table rows ('tr') in the HTML
    rows = soup.find_all('tr')

    # Loop through each row and print the text content of each cell ('td')
    for row in rows:
        cells = row.find_all('td')
        rida = []
        for cell in cells:
            rida.append(cell.get_text())
            # print(cell.get_text())
        # print('---')
        if (rida[0][0:4] == str(aasta)):
            f.write("_".join(rida) + "\n")

aastad = [
        "2025a", "2025b", "2025c", "2025d", "2025e", 
        "2024a", "2024b", "2024c", "2024d", "2024e", 
        "2023a", "2023b", "2023c", "2023d", "2023e"
]

õpilased = [
"""
Andero Albrecht
Henri Jõeorg
Kaspar Jõeorg
Mattias Jõgi
Violeta Jürgens
Joosep Jürissaar
Markus Kaur
Oliver Kikas
Artus Leo Marco Klemm
Robert Milan Kotjuh
Toomas Erik Kuhi
Kevin Kuudeberg
Rasmus Kõllo
Marten Leosk
Ants Liivamägi
Grete Magerramov
Tomm Ragnar Maidla
Viktoria Misnik
Robin Mäeots
Morten Oscar Orussaar
Ralf Robert Paabo
Anton Pašenkov
Agnes Peitel
Kristi Pihlak
Paula Puksov
Even Puusepp
Kris Puusepp
Uku Toomas Rand
Robin Randrüüt
Roosi Raudsepp
Annabel Taaber
Mirtel Teder
Marlon Tiik
Miia Tillmann
Kristella Mirell Uiboaed
""",
"""
Hedvig Altmäe
Karl Pärtel Arvi
Teena Haabmets
Aleksander Jalakas
Marta Joonas
Joonatan Kahre
Minna Marie Kask
Christelle Keller
Ott Kruuse
Hans Kristjan Kullamaa
Kristiin Lõhmus
Mati Mansberg
Oliver Mihkel Mertelsmann
Oliver Mikli
Martti Milk
Anna-Liisa Mägi
Lukas Müürsepp
Mart Johannes Nacke
Tambet Parm
Rando Pihlak
Triin Prii
Ingrid Puusepp
Madis Repän
Morgan Matthias Rikken
Oskar Saareall
Karina Saealle
Mattias Sinilaht
Andreas Soosaar
Simmo-Siim Soosaar
Rasmus Suur
Mihkel Tali
Ellinor Usai
Robin Vask
Jaan Artur Viirsalu
Sten Kaspar Vind
""",
"""
Heidi-Lii Aru
Artur Asi
Emilia Bachman
Margaret Braun
Ivar Golubenko
Hanna Saara Hiir
Artur Ipits
Elizabeth Ivask
Robert Kirk
Keili Krabbi
Kaisa Kõre
Mia Merili Laisaar
Liisi Liias
Beril-Amabel Lindmäe
Helen Loot
Janee Lootus
Aleksander Lõhmus
Keilika Meos
Miia Helen Merilo
Richard Oppar
Triinu Part
Mihkel Pennar
Maarja-Leen Piirimäe
Kirke Viktoria Plaado
Viktoria Päll
Kärt Pürn
Kätriin Randma
Annaliisa Rebane
Eva-Liisa Sepp
Liis Serv
Eliise Siimon
Emma Tammpere
Kirke Karolin Tark
Marjette Andrea Tederov
Natalie Uuemaa
Karen Viira
""",
"""
Leenu Aasrand
Annabel Allas
Hanna Allikas
Mirjam Gross
Emili Heinaste
Kristen Hurt
Herta-Marie Jatsa
Brenda Järv
Tuuli-Heleene Kalda
Kaisa Kangro
Eliis Kasenõmm
Kärt Kiiver
Marilis Kivi
Kristanna Koemets
Eliise Kolsar
Karoliina Kübar
Kirsi Laaniste
Sanne Laas
Mona Leis
Margot Liisbet Menind
Õnne-Mari Olev
Aleksandra Peskovski
Marleene Randmaa
Erik Johannes Rein
Liisa Riso
Karl Markus Saar
Polina Saar
Säde Sepp
Karl Silmere
Henri Suur
Annabel Tamm
Marta Tammiksaar
Elar Udumets
Marten Vellak
""",
"""
Anu Altnurme
Säde Einasto
Helena Gross
Maribel Haaviste
Mart Jaakson
Carmen Kallas
Stella Kivi
Victoria Kopamees
Pääsu Ladva
Mia-Marie Logina
Melissa Lokk
Denis Lotkov
Agne-Riin Mekk
Merili Meltsas
Ketlin Mutso
Karl Aksel Männik
Helena Nõmm
Ats-Artur Ploomipuu
Magnus Puija
Rico Päkk
Karin Pärtelpoeg
Mari-Liis Reemets
Hannes Villem Reimand
Taavet Saar
Elis Anete Saksman
Liina Sarv
Ronja Talunik
Kadri-Liis Tamm
Marleen Tamm
Heleri Tammemägi
Anette Teder
Elisabeth Tiidelepp
Andra Tuurmaa
Katarina Utsal
Ida Vares
""",
"""
Miia Isabel Anipai
Annette Annok
Klaus Jõela
Ingrid Järve
Kirke Kisand
Laura Kompus
Magnar Käärik
Arthur Lauk
Lucas Lausing
Kert Lelov
Emma Luht
Marten Lõhmus
Nansen Palo
Ivar Peeling
Heddy Ploom
Elsa Puu
Kaur Ruben Ragis
Rasmus Raie
Eva-Maria Raudsepp
Hans Henrik Rebane
Artur Ruul
Teodor Ruus
Kädi Rõõmus
Annabel Rüütel
Markus Rüütli
Ragnar Sarapuu
Maia Serv
Markos Soodla
Maria Terep
Kerdo Timak
Heidi Tõnisson
Markus Tõnson
Elenor Tõrva
Kristofer Robin Verev
Tregert Gustav Värv
""",
"""
Karoliina Enkvist
Elmira Fakhrutdinova
Jürgen Güsson
Martin Hindre
Marvin Kask
Uku Mihkel Kolka
Maria Kozõreva
Henrik Kreinin
Georg Kurjama
Triin-Elis Kuum
Kirke Linda Kuuse
Kaur Huko Käämbre
Orm Kaarel Kübarsepp
Liisa Laugesaar
Sander Lepik
Maria Helena Lõhmus
Mart Nikopensius
Katarina Ojaperv
Mihkel Pauklin
Liisa Viktooria Puurand
Karl Pärn
Carol Rand
Ragnar Reino
Karl Jan Riisaar
Laura-Liis Rull
Johanna Saavaste
Indrek Salo
Heliisa Theadora Sunts
Kristin Sõber
Joonas Teder
Kristjan Tiido
Tavid-Markus Trolla
Artur Türna
Nele Riin Vahelaan
""",
"""
Arabella Antons
Kertu Hurbola
Kris Kaspar Kalda
Marie Elise Kanarik
Mehka Kartau
Lauri Kask
Jaagup Konksi
Vladlena Kotenko
Anna Malena Kuris
Tristan Köhler
Lisette Laan
Joonas Aleksander Laipaik
Mia Marleen Lemetti
Sandra-Liisbet Lilleste
Madli Maran
Sonja Nämi
Anastasiia Pershko
Aneth Kaileen Peterson
Carolyn Prits
Joosep Pärnalaas
Rutha Pärt
Joosep Rand
Rando Remm
Kreeta Roose
Annika Rääbis
Sander Sarapuu
Sonja Sareal
Sireli Sildnik
Anna Viktoria Tammik
Lydia Helene Teder
Iris Tõnismaa
Mari Tämm
Kertu Virumäe
""",
"""
Aarto Abroi
Karl Romet Ainso
Elise Belov
Ella Cecilia Claesson
Jaan Erik Halliko
Lilian Hindrikson
Marit Anette Huik
Arlis Hunt
Laura Emilia Jõgi
Lota Kalberg
Laura-Lotta Kartsep
Annaliisa Karu
Emma Kilmi
Kaisa Kontkar
Juhan Martten Kull
Hilda Laidmets
Johanna Lauringson
Miili Lippus
Annika Moppel
Markos Mõttus-Asson
Ralf Niilus
Marta Näripä
Mete-Triin Otstavel
Emma Pastak
Rolando Põld
Adele Raidmets
Henn-Jaagup Rooba
Jaana Sommermann
Aleksandr Soorm
Rebekka Soosaar
Nelis-Katrina Säre
Kärt Tõnissaar
Robin Virunurm
""",
"""
Emili Kristelle Andrejev
Klaara Erepuu
Alessia Anna Gresele
Hans Jürgen Järs
Marja Järv
Ivan Kleštšin
Karolina Krautmann
Lisethe Kruus
Dea-Liis Kubbe
Mark Kaspar Kõnd
Tristan Kõomägi
Eerik Kääp
Gerda Lehis
Kertu Meerits
Jan Markus Metsoja
Mona-Liis Miil
Mia Marta Miller
Kristina Mölder
Karl-Markus Mütt
Hella Hildegard Niitra
Enri Piisner
Helena Ploom
Hubert Uku Prank
Piibe Pree
Riinu Maria Pungar
Ralf Rasmus Raal
Aleksandra-Eleene Rebane
Petra Räbin
Kaisa Saan
Robin Sepma
Sander Treumuth
Toomas-Erik Vahtra
""",
"""
Anders Aksjonov
Jonathan Astmäe
Liis Ernits
Kaspar Gutmann
Salme Adeele Hollas
Marta Kann
Nora Liis Kavald
Kaur Kivilaan
Kristo Krikmann
Manfred Kukk
Oskar Kurvits
Markus Kõiv
Rudolf Kõivupuu
Joosep Laanemägi
Laura Laugma
Aivo Liivat
Helena Lindeberg
Rando Lukk
Loore Luste
Oskar Männik
Rauno Paasoja
Ralf Paat
Liisi Paaver
Elina Papp
Ander Pavlov
Rainis Puusepp
Mattias Timm Rast
Laura Maria Rekand
Kusti Sammul
Hanna Tali
Laura Tamm
Thomas Tennisson
Andreas Tiit
Morten Ulp
""",
"""
Kevin Akkermann
Andreas Avameri
Toomas Herodes
Laur Härm
Angela Ikonen
Tuule-Liis Jaagant
Hendrik Jaks
Karl Joonas Jõepere
Johan Villem Kaare
Kristjan-Erik Kahu
Kristiine Kaldmaa
Jakob Miikael Kaljurand
Karl Markus Kiudma
Kertu Katriin Kotkas
Emma Kruusmäe
Hans Gustav Kõljalg
Susanne Lannes
Mattias Erik Liba
Kaur Lõhmus
Loviisa Lätt
Karl Mattias Milk
Indrek Nemvalts
Hendrik Pajur
Liisa Matilda Palgi
Mere-Helina Panksepp
Markus Roletsky
Kärt Trinity Sillaots
Hendrik Tammemägi
Mark Tarnovski
Tristan Timmermann
Triinu Vaher
Stella Vesi
Jakob Veske
Siim-Erik Viiding
Uku Viispert
Johan Värv
""",
"""
Maria Andresen
Hans Markus Danilas
Maria Frese
Kerttu Galka
Minna Gielen
Emma Goos
Holger Eric Hain
Kauri Ilves
Doris Keernik
Kea Rael Kukk
Marion Köhler
Kaia Laatspera
Liisa Lotta Lamp
Marie Agathe Laugesaar
Tristan Laur
Christofer Lepaste
Liisi Leppik
Marie Loog
Kertu Mölder
Aia Adele Narits
Mattias Oras
Marti Pastak
Linda Piirimäe
Leene Pärtel
Hanna Karin Randaru
Helena Rähni
Otto Richard Sokk
Liisa Tafenau
Tuuli Kärt Tammaru
Tiia Tomson
Jessica Uibo
Anette Vares
Anita Viineloo
Markus Viks
Elisabeth Võrk
Kaarup Öövel
""",
"""
Hanna Maria Fatkin
Alexander Hildebrandt
Berta Lorena Ipits
Marii Israel
Kevin-Richard Jõgi
Maarja Katariina Kerge
Magda Grete Kibuspuu
Karl Markus Kurs
Kaur Hannes Käämbre
Luise Laas
Märt Lillestik
Sally-Johanna Lõhmus
William Lõhmus
Kristofer Robin Maasalu
Madara Kuld Matsin
Anna Mutso
Sabiine Oras
Triine Ottender
Tambet Palgi
Kert Raudnõmm
Viiu Repän
Emily Riismandel
Johanna Saare
Rasmus Sareal
Friida Savi
Stenna Solovjov
Maria Zinatullina
Stefi Marie Talver
Merit Tomson
Taavet Tuisk
Catharina Undrus
Evelin Uue
Emma Vahelaan
Randar Vahtrik
Ville Markus Varik
Andre Villemson
""",
"""
Anette Ama
Eliise Antonov
Triinu Aru
Alger Avi
Veera Beljajeva
Gleen Gross
Karl Erik Hunt
Maria Jõesalu
Kaarel Kaldre
Getter Miida Kask
Grete Kivirüüt
Eleonora Kolga
Emma Kuuse
Riinu Külvik
Karmen Kütt
Tomi Lahe
Kertu Maria Luik
Annmari Meriste
Imre Nõmm
Kelly Orgusaar
Lee Orula
Maara Parhomenko
Mia Proover
Siimeon Raud
Lauri Raudsepp
Amina Rebane
Karl Reimand
Marleen Sule
Triinu Taivere
Tõnis Timmi
Hanna Marta Tsäkko
Brite Tõniste
Ann Marleen Varul
Robin Vool
Gerda Õunapuu
"""
]

klassijuhatajad = [
    "Raimond Lepiste",
    "Sandra Sagar",
    "Ott Maidre",
    "Anneli Mägi",
    "Age Salo",
    "Aimar Poom",
    "Indrek Pajur",
    "Ave Külter",
    "Eve Paap",
    "Toomas Jürgenstein",
    "Ülle Hüva",
    "Marcus Hildebrandt",
    "Ülle Seevri",
    "Aare Ristikivi",
    "Tiina Pluum"
]

i = -1
for klass in õpilased:
    i+=1
    a = klass.split("\n")
    u = a[1:-1]
    for õpilane in u:
        perenimi = õpilane.rsplit(" ", 1)[1]
        eesnimed = õpilane.rsplit(" ", 1)[0]
        f.write(f"{aastad[i]}_{perenimi}_{eesnimed}_{klassijuhatajad[i]}\n")
f.close()