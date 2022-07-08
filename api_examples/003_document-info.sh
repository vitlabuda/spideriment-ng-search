#!/bin/bash

SPIDERIMENT_SEARCH_HOST="http://127.0.0.1:5000"



##### Example 1 - Successful document info query #####
curl --request POST --header 'Content-Type: application/json' --data '{"url": "https://cs.wikipedia.org/wiki/Python"}' "${SPIDERIMENT_SEARCH_HOST}/api/document-info"

# {
#  "data": {
#    "author": "",
#    "content_snippets": [
#      {
#        "text": "Python",
#        "type": "heading_1"
#      },
#      {
#        "text": "Python 3.0[editovat | editovat zdroj]",
#        "type": "heading_2"
#      },
#      {
#        "text": "Navigační menu",
#        "type": "heading_2"
#      },
#      {
#        "text": "Výkon[editovat | editovat zdroj]",
#        "type": "heading_2"
#      },
#      {
#        "text": "Příklady[editovat | editovat zdroj]",
#        "type": "heading_2"
#      },
#      {
#        "text": "Jython[editovat | editovat zdroj]",
#        "type": "heading_3"
#      },
#      {
#        "text": "IronPython[editovat | editovat zdroj]",
#        "type": "heading_3"
#      },
#      {
#        "text": "Interaktivní režim překladače[editovat | editovat zdroj]",
#        "type": "heading_3"
#      },
#      {
#        "text": "Reference[editovat | editovat zdroj]",
#        "type": "heading_3"
#      },
#      {
#        "text": "Dokumentace, učebnice[editovat | editovat zdroj]",
#        "type": "heading_4"
#      },
#      {
#        "text": "Python se snadno vkládá do jiných aplikací (embedding), kde pak slouží jako jejich skriptovací jazyk. Tím lze aplikacím psaným v kompilovaných programovacích jazycích dodávat chybějící pružnost. Jiné aplikace nebo aplikační knihovny mohou naopak implementovat rozhraní, které umožní jejich použití v roli pythonovského modulu. Jinými slovy, pythonovský program je může využívat jako modul dostupný přímo z jazyka Python (tj. extending, viz sekce Spolupráce s jinými aplikacemi).",
#        "type": "regular_text"
#      },
#      {
#        "text": "Jython je implementace CPythonu 2. Poslední stabilní verze Jythonu 2.7.2 je z března roku 2020. Aktuální vývoj viz stránky projektu.",
#        "type": "regular_text"
#      },
#      {
#        "text": "Standardní Python je implementován v jazyce C, tato implementace je označována CPython. V ní probíhá další vývoj jazyka Python. Verze jazyka Python jsou zveřejňovány jak v podobě zdrojového kódu, tak v podobě přeložených instalačních balíků pro různé cílové platformy.",
#        "type": "regular_text"
#      },
#      {
#        "text": "V minulosti se pro zvýšení výkonu používala snadno použitelná knihovna Psyco, která transparentně optimalizovala kód Pythonu na výkon (JIT). Některé operace byly pomocí Psyco urychleny až řádově[4]. Dnes je tato knihovna neudržovaná (cca od roku 2010) a použitelná jen pro 32bitové prostředí a podporuje Python jen do verze 2.6.",
#        "type": "regular_text"
#      },
#      {
#        "text": "Údržba:Články k částečné úpravě",
#        "type": "list_item_text"
#      },
#      {
#        "text": "↑ KRČMÁŘ, Petr. Chyby v programovacích jazycích ohrožují bezpečnost aplikací. root.cz [online]. 12. 12. 2017. Dostupné online. ISSN 1212-8309.",
#        "type": "list_item_text"
#      },
#      {
#        "text": "Bahasa Melayu",
#        "type": "list_item_text"
#      },
#      {
#        "text": "vydáno též v edici CZ.NIC – knižně i elektronicky",
#        "type": "list_item_text"
#      }
#    ],
#    "crawled_at": "2022-07-04T23:30:24",
#    "description": "Python (anglická výslovnost [ˈpaiθən]) je vysokoúrovňový programovací jazyk, který v roce 1991[1] navrhl Guido van Rossum. Nabízí dynamickou kontrolu datových typů a podporuje různá programovací paradigmata, včetně objektově orientovaného, imperativního, procedurálního nebo funkcionálního. V roce 2018 vzrostla jeho popularita a zařadil se mezi nejoblíbenější jazyky. V řadě různých žebříčků dosahuje jedno z prvních třech míst, výjimkou nebývají první místa.",
#    "filetype": "html",
#    "images": [
#      {
#        "alt_text": "Logo Wikimedia Commons",
#        "title_text": "",
#        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/12px-Commons-logo.svg.png"
#      },
#      {
#        "alt_text": "Editovat na Wikidatech",
#        "title_text": "",
#        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/10px-OOjs_UI_icon_edit-ltr-progressive.svg.png"
#      },
#      {
#        "alt_text": "Powered by MediaWiki",
#        "title_text": "",
#        "url": "https://cs.wikipedia.org/static/images/footer/poweredby_mediawiki_88x31.png"
#      },
#      {
#        "alt_text": "ikona",
#        "title_text": "",
#        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Broom_icon.svg/48px-Broom_icon.svg.png"
#      },
#      {
#        "alt_text": "",
#        "title_text": "",
#        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Preferences-system.svg/16px-Preferences-system.svg.png"
#      },
#      {
#        "alt_text": "ikona",
#        "title_text": "",
#        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Ambox_outdated_content.svg/48px-Ambox_outdated_content.svg.png"
#      },
#      {
#        "alt_text": "Logo Pythonu",
#        "title_text": "",
#        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/200px-Python_logo_and_wordmark.svg.png"
#      },
#      {
#        "alt_text": "Python 3. The standard type hierarchy.png",
#        "title_text": "",
#        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Python_3._The_standard_type_hierarchy.png/220px-Python_3._The_standard_type_hierarchy.png"
#      },
#      {
#        "alt_text": "Python-logo-notext",
#        "title_text": "",
#        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/110px-Python-logo-notext.svg.png"
#      }
#    ],
#    "keywords": [],
#    "language": "cs",
#    "links": [
#      {
#        "text": "Linux",
#        "url": "https://cs.wikipedia.org/wiki/Linux"
#      },
#      {
#        "text": "MS Windows",
#        "url": "https://cs.wikipedia.org/wiki/Microsoft_Windows"
#      },
#      {
#        "text": "Vývojář",
#        "url": "https://cs.wikipedia.org/wiki/Program%C3%A1tor"
#      },
#      {
#        "text": "OS",
#        "url": "https://cs.wikipedia.org/wiki/Opera%C4%8Dn%C3%AD_syst%C3%A9m"
#      },
#      {
#        "text": "Unix",
#        "url": "https://cs.wikipedia.org/wiki/Unix"
#      },
#      {
#        "text": "textovém editoru",
#        "url": "https://cs.wikipedia.org/wiki/Textov%C3%BD_editor"
#      },
#      {
#        "text": "zdrojového kódu",
#        "url": "https://cs.wikipedia.org/wiki/Zdrojov%C3%BD_k%C3%B3d"
#      },
#      {
#        "text": "open source",
#        "url": "https://cs.wikipedia.org/wiki/Otev%C5%99en%C3%BD_software"
#      },
#      {
#        "text": "GNU",
#        "url": "https://cs.wikipedia.org/wiki/GNU"
#      },
#      {
#        "text": "1991",
#        "url": "https://cs.wikipedia.org/wiki/1991"
#      },
#      {
#        "text": "zdroj?!",
#        "url": "https://cs.wikipedia.org/wiki/Wikipedie%3AOv%C4%9B%C5%99itelnost"
#      },
#      {
#        "text": "distribucí",
#        "url": "https://cs.wikipedia.org/wiki/Linuxov%C3%A1_distribuce"
#      },
#      {
#        "text": "spam",
#        "url": "https://cs.wikipedia.org/wiki/Spam"
#      },
#      {
#        "text": "Microsoft",
#        "url": "https://cs.wikipedia.org/wiki/Microsoft"
#      },
#      {
#        "text": "Programování",
#        "url": "https://cs.wikipedia.org/wiki/Programov%C3%A1n%C3%AD"
#      },
#      {
#        "text": "interpret",
#        "url": "https://cs.wikipedia.org/wiki/Interpret_%28software%29"
#      },
#      {
#        "text": "programovací jazyk",
#        "url": "https://cs.wikipedia.org/wiki/Programovac%C3%AD_jazyk"
#      },
#      {
#        "text": "Web",
#        "url": "https://cs.wikipedia.org/wiki/World_Wide_Web"
#      },
#      {
#        "text": "C",
#        "url": "https://cs.wikipedia.org/wiki/C_%28programovac%C3%AD_jazyk%29"
#      },
#      {
#        "text": "instalátor",
#        "url": "https://cs.wikipedia.org/wiki/Instalace_%28software%29"
#      },
#      {
#        "text": "grafického uživatelského rozhraní",
#        "url": "https://cs.wikipedia.org/wiki/Grafick%C3%A9_u%C5%BEivatelsk%C3%A9_rozhran%C3%AD"
#      },
#      {
#        "text": "anglická výslovnost",
#        "url": "https://cs.wikipedia.org/wiki/Angli%C4%8Dtina"
#      },
#      {
#        "text": "Red Hat",
#        "url": "https://cs.wikipedia.org/wiki/Red_Hat"
#      },
#      {
#        "text": "Hlavní implementace",
#        "url": "https://cs.wikipedia.org/wiki/Implementace"
#      },
#      {
#        "text": "syntaxe",
#        "url": "https://cs.wikipedia.org/wiki/Syntax"
#      },
#      {
#        "text": "objektově orientovaného",
#        "url": "https://cs.wikipedia.org/wiki/Objektov%C4%9B_orientovan%C3%A9_programov%C3%A1n%C3%AD"
#      },
#      {
#        "text": "funkcionálního",
#        "url": "https://cs.wikipedia.org/wiki/Funkcion%C3%A1ln%C3%AD_programov%C3%A1n%C3%AD"
#      },
#      {
#        "text": "2020",
#        "url": "https://cs.wikipedia.org/wiki/2020"
#      },
#      {
#        "text": "2022",
#        "url": "https://cs.wikipedia.org/wiki/2022"
#      },
#      {
#        "text": "platforem",
#        "url": "https://cs.wikipedia.org/wiki/Po%C4%8D%C3%ADta%C4%8Dov%C3%A1_platforma"
#      },
#      {
#        "text": "Java",
#        "url": "https://cs.wikipedia.org/wiki/Java_%28programovac%C3%AD_jazyk%29"
#      },
#      {
#        "text": "C++",
#        "url": "https://cs.wikipedia.org/wiki/C%2B%2B"
#      },
#      {
#        "text": "JVM",
#        "url": "https://cs.wikipedia.org/wiki/Java_Virtual_Machine"
#      },
#      {
#        "text": "8bitovým",
#        "url": "https://cs.wikipedia.org/wiki/8bitov%C3%BD"
#      },
#      {
#        "text": "Vzhled a styl",
#        "url": "https://cs.wikipedia.org/wiki/Wikipedie%3AVzhled_a_styl"
#      },
#      {
#        "text": "Odkazy",
#        "url": "https://cs.wikipedia.org/wiki/Wikipedie%3APr%C5%AFvodce_%28odkazy%29"
#      },
#      {
#        "text": "Vim",
#        "url": "https://cs.wikipedia.org/wiki/Vim"
#      },
#      {
#        "text": "Smalltalk",
#        "url": "https://cs.wikipedia.org/wiki/Smalltalk"
#      },
#      {
#        "text": "Lisp",
#        "url": "https://cs.wikipedia.org/wiki/Lisp"
#      },
#      {
#        "text": "Mono",
#        "url": "https://cs.wikipedia.org/wiki/Mono_%28platforma%29"
#      },
#      {
#        "text": "macOS",
#        "url": "https://cs.wikipedia.org/wiki/OS_X"
#      },
#      {
#        "text": "14. ledna",
#        "url": "https://cs.wikipedia.org/wiki/14._leden"
#      },
#      {
#        "text": "10. února",
#        "url": "https://cs.wikipedia.org/wiki/10._%C3%BAnor"
#      },
#      {
#        "text": "20. dubna",
#        "url": "https://cs.wikipedia.org/wiki/20._duben"
#      },
#      {
#        "text": "20. února",
#        "url": "https://cs.wikipedia.org/wiki/20._%C3%BAnor"
#      },
#      {
#        "text": "Poslední verze",
#        "url": "https://cs.wikipedia.org/wiki/Verze"
#      },
#      {
#        "text": "GIMP",
#        "url": "https://cs.wikipedia.org/wiki/GIMP"
#      },
#      {
#        "text": "optimalizovala",
#        "url": "https://cs.wikipedia.org/wiki/Optimalizace_%28informatika%29"
#      },
#      {
#        "text": "OpenOffice.org",
#        "url": "https://cs.wikipedia.org/wiki/OpenOffice.org"
#      },
#      {
#        "text": "Blender",
#        "url": "https://cs.wikipedia.org/wiki/Blender"
#      },
#      {
#        "text": "Licence",
#        "url": "https://cs.wikipedia.org/wiki/Softwarov%C3%A1_licence"
#      },
#      {
#        "text": "Tcl",
#        "url": "https://cs.wikipedia.org/wiki/Tcl"
#      },
#      {
#        "text": "Perl",
#        "url": "https://cs.wikipedia.org/wiki/Perl"
#      },
#      {
#        "text": "multiplatformní",
#        "url": "https://cs.wikipedia.org/wiki/Multiplatformn%C3%AD_software"
#      },
#      {
#        "text": "Dialekty",
#        "url": "https://cs.wikipedia.org/wiki/Dialekt_%28programov%C3%A1n%C3%AD%29"
#      },
#      {
#        "text": "Skočit na navigaci",
#        "url": "https://cs.wikipedia.org/wiki/Python"
#      },
#      {
#        "text": "Ruby",
#        "url": "https://cs.wikipedia.org/wiki/Ruby"
#      },
#      {
#        "text": "procedurální",
#        "url": "https://cs.wikipedia.org/wiki/Procedur%C3%A1ln%C3%AD_programov%C3%A1n%C3%AD"
#      },
#      {
#        "text": "Rust",
#        "url": "https://cs.wikipedia.org/wiki/Rust_%28programovac%C3%AD_jazyk%29"
#      },
#      {
#        "text": "multiparadigmatický",
#        "url": "https://cs.wikipedia.org/wiki/Multiparadigmatick%C3%BD_programovac%C3%AD_jazyk"
#      },
#      {
#        "text": "imperativního",
#        "url": "https://cs.wikipedia.org/wiki/Imperativn%C3%AD_programov%C3%A1n%C3%AD"
#      },
#      {
#        "text": "Boo",
#        "url": "https://cs.wikipedia.org/wiki/Boo_%28programovac%C3%AD_jazyk%29"
#      },
#      {
#        "text": "Groovy",
#        "url": "https://cs.wikipedia.org/wiki/Groovy"
#      },
#      {
#        "text": "Paradigma",
#        "url": "https://cs.wikipedia.org/wiki/Programovac%C3%AD_paradigma"
#      },
#      {
#        "text": "interpretovaný jazyk",
#        "url": "https://cs.wikipedia.org/wiki/Interpretovan%C3%BD_jazyk"
#      },
#      {
#        "text": ".NET",
#        "url": "https://cs.wikipedia.org/wiki/.NET"
#      },
#      {
#        "text": "Qt",
#        "url": "https://cs.wikipedia.org/wiki/Qt_%28knihovna%29"
#      },
#      {
#        "text": "GTK+",
#        "url": "https://cs.wikipedia.org/wiki/GTK%2B"
#      },
#      {
#        "text": "3D",
#        "url": "https://cs.wikipedia.org/wiki/3D"
#      },
#      {
#        "text": "Typová kontrola",
#        "url": "https://cs.wikipedia.org/wiki/Typov%C3%A1_kontrola"
#      },
#      {
#        "text": "Raspberry Pi",
#        "url": "https://cs.wikipedia.org/wiki/Raspberry_Pi"
#      },
#      {
#        "text": "skriptovací jazyky",
#        "url": "https://cs.wikipedia.org/wiki/Skriptovac%C3%AD_jazyk"
#      },
#      {
#        "text": "Unicode",
#        "url": "https://cs.wikipedia.org/wiki/Unicode"
#      },
#      {
#        "text": "programování ve velkém",
#        "url": "https://cs.wikipedia.org/wiki/Programov%C3%A1n%C3%AD_ve_velk%C3%A9m"
#      },
#      {
#        "text": "jmenných prostorů",
#        "url": "https://cs.wikipedia.org/wiki/Jmenn%C3%BD_prostor"
#      },
#      {
#        "text": "unit testing",
#        "url": "https://cs.wikipedia.org/wiki/Unit_testing"
#      },
#      {
#        "text": "Guido van Rossum",
#        "url": "https://cs.wikipedia.org/wiki/Guido_van_Rossum"
#      },
#      {
#        "text": "výjimek",
#        "url": "https://cs.wikipedia.org/wiki/V%C3%BDjimka_%28programov%C3%A1n%C3%AD%29"
#      },
#      {
#        "text": "transparentně",
#        "url": "https://cs.wikipedia.org/wiki/Transparentnost_%28informatika%29"
#      },
#      {
#        "text": "CPython",
#        "url": "https://cs.wikipedia.org/wiki/CPython"
#      },
#      {
#        "text": "Jython",
#        "url": "https://cs.wikipedia.org/wiki/Jython"
#      },
#      {
#        "text": "bloků",
#        "url": "https://cs.wikipedia.org/wiki/Blok_%28programov%C3%A1n%C3%AD%29"
#      },
#      {
#        "text": "ABC",
#        "url": "https://cs.wikipedia.org/wiki/ABC_%28programovac%C3%AD_jazyk%29"
#      },
#      {
#        "text": "Mandelbrotovy množiny",
#        "url": "https://cs.wikipedia.org/wiki/Mandelbrotova_mno%C5%BEina"
#      },
#      {
#        "text": "Monty Python",
#        "url": "https://cs.wikipedia.org/wiki/Monty_Python"
#      },
#      {
#        "text": "wxWidgets",
#        "url": "https://cs.wikipedia.org/wiki/WxWidgets"
#      },
#      {
#        "text": "Cython",
#        "url": "https://cs.wikipedia.org/wiki/Cython"
#      },
#      {
#        "text": "IronPython",
#        "url": "https://cs.wikipedia.org/wiki/IronPython"
#      },
#      {
#        "text": "Python (rozcestník)",
#        "url": "https://cs.wikipedia.org/wiki/Python_%28rozcestn%C3%ADk%29"
#      },
#      {
#        "text": "vylepšíte",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit"
#      },
#      {
#        "text": "diskusní stránku",
#        "url": "https://cs.wikipedia.org/wiki/Diskuse%3APython"
#      },
#      {
#        "text": "Python Software Foundation",
#        "url": "https://www.python.org/psf"
#      },
#      {
#        "text": "duck-typing",
#        "url": "https://cs.wikipedia.org/wiki/Duck-typing"
#      },
#      {
#        "text": "PyPy",
#        "url": "https://cs.wikipedia.org/w/index.php?title=PyPy&action=edit&redlink=1"
#      },
#      {
#        "text": "Stackless Python",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Stackless_Python&action=edit&redlink=1"
#      },
#      {
#        "text": "RPython",
#        "url": "https://cs.wikipedia.org/w/index.php?title=RPython&action=edit&redlink=1"
#      },
#      {
#        "text": "Python Software Foundation License",
#        "url": "https://www.python.org/psf/license"
#      },
#      {
#        "text": "www.python.org",
#        "url": "https://www.python.org/"
#      },
#      {
#        "text": "Zope",
#        "url": "https://cs.wikipedia.org/wiki/Zope"
#      },
#      {
#        "text": "krajtu",
#        "url": "https://cs.wikipedia.org/wiki/Krajta_%28Python%29"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=1"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=1"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=2"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=2"
#      },
#      {
#        "text": "wxPython",
#        "url": "https://cs.wikipedia.org/wiki/WxPython"
#      },
#      {
#        "text": "PySide",
#        "url": "https://cs.wikipedia.org/w/index.php?title=PySide&action=edit&redlink=1"
#      },
#      {
#        "text": "PyQT",
#        "url": "https://cs.wikipedia.org/w/index.php?title=PyQT&action=edit&redlink=1"
#      },
#      {
#        "text": "PyGTK",
#        "url": "https://cs.wikipedia.org/wiki/PyGTK"
#      },
#      {
#        "text": "kompilovaných programovacích jazycích",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Kompilovan%C3%BD_programovac%C3%AD_jazyk&action=edit&redlink=1"
#      },
#      {
#        "text": "filosofii Pythonu",
#        "url": "https://cs.wikipedia.org/wiki/Filosofie_Pythonu"
#      },
#      {
#        "text": "PyPI",
#        "url": "https://cs.wikipedia.org/wiki/PyPI"
#      },
#      {
#        "text": "pip",
#        "url": "https://cs.wikipedia.org/wiki/Pip_%28Python%29"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=3"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=3"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=4"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=4"
#      },
#      {
#        "text": "Boost.Python",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Boost.Python&action=edit&redlink=1"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=5"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=5"
#      },
#      {
#        "text": "stránky projektu",
#        "url": "http://www.jython.org/"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=6"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=6"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=7"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=7"
#      },
#      {
#        "text": "Brython",
#        "url": "https://brython.info/index.html"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=8"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=8"
#      },
#      {
#        "text": "RPython",
#        "url": "https://rpython.readthedocs.io/en/latest/index.html"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=9"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=9"
#      },
#      {
#        "text": "Cython",
#        "url": "https://cython.org/"
#      },
#      {
#        "text": "optimalizací",
#        "url": "https://www.root.cz/clanky/prakticke-pouziti-nastroje-cython-pri-prekladu-pythonu-do-nativniho-kodu-1/"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=10"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=10"
#      },
#      {
#        "text": "PyPy",
#        "url": "https://www.pypy.org/features.html"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=11"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=11"
#      },
#      {
#        "text": "RustPython",
#        "url": "https://github.com/RustPython/RustPython"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=12"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=12"
#      },
#      {
#        "text": "Psyco",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Psyco&action=edit&redlink=1"
#      },
#      {
#        "text": "editovat",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&veaction=edit&section=13"
#      },
#      {
#        "text": "editovat zdroj",
#        "url": "https://cs.wikipedia.org/w/index.php?title=Python&action=edit&section=13"
#      },
#      {
#        "text": "Civilization IV",
#        "url": "https://cs.wikipedia.org/wiki/Civilization_IV"
#      }
#    ],
#    "title": "Python – Wikipedie",
#    "url": "https://cs.wikipedia.org/wiki/Python"
#  },
#  "success": true
# }



##### Example 2 - Failed document info query #####
curl --request POST --header 'Content-Type: application/json' --data '{"url": "https://example.com/"}' "${SPIDERIMENT_SEARCH_HOST}/api/document-info"

# {
#  "error_message": "A document with the URL of 'https://example.com/' is not present in the database!",
#  "success": false
# }
