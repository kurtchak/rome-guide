# -*- coding: utf-8 -*-
"""Obsah nórskych miest (Bergen, Stavanger, fjordy) pre data.js.

Rovnaký formát ako scripts/new_places_data.py:
každá položka má id, name, category, coords (tuple lat, lon), emoji,
info (Vstup/Sezóna/Web ...), texts (short/medium/long) a legends (2-3 ks).

Použitie: skopíruj do scripts/, vytvor inject_norway.py podľa inject_new_places.py
(zmena importu na `from norway_places_data import NORWAY_PLACES as NEW_PLACES`) a spusti.

Stav:
  - FLAGSHIP miesta = kompletné (short + medium + long + 2 legendy).
  - Ostatné = short + medium + info hotové; `long` a `legends` označené `# TODO`
    nech sa dopíšu v rovnakom tóne a dĺžke ako rímske miesta v data.js.
"""

NORWAY_PLACES = [

    # ============================================================
    # BERGEN
    # ============================================================
    {
        "id": "bryggen",
        "name": "Bryggen — hanzové nábrežie",
        "category": "bergen",
        "coords": (60.3975, 5.3236),
        "emoji": "⚓",
        "info": {
            "Postavené": "od 12. storočia (dnešná podoba po požiari 1702)",
            "Sloh": "drevená hanzová zástavba",
            "Význam": "Sídlo Hanzy, pamiatka UNESCO (od 1979)",
            "Vstup": "ulička zadarmo; Hanzové múzeum platené",
            "Web": "https://www.visitbergen.com",
        },
        "texts": {
            "short": (
                "Bryggen je staré hanzové nábrežie v Bergene a najznámejší obraz mesta — rad úzkych "
                "drevených domov s ostrými štítmi v okrovej, červenej a žltej farbe. Od 14. storočia tu "
                "sídlili nemeckí kupci Hanzy a obchodovali so sušenou treskou z Lofôt. Dnes je Bryggen "
                "pamiatkou svetového dedičstva UNESCO."
            ),
            "medium": (
                "Bryggen, doslova „nábrežie\", je najstaršia časť Bergenu a jeho najznámejší symbol — "
                "súvislý rad úzkych drevených domov s ostrými trojuholníkovými štítmi, natretých okrovou, "
                "hrdzavočervenou a žltou farbou, ktoré sa zrkadlia vo vode prístavu Vågen.\n\n"
                "Mesto založil kráľ Olaf Pokojný okolo roku 1070 a Bryggen sa rýchlo stalo centrom obchodu. "
                "Od polovice 14. storočia tu zriadila svoju pobočku Hanza — mocný zväz nemeckých obchodných "
                "miest. Nemeckí kupci tu vykupovali sušenú tresku, takzvaný stockfish, z Lofôt a vymieňali ju "
                "za obilie a tovar z kontinentu. Žili v uzavretej komunite s vlastnými pravidlami celé stáročia.\n\n"
                "Bryggen mnohokrát zničili požiare — drevené domy horeli znova a znova, no zakaždým ich postavili "
                "v rovnakom štýle na pôvodných základoch. Dnešná zástavba pochádza najmä z obnovy po veľkom požiari "
                "v roku 1702. Pre svoju jedinečnú históriu bolo Bryggen v roku 1979 zapísané na zoznam svetového "
                "dedičstva UNESCO. Za fasádami sa skrýva labyrint drevených uličiek, dvorov a krčmárskych dielní."
            ),
            "long": (
                "Bryggen, doslova „nábrežie\", je najstaršia a najslávnejšia časť Bergenu — súvislý rad úzkych "
                "drevených domov s ostrými trojuholníkovými štítmi, natretých okrovou, hrdzavočervenou a žltou "
                "farbou. Zrkadlia sa vo vode starého prístavu Vågen a tvoria pohľad, ktorý zdobí takmer každú "
                "pohľadnicu z Nórska.\n\n"
                "Mesto Bergen založil kráľ Olaf Pokojný okolo roku 1070 a vďaka svojej polohe pri mori sa rýchlo "
                "stalo najdôležitejším obchodným prístavom severnej Európy. Srdcom obchodu bolo práve Bryggen. "
                "Od polovice 14. storočia tu zriadila jednu zo svojich štyroch zahraničných pobočiek (kontorov) "
                "Hanza — mocný zväz nemeckých obchodných miest na čele s Lübeckom.\n\n"
                "Nemeckí kupci tu vykupovali sušenú tresku, takzvaný stockfish, ktorú rybári privážali z ďalekých "
                "Lofôt na severe, a vymieňali ju za obilie, múku, pivo a remeselný tovar z kontinentu. Sušená treska "
                "bola po stáročia hlavným nórskym exportom a Bryggen bol jeho prekladiskom. Hanzoví obchodníci žili "
                "v uzavretej, takmer kláštornej komunite — boli to len muži, platili prísne pravidlá, zákaz ohňa "
                "vo väčšine miestností a zákaz stýkať sa s miestnymi ženami. Moc Hanzy v Bergene trvala viac ako "
                "štyristo rokov, posledný nemecký kupec odišiel až v 18. storočí.\n\n"
                "Dejiny Bryggenu sú dejinami ohňa. Drevené domy postavené tesne vedľa seba horeli znova a znova — "
                "kroniky uvádzajú desiatky veľkých požiarov. Po každom z nich však Bergenčania postavili nábrežie "
                "nanovo, v rovnakom štýle a na pôvodných kamenných základoch. Dnešná zástavba pochádza najmä z obnovy "
                "po ničivom požiari v roku 1702. Posledný veľký požiar v roku 1955 zničil časť severného radu — "
                "vďaka tomu tu mohli archeológovia odkryť stredoveké vrstvy a založiť Bryggenské múzeum.\n\n"
                "Za pôvabnými fasádami sa skrýva celý svet — labyrint úzkych drevených pasáží, naklonených chodieb, "
                "vnútorných dvorov, skladov a niekdajších kupeckých kancelárií. Drevo vŕzga pod nohami, podlahy sa "
                "zvažujú a budovy sa o seba navzájom opierajú. Dnes tu sídlia galérie, ateliéry remeselníkov, "
                "obchodíky a útulné kaviarne.\n\n"
                "Pre svoju výnimočnú hodnotu bolo Bryggen v roku 1979 zapísané na zoznam svetového dedičstva UNESCO "
                "ako jedinečné svedectvo o stredovekom obchode a drevenej architektúre severnej Európy. Návšteva "
                "Bryggenu, Hanzového múzea a neďalekého rybieho trhu patrí k tomu, čo by v Bergene nemal nikto vynechať."
            ),
        },
        "legends": [
            {
                "id": "ohen-a-znovuzrodenie",
                "title": "Mesto, ktoré stále horelo",
                "text": (
                    "Bryggen je postavené takmer výhradne z dreva a po stáročia stálo tesne nahustené pri "
                    "prístave — ideálne podmienky pre oheň. Kroniky Bergenu zaznamenávajú desiatky veľkých "
                    "požiarov. Plamene zakaždým preleteli celým radom domov v priebehu hodín a zanechali po sebe "
                    "spálenisko.\n\n"
                    "Obyvatelia však zakaždým urobili to isté — postavili Bryggen nanovo, v rovnakom tvare, na "
                    "tých istých kamenných základoch a podľa starých rozmerov. Práve preto dnešné domy z 18. "
                    "storočia verne pripomínajú stredoveké nábrežie. Mesto sa doslova znovu a znovu rodilo z popola.\n\n"
                    "Posledný veľký požiar zachvátil severnú časť Bryggenu v roku 1955. Mal však aj nečakaný "
                    "prínos: na ohorenom mieste mohli archeológovia po prvý raz dôkladne preskúmať vrstvy hlboko "
                    "pod nábrežím. Našli runové nápisy, kožené topánky, kupecké pečate a tisíce predmetov, ktoré "
                    "dnes rozprávajú príbeh stredovekého Bergenu v Bryggenskom múzeu."
                ),
            },
            {
                "id": "hanza-pravidla",
                "title": "Život za hanzovými múrmi",
                "text": (
                    "Nemeckí kupci, ktorí v Bryggene sídlili od 14. storočia, žili v zvláštnom, takmer "
                    "kláštornom svete. Kontor — ako sa pobočka Hanzy volala — bol uzavretou mužskou komunitou, "
                    "ktorá sa riadila vlastnými prísnymi predpismi. Ženy mali do skladov a obytných domov vstup "
                    "zakázaný a kupci sa nesmeli ženiť s miestnymi Nórkami, aby majetok a vplyv zostali v rukách "
                    "Hanzy.\n\n"
                    "Kvôli neustálej hrozbe požiaru bol vo väčšine drevených miestností zakázaný akýkoľvek oheň. "
                    "Kúrilo a varilo sa len v spoločných kamenných budovách, takzvaných schøtstuene, ktoré stáli "
                    "bokom od skladov. Učni a mladí pomocníci museli prejsť tvrdým, často ponižujúcim zasväcovacím "
                    "obradom — od dymom napustených pivníc až po skúšky odvahy v ľadovej vode prístavu.\n\n"
                    "Tento uzavretý spôsob života pretrval stáročia a z Bergenu urobil takmer nemecké mesto v srdci "
                    "Nórska. Až s úpadkom moci Hanzy sa kontor postupne ponórčil a posledný nemecký obchodník "
                    "odovzdal svoj dom miestnym až koncom 18. storočia."
                ),
            },
        ],
    },

    # ------------------------------------------------------------
    {
        "id": "floyen",
        "name": "Fløyen a lanovka Fløibanen",
        "category": "bergen",
        "coords": (60.3936, 5.3508),
        "emoji": "🚠",
        "info": {
            "Otvorené": "lanovka Fløibanen 1918",
            "Výška": "vrchol Fløyen 320 m n. m.",
            "Význam": "Najnavštevovanejšia vyhliadka nad Bergenom",
            "Vstup": "lanovka platená (obojsmerne ~150 NOK)",
            "Web": "https://www.floyen.no",
        },
        "texts": {
            "short": (
                "Fløyen je jeden zo siedmich vrchov obklopujúcich Bergen a najobľúbenejšia vyhliadka v meste. "
                "Z centra naň za pár minút vyvezie historická lanovka Fløibanen z roku 1918. Z výšky 320 metrov "
                "sa otvára pohľad na celé mesto, prístav a okolité fjordy."
            ),
            "medium": (
                "Fløyen je jeden zo siedmich vrchov, ktoré obklopujú Bergen, a zároveň najnavštevovanejšia "
                "vyhliadka v meste. Priamo z historického centra naň vyvezie pozemná lanovka Fløibanen, ktorá "
                "premáva od roku 1918 a patrí k najznámejším dopravným atrakciám Nórska.\n\n"
                "Cesta nahor trvá len niekoľko minút a prevýšenie je viac ako tristo metrov. Z vrcholovej plošiny "
                "vo výške 320 metrov sa naskytá panoramatický pohľad na pestré strechy Bergenu, prístav Vågen, "
                "ostrovy a fjordy v diaľke. Pri jasnom počasí dovidíte ďaleko na more.\n\n"
                "Fløyen nie je len vyhliadka — od stanice vedú značené chodníky do rozsiahlych lesov, k jazierkam "
                "a ďalej až na susedný vrch Ulriken. Je to obľúbené miesto Bergenčanov na prechádzky, behanie aj "
                "rodinné výlety."
            ),
            "long": "",  # TODO: 5-6 odsekov + história lanovky, trollovia v lese, túra Fløyen→Ulriken
        },
        "legends": [],  # TODO: 2 legendy (napr. drevené sochy trolov v lese; prečo má Bergen sedem vrchov)
    },

    # ------------------------------------------------------------
    {
        "id": "troldhaugen",
        "name": "Troldhaugen — dom Edvarda Griega",
        "category": "bergen",
        "coords": (60.3318, 5.3284),
        "emoji": "🎹",
        "info": {
            "Postavené": "1885 (Grieg tu žil do 1907)",
            "Osobnosť": "Edvard Grieg, najslávnejší nórsky skladateľ",
            "Význam": "Domov, hrob a koncertná sieň skladateľa",
            "Vstup": "múzeum platené; letné koncerty",
            "Web": "https://kodebergen.no/en/troldhaugen",
        },
        "texts": {
            "short": (
                "Troldhaugen je vidiecka vila nad jazerom Nordås, kde žil najslávnejší nórsky skladateľ Edvard "
                "Grieg. V malej drevenej chatke pri brehu komponoval diela ako Peer Gynt či V jaskyni kráľa hôr. "
                "Dnes je z domu múzeum a v modernej koncertnej sieni znejú v lete jeho skladby."
            ),
            "medium": (
                "Troldhaugen, doslova „kopec trolov\", je vidiecka vila nad jazerom Nordås kúsok od Bergenu, kde "
                "od roku 1885 až do svojej smrti v roku 1907 žil Edvard Grieg — najslávnejší nórsky skladateľ a "
                "zakladateľ nórskej národnej hudby.\n\n"
                "Grieg si dom dal postaviť so svojou manželkou, speváčkou Ninou, a nazval ho s typickým humorom "
                "podľa trolov z nórskych povestí. Komponovať však nechodil do domu — pár desiatok metrov nižšie, "
                "priamo nad brehom jazera, si postavil maličkú drevenú chatku. V nej, obklopený tichom a prírodou, "
                "vznikali jeho najznámejšie melódie.\n\n"
                "Z Griegovej hudby pozná celý svet predohru Ráno a najmä dramatické V jaskyni kráľa hôr zo suity "
                "Peer Gynt. Dnes je z vily múzeum so zachovaným nábytkom a Griegovým klavírom značky Steinway. "
                "Manželia sú pochovaní v skale nad jazerom a v modernej koncertnej sieni Troldsalen, ktorá hľadí "
                "oknom priamo na skladateľovu chatku, znejú každé leto jeho diela."
            ),
            "long": (
                "Troldhaugen, doslova „kopec trolov\", je vidiecka drevená vila nad pokojným jazerom Nordås, "
                "len pár kilometrov od centra Bergenu. Od roku 1885 až do svojej smrti v roku 1907 tu žil Edvard "
                "Grieg, najslávnejší nórsky skladateľ a človek, ktorý dal nórskej hudbe vlastný, nezameniteľný hlas.\n\n"
                "Grieg sa narodil v Bergene v roku 1843 a hudobné vzdelanie získal v Lipsku. Vrátil sa však domov "
                "presvedčený, že Nórsko si zaslúži vlastnú vážnu hudbu — takú, ktorá v sebe ponesie ozvenu ľudových "
                "piesní, tancov a drsnej severskej prírody. Dom Troldhaugen si dal postaviť so svojou manželkou a "
                "celoživotnou hudobnou partnerkou, speváčkou Ninou Hagerupovou, ktorá bola zároveň jeho sesternicou. "
                "Meno domu vybrali s humorom, podľa trolov z nórskych povestí.\n\n"
                "Vo veľkom dome sa však Griegovi nekomponovalo dobre — rušili ho návštevy a domáci ruch. Preto si "
                "kúsok nižšie, na samom brehu jazera, postavil maličkú drevenú chatku s jediným oknom a klavírom. "
                "Tam sa každé ráno uťahoval do samoty a tvoril. Práve v tomto tichu vznikli mnohé z jeho najznámejších "
                "diel.\n\n"
                "Z Griegovho diela pozná melódie takmer každý, aj keď nevie, že sú jeho. Ranná nálada z hudby k dráme "
                "Peer Gynt zaznieva vo filmoch aj reklamách, a búrlivé V jaskyni kráľa hôr sa stalo jednou z "
                "najznámejších klasických skladieb vôbec. Jeho klavírny koncert a-mol patrí k pilierom svetového "
                "repertoáru.\n\n"
                "Edvard Grieg zomrel v roku 1907 a Bergen mu vystrojil pohreb, na ktorý prišli desaťtisíce ľudí. "
                "Spolu s manželkou Ninou je pochovaný v skalnej hrobke priamo nad jazerom Nordås, na mieste, ktoré si "
                "sám vybral. Urny sú vsadené do skaly s jednoduchým nápisom.\n\n"
                "Dnes je celý areál múzeom v správe inštitúcie KODE. Vo vile sa zachoval pôvodný nábytok, obrazy a "
                "Griegov klavír značky Steinway, na ktorom sa dodnes hrá. Súčasťou je moderná koncertná sieň Troldsalen, "
                "ktorej veľké okno za pódiom hľadí priamo na skladateľovu chatku pri jazere — takže poslucháči majú "
                "počas letných koncertov pred očami presne to miesto, kde hudba vznikla."
            ),
        },
        "legends": [
            {
                "id": "chatka-pri-jazere",
                "title": "Chatka, kde sa rodila hudba",
                "text": (
                    "Edvard Grieg nedokázal komponovať v rušnom dome plnom návštev. Preto si na samom brehu "
                    "jazera Nordås postavil drobnú drevenú chatku — sotva väčšiu než jedna izba, s klavírom, "
                    "stolíkom a oknom obráteným k vode. Každé ráno si do nej odniesol kávu a uzavrel sa do samoty.\n\n"
                    "Hovorí sa, že na stôl v chatke si položil malú hlinenú žabku pre šťastie a bez nej vraj "
                    "nedokázal začať pracovať. Keď ju raz zabudol doma, údajne sa po ňu vrátil celou cestou späť. "
                    "Drobné rituály a poverčivosť boli pre Griega rovnako dôležité ako talent.\n\n"
                    "Chatka stojí dodnes a je zachovaná tak, ako ju skladateľ zanechal. Z koncertnej siene "
                    "Troldsalen ju vidno cez veľké okno za pódiom — symbolické spojenie medzi miestom, kde hudba "
                    "vznikla, a miestom, kde dnes znie pre poslucháčov."
                ),
            },
            {
                "id": "v-jaskyni-krala-hor",
                "title": "V jaskyni kráľa hôr",
                "text": (
                    "Najznámejšia Griegova melódia pochádza zo scénickej hudby k dráme Henrika Ibsena Peer Gynt. "
                    "Skladba V jaskyni kráľa hôr sprevádza scénu, v ktorej tulák Peer Gynt vstúpi do podzemného "
                    "kráľovstva trolov a ich vládcu — kráľa hôr. Hudba začína potichu a krádavo, no postupne sa "
                    "zrýchľuje a hlasnie, až vyvrcholí v divokej, takmer desivej víchrici tónov, ako keď sa "
                    "rozzúrení trolovia rozbehnú za votrelcom.\n\n"
                    "Sám Grieg si o tejto skladbe v liste posťažoval, že znie tak prehnane „nórsky\", až ju "
                    "nedokáže počúvať bez výsmechu sám pre seba. Práve táto prehnanosť z nej však urobila "
                    "nesmrteľný hit. Dnes patrí k najpoužívanejším skladbám v histórii — zaznieva vo filmoch, "
                    "seriáloch, reklamách aj počítačových hrách.\n\n"
                    "Spojenie trolov, Griega a domu menom Troldhaugen — kopec trolov — tak nie je náhodné. "
                    "Skladateľ, ktorý dal melódiu kráľovi hôr, býval v dome pomenovanom po tých istých bytostiach "
                    "z nórskych povestí."
                ),
            },
        ],
    },

    # ------------------------------------------------------------
    {
        "id": "fisketorget",
        "name": "Rybí trh (Fisketorget)",
        "category": "bergen",
        "coords": (60.3955, 5.3243),
        "emoji": "🐟",
        "info": {
            "Existuje": "od 13. storočia",
            "Poloha": "pri prístave Vågen, vedľa Bryggenu",
            "Význam": "Tradičné trhovisko s morskými plodmi",
            "Vstup": "zadarmo (občerstvenie platené)",
            "Web": "https://www.visitbergen.com",
        },
        "texts": {
            "short": (
                "Rybí trh pri prístave Vågen je jedným zo srdc Bergenu už od stredoveku. Stretávali sa tu rybári, "
                "roľníci a kupci. Dnes ponúka čerstvé morské plody, lososa, kraby aj nórske špeciality a patrí k "
                "najživším miestam mesta."
            ),
            "medium": (
                "Rybí trh, po nórsky Fisketorget, leží priamo pri prístave Vågen, kúsok od hanzového nábrežia "
                "Bryggen. Trhovisko tu funguje už od 13. storočia a po stáročia bolo miestom, kde sa stretávali "
                "rybári z fjordov, roľníci z okolia a kupci z celej Európy.\n\n"
                "Bergen leží medzi morom a horami a more ho po celé dejiny živilo. Na trhu sa preto dodnes predáva "
                "to najlepšie, čo dáva nórske pobrežie — čerstvý losos, treska, kráľovské kraby, krevety, mušle aj "
                "udené a nakladané špeciality. Ochutnať sa dá aj odvážnejšia klasika ako veľrybie mäso.\n\n"
                "Dnes má trh aj krytú modernú časť s reštauráciami, no jeho atmosféra zostáva živá a hlučná. Pre "
                "návštevníkov je to ideálne miesto, kde spojiť prechádzku po prístave s ochutnávkou čerstvých "
                "morských plodov."
            ),
            "long": "",  # TODO: history of fish trade, Bergen-as-fishing-capital, veľrybie mäso kontroverzia
        },
        "legends": [],  # TODO: 2 legendy
    },

    # ------------------------------------------------------------
    {
        "id": "bergenhus",
        "name": "Pevnosť Bergenhus a Håkonova sieň",
        "category": "bergen",
        "coords": (60.3986, 5.3170),
        "emoji": "🏰",
        "info": {
            "Postavené": "Håkonova sieň 1247–1261",
            "Sloh": "stredoveká, renesančná veža",
            "Význam": "Jedna z najstarších pevností v Nórsku",
            "Vstup": "areál zadarmo; sieň a veža platené",
            "Web": "https://www.bymuseet.no",
        },
        "texts": {
            "short": (
                "Pevnosť Bergenhus stráži vstup do prístavu od stredoveku. Jej srdcom je Håkonova sieň, kamenná "
                "kráľovská hala z 13. storočia, kedy bol Bergen hlavným mestom Nórska, a renesančná Rosenkrantzova veža."
            ),
            "medium": (
                "Pevnosť Bergenhus na výbežku pri vstupe do prístavu Vågen je jednou z najstarších a najlepšie "
                "zachovaných pevností v Nórsku. Vznikla v období, keď bol Bergen hlavným mestom kráľovstva.\n\n"
                "Najvzácnejšou stavbou je Håkonova sieň (Håkonshallen), kamenná kráľovská hala, ktorú dal v rokoch "
                "1247 až 1261 postaviť kráľ Håkon Håkonsson ako miesto hostín a slávností. Vedľa stojí mohutná "
                "Rosenkrantzova veža zo 16. storočia, ktorá spájala obytné a obranné účely.\n\n"
                "Počas druhej svetovej vojny sieň ťažko poškodil výbuch holandskej lode naloženej muníciou, ktorá "
                "v roku 1944 vyletela do vzduchu v prístave. Sieň bola starostlivo obnovená a dnes slúži ako "
                "múzeum aj reprezentačný priestor."
            ),
            "long": "",  # TODO: Bergen ako hlavné mesto, Håkon Håkonsson, výbuch 1944, sga
        },
        "legends": [],  # TODO
    },

    # ------------------------------------------------------------
    {
        "id": "mariakirken",
        "name": "Kostol Panny Márie (Mariakirken)",
        "category": "bergen",
        "coords": (60.3978, 5.3196),
        "emoji": "⛪",
        "info": {
            "Postavené": "okolo 1130–1180",
            "Sloh": "románsky, gotické úpravy",
            "Význam": "Najstaršia zachovaná stavba v Bergene",
            "Vstup": "platené (mimo bohoslužieb)",
            "Web": "https://www.visitbergen.com",
        },
        "texts": {
            "short": (
                "Kostol Panny Márie je najstaršia zachovaná budova v Bergene, postavená v 12. storočí. Jeho dve "
                "kamenné veže prečkali požiare, ktoré opakovane ničili drevené mesto okolo. Slúžil aj hanzovým "
                "nemeckým kupcom z neďalekého Bryggenu."
            ),
            "medium": (
                "Kostol Panny Márie, po nórsky Mariakirken, je najstaršou zachovanou stavbou v Bergene. Postavili "
                "ho v románskom slohu okolo polovice 12. storočia a jeho dve mohutné kamenné veže sa stali pevným "
                "bodom v meste, ktoré inak tvorili horľavé drevené domy.\n\n"
                "Práve preto kostol prečkal stáročia požiarov, ktoré okolitú zástavbu opakovane zrovnali so zemou. "
                "Od 15. do 18. storočia slúžil nemeckým kupcom Hanzy z neďalekého nábrežia Bryggen, ktorí ho bohato "
                "vyzdobili — vnútri sa zachoval pôsobivý barokový oltár a kazateľnica.\n\n"
                "Kostol je dodnes funkčný a patrí k najcennejším stredovekým pamiatkam Nórska."
            ),
            "long": "",  # TODO
        },
        "legends": [],  # TODO
    },

    # ------------------------------------------------------------
    {
        "id": "ulriken",
        "name": "Ulriken 643",
        "category": "bergen",
        "coords": (60.3760, 5.3920),
        "emoji": "🚡",
        "info": {
            "Výška": "643 m n. m. (najvyšší zo 7 vrchov)",
            "Doprava": "kabínková lanovka Ulriksbanen",
            "Význam": "Najvyšší z bergenských vrchov, panoráma",
            "Vstup": "lanovka platená",
            "Web": "https://ulriken643.no",
        },
        "texts": {
            "short": (
                "Ulriken je najvyšší zo siedmich vrchov nad Bergenom — meria 643 metrov. Vyvezie naň kabínková "
                "lanovka a z vrcholu je najširší výhľad na mesto, fjordy a okolité hory. Zdatní turisti odtiaľ "
                "zvládnu hrebeňovku až na Fløyen."
            ),
            "medium": (
                "Ulriken je s výškou 643 metrov najvyšší zo siedmich vrchov, ktoré obklopujú Bergen. Na vrchol "
                "vynesie návštevníkov kabínková lanovka Ulriksbanen za pár minút a odmenou je najširší panoramatický "
                "výhľad v okolí — na mesto, prístav, ostrovy a fjordy.\n\n"
                "Vrchol je holý a skalnatý, s vysielačom a vyhliadkovou reštauráciou. Pre zdatných turistov je "
                "Ulriken východiskom obľúbenej celodennej hrebeňovej túry nazývanej Vidden, ktorá vedie náhornou "
                "plošinou až na susedný vrch Fløyen.\n\n"
                "Vďaka výške a otvorenému terénu sa počasie na Ulrikene mení rýchlo — pri hmle či vetre treba dbať "
                "na opatrnosť."
            ),
            "long": "",  # TODO
        },
        "legends": [],  # TODO
    },

    # ------------------------------------------------------------
    {
        "id": "fantoft",
        "name": "Drevený kostol Fantoft",
        "category": "bergen",
        "coords": (60.3349, 5.3370),
        "emoji": "🪵",
        "info": {
            "Postavené": "pôvodne ~1150 (presun 1883, obnova 1997)",
            "Sloh": "stĺpový drevený kostol (stavkirke)",
            "Význam": "Stredoveká drevená architektúra",
            "Vstup": "platené (sezónne)",
            "Web": "https://www.visitbergen.com",
        },
        "texts": {
            "short": (
                "Fantoft je stĺpový drevený kostol, takzvaný stavkirke — typ stredovekej nórskej stavby z dreva "
                "s ostrými strechami a dračími hlavami. Pôvodne stál inde a v roku 1883 ho premiestnili k Bergenu. "
                "V roku 1992 ho podpálili a o päť rokov verne obnovili."
            ),
            "medium": (
                "Fantoft je stĺpový drevený kostol, po nórsky stavkirke — typ stredovekej stavby, ktorá je pre "
                "Nórsko rovnako charakteristická ako fjordy. Tieto kostoly z dreva, s viacerými stupňami strmých "
                "striech, dračími hlavami na štítoch a smolou natretými stenami, stavali Nóri od 12. storočia.\n\n"
                "Pôvodný kostol Fantoft postavili okolo roku 1150 v dedine Fortun pri Sognefjorde. Keď mu v 19. "
                "storočí hrozila demolácia, v roku 1883 ho rozobrali a premiestnili na okraj Bergenu, aby ho zachránili.\n\n"
                "V roku 1992 kostol úplne zhorel pri podpaľačskom útoku spojenom s nórskou blackmetalovou scénou. "
                "Bergen ho však v rokoch 1995 až 1997 verne obnovil podľa pôvodných plánov, takže dnes opäť stojí "
                "ako pripomienka stredovekého umenia práce s drevom."
            ),
            "long": "",  # TODO: stavkirke ako typ, dračie hlavy/pohanské motívy, požiar 1992 blackmetal
        },
        "legends": [],  # TODO (požiar 1992 — vďačná, ale citlivá téma; faktograficky)
    },

    # ============================================================
    # STAVANGER
    # ============================================================
    {
        "id": "gamle-stavanger",
        "name": "Staré Stavanger",
        "category": "stavanger",
        "coords": (58.9690, 5.7280),
        "emoji": "🏘️",
        "info": {
            "Postavené": "18.–19. storočie",
            "Rozsah": "okolo 170 drevených domov",
            "Význam": "Najväčšia súvislá drevená zástavba v severnej Európe",
            "Vstup": "zadarmo (ulice)",
            "Web": "https://www.regionstavanger.com",
        },
        "texts": {
            "short": (
                "Staré Stavanger je štvrť úzkych dláždených uličiek s vyše stovkou nízkych bielych drevených "
                "domčekov z 18. a 19. storočia. Je to najväčší súvislý celok drevenej zástavby v severnej Európe "
                "a najpôvabnejšia časť mesta."
            ),
            "medium": (
                "Staré Stavanger, po nórsky Gamle Stavanger, je historická štvrť na západnom brehu prístavu, "
                "ktorú tvorí okolo stosedemdesiat nízkych bielych drevených domov z 18. a 19. storočia. Považuje "
                "sa za najväčšiu súvislú zachovanú drevenú zástavbu v severnej Európe.\n\n"
                "Úzke uličky vydláždené okruhliakmi, biele fasády, kvetináče v oknách a kované lampy vytvárajú "
                "atmosféru, ktorá sa za stáročia takmer nezmenila. Domy obývali rybári, remeselníci a robotníci, "
                "mnohé súvisia s érou rybolovu a konzervovania sardiniek, ktoré z mesta urobili priemyselné centrum.\n\n"
                "Že táto štvrť vôbec prežila, je zásluha miestneho architekta Einara Heddena, ktorý v polovici 20. "
                "storočia presadil jej ochranu namiesto búrania. Dnes je Gamle Stavanger chránenou pamiatkou a "
                "najfotografovanejším miestom mesta."
            ),
            "long": (
                "Staré Stavanger, po nórsky Gamle Stavanger, je historické jadro na západnom brehu prístavu — "
                "spleť úzkych dláždených uličiek s približne stosedemdesiatimi nízkymi bielymi drevenými domami "
                "zo 18. a 19. storočia. Je to najväčšia súvislá zachovaná drevená zástavba v severnej Európe a "
                "zároveň najpôvabnejšia časť mesta.\n\n"
                "Stavanger bol po stáročia mestom rybárov a námorníkov. V 19. a začiatkom 20. storočia ho preslávil "
                "rybolov a najmä konzervovanie sardiniek — v meste fungovali desiatky konzervární a ich vône a "
                "ruch určovali život celých štvrtí. Práve robotníci, rybári a remeselníci z tohto obdobia obývali "
                "drevené domčeky, ktoré sa zachovali dodnes.\n\n"
                "Biele fasády, okná s malými tabuľkami, kvetináče, kované pouličné lampy a okruhliaky pod nohami "
                "vytvárajú atmosféru, ktorá sa za stáročia takmer nezmenila. Štvrť pôsobí ako živý skanzen — domy "
                "sú stále obývané, nejde o múzeum za plotom.\n\n"
                "Že táto časť mesta vôbec prežila, nie je samozrejmé. V polovici 20. storočia hrozilo, že staré "
                "drevené domy ustúpia modernej výstavbe. Zachránil ich miestny architekt Einar Hedden, ktorý "
                "presadil ich ochranu a obnovu namiesto búrania — v dobe, keď sa to považovalo takmer za "
                "výstrednosť.\n\n"
                "Dnes je Gamle Stavanger chránenou pamiatkou a najfotografovanejším miestom mesta. V niektorých "
                "domoch sídlia drobné galérie, dielne a Nórske konzervárenské múzeum, ktoré pripomína éru sardiniek. "
                "Prechádzka touto štvrťou patrí k tomu najlepšiemu, čo Stavanger ponúka."
            ),
        },
        "legends": [
            {
                "id": "sardinky",
                "title": "Mesto, ktoré voňalo sardinkami",
                "text": (
                    "Na prelome 19. a 20. storočia bol Stavanger hlavným mestom nórskeho konzervárenského "
                    "priemyslu. V meste fungovali desiatky tovární, ktoré spracúvali a do plechoviek balili "
                    "sardinky a šproty. V čase najväčšieho rozmachu zamestnávali tisíce ľudí, najmä ženy a deti, "
                    "ktoré ručne ukladali rybky do plechoviek.\n\n"
                    "Charakteristická vôňa údených rýb sa niesla celým mestom a stala sa jeho poznávacím znamením. "
                    "Stavangerské sardinky sa vyvážali do celého sveta a etikety na plechovkách — často pestré a "
                    "vynaliezavé — sú dnes zberateľským predmetom. Práve tomuto obdobiu vďačí mesto za svoj rast.\n\n"
                    "Príbeh konzervární pripomína Nórske konzervárenské múzeum, zriadené v jednej z pôvodných "
                    "tovární v Starom Stavangeri. Návštevníci si tu môžu pozrieť pôvodné stroje aj vyskúšať, ako "
                    "sa rybky balili a údili."
                ),
            },
        ],  # možno doplniť 2. legendu
    },

    # ------------------------------------------------------------
    {
        "id": "stavanger-domkirken",
        "name": "Katedrála v Stavangeri",
        "category": "stavanger",
        "coords": (58.9700, 5.7330),
        "emoji": "⛪",
        "info": {
            "Postavené": "okolo 1125",
            "Sloh": "románsky, gotický chór",
            "Význam": "Najstaršia katedrála Nórska v pôvodnej podobe",
            "Vstup": "platené (mimo bohoslužieb)",
            "Web": "https://www.kirken.no",
        },
        "texts": {
            "short": (
                "Katedrála v Stavangeri je najstaršia nórska katedrála, ktorá si zachovala pôvodnú podobu. Postavili "
                "ju okolo roku 1125 a od tých čias slúži bez prerušenia. Spája románske jadro s neskorším gotickým chórom."
            ),
            "medium": (
                "Katedrála v Stavangeri, po nórsky Domkirken, je najstaršou katedrálou Nórska, ktorá sa zachovala "
                "v pôvodnej podobe a nepretržite slúži od svojho posvätenia. Postaviť ju dal okolo roku 1125 biskup "
                "Reinald, údajne pochádzajúci z Anglicka, a zasvätená je svätému Svithunovi.\n\n"
                "Stavba spája masívne románske jadro s loďou z 12. storočia a elegantnejší gotický chór, ktorý "
                "pribudol po požiari v 13. storočí. Vo vnútri zaujme bohato rezbársky zdobená baroková kazateľnica.\n\n"
                "Katedrála stojí v samom srdci mesta medzi dvoma námestiami a jazierkom Breiavatnet a je dôkazom, "
                "že Stavanger patrí k najstarším mestám Nórska — svoje výročie ráta práve od založenia biskupstva "
                "a katedrály."
            ),
            "long": "",  # TODO: sv. Svithun, biskup Reinald, požiar 13. stor., 900 rokov mesta
        },
        "legends": [],  # TODO
    },

    # ------------------------------------------------------------
    {
        "id": "fargegaten",
        "name": "Fargegaten (farebná ulica)",
        "category": "stavanger",
        "coords": (58.9712, 5.7345),
        "emoji": "🌈",
        "info": {
            "Vzniklo": "súčasná podoba okolo 2005",
            "Pôvodný názov": "Øvre Holmegate",
            "Význam": "Najfarebnejšia a najživšia ulica mesta",
            "Vstup": "zadarmo",
            "Web": "https://www.regionstavanger.com",
        },
        "texts": {
            "short": (
                "Fargegaten, doslova „farebná ulica\", je ulica Øvre Holmegate v centre Stavangeru, kde sú domy "
                "natreté živými farbami — tyrkysovou, ružovou, žltou, modrou. Z kedysi upadajúcej uličky sa stala "
                "najveselšia časť mesta plná kaviarní a barov."
            ),
            "medium": (
                "Fargegaten, doslova „farebná ulica\", je oficiálne ulica Øvre Holmegate v centre Stavangeru. "
                "Jej domy sú natreté žiarivými farbami — tyrkysovou, ružovou, žltou, oranžovou a modrou — a vytvárajú "
                "jeden z najveselších mestských pohľadov v Nórsku.\n\n"
                "Ešte na začiatku 21. storočia bola ulička upadajúca a takmer prázdna. Miestny kaderník Tom Kjørsvik "
                "prišiel s nápadom oživiť ju farbami a oslovil umelca Craiga Flannagana, ktorý navrhol presnú "
                "farebnú schému pre celú ulicu. Po počiatočnej nedôvere majiteľov sa premena podarila.\n\n"
                "Dnes je Fargegaten najživšou ulicou Stavangeru — lemujú ju kaviarne, bary, malé obchodíky a "
                "reštaurácie a je obľúbeným miestom stretnutí cez deň aj večer."
            ),
            "long": "",  # TODO: príbeh premeny, Craig Flannagan, gentrifikácia
        },
        "legends": [],  # TODO
    },

    # ------------------------------------------------------------
    {
        "id": "sverd-i-fjell",
        "name": "Meče v skale (Sverd i fjell)",
        "category": "stavanger",
        "coords": (58.8896, 5.7280),
        "emoji": "⚔️",
        "info": {
            "Postavené": "1983",
            "Autor": "Fritz Røed",
            "Pripomína": "Bitku pri Hafrsfjorde (872)",
            "Vstup": "zadarmo",
            "Web": "https://www.regionstavanger.com",
        },
        "texts": {
            "short": (
                "Tri obrovské bronzové meče zapichnuté do skaly nad fjordom Hafrsfjord pripomínajú bitku z roku 872, "
                "v ktorej kráľ Harald Krásnovlasý zjednotil Nórsko do jedného kráľovstva. Najväčší meč meria takmer "
                "desať metrov."
            ),
            "medium": (
                "Pamätník Sverd i fjell, doslova „meče v skale\", tvoria tri obrovské bronzové meče zapichnuté "
                "do skaly na brehu fjordu Hafrsfjord pri Stavangeri. Najväčší z nich meria takmer desať metrov. "
                "Monument vytvoril sochár Fritz Røed a odhalený bol v roku 1983 za účasti nórskeho kráľa.\n\n"
                "Meče pripomínajú rozhodujúcu bitku pri Hafrsfjorde z roku 872, v ktorej kráľ Harald Krásnovlasý "
                "porazil ostatných nórskych kniežat a po prvý raz zjednotil Nórsko do jedného kráľovstva. Podľa "
                "tradície je to zakladajúci okamih nórskeho národa.\n\n"
                "Tri meče zarazené napevno do skaly symbolizujú mier — boj sa skončil a zbrane už nikto nevytiahne. "
                "Najväčší meč predstavuje víťazného Haralda, dva menšie porazených kráľov. Miesto je voľne prístupné "
                "priamo pri vode."
            ),
            "long": (
                "Pamätník Sverd i fjell, doslova „meče v skale\", patrí k najpôsobivejším monumentom Nórska. "
                "Tvoria ho tri obrovské bronzové meče zarazené až po jílec do skaly na brehu fjordu Hafrsfjord, "
                "kúsok od Stavangeru. Najväčší z nich meria takmer desať metrov. Dielo vytvoril sochár Fritz Røed "
                "a slávnostne ho odhalil nórsky kráľ Olav Piaty v roku 1983.\n\n"
                "Monument pripomína bitku pri Hafrsfjorde, ktorá sa podľa tradície odohrala v roku 872. V nej "
                "kráľ Harald Krásnovlasý — po nórsky Harald Hårfagre — porazil spojené sily ostatných nórskych "
                "kniežat a po prvý raz zjednotil dovtedy rozdrobené územie do jediného kráľovstva. Práve tento "
                "okamih sa považuje za zrod Nórska ako národa.\n\n"
                "K bitke sa viaže slávna legenda o Haraldovom sľube. Vraj sa zaľúbil do hrdej princeznej Gydy, "
                "ktorá ho odmietla so slovami, že sa nevydá za muža, ktorý vládne len malému kúsku zeme. Harald "
                "preto prisahal, že si nedá ostrihať ani učesať vlasy, kým neovládne celé Nórsko. Po víťaznej "
                "bitke pri Hafrsfjorde si dal vlasy konečne upraviť a získal prezývku Krásnovlasý.\n\n"
                "Symbolika pamätníka je premyslená. Tri meče sú zarazené do živej skaly tak pevne, že ich už nikdy "
                "nikto nevytiahne — sú znamením mieru a zjednotenia, koniec bojov medzi nórskymi kráľovstvami. "
                "Najväčší meč predstavuje víťazného Haralda, dva menšie meče porazených kniežat. Tvar mečov vychádza "
                "zo skutočných typov zbraní z čias Vikingov nájdených v rôznych častiach krajiny.\n\n"
                "Pamätník stojí voľne prístupný priamo pri vode a v lete sa stáva obľúbeným miestom prechádzok aj "
                "kúpania. Pre Nórov má však aj hlbší význam — je to miesto, kde sa symbolicky začínajú dejiny ich "
                "zjednotenej krajiny."
            ),
        },
        "legends": [
            {
                "id": "harald-a-gyda",
                "title": "Sľub o neostrihaných vlasoch",
                "text": (
                    "Podľa ság, ktoré spísal islandský učenec Snorri Sturluson, sa mladý kráľ Harald zaľúbil do "
                    "krásnej a hrdej princeznej Gydy a poslal za ňou poslov so žiadosťou o ruku. Gyda im však "
                    "odkázala, že sa nevydá za muža, ktorý vládne len niekoľkým malým krajom. Vydá sa vraj iba za "
                    "kráľa, ktorý ovládne celé Nórsko, tak ako iní králi ovládli Dánsko či Švédsko.\n\n"
                    "Harald sa neurazil — naopak, jej slová ho zapálili. Verejne prisahal, že si nedá ostrihať ani "
                    "učesať vlasy dovtedy, kým nezjednotí celé Nórsko pod svojou vládou. Roky potom viedol boje s "
                    "ostatnými kniežatami a jeho vlasy rástli dlhé a strapaté, takže mu prischla prezývka Harald "
                    "Lufa — strapatý.\n\n"
                    "Až po rozhodujúcom víťazstve v bitke pri Hafrsfjorde si dal vlasy konečne upraviť. Vtedy "
                    "vraj získal nové, krajšie meno — Harald Hårfagre, Krásnovlasý. A podľa povesti napokon získal "
                    "aj Gydu. Tri meče v skale stoja presne na mieste, kde sa táto zakladajúca legenda nórskeho "
                    "kráľovstva odohrala."
                ),
            },
        ],
    },

    # ------------------------------------------------------------
    {
        "id": "oljemuseet",
        "name": "Nórske ropné múzeum",
        "category": "stavanger",
        "coords": (58.9740, 5.7310),
        "emoji": "🛢️",
        "info": {
            "Otvorené": "1999",
            "Téma": "Ťažba ropy a plynu v Severnom mori",
            "Význam": "Príbeh nórskeho ropného bohatstva",
            "Vstup": "platené",
            "Web": "https://www.norskolje.museum.no",
        },
        "texts": {
            "short": (
                "Nórske ropné múzeum v Stavangeri rozpráva príbeh, ktorý zmenil krajinu — objav ropy v Severnom "
                "mori koncom 60. rokov, ktorý z chudobnej rybárskej krajiny urobil jeden z najbohatších štátov "
                "sveta. Budova pri vode pripomína ropnú plošinu."
            ),
            "medium": (
                "Nórske ropné múzeum stojí pri vode v centre Stavangeru, mesta, ktoré sa stalo ropným hlavným "
                "mestom Nórska. Jeho budova s kovovými konštrukciami zámerne pripomína ropnú plošinu.\n\n"
                "Múzeum rozpráva príbeh, ktorý úplne zmenil osud krajiny. Koncom 60. rokov 20. storočia objavili "
                "v nórskej časti Severného mora obrovské ložiská ropy a plynu. Z chudobnej rybárskej a námornej "
                "krajiny sa za jedinú generáciu stal jeden z najbohatších štátov sveta.\n\n"
                "Expozícia ukazuje modely plošín, skutočné vrtné zariadenia, ochranné obleky aj záchranné kapsule "
                "a vysvetľuje, ako Nórsko premenilo ropné príjmy na obrovský štátny fond pre budúce generácie. "
                "Nevyhýba sa ani témam nehôd a vplyvu na klímu."
            ),
            "long": "",  # TODO: objav Ekofisk 1969, štátny fond, klimatický paradox, nehoda Alexander Kielland
        },
        "legends": [],  # TODO
    },

    # ------------------------------------------------------------
    {
        "id": "preikestolen",
        "name": "Preikestolen (Kazateľnica)",
        "category": "stavanger",
        "coords": (58.9864, 6.1904),
        "emoji": "🪨",
        "info": {
            "Výška": "604 m nad Lysefjordom",
            "Plošina": "približne 25 × 25 m",
            "Túra": "~8 km tam a späť, 3,5–4 h",
            "Vstup": "zadarmo (parkovisko platené)",
            "Web": "https://www.visitnorway.com",
        },
        "texts": {
            "short": (
                "Preikestolen, „Kazateľnica\", je plochá skalná plošina týčiaca sa 604 metrov kolmo nad "
                "Lysefjordom. Patrí k najslávnejším výhľadom Nórska. Vedie k nej obľúbená štvorhodinová túra a "
                "z okraja sa otvára závratný pohľad do hĺbky fjordu."
            ),
            "medium": (
                "Preikestolen, po nórsky „kazateľnica\", je takmer dokonale plochá skalná plošina, ktorá sa "
                "týči vo výške 604 metrov kolmo nad hladinou Lysefjordu. S rozmermi približne dvadsaťpäť krát "
                "dvadsaťpäť metrov a strmým zrázom bez akéhokoľvek zábradlia patrí k najikonickejším a "
                "najfotografovanejším miestam Nórska.\n\n"
                "Skala vznikla počas doby ľadovej, keď mráz rozštiepil žulu pozdĺž kolmých puklín a ľadovec "
                "odlomil zvyšok. Vznikol tak ostrý, rovný okraj, ktorý vyzerá ako umelo vytesaný.\n\n"
                "K Preikestolenu vedie značená túra dlhá zhruba osem kilometrov tam aj späť, ktorú väčšina ľudí "
                "zvládne za necelé štyri hodiny. Chodník je miestami strmý a kamenistý, no veľmi obľúbený — v "
                "sezóne ním prejdú tisíce ľudí denne. Odmenou je závratný pohľad do hĺbky fjordu a na okolité hory."
            ),
            "long": (
                "Preikestolen, po nórsky doslova „kazateľnica\", je takmer dokonale plochá skalná plošina, ktorá "
                "sa týči vo výške 604 metrov kolmo nad temnou hladinou Lysefjordu. S rozmermi približne dvadsaťpäť "
                "krát dvadsaťpäť metrov a takmer pravouhlým okrajom bez akéhokoľvek zábradlia patrí k "
                "najslávnejším a najfotografovanejším prírodným útvarom Nórska aj celej Európy.\n\n"
                "Skala vznikla počas poslednej doby ľadovej, asi pred desaťtisíc rokmi. Voda zamrznutá v zvislých "
                "puklinách žuly ich postupne rozširovala, až sa pozdĺž nich odlomili celé bloky kameňa. Ustupujúci "
                "ľadovec odniesol zvyšok a zanechal ostrý, rovný okraj, ktorý vyzerá, akoby ho niekto vytesal "
                "naschvál. Naprieč plošinou vedie nápadná trhlina — pre mnohých návštevníkov zdroj obáv, hoci "
                "geológovia ju považujú za stabilnú.\n\n"
                "Zaujímavé je, že Preikestolen sa stal turistickým cieľom až v 20. storočí. Miestni ľudia naň "
                "dovtedy nemali dôvod chodiť a názov „kazateľnica\" sa ujal až vďaka turistickému spolku začiatkom "
                "minulého storočia. Dnes je to úplný opak — v letnej sezóne sem prúdia tisíce turistov denne a "
                "patrí k najnavštevovanejším miestam krajiny.\n\n"
                "K plošine vedie značená horská túra dlhá zhruba osem kilometrov tam aj späť. Väčšina ľudí ju "
                "zvládne za tri a pol až štyri hodiny. Chodník striedava strmé kamenisté úseky s drevenými lávkami "
                "ponad mokrade a stúpa približne o tristopäťdesiat metrov. Nie je extrémne náročný, no vyžaduje "
                "pevnú obuv a slušnú kondíciu — a počasie v horách sa môže rýchlo zmeniť.\n\n"
                "Najväčším zážitkom je samotný okraj plošiny. Pohľad do šesťstometrovej hĺbky, kde sa fjord vinie "
                "medzi kolmými stenami, vyráža dych aj otrlým návštevníkom. Mnohí si sadnú s nohami nad priepasťou, "
                "iní sa k okraju neodvážia vôbec. Napriek absencii zábradlia je vážnych nehôd prekvapivo málo, no "
                "opatrnosť — najmä pri vetre a mokrej skale — je namieste. Pre pokojnejší zážitok bez davov sa "
                "oplatí vyraziť skoro ráno alebo neskoro popoludní."
            ),
        },
        "legends": [
            {
                "id": "sedem-bratov",
                "title": "Povera o siedmich bratoch",
                "text": (
                    "K Preikestolenu sa viaže stará miestna povera. Hovorí, že keď sa raz sedem bratov ožení so "
                    "siedmimi sestrami, alebo keď sa na plošine zosobášia dvaja súrodenci z jednej rodiny, skala "
                    "sa odlomí a zrúti do fjordu. Práve preto sa vraj kedysi miestni Preikestolenu vyhýbali a "
                    "nepovažovali ho za miesto na oslavy.\n\n"
                    "Povera odráža prirodzený rešpekt ľudí pred mohutnou skalou visiacou nad priepasťou. Naprieč "
                    "plošinou navyše vedie viditeľná trhlina, ktorá v návštevníkoch dodnes vzbudzuje otázku, či "
                    "raz okraj naozaj nespadne.\n\n"
                    "Geológovia sú však pokojní — merania ukazujú, že trhlina sa nerozširuje a skala je stabilná. "
                    "Napriek tomu sa práve na Preikestolene koná čoraz viac symbolických zásnub a svadieb, akoby "
                    "dnešní ľudia chceli starej povere vzdorovať."
                ),
            },
        ],
    },

    # ------------------------------------------------------------
    {
        "id": "lysefjord",
        "name": "Lysefjord",
        "category": "stavanger",
        "coords": (59.0400, 6.4000),
        "emoji": "🌊",
        "info": {
            "Dĺžka": "približne 42 km",
            "Steny": "kolmé útesy až do 1000 m",
            "Atrakcie": "Preikestolen, Kjerag, Flørli (4444 schodov)",
            "Vstup": "výletné lode z Stavangeru",
            "Web": "https://www.visitnorway.com",
        },
        "texts": {
            "short": (
                "Lysefjord, „svetlý fjord\", je 42 kilometrov dlhý fjord pri Stavangeri, lemovaný kolmými "
                "žulovými stenami. Týčia sa nad ním dve ikony Nórska — plošina Preikestolen a balvan Kjeragbolten. "
                "Najlepšie sa naň díva z paluby výletnej lode."
            ),
            "medium": (
                "Lysefjord, po nórsky „svetlý fjord\", dostal meno podľa svetlej žuly, ktorá sa za slnka leskne "
                "na jeho kolmých stenách. Tiahne sa zhruba štyridsaťdva kilometrov do vnútrozemia od Stavangeru a "
                "jeho útesy miestami spadajú do vody z výšky takmer tisíc metrov.\n\n"
                "Nad fjordom sa týčia dve najslávnejšie nórske atrakcie — plochá plošina Preikestolen a balvan "
                "Kjeragbolten zakliesnený medzi dve skalné steny. Pri dedinke Flørli vedie po svahu vyše štyritisíc "
                "drevených schodov pozdĺž starého potrubia vodnej elektrárne, vraj najdlhšie drevené schodisko sveta.\n\n"
                "Najpohodlnejší spôsob, ako Lysefjord zažiť, je výletná loď zo Stavangeru. Tá pláva tesne popod "
                "Preikestolen, zastavuje pod vodopádmi a ukazuje fjord z perspektívy, akú pešiaci na vrchole nemajú."
            ),
            "long": "",  # TODO: vznik fjordov, Flørli schody, Kjerag, lodné výlety, kozy pod vodopádom
        },
        "legends": [],  # TODO: 2 legendy
    },

    # ------------------------------------------------------------
    {
        "id": "kjerag",
        "name": "Kjerag a Kjeragbolten",
        "category": "stavanger",
        "coords": (59.0347, 6.5933),
        "emoji": "🧗",
        "info": {
            "Výška": "vrchol ~1084 m; balvan ~984 m nad fjordom",
            "Túra": "~10 km tam a späť, 6–7 h, náročná",
            "Atrakcia": "Kjeragbolten — balvan zakliesnený nad priepasťou",
            "Vstup": "zadarmo (parkovisko platené, sezónne)",
            "Web": "https://www.visitnorway.com",
        },
        "texts": {
            "short": (
                "Kjerag je vysoký masív nad Lysefjordom, známy balvanom Kjeragbolten — okrúhlym kameňom "
                "zakliesneným medzi dve skalné steny nad takmer tisícmetrovou priepasťou. Postaviť sa naň je "
                "obľúbená skúška odvahy."
            ),
            "medium": (
                "Kjerag je skalnatý masív týčiaci sa nad vnútornou časťou Lysefjordu. Jeho najvyšší bod dosahuje "
                "vyše tisícosemdesiat metrov a steny spadajú takmer kolmo do fjordu. Pre väčšinu návštevníkov je "
                "však hlavným lákadlom balvan Kjeragbolten.\n\n"
                "Ide o okrúhly päťkubíkový kameň, ktorý počas doby ľadovej uviazol zakliesnený medzi dve skalné "
                "steny tesne nad priepasťou hlbokou takmer tisíc metrov. Postaviť sa naň — s ničím pod nohami "
                "okrem vzduchu a hladiny fjordu hlboko dole — je jednou z najznámejších skúšok odvahy v Nórsku.\n\n"
                "Túra na Kjerag je výrazne náročnejšia než na Preikestolen — meria okolo desať kilometrov, vedie "
                "cez tri strmé stúpania istené reťazami a trvá šesť až sedem hodín. Kjerag je tiež obľúbeným "
                "miestom skokanov v overaloch (BASE jumping)."
            ),
            "long": "",  # TODO
        },
        "legends": [],  # TODO
    },

    # ============================================================
    # FJORDY (širšie západné Nórsko)
    # ============================================================
    {
        "id": "geirangerfjord",
        "name": "Geirangerfjord",
        "category": "fjordy",
        "coords": (62.1010, 7.0060),
        "emoji": "🏞️",
        "info": {
            "Dĺžka": "asi 15 km (rameno Storfjordu)",
            "Význam": "Pamiatka UNESCO (od 2005)",
            "Atrakcie": "vodopády Sedem sestier, Závojová fata, opustené horské farmy",
            "Vstup": "výletné lode a trajekt Geiranger–Hellesylt",
            "Web": "https://www.visitnorway.com",
        },
        "texts": {
            "short": (
                "Geirangerfjord je azda najkrajší nórsky fjord a pamiatka UNESCO. Úzke rameno medzi kolmými "
                "horami zdobia vodopády ako Sedem sestier a Závojová fata a na nedostupných skalných terasách "
                "ešte stoja opustené horské farmy."
            ),
            "medium": (
                "Geirangerfjord je často označovaný za najkrajší fjord Nórska a v roku 2005 ho spolu s "
                "Nærøyfjordom zapísali na zoznam svetového dedičstva UNESCO. Je to úzke, pätnásťkilometrové "
                "rameno veľkého Storfjordu, sevreté medzi takmer kolmými horami.\n\n"
                "Po stenách fjordu padá množstvo vodopádov. Najznámejší sú Sedem sestier — sedem prúdov vedľa "
                "seba — a oproti nim Závojová fata, takzvaný Nápadník. K nim sa viaže romantická povesť. Vysoko "
                "na nedostupných skalných terasách ešte stoja opustené horské farmy, ku ktorým sa kedysi roľníci "
                "šplhali po rebríkoch.\n\n"
                "Fjord sa najlepšie zažíva z paluby lode alebo trajektu medzi dedinkami Geiranger a Hellesylt. "
                "Nad fjordom vedie aj slávna serpentínová cesta s vyhliadkou Ørnesvingen, Orlia cesta."
            ),
            "long": (
                "Geirangerfjord je často označovaný za najkrajší fjord Nórska a patrí k najfotografovanejším "
                "krajinkám severnej Európy. V roku 2005 ho spolu s Nærøyfjordom zapísali na zoznam svetového "
                "dedičstva UNESCO ako jeden z najnádhernejších a najlepšie zachovaných fjordov sveta. Je to úzke "
                "rameno veľkého Storfjordu, dlhé asi pätnásť kilometrov, sevreté medzi horami, ktoré z vody "
                "stúpajú takmer kolmo do výšky vyše tisíc metrov.\n\n"
                "Fjordy vznikli počas dôb ľadových, keď obrovské ľadovce vyhĺbili do pevniny hlboké údolia. Keď "
                "ľad roztopil, do údolí vnikla morská voda a vytvorila dnešné fjordy s ich charakteristickými "
                "kolmými stenami a veľkou hĺbkou.\n\n"
                "Po stenách Geirangerfjordu padajú desiatky vodopádov, najmä na jar, keď sa topí sneh. "
                "Najznámejší z nich sú Sedem sestier — skupina siedmich prúdov padajúcich vedľa seba — a oproti "
                "nim na druhej strane fjordu vodopád prezývaný Nápadník alebo Závojová fata, ktorého tvar "
                "pripomína fľašu. K týmto vodopádom sa viaže romantická aj trpká ľudová povesť.\n\n"
                "Vysoko nad hladinou, na úzkych skalných terasách a strminách, ešte stoja opustené horské farmy "
                "ako Skageflå alebo Knivsflå. Roľníci tu kedysi obrábali nepatrné políčka a k svojim domom sa "
                "dostávali len po strmých chodníkoch a rebríkoch. Vraj keď prišiel výberca daní, rebríky jednoducho "
                "vytiahli a stali sa nedosiahnuteľnými. Život tu utíchol začiatkom 20. storočia, keď sa rodiny "
                "presťahovali do dolín.\n\n"
                "Najkrajší spôsob, ako fjord zažiť, je z paluby lode alebo trajektu, ktorý premáva medzi dedinkami "
                "Geiranger a Hellesylt a pláva tesne popod vodopády. Nad samotnou dedinou Geiranger sa vinie slávna "
                "serpentínová Orlia cesta s vyhliadkou Ørnesvingen a z opačnej strany sa fjord otvára z vyhliadky "
                "Dalsnibba vo výške vyše tisícpäťsto metrov. Pre svoju krásu sa však Geiranger stal aj obeťou "
                "vlastnej slávy — v sezóne sem pripláva množstvo veľkých výletných lodí."
            ),
        },
        "legends": [
            {
                "id": "sedem-sestier-napadnik",
                "title": "Sedem sestier a ich nápadník",
                "text": (
                    "Najznámejšie vodopády Geirangerfjordu majú podľa ľudovej povesti svoj príbeh. Na jednej "
                    "strane fjordu padá sedem štíhlych prúdov vedľa seba — Sedem sestier. Hovorí sa, že "
                    "predstavujú sedem hravých dievčat, ktoré tancujú a poskakujú dolu skalnou stenou.\n\n"
                    "Presne oproti nim, na druhom brehu, padá širší a mohutnejší vodopád prezývaný Nápadník, po "
                    "nórsky Friaren. Podľa povesti sa tento mládenec uchádzal o všetkých sedem sestier naraz, no "
                    "žiadna ho nechcela. Z neúspechu a žiaľu sa dal na pitie — a práve preto má jeho vodopád tvar "
                    "pripomínajúci fľašu, kvôli čomu sa mu hovorí aj Závojová fľaša.\n\n"
                    "Tak stoja Nápadník a Sedem sestier oproti sebe naveky, oddelení vodami fjordu — on márne "
                    "túžiaci, ony nedosiahnuteľné. Je to jedna z najmilších povestí, aké sa o nórskych vodopádoch "
                    "rozprávajú, a sprievodcovia na lodiach ju radi pripomínajú práve v mieste, kde sa oba "
                    "vodopády vidia naraz."
                ),
            },
            {
                "id": "horske-farmy",
                "title": "Farmy, kam sa liezlo po rebríku",
                "text": (
                    "Vysoko nad hladinou Geirangerfjordu, na úzkych skalných terasách, stoja dodnes opustené "
                    "horské farmy. Najznámejšie sú Skageflå a Knivsflå. Roľníci tu po stáročia hospodárili na "
                    "nepatrných políčkach zavesených nad priepasťou, pásli kozy a ovce a pestovali to málo, čo "
                    "sa na strmom svahu dalo.\n\n"
                    "K niektorým z týchto fariem neviedla žiadna cesta — dalo sa k nim dostať len po dlhých "
                    "drevených rebríkoch pripevnených k skale. Hovorí sa, že keď sa blížil kráľovský výberca "
                    "daní, obyvatelia jednoducho vytiahli rebríky nahor a farma sa stala nedosiahnuteľnou. "
                    "Daň teda neraz nezaplatili — nie zo vzdoru, ale preto, že sa k nim výberca nedostal.\n\n"
                    "Život na týchto farmách bol drsný a nebezpečný. Rodičia vraj malé deti priväzovali o lano "
                    "alebo o kôl, aby sa nezrútili do fjordu. Začiatkom 20. storočia ľudia tieto miesta postupne "
                    "opustili a presťahovali sa do dolín. Dnes sú opustené farmy obľúbeným cieľom turistov, ktorí "
                    "k nim stúpajú z paluby lode strmými chodníkmi."
                ),
            },
        ],
    },

    # ------------------------------------------------------------
    {
        "id": "naeroyfjord",
        "name": "Nærøyfjord",
        "category": "fjordy",
        "coords": (60.9170, 6.9330),
        "emoji": "🚣",
        "info": {
            "Dĺžka": "asi 17 km (rameno Sognefjordu)",
            "Šírka": "v najužšom mieste len ~250 m",
            "Význam": "Pamiatka UNESCO (od 2005)",
            "Vstup": "lode a kajaky z Gudvangenu/Flåmu",
            "Web": "https://www.visitnorway.com",
        },
        "texts": {
            "short": (
                "Nærøyfjord je najužší fjord Nórska — v najtesnejšom mieste má len asi 250 metrov, pričom hory "
                "okolo dosahujú vyše 1700 metrov. Spolu s Geirangerfjordom je pamiatkou UNESCO a patrí k "
                "najdramatickejším fjordom sveta."
            ),
            "medium": (
                "Nærøyfjord je rameno veľkého Sognefjordu, najdlhšieho fjordu Nórska, a zároveň jeho "
                "najdramatickejšia časť. V najužšom mieste má šírku len okolo dvestopäťdesiat metrov, kým hory "
                "po jeho stranách sa týčia do výšky vyše tisícsedemsto metrov. Vzniká tak pocit, akoby loď plávala "
                "úzkou skalnou chodbou.\n\n"
                "V roku 2005 bol Nærøyfjord spolu s Geirangerfjordom zapísaný na zoznam svetového dedičstva UNESCO. "
                "Po jeho stenách padajú vodopády a na brehoch sa krčia maličké dedinky a staré farmy.\n\n"
                "Fjord sa zvyčajne spája s výletom Nórsko v kocke — kombináciou vlaku, lode a autobusu. Lode aj "
                "kajaky vyrážajú z dedín Gudvangen a Flåm. Ticho a mohutnosť úzkeho fjordu robia z plavby "
                "nezabudnuteľný zážitok."
            ),
            "long": "",  # TODO
        },
        "legends": [],  # TODO
    },

    # ------------------------------------------------------------
    {
        "id": "flam",
        "name": "Flåm a železnica Flåmsbana",
        "category": "fjordy",
        "coords": (60.8625, 7.1138),
        "emoji": "🚂",
        "info": {
            "Otvorené": "železnica Flåmsbana 1940",
            "Trasa": "Flåm – Myrdal, 20 km, prevýšenie ~865 m",
            "Význam": "Jedna z najstrmších bežných železníc sveta",
            "Vstup": "lístok na vlak platený",
            "Web": "https://www.visitflam.com",
        },
        "texts": {
            "short": (
                "Flåm je dedinka na konci ramena Sognefjordu, odkiaľ vychádza slávna horská železnica Flåmsbana. "
                "Za necelú hodinu vystúpa dvadsaťkilometrovou traťou cez vodopády a tunely o vyše 800 metrov do "
                "horskej stanice Myrdal."
            ),
            "medium": (
                "Flåm je malebná dedinka na konci Aurlandsfjordu, ramena veľkého Sognefjordu, obklopená strmými "
                "horami. Preslávila ju železnica Flåmsbana, ktorá patrí k najstrmším železniciam normálneho rozchodu "
                "na svete.\n\n"
                "Trať dlhá dvadsať kilometrov spája prímorský Flåm s horskou stanicou Myrdal a prekonáva pritom "
                "prevýšenie vyše osemstošesťdesiat metrov. Cesta trvá necelú hodinu a vedie cez dvadsať tunelov, "
                "popri divokých vodopádoch a horských statkoch. Vlak na chvíľu zastaví pri vodopáde Kjosfossen, "
                "kde sa pre cestujúcich odohráva malé predstavenie.\n\n"
                "Flåm je dôležitou zastávkou na populárnej trase Nórsko v kocke a východiskom plavieb po "
                "Nærøyfjorde. V sezóne sem zavítajú aj veľké výletné lode."
            ),
            "long": (
                "Flåm je malebná dedinka na samom konci Aurlandsfjordu, jedného z ramien veľkého Sognefjordu — "
                "najdlhšieho a najhlbšieho fjordu Nórska. Hoci tu žije len niekoľko stoviek ľudí, Flåm patrí k "
                "najnavštevovanejším miestam krajiny. Dôvodom je predovšetkým železnica Flåmsbana.\n\n"
                "Flåmsbana spája prímorský Flåm s horskou stanicou Myrdal na hlavnej trati medzi Oslom a Bergenom. "
                "Na trase dlhej len dvadsať kilometrov prekonáva prevýšenie vyše osemstošesťdesiat metrov, čo z nej "
                "robí jednu z najstrmších železníc normálneho rozchodu na svete, ktorá nepoužíva ozubnicu. Stavba, "
                "ktorá sa začala v 20. rokoch a dokončila v roku 1940, bola obrovským inžinierskym výkonom — väčšina "
                "tunelov sa razila ručne.\n\n"
                "Cesta hore trvá necelú hodinu a je to jedna veľká panoráma. Vlak sa kľukatí cez dvadsať tunelov, "
                "popri zasnežených štítoch, horských statkoch a divokých riekach. Vrcholom je zastávka pri mohutnom "
                "vodopáde Kjosfossen, kde vlak na pár minút zastaví a cestujúci môžu vystúpiť na vyhliadkovú plošinu. "
                "Práve tu sa odohráva známe malé predstavenie — pri vodopáde sa zjaví tanečnica v červenom, "
                "predstavujúca huldru, zvodnú lesnú bytosť z nórskych povestí.\n\n"
                "Flåm je zároveň kľúčovou zastávkou na najpopulárnejšej turistickej trase Nórska, takzvanom Nórsku "
                "v kocke, ktoré kombinuje cestu vlakom z Osla, jazdu Flåmsbanou, plavbu po dramatickom Nærøyfjorde "
                "a autobus cez horské priesmyky. Z Flåmu vyrážajú výletné lode aj kajaky a v dedine je malé "
                "železničné múzeum, ktoré pripomína históriu trate.\n\n"
                "V posledných rokoch sa Flåm potýka s následkami vlastnej popularity — do drobnej dediny v sezóne "
                "pripláva množstvo veľkých výletných lodí a Nórsko hľadá spôsoby, ako turistický nápor a jeho "
                "vplyv na fjordy zvládnuť, vrátane prechodu na bezemisné lode."
            ),
        },
        "legends": [
            {
                "id": "huldra-pri-vodopade",
                "title": "Huldra pri vodopáde Kjosfossen",
                "text": (
                    "Pri zastávke vlaku Flåmsbana pri vodopáde Kjosfossen zažijú cestujúci nečakané divadlo. Spomedzi "
                    "skál a vodnej triešte sa zrazu ozve spev a objaví sa žena v dlhom červenom šate, ktorá tancuje "
                    "na skalách pri padajúcej vode. Je to huldra — bytosť z nórskeho folklóru.\n\n"
                    "Huldra je podľa povestí krásna lesná žena, ktorá láka mužov hlbšie do hôr a lesov. Navonok "
                    "vyzerá ako pôvabné dievča, no má jeden tajný znak, ktorý ju prezradí — kravský chvost ukrytý "
                    "pod sukňou. Ak sa muž do huldry zaľúbi a nasleduje ju, môže navždy zmiznúť v horách.\n\n"
                    "Predstavenie pri Kjosfosse je samozrejme inscenované pre turistov — tanečnica je obvykle "
                    "študentka a hudba znie z reproduktorov. Napriek tomu v hluku vodopádu a horskej scenérii "
                    "pôsobí kúzelne a pripomína, ako hlboko sú bytosti ako huldra, trolovia a škriatkovia "
                    "zakorenené v nórskej predstavivosti."
                ),
            },
        ],
    },

    # ------------------------------------------------------------
    {
        "id": "trolltunga",
        "name": "Trolltunga",
        "category": "fjordy",
        "coords": (60.1242, 6.7400),
        "emoji": "🥾",
        "info": {
            "Výška": "skala ~700 m nad jazerom Ringedalsvatnet",
            "Túra": "~27 km tam a späť, 10–12 h, náročná",
            "Sezóna": "bezpečne približne jún – september",
            "Vstup": "zadarmo (parkovisko platené)",
            "Web": "https://www.visitnorway.com",
        },
        "texts": {
            "short": (
                "Trolltunga, „trolí jazyk\", je tenká skalná rímsa vyčnievajúca vodorovne do priestoru asi 700 "
                "metrov nad jazerom Ringedalsvatnet. Vedie k nej jedna z najnáročnejších a najslávnejších "
                "celodenných túr Nórska."
            ),
            "medium": (
                "Trolltunga, doslova „trolí jazyk\", je úzka skalná rímsa, ktorá vodorovne vyčnieva do prázdna "
                "asi sedemsto metrov nad hladinou jazera Ringedalsvatnet pri mestečku Odda. Svojím tvarom naozaj "
                "pripomína jazyk a stala sa jedným z najfotografovanejších miest Nórska.\n\n"
                "Skala vznikla počas doby ľadovej, keď mráz pozdĺž puklín odlomil okolitý kameň a zanechal tento "
                "tenký výčnelok visiaci nad priepasťou. Postaviť sa na jeho špičku, s ničím okrem vzduchu pod nohami, "
                "je vrcholným zážitkom — a zároveň skúškou nervov.\n\n"
                "Cesta k Trolltunge však nie je prechádzka. Túra meria okolo dvadsaťsedem kilometrov tam aj späť, "
                "prekonáva vyše osemsto metrov prevýšenia a trvá desať až dvanásť hodín. Bezpečne sa dá absolvovať "
                "len v lete; mimo sezóny je trasa pokrytá snehom a nebezpečná."
            ),
            "long": (
                "Trolltunga, doslova „trolí jazyk\", je úzka vodorovná skalná rímsa, ktorá vyčnieva do prázdneho "
                "priestoru asi sedemsto metrov nad hladinou horského jazera Ringedalsvatnet, neďaleko mestečka "
                "Odda v regióne Hardanger. Svojím tvarom skutočne pripomína plochý jazyk a fotografia človeka "
                "stojaceho na jej špičke, s priepasťou pod nohami a horami v pozadí, sa stala jednou z ikon "
                "nórskeho turizmu.\n\n"
                "Skala vznikla počas poslednej doby ľadovej. Voda zamrznutá v puklinách žuly ich postupne "
                "rozširovala, až sa pozdĺž zvislých trhlín odlomili celé bloky a zanechali tento tenký výčnelok "
                "visiaci nad údolím. Je to rovnaký proces, aký vytvoril aj neďaleký Preikestolen.\n\n"
                "Ešte pred niekoľkými desaťročiami Trolltungu poznali len miestni a otužilí turisti. Rozmach "
                "sociálnych sietí z nej však urobil svetový fenomén a počet návštevníkov prudko vzrástol z "
                "niekoľkých stoviek na desaťtisíce ročne. To prinieslo aj problémy — preťažené chodníky, "
                "záchranné akcie nepripravených turistov a tlak na krehkú horskú prírodu.\n\n"
                "Cesta k Trolltunge totiž nie je nenáročná prechádzka, ako sa niektorí mylne nazdávajú. Túra meria "
                "okolo dvadsaťsedem kilometrov tam aj späť, prekonáva vyše osemsto metrov prevýšenia a väčšine ľudí "
                "trvá desať až dvanásť hodín. Vedie vysokohorským terénom, kde sa počasie mení rýchlo a nečakane. "
                "Bezpečne sa dá absolvovať len v letných mesiacoch, zhruba od polovice júna do polovice septembra; "
                "mimo sezóny je trasa pokrytá snehom a ľadom a vyžaduje horské vybavenie a skúsenosti.\n\n"
                "Tým, čo dlhú cestu zvládnu, sa naskytne odmena v podobe jedného z najveľkolepejších pohľadov v "
                "Nórsku. Na špičke skaly sa zvyčajne tvorí rad ľudí čakajúcich na svoju fotografiu. Záchranári aj "
                "miestne úrady opakovane pripomínajú, že túra si vyžaduje dobrú kondíciu, pevnú obuv, dostatok "
                "jedla a vody a sledovanie predpovede počasia — Trolltunga je nádherná, no podceniť ju sa "
                "nevypláca."
            ),
        },
        "legends": [
            {
                "id": "trol-a-slnko",
                "title": "Trol, ktorý nezvládol slnko",
                "text": (
                    "Názov Trolltunga — trolí jazyk — prirodzene priťahuje povesti o troloch, najtypickejších "
                    "bytostiach nórskeho folklóru. Trolovia boli podľa povestí veľkí, silní a nie veľmi múdri "
                    "obri, ktorí obývali hory, jaskyne a lesy. Mali jednu osudovú slabinu — neznášali slnečné "
                    "svetlo. Ak ich zastihol úsvit pod holým nebom, premenili sa na kameň.\n\n"
                    "Podľa jednej z ľudových verzií sa istý trol vysmieval, že slnko mu nemôže ublížiť, a na dôkaz "
                    "vyplazil jazyk smerom k vychádzajúcemu slnku. Lúče ho však v tej chvíli zasiahli a celý "
                    "skamenel — a jeho vyplazený jazyk zostal navždy trčať zo skaly nad jazerom ako kamenná rímsa, "
                    "ktorú dnes voláme Trolltunga.\n\n"
                    "Premena trolov na kameň je v nórskych povestiach mimoriadne obľúbeným motívom. Vysvetľuje "
                    "množstvo bizarných skalných útvarov, balvanov a štítov po celej krajine — pre dávnych ľudí "
                    "boli zrozumiteľným dôkazom, že hory kedysi obývali obri, ktorých prichytil deň."
                ),
            },
        ],
    },

    # ------------------------------------------------------------
    {
        "id": "voringsfossen",
        "name": "Vodopád Vøringsfossen",
        "category": "fjordy",
        "coords": (60.4264, 7.2533),
        "emoji": "💦",
        "info": {
            "Výška": "celkový pád 182 m (voľný pád 145 m)",
            "Poloha": "údolie Måbødalen, Hardangervidda",
            "Význam": "Jeden z najznámejších vodopádov Nórska",
            "Vstup": "zadarmo (vyhliadky, mosty)",
            "Web": "https://www.visitnorway.com",
        },
        "texts": {
            "short": (
                "Vøringsfossen je jeden z najznámejších nórskych vodopádov — voda tu padá celkovo o 182 metrov "
                "do divokého údolia Måbødalen na okraji náhornej plošiny Hardangervidda. Nad ním vedie odvážny "
                "vyhliadkový most."
            ),
            "medium": (
                "Vøringsfossen patrí k najslávnejším a najnavštevovanejším vodopádom Nórska. Voda rieky Bjoreio "
                "tu padá celkovo o stoosemdesiatdva metrov, z toho v jednom voľnom páde asi stoštyridsaťpäť metrov, "
                "do divokej rokliny údolia Måbødalen.\n\n"
                "Vodopád leží na okraji rozľahlej náhornej plošiny Hardangervidda, najväčšej svojho druhu v Európe. "
                "Návštevníci ho môžu obdivovať z viacerých vyhliadok — zhora od historického horského hotela aj "
                "z nového odvážneho oceľového mosta, ktorý sa klenie ponad roklinu.\n\n"
                "Okolie vodopádu prešlo modernou úpravou s vyhliadkovými plošinami a schodiskom, ktoré je súčasťou "
                "nórskeho projektu turistických ciest s pozoruhodnou architektúrou."
            ),
            "long": "",  # TODO
        },
        "legends": [],  # TODO
    },

    # ------------------------------------------------------------
    {
        "id": "trollstigen",
        "name": "Trollstigen (Cesta trolov)",
        "category": "fjordy",
        "coords": (62.4575, 7.6710),
        "emoji": "🛣️",
        "info": {
            "Otvorené": "1936",
            "Sklon": "až 9 %, 11 ostrých serpentín",
            "Sezóna": "obvykle máj/jún – október",
            "Vstup": "zadarmo (cesta a vyhliadka)",
            "Web": "https://www.visitnorway.com",
        },
        "texts": {
            "short": (
                "Trollstigen, „cesta trolov\", je dramatická horská cesta s jedenástimi ostrými serpentínami, "
                "ktorá stúpa po takmer kolmom svahu popri vodopáde Stigfossen. Patrí k najslávnejším cestám Nórska."
            ),
            "medium": (
                "Trollstigen, doslova „rebrík trolov\" alebo „cesta trolov\", je jedna z najznámejších a "
                "najdramatickejších horských ciest Nórska. Po takmer kolmom svahu stúpa jedenástimi ostrými "
                "serpentínami so sklonom až deväť percent a prekonáva pritom veľké prevýšenie.\n\n"
                "Cestu otvorili v roku 1936 po ôsmich rokoch náročnej stavby. Vinie sa popri mohutnom vodopáde "
                "Stigfossen, ktorý padá z výšky vyše dvesto metrov; na niektorých miestach cesta vedie tesne popod jeho prúd.\n\n"
                "Na vrchole čaká moderná vyhliadková plošina, ktorá visí nad údolím a ponúka závratný pohľad na "
                "serpentíny dole. Cesta je kvôli snehu otvorená len v teplejšej časti roka, zhruba od konca jari "
                "do jesene."
            ),
            "long": "",  # TODO
        },
        "legends": [],  # TODO
    },

    # ------------------------------------------------------------
    {
        "id": "briksdal",
        "name": "Ľadovec Briksdalsbreen",
        "category": "fjordy",
        "coords": (61.6650, 6.8870),
        "emoji": "❄️",
        "info": {
            "Časť": "rameno ľadovca Jostedalsbreen",
            "Význam": "Najväčší pevninský ľadovec Európy",
            "Túra": "~3 km od parkoviska k ľadovcovému jazeru",
            "Vstup": "zadarmo (vozíky Troll Car platené)",
            "Web": "https://www.visitnorway.com",
        },
        "texts": {
            "short": (
                "Briksdalsbreen je rameno Jostedalsbreenu, najväčšieho ľadovca kontinentálnej Európy. Splýva z "
                "hôr k malému jazierku s ľadovcovou vodou, ku ktorému vedie príjemná prechádzka popri vodopádoch."
            ),
            "medium": (
                "Briksdalsbreen je jedným z najdostupnejších ramien Jostedalsbreenu — najväčšieho ľadovca "
                "kontinentálnej Európy, ktorý pokrýva náhornú plošinu o rozlohe vyše štyristo štvorcových "
                "kilometrov. Splýva z hôr v zelenom údolí Oldedalen.\n\n"
                "Od parkoviska vedie k ľadovcu príjemná, asi trojkilometrová prechádzka popri hučiacich vodopádoch "
                "a bujnej zeleni až k malému jazierku, ktoré napája tečúca ľadovcová voda. Tých, čo nechcú kráčať, "
                "vyvezú vyššie otvorené vozíky zvané Troll Car.\n\n"
                "Ľadovec je citlivým ukazovateľom zmeny klímy — v posledných desaťročiach výrazne ustúpil a "
                "porovnania starých a nových fotografií ukazujú, ako rýchlo sa mení."
            ),
            "long": "",  # TODO
        },
        "legends": [],  # TODO
    },

]
