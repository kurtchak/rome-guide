"""Obsah pre 10 nových miest — pridanie do data.js.

Každá položka obsahuje: id, name, category, coords, image, emoji, info (vrátane Vstup/Rad/Extra/Web),
texts (short/medium/long) a legends (2-3 položky).
"""

NEW_PLACES = [
    # ============================================================
    {
        "id": "san-giovanni-laterano",
        "name": "Bazilika sv. Jána v Lateráne",
        "category": "rim",
        "coords": (41.8858, 12.5057),
        "emoji": "⛪",
        "info": {
            "Postavené": "okolo 320 (Konštantín), prestavba 17. stor. (Borromini)",
            "Architekt": "Borromini (interiér), Galilei (fasáda)",
            "Štýl": "Ranokresťanský, baroko",
            "Význam": "Katedrála rímskeho biskupa — pápeža",
            "Vstup": "zadarmo",
            "Extra": "Lateránsky palác a Krížová chodba platené (~5 €)",
            "Web": "https://www.vatican.va/various/basiliche/san_giovanni",
        },
        "texts": {
            "short": (
                "Bazilika svätého Jána v Lateráne je oficiálnou katedrálou rímskeho biskupa — teda samotného "
                "pápeža. Hoci ju slávou zatieňuje Bazilika svätého Petra, hierarchicky stojí nad ňou. "
                "Postavil ju cisár Konštantín okolo roku 320 a je najstaršou kresťanskou bazilikou na svete. "
                "Nesie titul „matka a hlava všetkých kostolov mesta a sveta\"."
            ),
            "medium": (
                "Bazilika svätého Jána v Lateráne je oficiálnou katedrálou rímskeho biskupa, teda pápeža. "
                "Hoci ju slávou zatieňuje Bazilika svätého Petra, hierarchicky je najvyššou kresťanskou bazilikou "
                "na svete a nesie titul „matka a hlava všetkých kostolov mesta a sveta\".\n\n"
                "Prvú baziliku dal postaviť cisár Konštantín okolo roku 320, len niekoľko rokov po Milánskom "
                "edikte, ktorým bolo kresťanstvo legalizované. Lateránsky palác bol oficiálnym sídlom pápežov "
                "celých tisíc rokov, kým sa v 14. storočí pápeži presťahovali do Vatikánu.\n\n"
                "Bazilika prešla viacerými prestavbami. Najvýznamnejšou bola baroková obnova interiéru od "
                "Francesca Borrominiho v polovici 17. storočia, monumentálnu fasádu pridal Alessandro Galilei "
                "v roku 1735. Vo vnútri stojí dvanásť obrovských sôch apoštolov a nad hlavným oltárom sa "
                "nachádza vzácny gotický baldachýn s relikviami údajných lebiek svätých Petra a Pavla."
            ),
            "long": (
                "Bazilika svätého Jána v Lateráne je oficiálnou katedrálou rímskeho biskupa — pápeža samotného. "
                "Hoci ju slávou zatieňuje Bazilika svätého Petra, hierarchicky je najvyššou kresťanskou bazilikou "
                "na svete a nesie titul „omnium urbis et orbis ecclesiarum mater et caput\" — matka a hlava "
                "všetkých kostolov mesta a sveta.\n\n"
                "Prvú baziliku dal postaviť cisár Konštantín okolo roku 320, len niekoľko rokov po Milánskom "
                "edikte, ktorým bolo kresťanstvo legalizované v rímskej ríši. Stojí na pozemku, ktorý cisár "
                "získal sobášom s rodom Lateranov a daroval ho biskupovi Ríma. Lateránsky palác sa stal "
                "oficiálnym sídlom pápežov a zostal ním celých tisíc rokov, až kým sa v 14. storočí presťahovali "
                "do Avignonu a po návrate do Vatikánu.\n\n"
                "Bazilika prešla mnohými pohromami a prestavbami. Vandali ju vyplienili v roku 455, dvakrát "
                "ju zničili zemetrasenia a v 14. storočí ju dvakrát vyhorel oheň. Najvýznamnejšou bola "
                "baroková obnova interiéru, ktorú v rokoch 1646 až 1649 viedol Francesco Borromini. "
                "Monumentálnu klasicistickú fasádu s pätnástimi obrovskými sochami pridal Alessandro Galilei "
                "v roku 1735.\n\n"
                "Interiér ohromuje dvanástimi sochami apoštolov vo výklenkoch hlavnej lode, každá vysoká päť "
                "metrov. Nad hlavným oltárom stojí vzácny gotický baldachýn z roku 1369, ktorý obsahuje "
                "relikvie údajných lebiek svätých Petra a Pavla. V apside sú stredoveké mozaiky a v podlahe "
                "kosmatesove mramorové intarzie z 13. storočia.\n\n"
                "Pred bazilikou stojí najvyšší egyptský obelisk v Ríme — vyše 32 metrov vysoký, pôvodne "
                "z chrámu v Karnaku z 15. storočia pred Kristom. Oproti bazilike sa nachádzajú aj Sväté schody "
                "a Lateránsky palác s historickými miestnosťami, kde sa konalo päť ekumenických koncilov."
            ),
        },
        "legends": [
            {
                "id": "papezka-jana",
                "title": "Legenda o pápežke Jane",
                "text": (
                    "Jednou z najtrvalejších cirkevných legiend stredoveku bola povera o pápežke Jane — "
                    "anglickej žene, ktorá sa v 9. storočí vraj prezliekla za muža, vďaka svojej učenosti "
                    "vystúpala v cirkevnej hierarchii a stala sa pápežom Jánom Ôsmym. Jej tajomstvo údajne "
                    "vyšlo najavo, keď počas procesie zo San Giovanni in Laterano cestou ku Kolozeu náhle "
                    "porodila dieťa.\n\n"
                    "Legenda hovorí, že zomrela na mieste, ukameňovaná rozhorčeným davom alebo zomrela pri "
                    "pôrode. Po tejto udalosti vraj cirkev zaviedla pravidlo, že každý nový pápež musí "
                    "sedieť na špeciálnom kresle s otvorom v sedadle, cez ktorý mu jeden z kardinálov "
                    "kontroluje, či je skutočne mužského pohlavia. Tieto kreslá — sedia stercoraria — "
                    "skutočne existujú a sú dnes uložené vo Vatikánskych múzeách.\n\n"
                    "Moderní historici legendu o pápežke Jane považujú za stredovekú fikciu, ktorá vznikla "
                    "v 13. storočí. Sediu stercoraria mali pravdepodobne iné, symbolické využitie. "
                    "Príbeh sa však šíril po Európe celé stáročia a viedol aj k rozsiahlym debatám počas "
                    "reformácie."
                ),
            },
            {
                "id": "svate-relikvie",
                "title": "Hlavy svätých Petra a Pavla",
                "text": (
                    "Nad hlavným oltárom Baziliky svätého Jána v Lateráne sa nachádza vzácny gotický "
                    "baldachýn z roku 1369. V hornej časti baldachýnu sú dva strieborné relikviáre, ktoré "
                    "podľa tradície obsahujú lebky apoštolov svätého Petra a svätého Pavla — dvoch "
                    "zakladateľov rímskej cirkvi.\n\n"
                    "Tieto relikvie sa do Lateránu dostali v stredoveku a sú jedným z najvzácnejších "
                    "pokladov kresťanstva. Pôvodne boli viditeľnejšie a vystavené pútnikom, no v roku "
                    "1799 ich francúzski vojaci napoleonskej armády vykradli a odtrhli z nich strieborné "
                    "ozdoby. Lebky boli neskôr nájdené a vrátené, no dnes sú uložené v relikviári mimo "
                    "dosahu verejnosti.\n\n"
                    "Cirkev nikdy oficiálne nepotvrdila, že relikvie skutočne patria apoštolom — relatívne "
                    "moderné výskumy DNA neboli povolené. Historici však pripúšťajú, že kosti môžu pochádzať "
                    "zo skorých rímskych kresťanov a sú nesporne starobylé. Pre veriacich však zostávajú "
                    "fyzickým prepojením s prvotnou cirkvou."
                ),
            },
        ],
    },
    # ============================================================
    {
        "id": "santa-maria-maggiore",
        "name": "Santa Maria Maggiore",
        "category": "rim",
        "coords": (41.8975, 12.4983),
        "emoji": "⛪",
        "info": {
            "Postavené": "5. storočie (založenie), 13.–18. stor. (úpravy)",
            "Architekt": "Pôvodne nezn., barok Domenico Fontana a iní",
            "Štýl": "Ranokresťanský, románsky, barok",
            "Význam": "Jedna zo 4 patriarchálnych bazilík Ríma",
            "Vstup": "zadarmo",
            "Extra": "archeologické múzeum a loggia ~3 €",
            "Web": "https://www.vatican.va/various/basiliche/sm_maggiore",
        },
        "texts": {
            "short": (
                "Santa Maria Maggiore je jednou zo štyroch hlavných patriarchálnych bazilík Ríma a najväčším "
                "kostolom v meste zasväteným Panne Márii. Jej založenie podľa legendy nariadila samotná "
                "Madona — v auguste roku 358 dala v Ríme nepadnúť snehu a tým označila miesto, kde mal "
                "byť postavený jej chrám. Bazilika sa preto dodnes volá aj Santa Maria ad Nives — Pannu "
                "Mária Snežná."
            ),
            "medium": (
                "Santa Maria Maggiore je najväčší rímsky kostol zasvätený Panne Márii a jedna zo štyroch "
                "patriarchálnych bazilík mesta. Jej založenie sa viaže na slávnu legendu o zázračnom snehu — "
                "v noci na piaty august roku 358 dala podľa tradície samotná Madona padnúť snehu na "
                "Esquilínsky pahorok a tým označila miesto, kde mal byť postavený jej chrám.\n\n"
                "Súčasná bazilika pochádza z 5. storočia, keď ju dal postaviť pápež Sixtus Tretí krátko "
                "po Efezskom koncile, ktorý oficiálne potvrdil titul Márie ako Bohorodičky. V interiéri "
                "zostali zachované unikátne ranokresťanské mozaiky z roku 432 — zobrazujú výjavy zo "
                "Starého zákona a sú jedným z najstarších cyklov svojho druhu na svete.\n\n"
                "Bazilika prešla viacerými prestavbami — v 13. storočí dostala monumentálnu romantickú "
                "kampanielu, najvyššiu v Ríme. Barokovú fasádu pridal v 18. storočí Ferdinando Fuga. "
                "Pred bazilikou stoja stĺp z Maxenciovej baziliky a egyptský obelisk."
            ),
            "long": (
                "Santa Maria Maggiore je najväčší rímsky kostol zasvätený Panne Márii a jedna zo štyroch "
                "patriarchálnych bazilík mesta — spolu s Bazilikou svätého Petra, San Giovanni in Laterano "
                "a San Paolo fuori le Mura. Stojí na vrchole Esquilínskeho pahorka, jedného zo siedmich "
                "kopcov Ríma.\n\n"
                "Jej vznik sa viaže na slávnu legendu o zázračnom snehu. Podľa tradície sa v noci na piaty "
                "august roku 358 zjavila Panna Mária zároveň pápežovi Liberiovi a bohatému rímskemu "
                "patricijovi Jánovi. Obaja dostali rovnakú víziu — Madona ich žiadala, aby na mieste, kde "
                "ráno nájdu sneh, postavili kostol. Napriek augustovým horúčavám pokrývala ráno celý "
                "Esquilín tenká vrstva snehu vo tvare pôdorysu budúcej baziliky. Tento zázrak sa každý "
                "rok pripomína piateho augusta, keď zo stropu baziliky padajú biele lupienky kvetov.\n\n"
                "Súčasnú baziliku dal postaviť pápež Sixtus Tretí v rokoch 432 až 440, krátko po Efezskom "
                "koncile, na ktorom bola Mária oficiálne uznaná za Bohorodičku. V interiéri sa zachovali "
                "unikátne ranokresťanské mozaiky z toho istého obdobia. Tieto mozaiky pokrývajú triumfálny "
                "oblúk a horné okraje hlavnej lode, zobrazujú výjavy zo Starého zákona — Abraháma, "
                "Mojžiša, Józueho — a sú jedným z najstarších a najlepšie zachovaných cyklov svojho druhu "
                "na svete.\n\n"
                "Bazilika prešla mnohými prestavbami. V 13. storočí dostala monumentálnu romantickú "
                "kampanielu, ktorá je s výškou 75 metrov najvyššou zvonicou v Ríme. Apsidu so zlatou "
                "korunovačnou mozaikou Márie pridal v rovnakom storočí umelec Jacopo Torriti.\n\n"
                "Vrcholom barokového obdobia sa stala Sixtínska a Pavlovská kaplnka — bohato zdobené "
                "rodinné kaplnky pápežov Sixta Piateho a Pavla Piateho, plné mramoru, sôch a fresiek. "
                "Hlavnú barokovú fasádu pridal v rokoch 1741 až 1743 Ferdinando Fuga. Pred bazilikou "
                "stojí najvyšší korintský stĺp v Ríme — vysoký 14 metrov, prevezený z Maxenciovej "
                "baziliky na Fóre — a v zadnej časti egyptský obelisk."
            ),
        },
        "legends": [
            {
                "id": "snehovy-zazrak",
                "title": "Snehový zázrak v auguste",
                "text": (
                    "Najslávnejšia rímska legenda o zázračnom snehu sa odohrala v noci na piaty august "
                    "roku 358. Panna Mária sa zjavila súčasne pápežovi Liberiovi a bohatému rímskemu "
                    "patricijovi menom Ján — bezdetnému párovi, ktorý sa modlil o Boží zámer pre svoje "
                    "bohatstvo. Madona obom dala rovnakú víziu — kostol mal byť postavený na mieste, "
                    "kde ráno nájdu sneh.\n\n"
                    "Augustové ráno v Ríme, v meste s priemernou letnou teplotou nad tridsať stupňov, "
                    "by malo byť všetko, len nie zasnežené. Napriek tomu vraj ráno pokrývala celý "
                    "Esquilínsky pahorok jemná vrstva čerstvého snehu vo tvare pôdorysu budúcej baziliky. "
                    "Pápež a patricij sa stretli, porozprávali si svoje vízie a okamžite začali stavať "
                    "kostol. Patricij Ján venoval celý svoj majetok na výstavbu.\n\n"
                    "Tento zázrak sa každý rok pripomína piateho augusta. Počas slávnostnej omše padajú "
                    "zo stropu baziliky tisíce bielych kvetových lupienkov, ktoré symbolizujú zázračný "
                    "sneh. Atrakciu sprevádzajú aj špeciálne svetelné efekty premietané na priečelie "
                    "baziliky. Tradícia sa zachovala viac ako pätnásť storočí a patrí k najstarším "
                    "kontinuálne dodržiavaným náboženským obradom v Európe."
                ),
            },
            {
                "id": "salvator-romanus",
                "title": "Salus Populi Romani — ochrankyňa Rimanov",
                "text": (
                    "V Pavlovskej kaplnke baziliky sa nachádza jedna z najuctievanejších ikon Ríma — "
                    "obraz Panny Márie známy ako Salus Populi Romani, čiže Záchrana rímskeho ľudu. "
                    "Tradícia ho pripisuje samému evanjelistovi Lukášovi, ktorý ju vraj namaľoval "
                    "ešte počas Máriinho života. Moderní historici však datujú obraz do 9. storočia.\n\n"
                    "Bez ohľadu na pôvod sa Salus Populi Romani stala symbolom ochrany Ríma v časoch "
                    "krízy. Pápež Gregor Veľký ju v roku 590 nosil v procesii proti moru a v ten "
                    "istý deň sa nad Anjelským hradom zjavil archanjel Michal — udalosť, ktorá je "
                    "na hrade dodnes pripomínaná. Ikona bola vynesená v procesiách aj počas vojen, "
                    "epidémií a iných katastrof.\n\n"
                    "Ikona má aj modernú ikonickú rolu — pápež František ju veľmi uctieval a pred "
                    "každou zahraničnou cestou sa pri nej prišiel modliť. Aj počas pandémie covidu v "
                    "roku 2020 sa pápež osobitne pomodlil pred ikonou za skončenie pandémie. Dlhé "
                    "obdobie jediná verejne prístupná hodina pre obraz bola počas omše. Dnes je "
                    "viditeľná z hlavnej lode baziliky každý deň."
                ),
            },
        ],
    },
    # ============================================================
    {
        "id": "san-pietro-in-vincoli",
        "name": "San Pietro in Vincoli",
        "category": "rim",
        "coords": (41.8940, 12.4938),
        "emoji": "⛓️",
        "info": {
            "Postavené": "5. storočie",
            "Architekt": "Pôvodne nezn.; Mojžiš od Michelangela (1515)",
            "Štýl": "Ranokresťanský s renesančnými prvkami",
            "Význam": "Okovy sv. Petra a Michelangelov Mojžiš",
            "Vstup": "zadarmo",
            "Extra": "otvorené 8:00–12:30, 15:00–18:00",
        },
        "texts": {
            "short": (
                "San Pietro in Vincoli — Svätý Peter v okovách — je nenápadný kostol na vrchole "
                "Esquilínskeho pahorka, ktorý ukrýva dva svetové poklady. Pod hlavným oltárom sú "
                "uložené reťaze, ktorými bol podľa tradície zviazaný apoštol Peter v rímskom väzení. "
                "V pravej bočnej kaplnke stojí Michelangelova socha Mojžiša — jedno z najsilnejších "
                "diel renesancie."
            ),
            "medium": (
                "San Pietro in Vincoli — Svätý Peter v okovách — je nenápadný kostol na vrchole "
                "Esquilínskeho pahorka, ktorý ukrýva dva svetové poklady. Pod hlavným oltárom v sklenenom "
                "relikviári sú uložené dvojité reťaze — jedna podľa tradície z rímskeho Mamertinského "
                "väzenia, kde bol Peter zviazaný pred svojou popravou, druhá z jeho jeruzalemského väznenia.\n\n"
                "Podľa legendy boli obe reťaze pri spojení v 5. storočí zázračne zviazané k sebe a "
                "nikdy ich nemožno oddeliť. Bazilika bola postavená práve na uchovanie týchto relikvií, "
                "ktoré daroval pápežovi Levovi Veľkému byzantský cisár.\n\n"
                "V pravej bočnej kaplnke sa však nachádza ešte slávnejší poklad — Michelangelova socha "
                "Mojžiša z roku 1515. Bola pôvodne určená pre monumentálnu hrobku pápeža Júlia Druhého, "
                "ktorá mala mať štyridsať sôch, no skončila ako jediný dokončený fragment ambiciózneho "
                "projektu. Mojžiš s rohmi na hlave a držiac dosky desatora patrí medzi Michelangelove "
                "najikonickejšie diela."
            ),
            "long": (
                "San Pietro in Vincoli, čo v latinčine znamená Svätý Peter v okovách, je nenápadný "
                "kostol na vrchole Esquilínskeho pahorka, ktorý ukrýva dva svetové poklady. Pod hlavným "
                "oltárom v sklenenom relikviári sú uložené dvojité reťaze, ktorými bol podľa tradície "
                "zviazaný apoštol Peter — jedna pochádza z rímskeho Mamertinského väzenia, kde bol "
                "Peter zatvorený pred svojou popravou v Nerónovom cirku, a druhá z jeho jeruzalemského "
                "väznenia opísaného v Skutkoch apoštolov.\n\n"
                "Podľa legendy boli obe reťaze pri spojení v 5. storočí zázračne zviazané k sebe a "
                "od tej doby ich nemožno oddeliť. Práve na uchovanie tejto vzácnej relikvie dala "
                "pápežská cisárovná Eudoxia okolo roku 432 postaviť baziliku. Reťaze venoval pápežovi "
                "Levovi Veľkému byzantský cisár Theodosius Druhý.\n\n"
                "V pravej bočnej kaplnke sa nachádza ešte slávnejší poklad — Michelangelova socha "
                "Mojžiša, vytesaná v rokoch 1513 až 1515. Bola pôvodne určená pre monumentálnu hrobku "
                "pápeža Júlia Druhého, ktorá mala mať štyridsať sôch a tvoriť centrum Baziliky svätého "
                "Petra. Pápežove ambície boli také, že Michelangelo na projekte pracoval s prerušeniami "
                "vyše štyridsať rokov. Po smrti Júlia Druhého boli plány postupne zoškrtené, až nakoniec "
                "Mojžiš skončil ako jediný plne dokončený fragment v skromnejšej hrobke v San Pietro "
                "in Vincoli.\n\n"
                "Mojžiš sedí na tróne, drží dve dosky desatora a hľadí akoby s prísnosťou dolu na "
                "Izraelcov, ktorí počas jeho neprítomnosti uctievali zlaté teľa. Z hlavy mu vychádzajú "
                "dva malé rohy — výsledok stredovekého prekladateľského omylu hebrejského slova qaran, "
                "ktoré znamená aj žiariť, aj mať rohy. V Michelangelovej dobe sa rohy považovali za "
                "atribút Mojžiša a tak ich vytesal.\n\n"
                "Mojžiš je univerzálne uznávaný ako jedno z najsilnejších diel renesančného sochárstva. "
                "Sigmund Freud o ňom napísal celú esej, v ktorej skúmal psychologickú dynamiku postavy. "
                "Michelangelo sám vraj po dokončení sochy v hneve udrel kladivom do Mojžišovho kolena "
                "a kričal: prečo nehovoríš?"
            ),
        },
        "legends": [
            {
                "id": "rohy-mojzisa",
                "title": "Prečo má Mojžiš rohy",
                "text": (
                    "Najnápadnejším detailom Michelangelovho Mojžiša sú dva malé rohy vychádzajúce "
                    "z jeho čela. Mnoho návštevníkov je nimi prekvapených — Mojžiš predsa nebol diablom. "
                    "Vysvetlenie je v stredovekom prekladateľskom omyle, ktorý pretrval celé storočia.\n\n"
                    "V Knihe Exodus sa píše, že po stretnutí s Bohom na Sinaji Mojžišova tvár žiarila — "
                    "v hebrejčine sa použilo slovo qaran, ktoré môže znamenať buď „žiariť\", alebo „mať "
                    "rohy\". Svätý Hieronym, ktorý v 4. storočí prekladal Bibliu do latinčiny, zvolil "
                    "druhý význam a do Vulgáty napísal, že Mojžišovi vyrástli rohy. Tento preklad sa "
                    "stal v stredovekej Európe štandardom a kresťanské umenie ho prijalo bez výhrad.\n\n"
                    "V čase Michelangela, na začiatku 16. storočia, bolo zobrazovanie Mojžiša s rohmi "
                    "úplne bežné — žiadny vzdelaný umelec by ho nezobrazil inak. Michelangelo teda "
                    "sledoval ikonografickú konvenciu svojej doby. Až oveľa neskôr, s pokrokom v "
                    "biblickej hebrejčine a novými prekladmi, sa zistilo, že pôvodne išlo o žiarenie "
                    "alebo lúče svetla. Niektoré moderné sochy Mojžiša ho dnes zobrazujú so svätožiarou "
                    "alebo lúčmi, no Michelangelove rohy sú už kultúrnou ikonou."
                ),
            },
            {
                "id": "michelangelov-tragicky-projekt",
                "title": "Tragédia hrobky Júlia Druhého",
                "text": (
                    "Michelangelov Mojžiš mal byť pôvodne len jednou z približne štyridsiatich sôch "
                    "v monumentálnej hrobke pápeža Júlia Druhého. Bola to najambicióznejšia objednávka, "
                    "akú kedy umelec dostal — voľne stojaca trojpodlažná štruktúra v Bazilike svätého "
                    "Petra, plná mramoru, sôch a víťazoslávnych prvkov.\n\n"
                    "Michelangelo strávil leto 1505 v carrarských lomoch, kde osobne vyberal mramor, "
                    "a pripravoval podrobné modely. Krátko po jeho návrate však pápež Július Druhý "
                    "stratil záujem a presmeroval umelca na fresky Sixtínskej kaplnky. Hrobka sa "
                    "postupne zmenšovala, pápež zomrel v roku 1513 a jeho dedičovia tlačili na "
                    "Michelangela, aby projekt dokončil.\n\n"
                    "Nasledovalo štyridsať rokov frustrácie. Michelangelo bol viackrát žalovaný za "
                    "neplnenie zmluvy, predĺžili sa termíny, projekt sa zmenšoval. Z pôvodných "
                    "štyridsiatich sôch zostali nakoniec len tri, ktoré skutočne dokončil sám Michelangelo "
                    "— Mojžiš a dvaja Otroci, ktorí dnes stoja v Louvre. Hrobka pápeža Júlia Druhého "
                    "tak skončila v skromnej bočnej kaplnke San Pietro in Vincoli, namiesto v centre "
                    "Baziliky svätého Petra. Sám Michelangelo o projekte hovoril ako o „tragédii "
                    "svojho života\"."
                ),
            },
        ],
    },
    # ============================================================
    {
        "id": "palatin",
        "name": "Palatín",
        "category": "rim",
        "coords": (41.8894, 12.4878),
        "emoji": "🏛️",
        "info": {
            "Postavené": "8. stor. p. n. l. (osídlenie), 1. stor. n. l. (paláce)",
            "Význam": "Kolíska Ríma, sídlo cisárov",
            "Vstup": "18 € (kombi Koloseum + Fórum, platí 24 h)",
            "Rad": "vstup cez Koloseum alebo Fórum",
            "Web": "https://parcocolosseo.it",
        },
        "texts": {
            "short": (
                "Palatín je jeden zo siedmich pahorkov Ríma a podľa legendy práve tu Romulus v roku "
                "753 pred Kristom založil mesto. Neskôr sa stal najprestížnejšou rezidenčnou štvrťou — "
                "tu si stavali svoje paláce cisári od Augusta po Septimia Severa. Slovo palác samotné "
                "pochádza z mena tohto pahorka."
            ),
            "medium": (
                "Palatín je centrálny zo siedmich pahorkov Ríma a najlegendárnejšie miesto v meste. "
                "Podľa tradície práve tu Romulus 21. apríla roku 753 pred Kristom orbal posvätnú "
                "brázdu, ktorá vyznačila hranice nového mesta. Archeológovia tu skutočne našli stopy "
                "po osídlení z 8. storočia pred Kristom, takže legenda má reálny základ.\n\n"
                "V cisárskej dobe sa Palatín stal najprestížnejšou rezidenčnou štvrťou. Cisár "
                "Augustus tu mal svoj skromný dom, jeho nasledovníci postupne zaberali celý "
                "pahorok monumentálnymi palácmi. Domitianus tu v 1. storočí postavil obrovský "
                "Domus Augustana — oficiálnu cisársku rezidenciu — a Domus Flavia pre verejné "
                "audiencie. Slovo palác (palace, palazzo) v európskych jazykoch pochádza priamo "
                "z mena tohto pahorka.\n\n"
                "Z Palatína je úchvatný výhľad na Rímske fórum dolu a na ruiny Cirkusu Maximus "
                "z opačnej strany. Dnes je archeologický park súčasťou kombinovaného lístka "
                "s Koloseom a Fórom."
            ),
            "long": (
                "Palatín je centrálny zo siedmich pahorkov Ríma a najlegendárnejšie miesto v meste. "
                "Podľa tradície práve tu Romulus 21. apríla roku 753 pred Kristom orbal posvätnú "
                "brázdu, ktorá vyznačila hranice nového mesta — ten istý deň sa dnes oslavuje ako "
                "Natale di Roma, narodeniny Ríma. Archeológovia tu skutočne našli stopy po osídlení "
                "z 8. storočia pred Kristom vrátane základov primitívnych chát zo slámy a hliny.\n\n"
                "V republikánskej dobe sa na Palatíne usádzali bohatí Rimania — Cicero, Marcus "
                "Antonius, Crassus. Stredobodom pahorka bola však Lupercal — posvätná jaskyňa, kde "
                "podľa legendy vlčica nakŕmila Romula a Réma. V roku 2007 archeológovia objavili "
                "pravdepodobnú skutočnú jaskyňu — bohato zdobenú mušľami a mozaikami, ktorú cisár "
                "Augustus označil za miesto Romulovho zázračného vychovania.\n\n"
                "Augustus, prvý cisár, sa narodil neďaleko a po nástupe k moci si na Palatíne kúpil "
                "skromný dom. Jeho dom je zachovaný a sprístupnený verejnosti — interiér zdobia "
                "vzácne nástenné maľby s motívmi vtákov a girland. Augustova manželka Lívia mala "
                "vlastnú vilu so slávnymi maľbami záhrady, ktoré sú dnes vystavené v Palazzo Massimo.\n\n"
                "Po Augustovi prevzal Palatín každý ďalší cisár. Tiberius a Caligula stavali svoje "
                "paláce, ale skutočnú monumentálnu transformáciu uskutočnil Domitianus na konci "
                "1. storočia. Postavil obrovský komplex Domus Augustana — súkromnú rezidenciu — "
                "a Domus Flavia — veľký reprezentačný palác s aulou trónou, kde prijímal poslov a "
                "veľvyslancov. Komplex zaberal niekoľko hektárov a obsahoval súkromný štadión, "
                "kúpele, jedálne s výhľadom a dokonca aj zoo s exotickými zvieratami.\n\n"
                "Slovo palác (palace, palazzo, palast) v európskych jazykoch pochádza priamo z mena "
                "tohto pahorka — po Domitianovej stavbe sa každá veľká cisárska rezidencia začala "
                "nazývať palatium.\n\n"
                "Po páde rímskej ríše Palatín postupne pustol. V stredoveku ho rody Frangipani a "
                "Pierleoni používali ako pevnosť. Renesanční pápeži tu zakladali záhrady — najznámejšia "
                "je Orti Farnesiani, prvá botanická záhrada v Európe. Dnes je celý pahorok archeologickým "
                "parkom s úchvatným výhľadom na Rímske fórum dolu a na ruiny Cirkusu Maximus z opačnej "
                "strany."
            ),
        },
        "legends": [
            {
                "id": "vlcica-romulus",
                "title": "Vlčica, Romulus a Remus",
                "text": (
                    "Najslávnejšia legenda Ríma sa odohrala práve na svahoch Palatínu. Dvojičky "
                    "Romulus a Remus boli synmi vestálky Rhei Silvie a boha Marsa. Keď ich zlovestný "
                    "strýko Amulius dal hodiť do Tibera v košíku, aby sa zbavil legitímnych dedičov "
                    "trónu, košík sa zachytil pri brehu pod Palatínom. Tam ich našla vlčica, ktorá "
                    "ich nakŕmila vlastným mliekom v jaskyni nazvanej Lupercal.\n\n"
                    "Neskôr ich pastier Faustulus s manželkou Acca Larentia vychovali ako vlastné "
                    "deti. Keď bratia vyrástli a zistili svoj kráľovský pôvod, zvrhli Amulia a "
                    "rozhodli sa založiť nové mesto na mieste, kde ich zachránila vlčica. Pri "
                    "vyznačovaní hraníc sa však pohádali — Romulus chcel založiť mesto na Palatíne, "
                    "Remus na neďalekom Aventíne. Po veštbách zvíťazil Romulus a začal orbať brázdu "
                    "okolo Palatínu. Remus ju z posmechu preskočil — Romulus ho v zúrivosti zabil "
                    "slovami: tak zomrie každý, kto preskočí moje hradby.\n\n"
                    "V roku 2007 talianski archeológovia oznámili objav pravdepodobnej Lupercal "
                    "jaskyne pod Palatínom. Pomocou endoskopov našli bohato zdobenú podzemnú "
                    "miestnosť pokrytú mušľami a farebnými mozaikami, presne v mieste, kde ju "
                    "podľa antických prameňov mal cisár Augustus rekonštruovať a používať ako "
                    "posvätné miesto svojho rodového kultu."
                ),
            },
            {
                "id": "augustove-vychodisko",
                "title": "Augustov skromný dom",
                "text": (
                    "Cisár Augustus, prvý a najmocnejší cisár Ríma, mal na Palatíne dom, ktorý je "
                    "dodnes zachovaný a sprístupnený verejnosti. Najprekvapujúcejšie na ňom je, aký "
                    "je skromný. Augustus vedel, že po Caesarovi musí starostlivo budovať imidž "
                    "občianskeho vodcu, nie kráľa, a tak žil v dome, ktorý kúpil od rečníka Hortensia "
                    "— relatívne malom, bez okázalých prvkov.\n\n"
                    "Antický spisovateľ Suetonius opisuje, že Augustus spal vyše štyridsať rokov v "
                    "tej istej spálni s jednoduchým drevenou posteľou bez prepychu. V lete sa "
                    "presúval do trochu chladnejších izieb prepojených s vilou jeho manželky Lívie. "
                    "Domácnosť bola porovnateľná so strednou rímskou patricijovou — nie cisárskou.\n\n"
                    "To, čo dom predsa len vynikol, boli nástenné maľby. Tie sú dnes pozoruhodne "
                    "zachované — jemné iluzionistické scény s vtákmi, kvetinami a architektonickými "
                    "motívmi v štýle, ktorý sa nazýva druhý pompejský štýl. Patria k najlepšie "
                    "zachovaným príkladom rímskej maľby svojho obdobia. Augustova spálňa s názvom "
                    "Studiolo, malá a intímna miestnosť pre čítanie a meditáciu, je obzvlášť cenná. "
                    "Dom bol verejnosti sprístupnený až v roku 2008 po desaťročiach reštaurátorských "
                    "prác."
                ),
            },
        ],
    },
    # ============================================================
    {
        "id": "galeria-borghese",
        "name": "Galéria Borghese",
        "category": "rim",
        "coords": (41.9142, 12.4921),
        "emoji": "🖼️",
        "info": {
            "Postavené": "1612–1633 (vila), zbierka 17. stor.",
            "Architekt": "Flaminio Ponzio, neskôr Antonio Asprucci",
            "Štýl": "Neskorá renesancia, baroko",
            "Význam": "Bernini, Caravaggio, Tizian, Canova",
            "Vstup": "13 € + povinná rezervácia online",
            "Rad": "vstup len v 2-hodinových slotoch",
            "Web": "https://galleriaborghese.beniculturali.it",
        },
        "texts": {
            "short": (
                "Galéria Borghese je jedna z najlepších malých galérií na svete. Stojí v krásnom "
                "parku Villa Borghese a obsahuje nedotknutú zbierku kardinála Scipiona Borghese — "
                "vášnivého mecenáša mladého Berniniho a Caravaggia. Nájdete tu Berniniho mramorové "
                "zázraky Apollo a Dafne, Únos Proserpiny a David, plus šesť obrazov Caravaggia."
            ),
            "medium": (
                "Galéria Borghese je jedna z najlepších malých galérií na svete. Stojí v elegantnej "
                "vile uprostred parku Villa Borghese a uchováva nedotknutú zbierku kardinála Scipiona "
                "Borghese, synovca pápeža Pavla Piateho. Scipione bol v začiatku 17. storočia "
                "najvášnivejším zberateľom umenia v Ríme — niektoré diela získal aj nečestne, "
                "zaberajúc obrazy iných zberateľov.\n\n"
                "Hlavnou atrakciou sú Berniniho ranné mramorové sochy. Apollo a Dafne, Únos "
                "Proserpiny a Dávid boli vytvorené, keď Berninimu bolo len niečo cez dvadsať. "
                "Patria medzi najtechnicky dokonalejšie sochy v dejinách umenia — Bernini dokázal "
                "v mramore zachytiť pohyb, dynamiku a dokonca aj jemnosť kože tlačenej prstami.\n\n"
                "V obrazovej časti sú vystavené hlavné Caravaggiove diela vrátane Madony so "
                "hadom, Mladého Bakchusa a Sv. Hieronyma. Nechýbajú aj Tizian, Rafael a Canovove "
                "klasicistická socha Pauline Borghese ako Venuša."
            ),
            "long": (
                "Galéria Borghese je jedna z najlepších malých galérií na svete. Stojí v elegantnej "
                "neskororenesančnej vile uprostred 80-hektárového parku Villa Borghese a uchováva "
                "nedotknutú zbierku kardinála Scipiona Borghese, synovca pápeža Pavla Piateho, "
                "z začiatku 17. storočia.\n\n"
                "Scipione Borghese bol v začiatku 17. storočia najvášnivejším zberateľom umenia "
                "v Ríme. Mal absolútnu moc — bol synovcom úradujúceho pápeža a kardinálom, čo "
                "mu umožňovalo získavať umelecké diela za cenu, ktorú si určil sám. Niekedy "
                "získal diela aj nečestne — napríklad Caravaggiov obraz Madona so hadom doslova "
                "skonfiškoval iným zberateľom. Práve on objavil mladého Berniniho a stal sa jeho "
                "prvým a hlavným mecenášom.\n\n"
                "Hlavnou atrakciou galérie sú štyri Berniniho ranné mramorové sochy, vytvorené "
                "v rokoch 1620 až 1625, keď mal sochár medzi 21 a 26 rokov. Apollo a Dafne "
                "zachytáva moment premeny nymfy na vavrínový strom — vidíte, ako jej pri "
                "Apollovom dotyku z prstov vyrastajú listy a kôra obklopuje jej telo. Únos "
                "Proserpiny zobrazuje Plutona dvíhajúceho dievča do podsvetia — jeho prsty sa "
                "doslova zarezávajú do mäkkej kože jej stehna, mramor pôsobí ako živé mäso. "
                "Dávid je dynamický autoportrét Berniniho v okamihu, keď napína prak proti "
                "Goliášovi. A Aeneas, Anchises a Askanios zobrazuje útek z horiacej Tróje.\n\n"
                "Tieto sochy patria medzi najtechnicky dokonalejšie diela v dejinách umenia. "
                "Bernini dokázal v mramore zachytiť pohyb, dynamiku, jemnosť tkaniny aj kože — "
                "veci, ktoré boli predtým považované za nemožné v tak tvrdom materiáli.\n\n"
                "V obrazovej časti sú vystavené hlavné Caravaggiove diela vrátane Madony so hadom, "
                "Mladého Bakchusa, Hráča lutny a sv. Hieronyma. Caravaggio bol Scipionov "
                "obľúbený maliar napriek svojej škandalóznej povahe — sám sa skrýval na úteku "
                "po vražde, no Borghesemu posielal obrazy ako pokus o milosť.\n\n"
                "Ďalšie významné diela zahŕňajú Tizianovu Posvätnú a profánnu lásku, Rafaelovo "
                "Snímanie z kríža, Correggiovu Danae a Canovovu klasicistickú sochu Pauline "
                "Bonaparte ako Venuše Víťaznej, vytesanú v roku 1808 pre Camilla Borgheseho, "
                "manžela Napoleonovej sestry. Galéria má prísne pravidlá — vstup je len v "
                "rezervovaných dvojhodinových slotoch a počet návštevníkov je limitovaný, čo "
                "umožňuje pokojné pozorovanie diel."
            ),
        },
        "legends": [
            {
                "id": "bernini-rivalita",
                "title": "Bernini ako Caravaggio sochárstva",
                "text": (
                    "Scipione Borghese mal výnimočný cit pre objavovanie talentu. V roku 1618, "
                    "keď mal Gian Lorenzo Bernini len dvadsať rokov, kardinál mu objednal sériu "
                    "sôch pre svoju vilu. To, čo mladý sochár vytvoril v nasledujúcich siedmich "
                    "rokoch, zmenilo dejiny sochárstva.\n\n"
                    "Apollo a Dafne, dokončené v roku 1625, sú azda najtechnicky úžasnejšie. "
                    "Mramor je v miestach, kde sa mení Dafne na vavrín, vytesaný do hrúbky "
                    "milimetrov — listy a vetvičky sú také tenké, že priesvitné svetlo cez ne "
                    "preniká. Bernini doslova klamal mramor — hovoril, že to nie je kameň, "
                    "ale iba farba na ňom.\n\n"
                    "Pápež Maffeo Barberini, ktorý súše obdivoval, vraj povedal Berninimu: "
                    "máš veľké šťastie, syn môj, vidieť za svojho života pápeža Maffea Barberiniho. "
                    "Ale my máme ešte väčšie šťastie, že kavalier Bernini žije za nášho pontifikátu. "
                    "Tieto sochy boli pre kardinála Scipiona také vzácne, že nikdy nepustil "
                    "diela z vily. Galéria preto dnes zostáva jediným miestom na svete, kde si "
                    "možno mladého Berniniho prezrieť — všetky sa nikdy nepožičiavajú na výstavy."
                ),
            },
            {
                "id": "pauline-borghese",
                "title": "Pauline Bonaparte ako Venuša",
                "text": (
                    "V jednej z miestností galérie sa nachádza nahá mramorová socha mladej ženy "
                    "ležiaca na pohovke ako klasická Venuša. Je to Pauline Bonaparte, sestra "
                    "Napoleona, vytvorená sochárom Antoniom Canovom v roku 1808 pre jej manžela "
                    "kniežaťa Camilla Borgheseho.\n\n"
                    "Pauline bola známa svojou krásou, ale aj škandálnym životným štýlom. "
                    "Súdobí návštevníci sa jej vraj pýtali, ako mohla pózovať nahá pred sochárom. "
                    "Jej legendárna odpoveď znela: „V dielni bola dobre vykurovaná pec.\" "
                    "Iný príbeh hovorí, že jej manžel Camillo bol natoľko vychladol z reality, "
                    "že nahú sochu manželky uchovával zamknutú v miestnosti, do ktorej mal kľúč "
                    "len on sám.\n\n"
                    "Socha má jeden originálny technický prvok — Pauline drží jablko, "
                    "symbol Venuše, a je položená na drevenej pohovke s mramorovým povrchom. "
                    "Pôvodne bola pohovka mechanická a otáčala sa, takže sochu bolo možné "
                    "obdivovať zo všetkých strán pri svetle sviečok. Pauline prežila Napoleonov "
                    "pád, opustila svojho manžela a strávila posledné roky života v Taliansku, "
                    "kde sa preslávila milostnými dobrodružstvami. Zomrela v roku 1825 "
                    "vo Florencii."
                ),
            },
        ],
    },
    # ============================================================
    {
        "id": "kapitolske-muzea",
        "name": "Kapitolské múzeá",
        "category": "rim",
        "coords": (41.8931, 12.4828),
        "emoji": "🏛️",
        "info": {
            "Postavené": "Piazza navrhol Michelangelo (1536), múzeum 1471",
            "Architekt": "Michelangelo (urbanizmus)",
            "Štýl": "Renesancia, antika",
            "Význam": "Najstaršie verejné múzeum sveta",
            "Vstup": "16 €",
            "Web": "https://www.museicapitolini.org",
        },
        "texts": {
            "short": (
                "Kapitolské múzeá sú najstaršie verejné múzeum sveta — boli založené v roku 1471, "
                "keď pápež Sixtus Štvrtý daroval rímskej obci zbierku antických bronzov. Sídlia "
                "v dvoch palácoch na Kapitole, ktorých námestie navrhol Michelangelo. Hlavnými "
                "pokladmi sú originál Kapitolskej vlčice, kolosálne sochy a Marcus Aurelius na koni."
            ),
            "medium": (
                "Kapitolské múzeá sú považované za najstaršie verejné múzeum na svete. Boli "
                "založené v roku 1471, keď pápež Sixtus Štvrtý daroval rímskej obci zbierku "
                "antických bronzových sôch — vrátane slávnej Kapitolskej vlčice. Toto bola "
                "prvá inštitúcia v histórii, kde umelecké diela neboli súkromné, ale prístupné "
                "verejnosti.\n\n"
                "Múzeá sídlia v dvoch palácoch na vrchole Kapitolu — Palazzo dei Conservatori "
                "a Palazzo Nuovo — ktoré boli postavené podľa návrhu Michelangela. Námestie "
                "Piazza del Campidoglio s charakteristickou hviezdicovou dlažbou je jedným z "
                "najkrajších urbanistických celkov renesancie.\n\n"
                "Hlavnými pokladmi zbierky sú originál Kapitolskej vlčice — etruský bronz "
                "z 5. storočia pred Kristom, pod ktorým neskôr boli pridané postavy Romula "
                "a Réma. Na nádvorí stojí kolosálna mramorová hlava Konštantína Veľkého — "
                "fragment sochy, ktorá pôvodne bola vyše 12 metrov vysoká. V centrálnej "
                "miestnosti je originál bronzovej jazdeckej sochy Marca Aurelia, ktorá "
                "bola pôvodne na námestí pred múzeom."
            ),
            "long": (
                "Kapitolské múzeá sú považované za najstaršie verejné múzeum na svete. Boli "
                "založené v roku 1471, keď pápež Sixtus Štvrtý daroval rímskej obci zbierku "
                "antických bronzových sôch ako gesto úcty k mestu. Bola to prvá inštitúcia "
                "v histórii, kde umelecké diela neboli súkromným zberateľským majetkom, ale "
                "prístupné verejnosti — koncept, ktorý sa neskôr stal základom moderného múzejníctva.\n\n"
                "Múzeá sídlia v dvoch palácoch na vrchole Kapitolu — najmenšieho zo siedmich "
                "rímskych pahorkov, no historicky najdôležitejšieho. V antickej dobe tu stál "
                "chrám Jupitera Capitolinusa, najposvätnejšie miesto rímskeho štátu. V stredoveku "
                "bol Kapitol sídlom rímskej mestskej rady.\n\n"
                "V rokoch 1536 až 1546 dostal Michelangelo Buonarroti od pápeža Pavla Tretieho "
                "úlohu kompletne zrekonštruovať Kapitol. Vytvoril majstrovsky komponované "
                "trapézové námestie Piazza del Campidoglio s charakteristickou hviezdicovou "
                "dlažbou v podobe dvanásťcípej hviezdy a navrhol nové fasády palácov. V strede "
                "umiestnil bronzovú jazdeckú sochu cisára Marca Aurelia — jediný zachovaný "
                "antický jazdecký bronz, ktorý prežil len preto, lebo stredovek ho omylom "
                "považoval za sochu kresťanského cisára Konštantína.\n\n"
                "Hlavnými pokladmi zbierky sú: originál Kapitolskej vlčice — etruský bronz z "
                "5. storočia pred Kristom, pod ktorý boli v 15. storočí pridané strieborné "
                "postavy Romula a Réma. Tento symbol Ríma je najznámejším obrazom mesta na svete.\n\n"
                "Na nádvorí Palazzo dei Conservatori sú vystavené fragmenty kolosálnej mramorovej "
                "sochy cisára Konštantína, ktorá pôvodne stála v Maxenciovej bazilike. Hlava "
                "samotná je vyše dvoch metrov vysoká, kompletná socha mala viac ako dvanásť "
                "metrov. Vidieť tiež kolosálnu nohu, ruku a zlomený prst.\n\n"
                "V centrálnej miestnosti je originál bronzovej jazdeckej sochy Marca Aurelia "
                "z 2. storočia. Na námestí pred múzeom dnes stojí presná kópia — originál "
                "musel byť po stáročiach v exteriéri presunutý do chráneného priestoru.\n\n"
                "Ďalšie poklady zahŕňajú Trnového vyťahovača — bronzová socha mladíka "
                "vyťahujúceho si tŕň z chodidla, jeden zo symbolov rímskeho ducha — a obraziu "
                "galériu s dielami Caravaggia, Tiziana a Rubensa. Z múzea je tiež úžasný výhľad "
                "na Rímske fórum, ktoré sa rozprestiera priamo pod ním."
            ),
        },
        "legends": [
            {
                "id": "vlcica-bronz",
                "title": "Kapitolská vlčica — etruský záhad",
                "text": (
                    "Kapitolská vlčica — bronzová socha dvíhajúcej sa vlčice s dvomi malými "
                    "ľudskými postavami pod bruchom — je najznámejším symbolom Ríma. Ale jej "
                    "skutočný pôvod a vek sú dodnes predmetom akademickej debaty.\n\n"
                    "Stáročia sa verilo, že socha pochádza z 5. storočia pred Kristom a je "
                    "etruského pôvodu. Iné teórie tvrdili, že ide priamo o legendárnu sochu "
                    "z 296 pred Kristom, ktorú pri Cicerove čase zasiahol blesk, a ktorá je "
                    "zmienená v starovekých prameňoch. V roku 2007 však reštaurátorka Anna "
                    "Maria Carruba publikovala kontroverznú štúdiu, podľa ktorej je vlčica "
                    "v skutočnosti stredoveká — z 11. alebo 12. storočia po Kristovi.\n\n"
                    "Carruba argumentovala, že technika lievania na jeden kus je typická pre "
                    "stredovek, nie pre antiku, ktorá zvyčajne odlievala sochy v častiach. "
                    "Rádiouhlíkové datovanie v roku 2008 podporilo jej teóriu — datovanie "
                    "ukázalo stredovekú dobu. Ďalšie analýzy sú stále spochybňované.\n\n"
                    "Bez ohľadu na presný vek je vlčica unikátnym symbolom. Postavy Romula "
                    "a Réma boli pridané až v 15. storočí Antoniom Pollaiuolom — predtým "
                    "vlčica stála sama. Stáročia pred kresťanstvom zdobila Lateránsky palác, "
                    "v 15. storočí bola presunutá na Kapitol. Stala sa symbolom rímskej "
                    "republiky aj fašizmu — Mussolini s ňou rád pózoval — a dnes znovu "
                    "demokratického mesta."
                ),
            },
            {
                "id": "michelangelo-piazza",
                "title": "Michelangelovo námestie",
                "text": (
                    "Piazza del Campidoglio, námestie pred Kapitolskými múzeami, je jedným z "
                    "najkrajších urbanistických diel renesancie. Navrhol ho Michelangelo "
                    "Buonarroti v roku 1536 na objednávku pápeža Pavla Tretieho, ktorý chcel "
                    "dôstojne prijať cisára Karola Piateho po jeho víťazstve nad Tunisom.\n\n"
                    "Michelangelo navrhol komplexné trapézové námestie s tromi palácmi. "
                    "Charakteristická dlažba s dvanásťcípou hviezdou v centre nebola pôvodne "
                    "realizovaná za jeho života — pápež Pavol Tretí ju odmietol s tým, že "
                    "vyzerala príliš pohansky. Realizovaná bola až v roku 1940 podľa "
                    "Michelangelovej originálnej kresby.\n\n"
                    "V centre dvanásťcípej hviezdy bola umiestnená bronzová jazdecká socha "
                    "Marca Aurelia. Michelangelo bol pôvodne proti jej presunu — namietal, "
                    "že je príliš krásna a námestie ju zatieni. Pápež však trval na svojom "
                    "a Michelangelo nakoniec celé námestie skomponoval okolo sochy. "
                    "Originálnu sochu dnes nájdete vo vnútri múzea, na námestí stojí "
                    "presná kópia z 1990. Z Michelangelovho námestia vedú dole z Kapitolu "
                    "tri schody — známe ako Cordonata — navrhnuté pre pohodlný výstup nielen "
                    "pre ľudí, ale aj pre kone."
                ),
            },
        ],
    },
    # ============================================================
    {
        "id": "trastevere",
        "name": "Trastevere",
        "category": "rim",
        "coords": (41.8892, 12.4697),
        "emoji": "🏘️",
        "info": {
            "Postavené": "Antika (osídlenie), stredovek (uličky)",
            "Význam": "Najautentickejšia rímska štvrť",
            "Vstup": "zadarmo (verejné priestory)",
            "Extra": "Santa Maria in Trastevere zadarmo",
        },
        "texts": {
            "short": (
                "Trastevere — doslova „Za Tibrom\" — je jednou z najautentickejších štvrtí Ríma. "
                "Úzke dláždené uličky, brečtanové fasády domov a malé piazze s fontánami pripomínajú, "
                "ako mesto vyzeralo v 19. storočí. Centrom je Bazilika Santa Maria in Trastevere — "
                "jeden z najstarších kostolov v Ríme a podľa tradície prvý v meste oficiálne "
                "zasvätený Panne Márii."
            ),
            "medium": (
                "Trastevere — doslova „Za Tibrom\" — je jednou z najautentickejších štvrtí Ríma. "
                "Úzke dláždené uličky, brečtanové fasády domov, malé piazze s fontánami a "
                "zachované remeselnícke obchody pripomínajú, ako mesto vyzeralo v 19. storočí. "
                "V antickej dobe tu žili prevažne prisťahovalci, námorníci a Židia, neskôr to "
                "bola štvrť robotníkov a remeselníkov.\n\n"
                "Centrom Trastevere je Bazilika Santa Maria in Trastevere — jeden z najstarších "
                "kostolov v Ríme a podľa tradície prvý v meste oficiálne zasvätený Panne Márii. "
                "Pôvodný kostol tu stál už v 3. storočí, súčasná stavba pochádza z 12. storočia. "
                "Zlaté byzantské mozaiky v apside patria k najkrajším v Ríme.\n\n"
                "Štvrť je dnes obľúbená pre večerný život — desiatky tradičných tratorií, "
                "vinární a barov sa otvárajú pri západe slnka a piazze sa zaplnia Rimanmi aj "
                "turistami. Cez deň si môžete preskúmať aj farmaceutické múzeum, dom "
                "Rafaelovej milenky La Fornariny alebo vystúpiť na Janikulský pahorok s "
                "panoramatickým výhľadom."
            ),
            "long": (
                "Trastevere — doslova „Za Tibrom\" — je jednou z najautentickejších a "
                "najmilovanejších štvrtí Ríma. Rozprestiera sa na pravom brehu rieky Tiber, "
                "naproti hlavnému historickému centru, a nemá rovnaký turistický nálet ako "
                "Pantheon či Trevi. Práve preto si zachovala atmosféru skutočného rímskeho "
                "života — úzke dláždené uličky pokryté staršími sampietrini kameňmi, "
                "brečtanové fasády pôvodných domov, drobné piazze s mramorovými fontánami "
                "a zachované remeselnícke obchody, ktoré pripomínajú, ako mesto vyzeralo v "
                "19. storočí.\n\n"
                "V antickej dobe tu žili prevažne prisťahovalci — sýrski a egyptskí námorníci, "
                "Židia z palestínskej diaspóry a obchodníci zo všetkých kútov ríše. Tu vznikla "
                "aj najstaršia židovská komunita v Európe, ktorá sa neskôr presunula na "
                "opačný breh. V stredoveku a renesancii bol Trastevere štvrťou robotníkov, "
                "remeselníkov a fishermenov, ktorí pracovali na rieke. Trasteveri — "
                "obyvatelia štvrte — boli povestní svojou hrdosťou a samostatnou identitou. "
                "Hovorili svojou vlastnou verziou rímskeho dialektu a do 20. storočia sa "
                "vraj nechceli ženiť mimo svojej štvrte.\n\n"
                "Centrom Trastevere je Bazilika Santa Maria in Trastevere — jeden z najstarších "
                "kostolov v Ríme a podľa tradície prvý v meste oficiálne zasvätený Panne "
                "Márii. Pôvodný kostol tu stál už v 3. storočí. Súčasná stavba pochádza z "
                "12. storočia, keď ju pápež Inocent Druhý zrekonštruoval. Zlaté byzantské "
                "mozaiky v apside, ktoré zobrazujú Krista s Pannou Máriou na tróne, patria "
                "k najkrajším v Ríme. Pred bazilikou stojí stredoveká fontána — najstaršia "
                "v Ríme v nepretržitom funkčnom stave od 8. storočia.\n\n"
                "Pred bazilikou sa rozprestiera jedna z najživších piaziet v Ríme — Piazza "
                "Santa Maria in Trastevere. Stredobod štvrťového života. V kaviarňach "
                "s vyhliadkou na fontánu sedávajú celé generácie Rimanov.\n\n"
                "Iné zaujímavosti zahŕňajú Villa Farnesina — renesančnú vilu vyzdobenú "
                "freskami Rafaela, San Pietro in Montorio s Bramanteho Tempiettom — malou "
                "kruhovou kaplnkou, ktorá ovplyvnila celú západnú architektúru, a dom "
                "Margherity Lutiovej, slávnej La Fornariny, milenky Rafaela. Janikulský "
                "pahorok hneď nad štvrťou ponúka jeden z najkrajších výhľadov na celý Rím.\n\n"
                "Trastevere je dnes známy najmä večerným životom. Desiatky tradičných "
                "tratorií, vinární a barov sa otvárajú pri západe slnka a piazze sa zaplnia "
                "Rimanmi aj turistami. Štvrť slávi vlastný letný festival — Festa de Noantri "
                "v júli — počas ktorého ulice zaplnia stánky, dĺžkové stoly a procesia "
                "sochy Panny Márie."
            ),
        },
        "legends": [
            {
                "id": "olejovy-zazrak",
                "title": "Zázrak olivového oleja",
                "text": (
                    "Podľa starobylej tradície vzniklo miesto, kde dnes stojí Bazilika "
                    "Santa Maria in Trastevere, vďaka zázraku olivového oleja. V roku 38 "
                    "pred Kristom — viac ako tri desaťročia pred narodením Krista — vraj "
                    "z tejto pôdy vyhŕkol prameň čistého olivového oleja. Olej tiekol "
                    "celý deň a noc.\n\n"
                    "Antický spisovateľ Eusebius zapísal túto udalosť ako predznamenanie "
                    "príchodu Krista — Mesiáša, čo doslova znamená Pomazaný. Olej bol v "
                    "antike symbolom posvätenia kráľov a kňazov. Kresťania neskôr toto "
                    "miesto považovali za prorocké označenie príchodu kresťanstva do Ríma.\n\n"
                    "V 3. storočí tu pápež Kalixt založil prvú modlitebňu — pravdepodobne "
                    "v dome svojho otca. Bola to jedna z prvých kresťanských stavieb v "
                    "Ríme, vybudovaná ešte v dobe prenasledovania. V 4. storočí ju pápež "
                    "Július Prvý prestaval na riadnu baziliku. Súčasná stavba s nádhernou "
                    "románskou kampanielou pochádza z polovice 12. storočia, keď ju "
                    "pápež Inocent Druhý kompletne obnovil. Vo vnútri sa vraj na podlahe "
                    "dodnes nachádza miesto, kde olej v zázračný deň vyhŕkol — označené "
                    "kruhovou platňou s nápisom „Fons Olei\" — Prameň oleja."
                ),
            },
            {
                "id": "fornarina",
                "title": "Fornarina — Rafaelova milenka",
                "text": (
                    "V Trastevere stojí nenápadný dom na ulici Via di Santa Dorotea, ktorý "
                    "podľa tradície patril Margherita Luti — krásnej dcére pekára, známej "
                    "ako La Fornarina. Rafael Santi, najslávnejší maliar svojej doby, sa "
                    "do nej vášnivo zamiloval a ich pomer trval až do jeho predčasnej smrti "
                    "v roku 1520.\n\n"
                    "Margherita bola veľmi pravdepodobne modelom pre niekoľko Rafaelových "
                    "obrazov, vrátane slávnej Sixtínskej Madony a polovičatého aktu La "
                    "Fornarina, ktorý je dnes vystavený v Palazzo Barberini. Na obraze "
                    "má na ramene náramok s nápisom „Raphael Urbinas\" — podpis maliara.\n\n"
                    "Podľa biografie Giorgia Vasariho mala Margherita s Rafaelovou smrťou "
                    "veľmi do činenia. Vasari opisuje, že v noc pred Veľkým piatkom roku "
                    "1520 — dva dni pred svojimi tridsiatymi siedmymi narodeninami — "
                    "Rafael strávil nadmieru vášnivú noc s Fornarinou. Keď ráno prišiel "
                    "domov vyčerpaný a horel, lekári ho mylne diagnostikovali a pustením "
                    "žilou ho vlastne zabili.\n\n"
                    "Po Rafaelovej smrti vraj Margherita vstúpila do kláštora svätej "
                    "Apolónie. Záznamy z kláštora skutočne hovoria o vdove menom Margherita "
                    "Luti, ktorá v ňom strávila zvyšok života. Zomrela v roku 1521, len "
                    "rok po svojom slávnom milencovi. Jej dom v Trastevere je dnes "
                    "súkromnou rezidenciou s pamätnou tabuľkou."
                ),
            },
        ],
    },
    # ============================================================
    {
        "id": "cirkus-maximus",
        "name": "Cirkus Maximus",
        "category": "rim",
        "coords": (41.8864, 12.4852),
        "emoji": "🐎",
        "info": {
            "Postavené": "6. stor. p. n. l. (drevený), kameň 1. stor. n. l.",
            "Význam": "Najväčší rímsky štadión, 250 000 divákov",
            "Vstup": "zadarmo (otvorený park)",
            "Extra": "audio sprievodca v App ~5 €",
            "Web": "https://parcocolosseo.it",
        },
        "texts": {
            "short": (
                "Cirkus Maximus bol najväčší športový štadión antického sveta — pojme až "
                "250 tisíc divákov, čo je viac, než dnešné najväčšie futbalové štadióny. "
                "Konali sa tu legendárne preteky kočov, ktoré boli obľúbenejšie než "
                "gladiátorské zápasy v Koloseu. Dnes je to obrovský zelený park v tvare "
                "podlhovastého oválu, kde sa konajú veľké koncerty."
            ),
            "medium": (
                "Cirkus Maximus bol najväčší športový štadión antického sveta. S dĺžkou 621 "
                "metrov a šírkou 118 metrov pojme až 250 tisíc divákov — viac než dnešné "
                "najväčšie futbalové štadióny. Konali sa tu legendárne preteky kočov, "
                "ktoré boli pre Rimanov obľúbenejšie než gladiátorské zápasy v Koloseu.\n\n"
                "Pôvodný drevený štadión postavil etruský kráľ Tarquinius Priscus už v 6. "
                "storočí pred Kristom. Postupne sa rozširoval, kameňom ho oblicoval Augustus "
                "a definitívnu monumentálnu podobu mu dal cisár Trajanus po roku 100 nášho "
                "letopočtu. Pretekalo sa po dráhe okolo centrálneho hrebeňa zvaného spina, "
                "v strede ktorého stáli dva egyptské obelisky — jeden z nich dnes stojí na "
                "Piazza del Popolo.\n\n"
                "Vodiči kočov, takzvaní aurigae, boli najslávnejšími hviezdami antického "
                "Ríma — ako moderní futbalisti. Najznámejší z nich, Diocles z Lusitanie, "
                "zarobil za svoju kariéru ekvivalent niekoľkých miliárd dolárov v dnešných "
                "peniazoch. Dnes je Cirkus Maximus obrovský zelený park v tvare podlhovastého "
                "oválu, kde sa občas konajú veľké koncerty a kultúrne podujatia."
            ),
            "long": (
                "Cirkus Maximus bol najväčší športový štadión antického sveta a srdce "
                "rímskej zábavy po vyše tisíc rokov. S dĺžkou 621 metrov a šírkou 118 "
                "metrov pojme až 250 tisíc divákov — približne štvrtinu obyvateľstva "
                "antického Ríma a viac než najväčšie moderné futbalové štadióny. Pre "
                "porovnanie, Wembley v Londýne má kapacitu 90 tisíc.\n\n"
                "Pôvodný drevený štadión postavil etruský kráľ Tarquinius Priscus už v 6. "
                "storočí pred Kristom v prirodzenej priehlbine medzi pahorkami Palatín a "
                "Aventín. Postupne sa rozširoval — Caesar pridal kamenné tribúny, Augustus "
                "ho oblicoval mramorom a postavil cisársku lóžu na svahu Palatína. "
                "Definitívnu monumentálnu podobu mu dal cisár Trajanus po roku 100 nášho "
                "letopočtu — vtedy to bola monumentálna trojposchodová stavba s mramorovými "
                "tribúnami, sochami a portikami.\n\n"
                "Pretekalo sa po dráhe okolo centrálneho hrebeňa zvaného spina — dlhého "
                "barierového múru, ktorý rozdelil arénu na dve dráhy. V strede spiny stáli "
                "dva egyptské obelisky — jeden, ktorý priviezol Augustus, dnes stojí na "
                "Piazza del Popolo, druhý, ktorý priviezol Konštantínius Druhý, je dnes "
                "v Lateráne.\n\n"
                "V typický deň pretekov sa konalo dvadsaťštyri pretekov — každý pozostával "
                "zo siedmich okruhov okolo spiny, čo je celkovo asi 5 kilometrov. Vodiči "
                "kočov, takzvaní aurigae, boli najslávnejšími hviezdami antického Ríma — "
                "ako moderní futbalisti. Súťažili pre štyri profesionálne stajne, "
                "rozlíšené farbami: modrá, zelená, červená a biela. Fanúšikovia patrili "
                "k jednému z týchto klubov a rivalita bola tvrdá — niekedy končiac aj "
                "pouličnými bitkami.\n\n"
                "Najznámejším pretekárom v dejinách bol Diocles z Lusitanie. Počas svojej "
                "kariéry, ktorá trvala 24 rokov, vyhral 1462 pretekov a zarobil "
                "ekvivalent niekoľkých miliárd dolárov v dnešných peniazoch — bol "
                "najlepšie zarábajúcim športovcom v dejinách až do moderných čias.\n\n"
                "Cirkus Maximus fungoval kontinuálne až do roku 549 nášho letopočtu, keď "
                "Totila, kráľ Ostrogótov, usporiadal posledné preteky. Po páde ríše "
                "stavby postupne rozobrali na materiál pre kostoly a paláce. Dnes je "
                "Cirkus Maximus obrovský zelený park v tvare podlhovastého oválu — "
                "verejne prístupný, slúži pre cvičenie, behanie a občasné veľké koncerty. "
                "Vystúpili tu Madonna, Rolling Stones a Bruce Springsteen pred státisícmi "
                "divákov — symbolicky obnovujúc cirkusovú tradíciu po pätnástich storočiach."
            ),
        },
        "legends": [
            {
                "id": "diocles-superstar",
                "title": "Diocles — najlepšie zarábajúci športovec dejín",
                "text": (
                    "Gaius Apuleius Diocles bol vodičom kočov v Cirkuse Maximus, ktorý zarobil "
                    "počas svojej dvadsaťštyriročnej kariéry sumu, akú by súčasní športovci "
                    "len ťažko prekonali. Jeho celkový zárobok 35 863 120 sesterciov bol "
                    "v jeho dobe taký obrovský, že na jeho hrobový nápis bolo treba presné "
                    "číslo zaznamenať.\n\n"
                    "V prepočte na moderné peniaze (zohľadňujúc kúpnu silu zlata a obilia) "
                    "ide o ekvivalent okolo 15 miliárd dolárov — viac, než zarobili Tiger "
                    "Woods, Michael Jordan a Lionel Messi spolu počas svojich kariér. "
                    "Diocles bol skutočne najlepšie zarábajúcim športovcom v zaznamenanej "
                    "histórii.\n\n"
                    "Pochádzal z Lusitanie — dnešného Portugalska — a do Ríma prišiel ako "
                    "mladík. Začínal v stajni Bielych, neskôr prešiel k Zeleným, a väčšinu "
                    "svojej kariéry strávil u Červených. Vyhral celkom 1462 pretekov, čo "
                    "tiež bol rekord. Jeho hrobový nápis ho oslavuje ako „šampióna všetkých "
                    "vodičov kočov\" a presne uvádza, koľkokrát štartoval z prvej dráhy, "
                    "koľko závodov začal a koľko nakoniec vyhral.\n\n"
                    "Vodiči kočov boli zvyčajne otroci alebo prepustenci, ktorí sa cez "
                    "víťazstvá prepracovali k bohatstvu a slobode. Mali fanúšikov, "
                    "obdivovateľky, sponzorské zmluvy s manufaktúrami konských ozdôb "
                    "a vlastné vozy ozdobené drahokamami. Diocles odišiel do dôchodku "
                    "v 42 rokoch — neslýchaný vek pre vodiča kočov, väčšina z nich "
                    "umierala mladí pri haváriách. Žil pokojne v Ríme až do staroby."
                ),
            },
        ],
    },
    # ============================================================
    {
        "id": "svata-schody",
        "name": "Svätá schody (Scala Santa)",
        "category": "rim",
        "coords": (41.8870, 12.5064),
        "emoji": "🙏",
        "info": {
            "Postavené": "Pôvodne v Jeruzaleme, do Ríma 326",
            "Význam": "Schody z paláca Pontia Piláta",
            "Vstup": "zadarmo",
            "Extra": "Sancta Sanctorum 3,5 €",
            "Web": "https://www.scala-santa.com",
        },
        "texts": {
            "short": (
                "Svätá schody — Scala Santa — sú podľa tradície dvadsaťosem mramorových "
                "schodov, po ktorých Ježiš kráčal pred Pontiom Pilátom v Jeruzaleme. Do "
                "Ríma ich vraj v roku 326 priniesla cisárovná Helena, matka Konštantína "
                "Veľkého. Pútnici po nich tradične postupujú výhradne po kolenách — je "
                "to jedna z najuctievanejších relikvií kresťanstva."
            ),
            "medium": (
                "Svätá schody — Scala Santa — sú podľa tradície dvadsaťosem mramorových "
                "schodov, po ktorých Ježiš kráčal pred Pontiom Pilátom v Jeruzaleme tesne "
                "pred svojou popravou. Do Ríma ich vraj v roku 326 priniesla cisárovná "
                "Helena, matka Konštantína Veľkého, ako súčasť svojho legendárneho hľadania "
                "kresťanských relikvií v Svätej zemi.\n\n"
                "Schody pôvodne stáli v Lateránskom paláci — vtedajšom sídle pápežov. V "
                "16. storočí ich pápež Sixtus Piaty preniesol do dnešnej kaplnky oproti "
                "Bazilike svätého Jána v Lateráne, kde stoja dodnes. Pútnici po nich "
                "tradične postupujú výhradne po kolenách — je to jedna z najintenzívnejších "
                "duchovných praxí v kresťanstve.\n\n"
                "Mramor je v stopách kolien po stáročiach pútí značne ošúchaný — schody "
                "sú dnes pokryté drevenými doskami, ktoré chránia originál. Na vrchu schodov "
                "sa nachádza Sancta Sanctorum — súkromná pápežská kaplnka, jedna z "
                "najstarších v Ríme. V nej je uložená vzácna relikvia — obraz Krista, "
                "ktorý vraj namaľoval samotný Lukáš a anjel."
            ),
            "long": (
                "Svätá schody — Scala Santa, latinsky Scala Pilati — sú podľa tradície "
                "dvadsaťosem mramorových schodov, po ktorých Ježiš kráčal pred Pontiom "
                "Pilátom v Jeruzaleme tesne pred svojou popravou. Do Ríma ich vraj v "
                "roku 326 priniesla cisárovná Helena, matka Konštantína Veľkého, ako "
                "súčasť svojho legendárneho hľadania kresťanských relikvií vo Svätej "
                "zemi. Helena vtedy mala vyše osemdesiat rokov a podľa tradície práve "
                "ona objavila aj Pravý kríž a hroby v Svätej zemi.\n\n"
                "Schody pôvodne stáli v Lateránskom paláci, vtedajšom oficiálnom sídle "
                "pápežov. Po stáročia po nich pútnici postupovali po kolenách — verilo "
                "sa, že kto absolvuje celú výstup po kolenách so zbožnými modlitbami, "
                "získa odpustky a duchovnú milosť. Pravidlá boli prísne — na schodoch "
                "sa nesmie hovoriť, nesmie sa po nich kráčať a každý stupeň treba "
                "pomodliť.\n\n"
                "V 16. storočí pápež Sixtus Piaty zrekonštruoval Lateránsky komplex a "
                "v rámci toho dal Sväté schody preniesť do dnešnej kaplnky oproti "
                "Bazilike svätého Jána. Pri prenose pracovali pracovníci po kolenách — "
                "nikto sa nesmel po posvätnom mramore prejsť normálne.\n\n"
                "Mramor je v stopách kolien po stáročiach pútí značne ošúchaný — "
                "schody sú dnes pokryté drevenými doskami, ktoré chránia originál. "
                "Tieto dosky majú malé okienka v kľúčových miestach, kde sú viditeľné "
                "miesta, ktoré tradícia spája s kvapkami Kristovej krvi. Pútnici sa "
                "ich snažia bozkávať alebo dotýkať počas výstupu.\n\n"
                "V roku 2019 boli schody po prvý raz po tristopäťdesiatich rokoch "
                "odkryté — drevené dosky odstránili kvôli reštaurátorským prácam. "
                "Niekoľko mesiacov mohli pútnici po kolenách postupovať priamo po "
                "originálnom mramore — historický moment, ktorý sa pravdepodobne "
                "už nezopakuje.\n\n"
                "Na vrchu schodov sa nachádza Sancta Sanctorum — „Svätá svätých\" — "
                "súkromná pápežská kaplnka a jedna z najstarších v Ríme. V nej je "
                "uložená vzácna ikona Krista zvaná Acheiropoieta, čo doslova znamená "
                "„nie urobená rukou\". Tradícia hovorí, že ju načal evanjelista Lukáš "
                "a dokončil ju anjel počas Lukášovho spánku. Ikona bola stáročia "
                "skrytá pred verejnosťou, dnes je viditeľná za sklom.\n\n"
                "Iné schody v komplexe sú normálne — pútnici po nich môžu zostupovať "
                "alebo vystupovať, ak si neželajú duchovnú prax po kolenách. Sväté "
                "schody sú symbolom najpokornejšej formy zbožnosti — po nich "
                "vystupovali aj Martin Luther v roku 1510 a John Henry Newman v 19. "
                "storočí."
            ),
        },
        "legends": [
            {
                "id": "luther-na-schodoch",
                "title": "Martin Luther a kríza viery",
                "text": (
                    "V roku 1510, dvanásť rokov pred tým, ako začal reformáciu, prišiel "
                    "do Ríma mladý nemecký mních Martin Luther. Bol súčasťou augustiánskej "
                    "delegácie a využil pobyt na pútnické skutky. Jedným z hlavných cieľov "
                    "boli práve Sväté schody.\n\n"
                    "Luther po nich začal vystupovať po kolenách s modlitbami, podľa "
                    "tradície. Veril, že tým získava odpustky za hriechy svojho mŕtveho "
                    "otca. V polovici výstupu, podľa neho samotného, ho však zasiahla "
                    "zrazu krízová myšlienka. Spomenul si na slová apoštola Pavla z Listu "
                    "Rimanom: „Spravodlivý bude žiť z viery.\"\n\n"
                    "V tom okamihu sa Luther vraj pozrel na schody, na pútnikov okolo "
                    "seba a uvedomil si, že žiadne fyzické skutky nemôžu nahradiť vieru. "
                    "Nedokončil výstup. Zostúpil dolu a vrátil sa do Nemecka so "
                    "semiankou pochybnosti, ktorá o desať rokov neskôr explodovala "
                    "v reformácii a rozdelila kresťanský svet.\n\n"
                    "Tento príbeh poznáme z Lutherovej vlastnej spomienky a z biografie "
                    "jeho syna. Niektorí historici ho považujú za dramatickú legendu, "
                    "iní za skutočný moment teologického prebudenia. Bez ohľadu na "
                    "presnosť detailov je ironické, že práve na Svätých schodoch — "
                    "symbole katolíckej zbožnosti — sa zrodila myšlienka, ktorá rozdelila "
                    "cirkev. Dnes na schodoch často vystupujú aj protestantskí turisti, "
                    "ktorí sa zastavujú pri miestach, kde podľa tradície stál Luther."
                ),
            },
        ],
    },
    # ============================================================
    {
        "id": "piazza-del-popolo",
        "name": "Piazza del Popolo",
        "category": "rim",
        "coords": (41.9108, 12.4765),
        "emoji": "⛲",
        "info": {
            "Postavené": "16.–19. stor. (postupne)",
            "Architekt": "Giuseppe Valadier (súčasná podoba 1811–1822)",
            "Štýl": "Neoklasicizmus, baroko",
            "Význam": "Severná brána do Ríma, symbol mesta",
            "Vstup": "zadarmo",
            "Extra": "Santa Maria del Popolo zadarmo (Caravaggio)",
        },
        "texts": {
            "short": (
                "Piazza del Popolo je jedno z najmonumentálnejších námestí Ríma — bránou, "
                "cez ktorú do mesta tradične vstupovali pútnici a panovníci zo severu. "
                "V strede stojí 24-metrový egyptský obelisk z 13. storočia pred Kristom, "
                "okolo neho dva takzvané dvojičkové kostoly. V Bazilike Santa Maria del "
                "Popolo sú dva z najlepších Caravaggiových obrazov."
            ),
            "medium": (
                "Piazza del Popolo je jedno z najmonumentálnejších námestí Ríma — bránou, "
                "cez ktorú do mesta tradične vstupovali pútnici a panovníci zo severu. "
                "Mestská brána Porta del Popolo viedla na slávnu rímsku cestu Via Flaminia, "
                "ktorá spájala Rím s severnou Európou. Prvý dojem každého návštevníka "
                "Ríma býval tento — vstup cez monumentálnu bránu na obrovské námestie.\n\n"
                "Súčasnú elegantnú neoklasicistickú podobu dostalo námestie v rokoch 1811 "
                "až 1822 podľa návrhu architekta Giuseppe Valadiera. Stred námestia "
                "dominuje 24-metrový egyptský obelisk Flamínius, ktorý dal do Ríma "
                "priniesť Augustus v roku 10 pred Kristom. Pôvodne stál v Cirkuse "
                "Maximus.\n\n"
                "Námestie obklopujú tri kostoly. Dva z nich — Santa Maria dei Miracoli "
                "a Santa Maria in Montesanto — sú takzvané „dvojičkové kostoly\" "
                "vybudované Berniniho žiakom Carlom Rainaldim v 17. storočí. Vyzerajú "
                "identicky, no v skutočnosti majú rôzne pôdorysy. Tretí kostol — "
                "Santa Maria del Popolo — ukrýva dva z najlepších Caravaggiových obrazov: "
                "Konverzia svätého Pavla a Ukrižovanie svätého Petra."
            ),
            "long": (
                "Piazza del Popolo je jedno z najmonumentálnejších námestí Ríma — bránou, "
                "cez ktorú do mesta tradične vstupovali pútnici a panovníci zo severu. "
                "Mestská brána Porta del Popolo viedla na slávnu rímsku cestu Via "
                "Flaminia, ktorá spájala Rím s severnou Európou. Prvý dojem každého "
                "návštevníka Ríma býval tento — vstup cez monumentálnu bránu na obrovské "
                "námestie. V minulosti tu stáli aj popraviská — verejné popravy sa konali "
                "až do polovice 19. storočia.\n\n"
                "Súčasnú elegantnú neoklasicistickú podobu dostalo námestie v rokoch "
                "1811 až 1822 podľa návrhu pápežského architekta Giuseppe Valadiera, "
                "ktorý bol v tej dobe najvplyvnejším urbanistom Ríma. Pred jeho úpravou "
                "bolo námestie skôr trapézové a zanedbané. Valadier vytvoril dokonalý "
                "ovál ohraničený polkruhovými stenami so sochami štyroch ročných období "
                "a fontánami v tvare leví, plus rampu, ktorá vedie hore na pahorok "
                "Pincio s jedným z najkrajších výhľadov na Rím.\n\n"
                "Stred námestia dominuje 24-metrový egyptský obelisk Flamínius — jeden "
                "z najstarších v Ríme. Pôvodne stál v Heliopolise už okolo roku 1300 "
                "pred Kristom, do Ríma ho dal priniesť Augustus v roku 10 pred Kristom "
                "ako trofej z anekcie Egypta. Pôvodne stál v Cirkuse Maximus, kde ho "
                "možno videli ešte aj kresťanskí mučeníci. V roku 1589 ho pápež Sixtus "
                "Piaty dal presunúť na dnešné miesto.\n\n"
                "Námestie obklopujú tri kostoly. Dva z nich — Santa Maria dei Miracoli "
                "a Santa Maria in Montesanto — sú takzvané „dvojičkové kostoly\" "
                "vybudované Berniniho žiakom Carlom Rainaldim v 17. storočí. Vyzerajú "
                "na prvý pohľad identicky — vytvárajú symetrický rám pre Via del Corso, "
                "hlavnú rímsku triedu vedúcu z námestia. V skutočnosti však majú "
                "rôzne pôdorysy: Santa Maria dei Miracoli (vpravo) má kruhový pôdorys, "
                "Santa Maria in Montesanto (vľavo) je oválny. Aby vyzerali rovnako, "
                "Rainaldi pridal Santa Maria in Montesanto eliptickú kupolu, ktorá sa "
                "z čelného pohľadu javí ako kruhová.\n\n"
                "Tretí a najstarší kostol — Santa Maria del Popolo — stojí v severnom "
                "rohu pri samotnej bráne. Bol postavený v 11. storočí na mieste, kde "
                "podľa legendy stálo prekliate strom rastúci nad hrobom cisára Nerona. "
                "Pápež Paschal Druhý ho vraj na pokyn Panny Márie zoťal a hrob exhumoval, "
                "aby sa Rím zbavil zlej energie. Súčasná stavba je z 15. storočia s "
                "barokovou obnovou Berniniho.\n\n"
                "V Cerasiho kaplnke Santa Maria del Popolo sa nachádzajú dva z najlepších "
                "Caravaggiových obrazov — Konverzia svätého Pavla a Ukrižovanie svätého "
                "Petra. Oba boli vytvorené v rokoch 1600 až 1601 a sú stále na svojom "
                "originálnom mieste. Ide o dramatické scény s revolučným využitím svetla "
                "a tieňa, ktoré definovali maniérizmus a inšpirovali celú barokovú "
                "maľbu. V tej istej kaplnke sú aj diela Caravaggiovho večného rivala "
                "Annibale Carracciho. Vstup do kostola je zadarmo — ide o jednu z "
                "najlepších návštevných hodnôt v Ríme."
            ),
        },
        "legends": [
            {
                "id": "neronovo-prekliatie",
                "title": "Nerov hrob a prekliaty orech",
                "text": (
                    "V mieste, kde dnes stojí Bazilika Santa Maria del Popolo, mal byť "
                    "v staroveku pochovaný cisár Nero — najnenávidenejší rímsky cisár, "
                    "známy podpaľačmi Ríma a prenasledovaním kresťanov. Po jeho samovražde "
                    "v roku 68 nášho letopočtu jeho ostatky tajne pochovala bývalá milenka "
                    "Acte v rodinnej hrobke Domiciovcov pri Via Flaminia.\n\n"
                    "V stredoveku vraj nad hrobom vyrástol mohutný orech a v jeho "
                    "konároch sídlilo množstvo havranov a vrán. Rimania verili, že tieto "
                    "vtáky sú stelesnenia Nerovho ducha a démonov, ktorí ho sprevádzali. "
                    "Strom bol vraj prekliaty a celá oblasť sa stala neobývateľnou — "
                    "ľudia sa tam báli prejsť po zotmení.\n\n"
                    "Podľa legendy z roku 1099 sa pápežovi Paschalovi Druhému zjavila "
                    "Panna Mária. Žiadala ho, aby strom zoťal, hrob exhumoval, "
                    "Nerove ostatky hodil do Tibera a na mieste postavil kostol. Pápež "
                    "ju poslúchol — stromu sa chopil osobne sekerou, hrob otvoril a "
                    "kosti hodil do rieky. Na mieste postavil malú modlitebňu "
                    "zasvätenú Madone, predchodcu dnešnej baziliky.\n\n"
                    "Bola to dramatická symbolika — kresťanstvo doslova vykorenilo "
                    "pamiatku najhorších rímskych prenasledovateľov a postavilo na "
                    "ich mieste svätyňu. Bazilika sa volá „del Popolo\" — „z ľudu\" — "
                    "lebo bola podľa tradície postavená z verejných milodarov bežných "
                    "Rimanov, ktorí sa konečne mohli zbaviť strachu z Nerovho ducha."
                ),
            },
            {
                "id": "caravaggio-cerasi",
                "title": "Caravaggio v Cerasiho kaplnke",
                "text": (
                    "V Bazilike Santa Maria del Popolo sa nachádza Cerasiho kaplnka — "
                    "jedna z najfascinujúcejších umeleckých zostáv v Ríme. V nej visia "
                    "tri obrazy: dva od Caravaggia (Konverzia svätého Pavla a Ukrižovanie "
                    "svätého Petra) a jeden od jeho večného rivala Annibale Carracciho "
                    "(Nanebovzatie Panny Márie).\n\n"
                    "Kardinál Tiberio Cerasi obojstranne objednal v roku 1600 oba "
                    "obrazy ako vrcholné dielo svojej osobnej kaplnky. Caravaggio dodal "
                    "prvé verzie, ktoré boli pre kardinála a jeho rádu Augustiniánov "
                    "natoľko šokujúce, že ich odmietli a požiadali o opravu. Originály "
                    "sa stratili — pravdepodobne ich Caravaggio predal súkromnému "
                    "zberateľovi.\n\n"
                    "Druhá verzia — tá, ktorá dnes visí v kaplnke — je revolučná. "
                    "Konverzia svätého Pavla zobrazuje moment, keď sa Pavol pri ceste "
                    "do Damasku vrhol z koňa po stretnutí s Kristom. Caravaggio "
                    "umiestnil koňa do popredia a zaberá väčšinu plátna. Pavol leží "
                    "na zemi s rukami zdvihnutými, ožiarený svetlom z neba. Žiadne "
                    "anjelské zjavenie, žiadne dramatické gesto — len obrovský kôň "
                    "a oslepený človek pod ním.\n\n"
                    "Ukrižovanie svätého Petra zobrazuje moment, keď traja rímski vojaci "
                    "dvíhajú kríž s Petrom ukrižovaným hlavou dolu. Petrove svaly sú "
                    "napnuté, jeho tvár plná bolesti a údivu. Vojaci sú zobrazení ako "
                    "obyčajní robotníci zápasiaci s ťažkým bremenom. Žiadne hrdinstvo, "
                    "len ľudská dráma. Dva obrazy spolu predstavujú summu Caravaggiovho "
                    "génia — radikálne nový pohľad na náboženské témy, ktorý zmenil "
                    "celé európske umenie."
                ),
            },
        ],
    },
]
