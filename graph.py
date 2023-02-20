import networkx as nx
import matplotlib.pyplot as plt
import colors as col

from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community.label_propagation import asyn_lpa_communities


def drawgraph():
    myGraph = nx.Graph()
    myGraph.add_node("neuer", club="fcb", club2="s04", color="red")
    myGraph.add_node("sane", club="fcb", club2="mnc", club3="s04", color="red")
    myGraph.add_node("kimmich", club="fcb", club2="vfb", color="red")
    myGraph.add_node("hummels", club="bvb", club2="fcb", color="yellow")
    myGraph.add_node("schlotterbeck", club="bvb", club2="scf", color="yellow")
    myGraph.add_node("reus", club="bvb", club2="bmg", color="yellow")
    myGraph.add_node("kramer", club="bmg", club2="lev", color="green")
    myGraph.add_node("hofmann", club="bmg", club2="bvb", color="green")
    myGraph.add_node("sommer", club="fcb", club2="bmg", color="red")

    myGraph.add_edge("neuer", "sane", weight=5.0)
    myGraph.add_edge("neuer", "kimmich", weight=5.0)
    myGraph.add_edge("neuer", "sommer", weight=5.0)
    myGraph.add_edge("neuer", "hummels", weight=2.5)
    myGraph.add_edge("hummels", "kimmich", weight=2.5)
    myGraph.add_edge("sane", "kimmich", weight=5.0)
    myGraph.add_edge("sane", "sommer", weight=5.0)
    myGraph.add_edge("sane", "hummels", weight=2.5)
    myGraph.add_edge("hummels", "reus", weight=5.0)
    myGraph.add_edge("hummels", "schlotterbeck", weight=5.0)
    myGraph.add_edge("reus", "schlotterbeck", weight=5.0)
    myGraph.add_edge("reus", "hofmann", weight=2.5)
    myGraph.add_edge("reus", "kramer", weight=2.5)
    myGraph.add_edge("reus", "sommer", weight=2.5)
    myGraph.add_edge("sommer", "hofmann", weight=2.5)
    myGraph.add_edge("sommer", "kramer", weight=2.5)
    myGraph.add_edge("hofmann", "hummels", weight=2.5)
    myGraph.add_edge("hofmann", "schlotterbeck", weight=2.5)

    communities = girvan_newman(myGraph)
    nodeGroups = []

    for c in next(communities):
        nodeGroups.append(list(c))

    print(nodeGroups)
    print(len(nodeGroups))

    colorMap = []

    for node in myGraph:
        if node in nodeGroups[0]:
            colorMap.append("red")
        else:
            colorMap.append("yellow")

    nx.draw(myGraph, node_color=colorMap, with_labels=True)
    plt.show()


def createnodes():
    # pattern:  y2013=, y2014=, y2015=, y2016=, y2017=, y2018=, y2019=, y2020=, y2021=, y2022=)
    bundesliga = nx.Graph()
    bundesliga.add_node(1, name='Reece Oxford', club='FC Augsburg', y2013='West Ham United FC', y2014='West Ham United FC', y2015='West Ham United FC', y2016='West Ham United FC', y2017='Borussia Mönchengladbach', y2018='West Ham United FC', y2019='FC Augsburg', y2020='FC Augsburg', y2021='FC Augsburg', y2022='FC Augsburg')
    bundesliga.add_node(2, name='Jordan', club='1. FC Union Berlin',y2013='Stade de Reims', y2014='Stade de Reims', y2015='Stade de Reims', y2016='Stade de Reims', y2017='LB Chateauroux',y2018='Stade Rennais FC',y2019='Stade Rennais FC',y2020='Berner SC Young Boys',y2021 = 'Berner SC Young Boys',y2022 = 'Berner SC Young Boys')
    bundesliga.add_node(3, name='Peter Pekarík', club='Hertha BSC Berlin',y2013='Hertha BSC Berlin',y2014='Hertha BSC Berlin',y2015='Hertha BSC Berlin',y2016='Hertha BSC Berlin',y2017='Hertha BSC Berlin',y2018='Hertha BSC Berlin',y2019='Hertha BSC Berlin',y2020='Hertha BSC Berlin',y2021='Hertha BSC Berlin',y2022='Hertha BSC Berlin')
    bundesliga.add_node(4, name='Tim Lemperle', club='1. FC Köln',y2013='1. FSV Mainz',y2014='1. FSV Mainz 05',y2015='FSV Frankfurt',y2016='FSV Frankfurt',y2017='1. FC Köln',y2018='1. FC Köln',y2019='1. FC Köln',y2020='1. FC Köln',y2021='1. FC Köln',y2022='1.FC Köln')
    bundesliga.add_node(5, name='Thomas Meunier', club='Borussia Dortmund',y2013='Club Brügge',y2014='Club Brügge',y2015='Club Brügge',y2016='Paris Saint-Germain FC',y2017='Paris Saint-Germain FC',y2018='Paris Saint-Germain FC',y2019='Paris Saint-Germain FC',y2020='Borussia Dortmund',y2021='Borussia Dortmund',y2022='Borussia Dortmund')
    bundesliga.add_node(6, name='Levin Öztunali', club='1. FC Union Berlin',y2013='Bayer 04 Leverkusen',y2014='Bayer 04 Leverkusen',y2015='SV Werder Bremen',y2016='1. FSV Mainz 05',y2017='1. FSV Mainz 05',y2018='1. FSV Mainz 05',y2019='1. FSV Mainz 05',y2020='1. FSV Mainz 05',y2021='1. FC Union Berlin',y2022='1. FC Union Berlin')
    bundesliga.add_node(7, name='Yann Sommer', club='FC Bayern München',y2013='FC Basel',y2014='Borussia Mönchengladbach',y2015='Borussia Mönchengladbach',y2016='Borussia Mönchengladbach',y2017='Borussia Mönchengladbach',y2018='Borussia Mönchengladbach',y2019='Borussia Mönchengladbach',y2020='Borussia Mönchengladbach',y2021='Borussia Mönchengladbach',y2022 ='Borussia Mönchengladbach')
    bundesliga.add_node(8, name='Johannes Schenk', club='FC Bayern München')
    bundesliga.add_node(9, name='Kelvin Yeboah', club='FC Augsburg',y2017='AC Gozzano',y2018='WSG Wattens',y2019='WSG Swarovski Tirol',y2020='WSG Swarovski Tirol',y2021='SK Puntigamer Sturm Graz',y2022='Genua CFC 1893')
    bundesliga.add_node(10, name='Konrad Laimer', club='RB Leipzig',y2013='FC Red Bull Salzburg',y2014='FC Red Bull Salzburg',y2015='FC Red Bull Salzburg',y2016='FC Red Bull Salzburg',y2017='RB Leipzig',y2018='RB Leipzig',y2019='RB Leipzig',y2020='RB Leipzig',y2021='RB Leipzig',y2022='RB Leipzig')
    bundesliga.add_node(11, name='Filip Uremović', club='Hertha BSC Berlin',y2013 = 'HNK Cibalia Vinkovci',y2014 = 'HNK Cibalia Vinkovci',y2015 = 'HNK Cibalia Vinkovci',y2016 = 'GNK Dinamo Zagreb',y2017 = 'GNK Dinamo Zagreb',y2018 = 'FC Rubin Kazan',y2019 = 'FC Rubin Kazan',y2020 = 'FC Rubin Kazan',y2021 = 'FC Rubin Kazan',y2022 = 'Sheffield United')
    bundesliga.add_node(12, name='Patrick Wimmer', club='VfL Wolfsburg',y2013 = 'Sportklub Sitzenberg-Reidling',y2014 = 'Sportklub Sitzenberg-Reidling',y2015 = 'FC Waidhofen',y2016 = 'FC Waidhofen',y2017 = 'SV Gaflenz',y2018 = 'SV Gaflenz',y2019 = 'FK Austria Wien',y2020 = 'FK Austria Wien',y2021 = 'DSC Arminia Bielefeld',y2022 = 'VfL Wolfsburg')
    bundesliga.add_node(13, name='Lars Stindl', club='Borussia Mönchengladbach',y2013='Hannover 96',y2014='Hannover 96',y2015='Borussia Mönchengladbach',y2016='Borussia Mönchengladbach',y2017='Borussia Mönchengladbach',y2018='Borussia Mönchengladbach',y2019='Borussia Mönchengladbach',y2020='Borussia Mönchengladbach',y2021='Borussia Mönchengladbach',y2022='Borussia Mönchengladbach')
    bundesliga.add_node(14, name='Ozan Kabak', club='TSG 1899 Hoffenheim',y2013 = 'Galatasaray SK Istanbul',y2014 = 'Galatasaray SK Istanbul',y2015 = 'Galatasaray SK Istanbul',y2016 = 'Galatasaray SK Istanbul',y2017 = 'Galatasaray SK Istanbul',y2018 = 'Galatasaray SK Istanbul',y2019 = 'VfB Stuttgart',y2020 = 'FC Schalke 04',y2021 = 'Liverpool FC',y2022 = 'TSG Hoffenheim')
    bundesliga.add_node(15, name='Michael Langer', club='FC Schalke 04', y2013='SV Sandhausen', y2014='Valerenga IF Oslo', y2015='Valerenga IF Oslo', y2016='IFK Norrköping', y2017='FC Schalke 04', y2018='FC Schalke 04', y2019='FC Schalke 04', y2020='FC Schalke 04', y2021='FC Schalke 04', y2022='FC Schalke 04')
    bundesliga.add_node(16, name='Sadio Mané', club='FC Bayern München', y2013='FC Red Bull Salzburg', y2014='Southampton FC', y2015='Southampton FC', y2016='Liverpool FC', y2017='Liverpool FC', y2018='Liverpool FC', y2019='Liverpool FC', y2020='Liverpool FC', y2021='Liverpool FC', y2022='FC Bayern München')
    bundesliga.add_node(17, name='Maximilian Philipp', club='SV Werder Bremen', y2013='SC Freiburg', y2014='SC Freiburg', y2015='SC Freiburg', y2016='SC Freiburg', y2017='Borussia Dortmund', y2018='Borussia Dortmund', y2019='Borussia Dortmund', y2020='Dinamo Moskau', y2021='VfL Wolfsburg', y2022='VfL Wolfsburg')
    bundesliga.add_node(18, name='Elias Bakatukanda ', club='1. FC Köln', y2013='1. FC Köln', y2014='1. FC Köln', y2015='1. FC Köln', y2016='1. FC Köln', y2017='1. FC Köln', y2018='1. FC Köln', y2019='1. FC Köln', y2020='1. FC Köln', y2021='1. FC Köln', y2022='1. FC Köln')
    bundesliga.add_node(19, name='Matthias Ginter', club='SC Freiburg', y2013='SC Freiburg', y2014='Borussia Dortmund', y2015='Borussia Dortmund', y2016='Borussia Dortmund', y2017='Borussia Mönchengladbach', y2018='Borussia Mönchengladbach', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(20, name='Amadou Haidara', club='RB Leipzig', y2015='JMG Academy Bamako', y2016='FC Liefering', y2017='FC Red Bull Salzburg', y2018='FC Red Bull Salzburg', y2019='RB Leipzig', y2020='RB Leipzig', y2021='RB Leipzig', y2022='RB Leipzig')
    bundesliga.add_node(21, name='Malick Sanogo', club='1. FC Union Berlin', y2018='FC Energie Cottbus', y2019='1. FC Union Berlin', y2020='1. FC Union Berlin', y2021='1. FC Union Berlin', y2022='1. FC Union Berlin')
    bundesliga.add_node(22, name='Josip Stanišić', club='FC Bayern München')
    bundesliga.add_node(23, name='Yannick Gerhardt', club='VfL Wolfsburg', y2013='1. FC Köln', y2014='1. FC Köln', y2015='1. FC Köln', y2016='VfL Wolfsburg', y2017='VfL Wolfsburg', y2018='VfL Wolfsburg', y2019='VfL Wolfsburg', y2020='VfL Wolfsburg', y2021='VfL Wolfsburg', y2022='VfL Wolfsburg')
    bundesliga.add_node(24, name='Irvin Cardona', club='FC Augsburg', y2013='AS Monaco', y2014='AS Monaco', y2015='AS Monaco', y2016='AS Monaco', y2017='Cercle Brügge KSV', y2018='Cercle Brügge KSV', y2019='Stade Brestois', y2020='Stade Brestois', y2021='Stade Brestois', y2022='Stade Brestois')
    bundesliga.add_node(25, name='Jessic Ngankam', club='Hertha BSC Berlin', y2013='Hertha BSC Berlin', y2014='Hertha BSC Berlin', y2015='Hertha BSC Berlin', y2016='Hertha BSC Berlin', y2017='Hertha BSC Berlin', y2018='Hertha BSC Berlin', y2019='Hertha BSC Berlin', y2020='Hertha BSC Berlin', y2021='SpVgg Greuther Fürth', y2022='SpVgg Greuther Fürth')
    bundesliga.add_node(26, name='Benjamin Uphoff', club='Sport-Club Freiburg', y2013='1. FC Nürnberg', y2014='VfB Stuttgart', y2015='VfB Stuttgart', y2016='VfB Stuttgart', y2017='Karlsruher SC', y2018='Karlsruher SC', y2019='Karlsruher SC', y2020='SC Freiburg', y2021='SC Freiburg', y2022='SC Freiburg')
    bundesliga.add_node(27, name='Dani Olmo', club='RB Leipzig', y2013='FC Barcelona', y2014='GNK Dinamo Zagreb', y2015='GNK Dinamo Zagreb', y2016='GNK Dinamo Zagreb', y2017='GNK Dinamo Zagreb', y2018='GNK Dinamo Zagreb', y2019='GNK Dinamo Zagreb', y2020='RB Leipzig', y2021='RB Leipzig', y2022='RB Leipzig')
    bundesliga.add_node(28, name='Grischa Prömel', club='TSG 1899 Hoffenheim', y2013='TSG 1899 Hoffenheim', y2014='TSG 1899 Hoffenheim', y2015='Karlsruher SC', y2016='Karlsruher SC', y2017='1. FC Union Berlin', y2018='1. FC Union Berlin', y2019='1. FC Union Berlin', y2020='1. FC Union Berlin', y2021='1. FC Union Berlin', y2022='1. FC Union Berlin')
    bundesliga.add_node(29, name='Mark Uth', club='1. FC Köln', y2013='Heracles Almelo', y2014='SC Heerenveen', y2015='TSG 1899 Hoffenheim', y2016='TSG 1899 Hoffenheim', y2017='TSG 1899 Hoffenheim', y2018='FC Schalke 04', y2019='FC Schalke 04', y2020='FC Schalke 04', y2021='1. FC Köln', y2022='1. FC Köln')
    bundesliga.add_node(30, name='Exequiel Palacios', club='Bayer 04 Leverkusen',y2013='CA River Plate', y2014='CA River Plate', y2015='CA River Plate', y2016='CA River Plate', y2017='CA River Plate', y2018='CA River Plate', y2019='CA River Plate', y2020='Bayer 04 Leverkusen', y2021='Bayer 04 Leverkusen', y2022='Bayer 04 Leverkusen')
    bundesliga.add_node(31, name='Luca Pfeiffer', club='VfB Stuttgart', y2013='FSV Hollenbach', y2014='FSV Hollenbach', y2015='FSV Hollenbach', y2016='SV Stuttgarter Kickers', y2017='SV Stuttgarter Kickers', y2018='VfL Osnabrück', y2019='FC Würzburger Kickers', y2020='SV Darmstadt 98', y2021='SV Darmstadt 98', y2022='SV Darmstadt 98')
    bundesliga.add_node(32, name='Silvan Widmer', club='1. FSV Mainz 05', y2013='Udinese Calcio', y2014='Udinese Calcio', y2015='Udinese Calcio', y2016='Udinese Calcio', y2017='Udinese Calcio', y2018='FC Basel', y2019='FC Basel', y2020='FC Basel', y2021='1. FSV Mainz 05', y2022='1. FSV Mainz 05')
    bundesliga.add_node(33, name='Moritz Jenz', club='FC Schalke 04', y2014='Tennis Borussia Berlin', y2015='Fulham FC', y2016='Fulham FC', y2017='Fulham FC', y2018='Fulham FC', y2019='Fulham FC', y2020='Lausanne-Sports', y2021='FC Lorient', y2022='Celtic Glasgow FC')
    bundesliga.add_node(34, name='Marcus Thuram', club='Borussia Mönchengladbach', y2013='FC Sochaux', y2014='FC Sochaux', y2015='FC Sochaux', y2016='FC Sochaux', y2017='En Avant de Guingamp', y2018='En Avant de Guingamp', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(35, name='Florian Müller', club='VfB Stuttgart', y2013='1. FSV Mainz 05', y2014='1. FSV Mainz 05', y2015='1. FSV Mainz 05', y2016='1. FSV Mainz 05', y2017='1. FSV Mainz 05', y2018='1. FSV Mainz 05', y2019='1. FSV Mainz 05', y2020='1. FSV Mainz 05', y2021='VfB Stuttgart', y2022='VfB Stuttgart')
    bundesliga.add_node(36, name='Kevin Vogt', club='TSG 1899 Hoffenheim', y2013='FC Augsburg', y2014='1. FC Köln', y2015='1. FC Köln', y2016='TSG 1899 Hoffenheim', y2017='TSG 1899 Hoffenheim', y2018='TSG 1899 Hoffenheim', y2019='TSG 1899 Hoffenheim', y2020='SV Werder Bremen', y2021='TSG 1899 Hoffenheim', y2022='TSG 1899 Hoffenheim')
    bundesliga.add_node(37, name='Iago', club='FC Augsburg', y2013='SC Internacional', y2014='SC Internacional', y2015='SC Internacional', y2016='SC Internacional', y2017='SC Internacional', y2018='SC Internacional', y2019='FC Augsburg', y2020='FC Augsburg', y2021='FC Augsburg', y2022='FC Augsburg')
    bundesliga.add_node(38, name='Takuma Asano', club='VfL Bochum', y2013='Sanfrecce Hiroshima', y2014='Sanfrecce Hiroshima', y2015='Sanfrecce Hiroshima', y2016='Arsenal FC', y2017='VfB Stuttgart', y2018='Hannover 96', y2019='Arsenal FC', y2020='FK Partizan Belgrad', y2021='VfL Bochum', y2022='VfL Bochum')
    bundesliga.add_node(39, name='Nico Elvedi', club='Borussia Mönchengladbach', y2013='FC Zürich', y2014='FC Zürich', y2015='Borussia Mönchengladbach', y2016='Borussia Mönchengladbach', y2017='Borussia Mönchengladbach', y2018='Borussia Mönchengladbach', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(40, name='Lucas Hernández', club='FC Bayern München', y2013='Atletico Madrid', y2014='Atletico Madrid', y2015='Atletico Madrid', y2016='Atletico Madrid', y2017='Atletico Madrid', y2018='Atletico Madrid', y2019='FC Bayern München', y2020='FC Bayern München', y2021='FC Bayern München', y2022='FC Bayern München')
    bundesliga.add_node(41, name='Luca Waldschmidt', club='VfL Wolfsburg', y2013='Eintracht Frankfurt', y2014='Eintracht Frankfurt', y2015='Eintracht Frankfurt', y2016='Hamburger SV', y2017='Hamburger SV', y2018='SC Freiburg', y2019='SC Freiburg', y2020='SL Benfica Lissabon', y2021='VfL Wolfsburg', y2022='VfL Wolfsburg')
    bundesliga.add_node(42, name='Marius Wolf', club='Borussia Dortmund', y2013='TSV 1860 München', y2014='TSV 1860 München', y2015='TSV 1860 München', y2016='Hannover 96', y2017='Eintracht Frankfurt', y2018='Borussia Dortmund', y2019='Hertha BSC Berlin', y2020='Borussia Dortmund', y2021='1. FC Köln', y2022='Borussia Dortmund')
    bundesliga.add_node(43, name='Konstantinos Mavropanos', club='VfB Stuttgart', y2013='Apollon Smyrnis', y2014='Apollon Smyrnis', y2015='Apollon Smyrnis', y2016='PAS Giannina FC', y2017='PAS Giannina FC', y2018='Arsenal FC', y2019='Arsenal FC', y2020='1. FC Nürnberg', y2021='VfB Stuttgart', y2022='VfB Stuttgart')
    bundesliga.add_node(44, name='Joshua Kimmich', club='FC Bayern München', y2013='RB Leipzig', y2014='RB Leipzig', y2015='FC Bayern München', y2016='FC Bayern München', y2017='FC Bayern München', y2018='FC Bayern München', y2019='FC Bayern München', y2020='FC Bayern München', y2021='FC Bayern München', y2022='FC Bayern München')
    bundesliga.add_node(45, name='Christoph Baumgartner', club='TSG 1899 Hoffenheim', y2013='AKA St. Pölten' , y2014='AKA St. Pölten' , y2015='AKA St. Pölten' , y2016='AKA St. Pölten' , y2017='TSG 1899 Hoffenheim', y2018='TSG 1899 Hoffenheim', y2019='TSG 1899 Hoffenheim', y2020='TSG 1899 Hoffenheim', y2021='TSG 1899 Hoffenheim', y2022='TSG 1899 Hoffenheim')
    bundesliga.add_node(46, name='Lee Buchanan', club='SV Werder Bremen', y2013='Derby County FC', y2014='Derby County FC', y2015='Derby County FC', y2016='Derby County FC', y2017='Derby County FC', y2018='Derby County FC', y2019='Derby County FC', y2020='Derby County FC', y2021='Derby County FC', y2022='SV Werder Bremen')
    bundesliga.add_node(47, name='Michael Gregoritsch', club='SC Freiburg', y2013='FC St. Pauli', y2014='VfL Bochum', y2015='Hamburger SV', y2016='Hamburger SV', y2017='FC Augsburg', y2018='FC Augsburg', y2019='FC Augsburg', y2020='FC Schalke', y2021='FC Augsburg', y2022='SC Freiburg')
    bundesliga.add_node(48, name='Benjamin Leneis', club='FC Augsburg', y2014='1. FC Nürnberg', y2015='FC Augsburg', y2016='FC Augsburg', y2017='FC Augsburg', y2018='FC Augsburg', y2019='FC Augsburg', y2020='FC Augsburg', y2021='1. FC Magdeburg', y2022='FC Augsburg')
    bundesliga.add_node(49, name='Dženan Pejčinović', club='VfL Wolfsburg', y2016='FC Bayern München', y2017='FC Augsburg', y2018='FC Augsburg', y2019='FC Augsburg', y2020='FC Augsburg', y2021='FC Augsburg', y2022='VfL Wolfsburg')
    bundesliga.add_node(50, name='Niklas Lomb', club='Bayer 04 Leverkusen', y2013='Bayer 04 Leverkusen', y2014='Bayer 04 Leverkusen', y2015='Hallescher FC', y2016='SC Preußen Münster', y2017='Bayer 04 Leverkusen', y2018='SV Sandhausen', y2019='SV Sandhausen', y2020='Bayer 04 Leverkusen', y2021='Bayer 04 Leverkusen', y2022='Bayer 04 Leverkusen')
    bundesliga.add_node(51, name='Muhammed Damar', club='TSG 1899 Hoffenheim', y2013='FC Hertha 03 Zehlendorf', y2014='FC Hertha 03 Zehlendorf', y2015='Hertha BSC Berlin', y2016='Hertha BSC Berlin', y2017='Hertha BSC Berlin', y2018='Hertha BSC Berlin', y2019='FC Hertha 03 Zehlendorf', y2020='Eintracht Frankfurt', y2021='Eintracht Frankfurt', y2022='TSG 1899 Hoffenheim')
    bundesliga.add_node(52, name='John Anthony Brooks', club='TSG 1899 Hoffenheim', y2013='Hertha BSC Berlin', y2014='Hertha BSC Berlin', y2015='Hertha BSC Berlin', y2016='Hertha BSC Berlin', y2017='VfL Wolfsburg', y2018='VfL Wolfsburg', y2019='VfL Wolfsburg', y2020='VfL Wolfsburg', y2021='VfL Wolfsburg', y2022='SL Benfica Lissabon')
    bundesliga.add_node(53, name='Patrik Schick', club='Bayer 04 Leverkusen', y2013='AC Sparta Prag', y2014='AC Sparta Prag', y2015='Bohemians Prag', y2016='AC Sparta Prag', y2017='AS Rom', y2018='AS Rom', y2019='RB Leipzig', y2020='RB Leipzig', y2021='Bayer 04 Leverkusen', y2022='Bayer 04 Leverkusen')
    bundesliga.add_node(54, name='Christopher Lenz', club='Eintracht Frankfurt', y2013='Borussia Mönchengladbach', y2014='Borussia Mönchengladbach', y2015='Borussia Mönchengladbach', y2016='1. FC Union Berlin', y2017='Holstein Kiel', y2018='1. FC Union Berlin', y2019='1. FC Union Berlin', y2020='1. FC Union Berlin', y2021='Eintracht Frankfurt', y2022='Eintracht Frankfurt')
    bundesliga.add_node(55, name='Sebastian Polter', club='FC Schalke 04', y2013='1. FSV Mainz 05', y2014='1. FC Union Berlin', y2015='Queens Park Rangers', y2016='Queens Park Rangers', y2017='1. FC Union Berlin', y2018='1. FC Union Berlin', y2019='1. FC Union Berlin', y2020='VfL Bochum', y2021='VfL Bochum', y2022='FC Schalke 04')
    bundesliga.add_node(56, name='Jakob Busk', club='1. FC Union Berlin', y2013='FC Kopenhagen', y2014='AC Horsens', y2015='Sandefjord Fotball', y2016='FC Kopenhagen', y2017='1. FC Union Berlin', y2018='1. FC Union Berlin', y2019='1. FC Union Berlin', y2020='1. FC Union Berlin', y2021='1. FC Union Berlin', y2022='1. FC Union Berlin')
    bundesliga.add_node(57, name='Conor Noß', club='Borussia Mönchengladbach', y2013='Borussia Mönchengladbach', y2014='Borussia Mönchengladbach', y2015='Borussia Mönchengladbach', y2016='Borussia Mönchengladbach', y2017='Borussia Mönchengladbach', y2018='Borussia Mönchengladbach', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')
    bundesliga.add_node(58, name='Lukáš Ambros ', club='VfL Wolfsburg', y2015='1. FC Slovacko', y2016='1. FC Slovacko', y2017='SK Slavia Prag', y2018='SK Slavia Prag', y2019='SK Slavia Prag', y2020='VfL Wolfsburg', y2021='VfL Wolfsburg', y2022='VfL Wolfsburg')
    bundesliga.add_node(59, name='Mërgim Berisha  ', club='FC Augsburg',y2016='FC Liefering', y2017='FC Red Bull Salzburg', y2018='1. FC Magdeburg', y2019='FC Red Bull Salzburg', y2020='FC Red Bull Salzburg', y2021='Fenerbahce SK Istanbul', y2022='FC Augsburg')
    bundesliga.add_node(60, name='Erhan Mašović nd ', club='VfL Bochum', y2013='FK Cukaricki', y2014='FK Cukaricki', y2015='FK Cukaricki', y2016='FK Cukaricki', y2017='Club Brügge KV', y2018='FK AS Trencin', y2019='Club Brügge KV', y2020='VfL Bochum', y2021='VfL Bochum', y2022='VfL Bochum')

    bundesliga.add_node(61, name='Tim Skarke', club='FC Schalke 04', y2013='1. FC Heidenheim', y2014='1. FC Heidenheim', y2015='1. FC Heidenheim', y2016='1. FC Heidenheim', y2017='1. FC Heidenheim', y2018='1. FC Heidenheim', y2019='SV Darmstadt 98', y2020='SV Darmstadt 98', y2021='SV Darmstadt 98', y2022='1. FC Union Berlin')

    bundesliga.add_node(62, name='Philipp Förster ', club='VfL Bochum', y2013='VfB Stuttgart', y2014='SV Waldhof Mannheim', y2015='SV Waldhof Mannheim', y2016='SV Waldhof Mannheim', y2017='1. FC Nürnberg', y2018='SV Sandhausen', y2019='VfB Stuttgart', y2020='VfB Stuttgart', y2021='VfB Stuttgart', y2022='VfL Bochum')

    bundesliga.add_node(63, name='Jonas Hofmann ', club='Borussia Mönchengladbach', y2013='Borussia Dortmund', y2014='1. FSV Mainz 05', y2015='Borussia Dortmund', y2016='Borussia Mönchengladbach', y2017='Borussia Mönchengladbach', y2018='Borussia Mönchengladbach', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')

    bundesliga.add_node(64, name='Ko Itakura', club='Borussia Mönchengladbach', y2013='Kawasaki Frontale', y2014='Kawasaki Frontale', y2015='Kawasaki Frontale', y2016='Kawasaki Frontale', y2017='Kawasaki Frontale', y2018='Vegalta Sendai', y2019='Kawasaki Frontale', y2020='Manchester City FC', y2021='Manchester City FC', y2022='Borussia Mönchengladbach')

    bundesliga.add_node(65, name='Daniel Klein', club='FC Augsburg', y2013='FC Astoria Walldorf', y2014='TSG 1899 Hoffenheim', y2015='TSG 1899 Hoffenheim', y2016='TSG 1899 Hoffenheim', y2017='TSG 1899 Hoffenheim', y2018='TSG 1899 Hoffenheim', y2019='TSG 1899 Hoffenheim', y2020='TSG 1899 Hoffenheim', y2021='FC Augsburg', y2022='FC Augsburg')

    bundesliga.add_node(66, name='Frederik Rønnow', club='1. FC Union Berlin', y2013='Esbjerg FB', y2014='AC Horsens', y2015='Bröndby IF', y2016='Bröndby IF', y2017='Bröndby IF', y2018='Eintracht Frankfurt', y2019='Eintracht Frankfurt', y2020='Eintracht Frankfurt', y2021='1. FC Union Berlin', y2022='1. FC Union Berlin')

    bundesliga.add_node(67, name='Chidera Ejuke', club='Hertha Berlin', y2016='Gombe United FC', y2017='Valerenga IF Oslo', y2018='Valerenga IF Oslo', y2019='SC Heerenveen', y2020='PFC CSKA Moskau', y2021='PFC CSKA Moskau', y2022='Hertha BSC Berlin')

    bundesliga.add_node(68, name='Sven Michel', club='1. FC Union Berlin', y2013='Borussia Mönchengladbach', y2014='FC Energie Cottbus', y2015='FC Energie Cottbus', y2016='SC Paderborn 07', y2017='SC Paderborn 07', y2018='SC Paderborn 07', y2019='SC Paderborn 07', y2020='SC Paderborn 07', y2021='SC Paderborn 07', y2022='1. FC Union Berlin')

    bundesliga.add_node(69, name='Alassane Pléa', club='Borussia Mönchengladbach', y2013='Olympique Lyonnais', y2014='AJ Auxerre' , y2015='OGC Nice', y2016='OGC Nice', y2017='OGC Nice', y2018='Borussia Mönchengladbach', y2019='Borussia Mönchengladbach', y2020='Borussia Mönchengladbach', y2021='Borussia Mönchengladbach', y2022='Borussia Mönchengladbach')

    bundesliga.add_node(70, name='Waldemar Anton', club = 'VfB Stuttgart', y2013='Hannover 96', y2014='Hannover 96', y2015='Hannover 96', y2016='Hannover 96', y2017='Hannover 96', y2018='Hannover 96', y2019='Hannover 96', y2020='VfB Stuttgart', y2021='VfB Stuttgart', y2022='VfB Stuttgart')

    bundesliga.add_node(71, name='Angeliño', club='TSG 1899 Hoffenheim', y2013='Manchester City FC', y2014='Manchester City FC', y2015='New York City FC', y2016='Manchester City FC', y2017='RCD Mallorca', y2018='PSV Eindhoven', y2019='Manchester City FC', y2020='RB Leipzig', y2021='RB Leipzig', y2022='TSG 1899 Hoffenheim')

    bundesliga.add_node(72, name='Niclas Füllkrug', club='SV Werder Bremen', y2013='SpVgg Greuther Fürth', y2014='1. FC Nürnberg', y2015='1. FC Nürnberg', y2016='Hannover 96', y2017='Hannover 96', y2018='Hannover 96', y2019='SV Werder Bremen', y2020='SV Werder Bremen', y2021='SV Werder Bremen', y2022='SV Werder Bremen')

    bundesliga.add_node(73, name='Antonis Aidonis', club='VfB Stuttgart', y2013='TSG 1899 Hoffenheim', y2014='TSG 1899 Hoffenheim', y2015='TSG 1899 Hoffenheim', y2016='TSG 1899 Hoffenheim', y2017='TSG 1899 Hoffenheim', y2018='VfB Stuttgart', y2019='VfB Stuttgart', y2020='VfB Stuttgart', y2021='SG Dynamo Dresden', y2022='VfB Stuttgart')

    bundesliga.add_node(74, name='Adam Hložek', club='Bayer 04 Leverkusen', y2013='FC Ivancice', y2014='AC Sparta Prag', y2015='AC Sparta Prag', y2016='AC Sparta Prag', y2017='AC Sparta Prag', y2018='AC Sparta Prag', y2019='AC Sparta Prag', y2020='AC Sparta Prag', y2021='AC Sparta Prag', y2022='Bayer 04 Leverkusen')

    bundesliga.add_node(75, name='Jonas Wind', club='VfL Wolfsburg', y2013='FC Kopenhagen', y2014='FC Kopenhagen', y2015='FC Kopenhagen', y2016='FC Kopenhagen', y2017='FC Kopenhagen', y2018='FC Kopenhagen', y2019='FC Kopenhagen', y2020='FC Kopenhagen', y2021='FC Kopenhagen', y2022='FC Kopenhagen')

    bundesliga.add_node(76, name='Jonas Hector', club='1. FC Köln', y2013='1. FC Köln', y2014='1. FC Köln', y2015='1. FC Köln', y2016='1. FC Köln', y2017='1. FC Köln', y2018='1. FC Köln', y2019='1. FC Köln', y2020='1. FC Köln', y2021='1. FC Köln', y2022='1. FC Köln')

    bundesliga.add_node(77, name='Tjark Ernst', club='Hertha BSC Berlin', y2013='VfL Bochum', y2014='VfL Bochum', y2015='VfL Bochum', y2016='VfL Bochum', y2017='VfL Bochum', y2018='VfL Bochum', y2019='VfL Bochum', y2020='VfL Bochum', y2021='VfL Bochum', y2022='Hertha BSC Berlin')

    bundesliga.add_node(78, name='Yussuf Poulsen', club='RB Leipzig', y2013='RB Leipzig', y2014='RB Leipzig', y2015='RB Leipzig', y2016='RB Leipzig', y2017='RB Leipzig', y2018='RB Leipzig', y2019='RB Leipzig', y2020='RB Leipzig', y2021='RB Leipzig', y2022='RB Leipzig')

    bundesliga.add_node(79, name='Sven Ulreich', club='FC Bayern München', y2013='VfB Stuttgart', y2014='VfB Stuttgart', y2015='FC Bayern München', y2016='FC Bayern München', y2017='FC Bayern München', y2018='FC Bayern München', y2019='FC Bayern München', y2020='Hamburger SV', y2021='FC Bayern München', y2022='FC Bayern München')

    bundesliga.add_node(80, name='Miloš Veljković', club='SV Werder Bremen')
    bundesliga.add_node(81, name='Semir Telalovic', club='Borussia Mönchengladbach', y2017='SSV Ehingen-Süd', y2018='SSV Ehingen-Süd', y2019='SSV Ehingen-Süd', y2020='SSV Ehingen-Süd', y2021='FV Illertissen', y2022='Borussia Mönchengladbach')

    bundesliga.add_node(82, name='Alexander Meyer', club='Borussia Dortmund', y2013='TSV Havelse', y2014='TSV Havelse', y2015='TSV Havelse', y2016='FC Energie Cottbus', y2017='VfB Stuttgart', y2018='VfB Stuttgart', y2019='SSV Jahn Regensburg', y2020='SSV Jahn Regensburg', y2021='SSV Jahn Regensburg', y2022='Borussia Dortmund')

    bundesliga.add_node(83, name='Ibrahima Cissé', club='FC Schalke 04', y2018='LB Chateauroux', y2019='KAA Gent', y2020='KAA Gent', y2021='KAA Gent', y2022='FC Schalke 04')

    bundesliga.add_node(84, name='Atakan Karazor', club='VfB Stuttgart', y2013='VfL Bochum', y2014='VfL Bochum', y2015='Borussia Dortmund', y2016='Borussia Dortmund', y2017='Holstein Kiel', y2018='Holstein Kiel', y2019='VfB Stuttgart', y2020='VfB Stuttgart', y2021='VfB Stuttgart', y2022='VfB Stuttgart')

    bundesliga.add_node(85, name='Kevin Akpoguma', club='TSG 1899 Hoffenheim', y2013='TSG 1899 Hoffenheim', y2014='TSG 1899 Hoffenheim', y2015='Fortuna Düsseldorf', y2016='Fortuna Düsseldorf', y2017='TSG 1899 Hoffenheim', y2018='TSG 1899 Hoffenheim', y2019='Hannover 96', y2020='TSG 1899 Hoffenheim', y2021='TSG 1899 Hoffenheim', y2022='TSG 1899 Hoffenheim')

    bundesliga.add_node(86, name='Andreas Hanche-Olsen', club='1. FSV Mainz 05', y2013='Stabaek IF', y2014='Stabaek IF', y2015='Stabaek IF', y2016='Stabaek IF', y2017='Stabaek IF', y2018='Stabaek IF', y2019='Stabaek IF', y2020='KAA Gent', y2021='KAA Gent', y2022='KAA Gent')

    bundesliga.add_node(87, name='Felix Uduokhai', club='FC Augsburg', y2013='TSV 1860 München', y2014='TSV 1860 München', y2015='TSV 1860 München', y2016='TSV 1860 München', y2017='TSV 1860 München', y2018='TSV 1860 München', y2019='FC Augsburg', y2020='FC Augsburg', y2021='FC Augsburg', y2022='FC Augsburg')

    bundesliga.add_node(88, name='Saidy Janko', club='VfL Bochum', y2013='Manchester United FC', y2014='Manchester United FC', y2015='Bolton Wanderers FC', y2016='Barnsley FC', y2017='AS Saint Etienne', y2018='FC Porto', y2019='Berner SC Young Boys', y2020='FC Porto', y2021='VfL Bochum', y2022='VfL Bochum')

    bundesliga.add_node(89, name='Linton Maina', club='1. FC Köln', y2013='SV Empor Berlin', y2014='Hannover 96', y2015='Hannover 96', y2016='Hannover 96', y2017='Hannover 96', y2018='Hannover 96', y2019='Hannover 96', y2020='Hannover 96', y2021='Hannover 96', y2022='1. FC Köln')

    bundesliga.add_node(90, name='Kevin Möhwald', club='1. FC Union Berlin', y2013= 'FC Rot-Weiß Erfurt', y2014= 'FC Rot-Weiß Erfurt', y2015='1. FC Nürnberg', y2016='1. FC Nürnberg', y2017='1. FC Nürnberg', y2018='SV Werder Bremen', y2019='SV Werder Bremen', y2020='SV Werder Bremen', y2021='1. FC Union Berlin', y2022='1. FC Union Berlin')


    bundesliga.add_node(91, name='Benno Schmitz', club='1. FC Köln', y2013='FC Bayern München', y2014='FC Red Bull Salzburg', y2015='FC Red Bull Salzburg', y2016='RB Leipzig', y2017='RB Leipzig', y2018='1. FC Köln', y2019='1. FC Köln', y2020='1. FC Köln', y2021='1. FC Köln', y2022='1. FC Köln')
    """
    bundesliga.add_node(92, name='Mario Götze', club='Eintracht Frankfurt', y2013=, y2014=, y2015=, y2016=, y2017=, y2018=, y2019=, y2020=, y2021=, y2022=)
                        'SC Ronsberg 1995-1998, ',
                        'FC Eintracht Hombruch 1998-2001, ', 'Borussia Dortmund 2001-2013, ',
                        'FC Bayern München 2013-2016, ', 'Borussia Dortmund 2016-2020, ',
                        'PSV Eindhoven 2020-2022 and has played ', 'Eintracht Frankfurt since 2022'
    bundesliga.add_node(93, name='Amine Adli', club='Bayer 04 Leverkusen', y2013=, y2014=, y2015=, y2016=, y2017=, y2018=, y2019=, y2020=, y2021=, y2022=)
                        'AS Pezenas Tourbes 2007-2012, ',
                        'AS Beziers 2012-2015, ', 'Toulouse FC 2015-2021 and has played ',
                        'Bayer 04 Leverkusen since 2021'
    bundesliga.add_node(94, name='Stanley Nsoki', club='TSG 1899 Hoffenheim', y2013=, y2014=, y2015=, y2016=, y2017=, y2018=, y2019=, y2020=, y2021=, y2022=)
                        'US Roissy-en-Brie 2007-2014, ',
                        'Paris Saint-Germain FC 2014-2019, ', 'OGC Nice 2019-2021, ',
                        'Club Brügge KV 2021-2022 and has played ', 'TSG Hoffenheim since 2022'
    bundesliga.add_node(95, name='Gabriel Marušić', club='FC Bayern München')
    bundesliga.add_node(96, name='Robert Skov', club='TSG 1899 Hoffenheim', y2013=, y2014=, y2015=, y2016=, y2017=, y2018=, y2019=, y2020=, y2021=, y2022=)
                        'Silkeborg IF 2012-2018, ',
                        'FC Kopenhagen 2018-2019 and has played ', 'TSG Hoffenheim since 2019'
    bundesliga.add_node(97, name='André Hahn', club='FC Augsburg', y2013=, y2014=, y2015=, y2016=, y2017=, y2018=, y2019=, y2020=, y2021=, y2022=)
                        'TSV Otterndorf 1862 1997-2003, ',
                        'Leher Turnerschaft 2003-2005, ', 'Rot-Weiss Cuxhaven 2005-2007, ',
                        'FC Bremerhaven 2008-2008, ', 'Hamburger SV 2008-2010, ', 'FC Oberneuland 2010-2011, ',
                        'TuS Koblenz 2011-2011, ', 'Kickers Offenbach 2011-2013, ', 'FC Augsburg 2013-2014, ',
                        " Borussia M'gladbach 2014-2017, ", 'Hamburger SV 2017-2018 and has played ',
                        'FC Augsburg since 2018'
    bundesliga.add_node(98, name='Matthijs de Ligt', club='FC Bayern München', y2013=, y2014=, y2015=, y2016=, y2017=, y2018=, y2019=, y2020=, y2021=, y2022=)
                        'FC Abcoude 2005-2009, ',
                        'Ajax Amsterdam 2009-2019, ', 'Juventus FC Turin 2019-2022 and has played ',
                        'FC Bayern München since 2022'
    bundesliga.add_node(99, name='Hiroki Ito', club='VfB Stuttgart', y2013=, y2014=, y2015=, y2016=, y2017=, y2018=, y2019=, y2020=, y2021=, y2022=)
                        'Jubilo Iwata 2015-2019, ',
                        'Nagoya Grampus Eight 2019-2020, ', 'Jubilo Iwata 2020-2021 and has played ',
                        'VfB Stuttgart since 2021'
    bundesliga.add_node(100, name='Moritz Broschinski', club='VfL Bochum', y2013=, y2014=, y2015=, y2016=, y2017=, y2018=, y2019=, y2020=, y2021=, y2022=)
                        'SV Hertha Finsterwalde 2005-2011, ',
                        'FSV Brieske/Senftenberg 2011-2012, ', 'FC Energie Cottbus 2012-2020, ',
                        'Borussia Dortmund 2020-2023, ', 'Borussia Dortmund II 2020-2023 and has played ',
                        'VfL Bochum 1848 since 2023'
    bundesliga.add_node(101, name='Noah Sarenren Bazee', club='FC Augsburg', 'JFC Allertal 2010-2011, ',
                        'TSV Havelse 2011-2013, ', 'Hannover 96 2013-2019 and has played ', 'FC Augsburg since 2019'
    bundesliga.add_node(102, name='Julian Eitschberger', club='Hertha Berlin', 'SC Staaken 2016-2017 and has played ',
                        'Hertha BSC since 2017'
    bundesliga.add_node(103, name='Arne Engels', club='FC Augsburg', 'KAA Gent 2014-2015, ',
                        'Club Brügge KV 2015-2023 and has played ', 'FC Augsburg since 2023'
    bundesliga.add_node(104, name='Dan-Axel Zagadou', club='VfB Stuttgart', 'US Creteil-Lusitanos 2006-2011, ',
                        'Paris Saint-Germain FC 2011-2017, ', 'Borussia Dortmund 2017-2022, ',
                        'Borussia Dortmund II 2017-2022 and has played ', 'VfB Stuttgart since 2022'
    bundesliga.add_node(105, name='David Čolina', club='FC Augsburg', 'NK Hrvatski Dragovoljac 2008-2009, ',
                        'GNK Dinamo Zagreb 2009-2018, ', 'AS Monaco FC 2018-2019, ',
                        'HNK Hajduk Split 2019-2023 and has played ', 'FC Augsburg since 2023'
    bundesliga.add_node(106, name='Cristian Gamboa', club='VfL Bochum', 'Municipal Liberia Mia 2006-2010, ',
                        'Fredrikstad FK 2010-2011, ', 'FC Kopenhagen 2011-2012, ', 'Rosenborg Trondheim 2012-2014, ',
                        'West Bromwich Albion FC 2014-2016, ', 'Celtic Glasgow FC 2016-2019 and has played ',
                        'VfL Bochum 1848 since 2019'
    bundesliga.add_node(107, name='Pavel Kadeřábek', club='TSG 1899 Hoffenheim', 'AC Sparta Prag 1999-2011, ',
                        'Viktoria Zizkov 2011-2011, ', 'AC Sparta Prag 2012-2015 and has played ',
                        'TSG Hoffenheim since 2015'
    bundesliga.add_node(108, name='Patrick Pentz', club='Bayer 04 Leverkusen', 'SV Bürmoos 2003-2006, ',
                        'FC Red Bull Salzburg 2006-2013, ', 'FK Austria Wien 2013-2022, ',
                        'Stade de Reims 2022-2023 and has played ', 'Bayer 04 Leverkusen since 2023'
    bundesliga.add_node(109, name='Yannic Stein', club='1. FC Union Berlin',
                        'FC Viktoria 1889 Berlin 2018-2019 and has played ', '1. FC Union Berlin since 2019'
    bundesliga.add_node(110, name='Anthony Jung', club='SV Werder Bremen', 'SV Wehen Wiesbaden 2004-2005, ',
                        'Eintracht Frankfurt 2005-2012, ', 'FSV Frankfurt 2012-2013, ', 'RB Leipzig 2013-2016, ',
                        'FC Ingolstadt 04 2016-2017, ', 'Bröndby IF 2017-2021, ',
                        'RB Leipzig 2017-2017 and has played ', 'SV Werder Bremen since 2021'
    bundesliga.add_node(111, name='Maximilian Brüll', club='Borussia Mönchengladbach'
    bundesliga.add_node(112, name='Márton Dárdai', club='Hertha Berlin', '1.FC Wilmersdorf 2011-2012 and has played ',
                        'Hertha BSC since 2012'
    bundesliga.add_node(113, name='Noussair Mazraoui', club='FC Bayern München', 'Alphense Boys 2004-2005, ',
                        'Ajax Amsterdam 2005-2022 and has played ', 'FC Bayern München since 2022'
    bundesliga.add_node(114, name='Dominik Szoboszlai', club='RB Leipzig', 'Videoton FC 2006-2007, ',
                        'Fönix Gold FC Fehervar 2007-2015, ', 'MTK Budapest 2015-2016, ', 'Videoton FC 2016-2017, ',
                        'FC Liefering 2017-2018, ', 'FC Red Bull Salzburg 2018-2020 and has played ',
                        'RB Leipzig since 2021'
    bundesliga.add_node(115, name='Timo Werner', club='RB Leipzig', 'TSV Steinhaldenfeld 2000-2002, ',
                        'VfB Stuttgart 2002-2016, ', 'RB Leipzig 2016-2020, ', 'Chelsea FC 2020-2022 and has played ',
                        'RB Leipzig since 2022'
    bundesliga.add_node(116, name='Lucas Höler', club='Sport-Club Freiburg', 'Hansa Schwanewede 1998-2008, ',
                        'Osterholz-Scharmbeck 2008-2011, ', 'Blumenthaler SV 2011-2013, ', 'VfB Oldenburg 2013-2014, ',
                        '1.FSV Mainz 05 II 2014-2016, ', 'SV Sandhausen 2016-2017, ',
                        'SC Freiburg since 2018 and has played ', 'SC Freiburg II since 2018'
    bundesliga.add_node(117, name='Manuel Mbom', club='SV Werder Bremen', 'Bovender SV 2006-2012, ',
                        'JFV Göttingen 2012-2013, ', 'SV Werder Bremen 2013-2019, ',
                        'KFC Uerdingen 05 2019-2020 and has played ', 'SV Werder Bremen since 2020'
    bundesliga.add_node(118, name='Maximilian Arnold', club='VfL Wolfsburg', 'BSV Strehla 2000-2003, ',
                        'SC Riesa 2003-2006, ', 'SG Dynamo Dresden 2006-2009 and has played ',
                        'VfL Wolfsburg since 2009'
    bundesliga.add_node(119, name='Daley Sinkgraven', club='Bayer 04 Leverkusen', 'MVV Alcides 2002-2008, ',
                        'SC Heerenveen 2008-2015, ', 'Ajax Amsterdam 2015-2019 and has played ',
                        'Bayer 04 Leverkusen since 2019'
    bundesliga.add_node(120, name='Elvis Rexhbecaj', club='FC Augsburg', 'Brandenburger SC Süd 05 2009-2010, ',
                        'VfL Wolfsburg 2010-2020, ', '1. FC Köln 2020-2021, ', 'VfL Wolfsburg 2021-2021, ',
                        'VfL Bochum 1848 2021-2022, ', 'VfL Wolfsburg 2022-2022 and has played ',
                        'FC Augsburg since 2022'
    bundesliga.add_node(121, name='Steffen Tigges', club='1. FC Köln', 'TuS Glane 2002-2011, ',
                        'VfL Osnabrück 2011-2019, ', 'Borussia Dortmund 2019-2022, ',
                        'Borussia Dortmund II 2019-2022 and has played ', '1. FC Köln since 2022'
    bundesliga.add_node(122, name='Robert Kwasigroch', club='Hertha Berlin', 'Berliner SC 2016-2017 and has played ',
                        'Hertha BSC since 2017'
    bundesliga.add_node(123, name='Felix Passlack', club='Borussia Dortmund'
    bundesliga.add_node(124, name='Michael Zetterer', club='SV Werder Bremen', 'DJK Darching 2005-2006, ',
                        'SpVgg Unterhaching 2006-2015, ', 'SV Werder Bremen 2015-2019, ',
                        'Werder Bremen II 2015-2019, ', 'SK Austria Klagenfurt 2019-2019, ',
                        'PEC Zwolle 2019-2021 and has played ', 'SV Werder Bremen since 2021'
    bundesliga.add_node(125, name='Keke Topp', club='FC Schalke 04', 'TSV Gnarrenburg 2012-2013, ',
                        'SV Werder Bremen 2013-2021 and has played ', 'FC Schalke 04 since 2021'
    bundesliga.add_node(126, name='Raphaël Guerreiro', club='Borussia Dortmund', 'Le Blanc-Mesnil SF 1999-2005, ',
                        'I.N.F. Clairefontaine 2005-2008, ', 'SM Caen 2008-2013, ',
                        'FC Lorient 2013-2016 and has played ', 'Borussia Dortmund since 2016'
    bundesliga.add_node(127, name='Mitchel Bakker', club='Bayer 04 Leverkusen', 'FC Purmerend 2009-2010, ',
                        'Ajax Amsterdam 2010-2019, ', 'Paris Saint-Germain FC 2019-2021 and has played ',
                        'Bayer 04 Leverkusen since 2021'
    bundesliga.add_node(128, name='Michael Esser', club='VfL Bochum', 'SC Arminia Ickern 1992-1993, ',
                        'VfR Rauxel 08 1993-1997, ', 'VfB Habinghorst 1997-1999, ', 'VfL Bochum 1848 1999-2001, ',
                        'SpVgg Erkenschwick 2001-2004, ', 'VfB Habinghorst 2004-2006, ',
                        'SV Wacker Obercastrop 2006-2007, ', 'SV Sodingen 2007-2008, ', 'VfL Bochum 1848 2008-2015, ',
                        'SK Puntigamer Sturm Graz 2015-2016, ', 'SV Darmstadt 98 2016-2017, ',
                        'Hannover 96 2017-2020, ', 'TSG Hoffenheim 2020-2020, ',
                        'Hannover 96 2020-2021 and has played ', 'VfL Bochum 1848 since 2021'
    bundesliga.add_node(129, name='Finn Dahmen', club='1. FSV Mainz 05', 'FC 1934 Wiesbaden-Bierstadt 2002-2006, ',
                        'Eintracht Frankfurt 2006-2008 and has played ', '1. FSV Mainz 05 since 2008'
    bundesliga.add_node(130, name='Justin Diehl', club='1. FC Köln',
                        '1.Jugend-Fußball-Schule Köln 2010-2011 and has played ', '1. FC Köln since 2011'
    bundesliga.add_node(131, name='Dodi Lukébakio', club='Hertha Berlin', 'Brussels FC 2010-2011, ',
                        'RSC Anderlecht 2011-2016, ', 'Toulouse FC 2016-2017, ', 'Royal Charleroi SC 2017-2018, ',
                        'Wat', 'd FC 2018-2018, ', 'Fortuna Düsseldorf 2018-2019, ', 'Wat', 'd FC 2019-2019, ',
                        'Hertha BSC 2019-2021, ', 'VfL Wolfsburg 2021-2022 and has played ', 'Hertha BSC since 2022'
    bundesliga.add_node(132, name='Janis Blaswich', club='RB Leipzig', 'VfR Mehrhoog 1997-2006, ',
                        " Borussia M'gladbach 2006-2015, ", 'SG Dynamo Dresden 2015-2016, ',
                        " Borussia M'gladbach 2016-2017, ", 'FC Hansa Rostock 2017-2018, ',
                        'Heracles Almelo 2018-2022 and has played ', 'RB Leipzig since 2022'
    bundesliga.add_node(133, name='Kimberly Ezekwem', club='Sport-Club Freiburg'
    bundesliga.add_node(134, name='Umut Tohumcu', club='TSG 1899 Hoffenheim'
    bundesliga.add_node(135, name='Niklas Tauer', club='FC Schalke 04', 'SV Weisenau-Mainz 2010-2012, ',
                        '1. FSV Mainz 05 2012-2022, ', '1.FSV Mainz 05 U 19 2018-2020 and has played ',
                        'FC Schalke 04 since 2023'
    bundesliga.add_node(136, name='Matteo Bignetti', club='Eintracht Frankfurt', 'Grazer AK 2013-2016, ',
                        'SK Puntigamer Sturm Graz 2016-2020 and has played ', 'Eintracht Frankfurt since 2020'
    bundesliga.add_node(137, name='Timo Schlieck', club='RB Leipzig', 'SpVgg Oelde 2017-2018, ',
                        'DSC Arminia Bielefeld 2018-2018, ', 'Borussia Dortmund 2018-2021 and has played ',
                        'RB Leipzig since 2021'
    bundesliga.add_node(138, name='Robin Zentner  ', club='1. FSV Mainz 05', 'SpVgg Eltville 2001-2006, ',
                        '1. FSV Mainz 05 2006-2015, ', '1.FSV Mainz 05 II 2006-2015, ',
                        'Holstein Kiel 2015-2017 and has played ', '1. FSV Mainz 05 since 2017'
    bundesliga.add_node(139, name='Christopher Trimmel', club='1. FC Union Berlin', 'UFC Mannersdorf 1994-2006, ',
                        'ASK Horitschon-Unterpetersdorf 2006-2008, ', 'SK Rapid Wien 2008-2014 and has played ',
                        '1. FC Union Berlin since 2014'
    bundesliga.add_node(140, name='Tim Maciejewski', club='1. FC Union Berlin', 'SC Staaken 2005-2012, ',
                        'Hertha BSC 2012-2017, ', '1. FC Union Berlin 2017-2021, ',
                        'SK Austria Klagenfurt 2021-2022 and has played ', '1. FC Union Berlin since 2022'
    bundesliga.add_node(141, name='Jens Grahl', club='Eintracht Frankfurt', 'VfB Stuttgart 2004-2005, ',
                        'SV Stuttgarter Kickers 2005-2006, ', 'SpVgg Greuther Fürth 2006-2009, ',
                        'TSG Hoffenheim 2009-2011, ', 'SC Paderborn 07 2011-2012, ', 'TSG Hoffenheim 2012-2016, ',
                        'VfB Stuttgart 2016-2021 and has played ', 'Eintracht Frankfurt since 2021'
    bundesliga.add_node(142, name='Marvin Ducksch', club='SV Werder Bremen', 'BSV Fortuna Dortmund 1998-2002, ',
                        'Borussia Dortmund 2002-2014, ', 'Borussia Dortmund II 2002-2014, ',
                        'SC Paderborn 07 2014-2015, ', 'Borussia Dortmund 2015-2016, ', 'FC St. Pauli 2016-2017, ',
                        'Holstein Kiel 2017-2018, ', 'Fortuna Düsseldorf 2018-2019, ',
                        'Hannover 96 2019-2021 and has played ', 'SV Werder Bremen since 2021'
    bundesliga.add_node(143, name='Mathias Olesen', club='1. FC Köln'
    bundesliga.add_node(144, name='Christian Groß', club='SV Werder Bremen', 'BV Cloppenburg 2004-2005, ',
                        'VfL Osnabrück 2005-2006, ', 'Hamburger SV 2006-2011, ', 'Hamburger SV II 2006-2011, ',
                        'SV Babelsberg 03 2011-2013, ', 'Sportfreunde Lotte 2013-2014, ',
                        'VfL Osnabrück 2014-2018 and has played ', 'SV Werder Bremen since 2018'
    bundesliga.add_node(145, name='Wilfried Kanga', club='Hertha Berlin', 'FCM Garges-Les-Gonesse 2004-2007, ',
                        'FC Villepinte 2007-2009, ', 'Sevran Footbal Club 2009-2010, ',
                        'Paris Saint-Germain FC 2010-2016, ', 'US Creteil-Lusitanos 2016-2017, ',
                        'SCO Angers 2017-2020, ', 'Kayserispor K 2020-2021, ',
                        'Berner SC Young Boys 2021-2022 and has played ', 'Hertha BSC since 2022'
    bundesliga.add_node(146, name='Marcel Halstenberg', club='RB Leipzig', 'SV Germania Grasdorf 1998-1999, ',
                        'Hannover 96 1999-2011, ', 'Borussia Dortmund 2011-2013, ', 'Borussia Dortmund II 2011-2013, ',
                        'FC St. Pauli 2013-2015 and has played ', 'RB Leipzig since 2015'
    bundesliga.add_node(147, name='Jan Thielmann', club='1. FC Köln', 'SV Hetzerath 2014-2015, ',
                        'SV Eintracht Trier 2015-2017 and has played ', '1. FC Köln since 2017'
    bundesliga.add_node(148, name='Ihlas Bebou', club='TSG 1899 Hoffenheim', 'Garather SV 2004-2009, ',
                        'VfB Hilden 2009-2011, ', 'Fortuna Düsseldorf 2011-2017, ',
                        'Hannover 96 2017-2019 and has played ', 'TSG Hoffenheim since 2019'
    bundesliga.add_node(149, name='Anton Stach', club='1. FSV Mainz 05', 'Buchholzer FC 2001-2011, ',
                        'SV Werder Bremen 2011-2015, ', 'JFV Nordwest 2015-2016, ', 'VfL Osnabrück 2016-2017, ',
                        'SSV Jeddeloh II 2017-2018, ', 'VfL Wolfsburg 2018-2020, ',
                        'SpVgg Greuther Fürth 2020-2021 and has played ', '1. FSV Mainz 05 since 2021'
    bundesliga.add_node(150, name='Nelson Weiper', club='1. FSV Mainz 05. He has played ', '1. FSV Mainz 05 since 2012'
    bundesliga.add_node(151, name='Marvin Schwäbe', club='1. FC Köln', 'Kickers Offenbach 2008-2009, ',
                        'Eintracht Frankfurt 2009-2013, ', 'TSG Hoffenheim 2013-2015, ', 'VfL Osnabrück 2015-2016, ',
                        'SG Dynamo Dresden 2016-2018, ', 'Bröndby IF 2018-2021 and has played ', '1. FC Köln since 2021'
    bundesliga.add_node(152, name='Noah Atubolu', club='Sport-Club Freiburg'
    bundesliga.add_node(153, name='Maximilian Schmid', club='1. FC Köln', 'FSV Frankfurt 2015-2016, ',
                        '1. FSV Mainz 05 2016-2018 and has played ', '1. FC Köln since 2018'
    bundesliga.add_node(154, name='Mattias Svanberg', club='VfL Wolfsburg', 'IF Limhamn Bunkeflo 2008-2012, ',
                        'Malmö FF 2013-2018, ', 'Bologna FC 2018-2022 and has played ', 'VfL Wolfsburg since 2022'
    bundesliga.add_node(155, name='Tony Jantschke', club='Borussia Mönchengladbach',
                        'Hoyerswerdaer SV Einheit 1996-2001, ', 'FV Dresden Nord 2001-2006 and has played ',
                        " Borussia M'gladbach since 2006."
    bundesliga.add_node(156, name='Rodrigo Zalazar', club='FC Schalke 04', 'Albacete Balompie 2007-2015, ',
                        'Malaga CF 2015-2016, ', 'CD San Felix 2016-2017, ', 'Malaga CF 2017-2019, ',
                        'Eintracht Frankfurt 2019-2019, ', 'Korona Kielce 2019-2020, ',
                        'Eintracht Frankfurt 2020-2020, ', 'FC St. Pauli 2020-2021, ',
                        'Eintracht Frankfurt 2021-2021 and has played ', 'FC Schalke 04 since 2021'
    bundesliga.add_node(157, name='Joey Müller', club='FC Schalke 04', 'Gütersloher TV 2010-2011, ',
                        'DSC Arminia Bielefeld 2011-2019, ', 'Wuppertaler SV 2019-2021 and has played ',
                        'FC Schalke 04 since 2021'
    bundesliga.add_node(158, name='Christoph Kramer', club='Borussia Mönchengladbach', 'BV Gräfrath 1996-1999, ',
                        'Bayer 04 Leverkusen 1999-2006, ', 'Fortuna Düsseldorf 2006-2008, ',
                        'Bayer 04 Leverkusen 2008-2011, ', 'VfL Bochum 1848 2011-2013, ',
                        " Borussia M'gladbach 2013-2015, ", 'Bayer 04 Leverkusen 2015-2016 and has played ',
                        " Borussia M'gladbach since 2016."
    bundesliga.add_node(159, name='Diant Ramaj', club='Eintracht Frankfurt', 'VfB Stuttgart 2014-2015, ',
                        'SV Stuttgarter Kickers 2015-2018, ', '1. FC Heidenheim 1846 2018-2021, ',
                        '1.FC Heidenheim U 19 2018-2020 and has played ', 'Eintracht Frankfurt since 2021'
    bundesliga.add_node(160, name='Daichi Kamada', club='Eintracht Frankfurt', 'Gamba Osaka 2009-2012, ',
                        'Higashiyama High School 2012-2014, ', 'Sagan Tosu FC 2015-2017, ',
                        'Eintracht Frankfurt 2017-2018, ', 'Sint-Truidense VV 2018-2019 and has played ',
                        'Eintracht Frankfurt since 2019'
    bundesliga.add_node(161, name='Joshua Eze ', club='Bayer 04 Leverkusen'
    bundesliga.add_node(162, name='Sheraldo Becker', club='1. FC Union Berlin', 'Ajax Amsterdam 2004-2015, ',
                        'PEC Zwolle 2015-2016, ', 'Ajax Amsterdam 2016-2016, ',
                        'ADO Den Haag 2016-2019 and has played ', '1. FC Union Berlin since 2019'
    bundesliga.add_node(163, name='Daniel-Kofi Kyereh', club='Sport-Club Freiburg', 'SC Gitter 2007-2008, ',
                        'Eintracht Braunschweig 2008-2012, ', 'VfL Wolfsburg 2012-2014, ', 'TSV Havelse 2014-2018, ',
                        'SV Wehen Wiesbaden 2018-2020, ', 'FC St. Pauli 2020-2022, ',
                        'SC Freiburg since 2022 and has played ', 'SC Freiburg II since 2022'
    bundesliga.add_node(164, name='Justin Janitzek', club='FC Bayern München'
    bundesliga.add_node(165, name='Timo Horn', club='1. FC Köln', 'SC Rondorf 1999-2002 and has played ',
                        '1. FC Köln since 2002'
    bundesliga.add_node(166, name='Fabian Bredlow', club='VfB Stuttgart', 'Berliner FC Preussen 1998-2008, ',
                        'Lichtenrader BC 2008-2010, ', 'FC Hertha 03 Zehlendorf 2010-2012, ', 'RB Leipzig 2012-2014, ',
                        'FC Red Bull Salzburg 2014-2015, ', 'Hallescher FC 2015-2017, ',
                        '1. FC Nürnberg 2017-2019 and has played ', 'VfB Stuttgart since 2019'
    bundesliga.add_node(167, name='Konstantinos Stafylidis', club='VfL Bochum', 'PAOK FC Thessaloniki 2007-2013, ',
                        'Bayer 04 Leverkusen 2013-2014, ', 'Fulham FC 2014-2015, ', 'Bayer 04 Leverkusen 2015-2015, ',
                        'FC Augsburg 2015-2018, ', 'Stoke City FC 2018-2018, ', 'FC Augsburg 2018-2019, ',
                        'TSG Hoffenheim 2019-2021 and has played ', 'VfL Bochum 1848 since 2021'
    bundesliga.add_node(168, name='Marko Johansson', club='VfL Bochum', 'Malmö FF 2003-2017, ',
                        'Trelleborgs FF 2017-2018, ', 'Malmö FF 2018-2019, ', 'GAIS Göteborg 2019-2019, ',
                        'Malmö FF 2019-2020, ', 'Mjällby AIF 2020-2020, ', 'Malmö FF 2020-2021, ',
                        'Hamburger SV 2021-2022 and has played ', 'VfL Bochum 1848 since 2022'
    bundesliga.add_node(169, name='Andrej Kramarić', club='TSG 1899 Hoffenheim', 'GNK Dinamo Zagreb 1997-2012, ',
                        'NK Lokomotiva Zagreb 2012-2013, ', 'GNK Dinamo Zagreb 2013-2013, ', 'HNK Rijeka 2013-2015, ',
                        'Leicester City FC 2015-2016 and has played ', 'TSG Hoffenheim since 2016'
    bundesliga.add_node(170, name='Kevin Kampl ', club='RB Leipzig', 'VfB Solingen 1994-1997, ',
                        'Bayer 04 Leverkusen 1997-2010, ', 'SpVgg Greuther Fürth 2010-2010, ',
                        'Bayer 04 Leverkusen 2011-2011, ', 'VfL Osnabrück 2011-2012, ', 'VfR Aalen 2012-2012, ',
                        'FC Red Bull Salzburg 2012-2014, ', 'Borussia Dortmund 2015-2015, ',
                        'Bayer 04 Leverkusen 2015-2017 and has played ', 'RB Leipzig since 2017'
    bundesliga.add_node(171, name='Niko Gießelmann', club='1. FC Union Berlin', 'TSV Godshorn 1995-2005, ',
                        'SC Langenhagen 2005-2007, ', 'Hannover 96 2007-2013, ', 'SpVgg Greuther Fürth 2013-2017, ',
                        'Fortuna Düsseldorf 2017-2020 and has played ', '1. FC Union Berlin since 2020'
    bundesliga.add_node(172, name='Roland Sallai', club='Sport-Club Freiburg', 'Diosgyöri VTK 2003-2007, ',
                        'BFC Siofok 2007-2009, ', 'Videoton FC 2009-2014, ', 'Puskas Akademia FC 2014-2016, ',
                        'US Palermo 2016-2017, ', 'Puskas Akademia FC 2017-2017, ', 'APOEL FC Nicosia 2017-2018, ',
                        'SC Freiburg since 2018 and has played ', 'SC Freiburg II since 2022'
    bundesliga.add_node(173, name='Julian Weigl', club='Borussia Mönchengladbach', 'SV Ostermünchen 2001-2006, ',
                        'TSV 1860 Rosenheim 2006-2010, ', 'TSV 1860 München 2010-2015, ',
                        'Borussia Dortmund 2015-2020, ', 'SL Benfica Lissabon 2020-2022 and has played ',
                        " Borussia M'gladbach since 2022."
    bundesliga.add_node(174, name='Marcel Lotka', club='Borussia Dortmund', 'MSV Duisburg 2013-2014, ',
                        'FC Schalke 04 2014-2015, ', 'Rot-Weiss Essen 2015-2017, ', 'Bayer 04 Leverkusen 2017-2020, ',
                        'Bayer 04 Leverkusen U-Team 2019-2020, ', 'Hertha BSC 2020-2022, ',
                        'Borussia Dortmund since 2022 and has played ', 'Borussia Dortmund II since 2022'
    bundesliga.add_node(175, name='Matthias Köbbing', club='1. FC Köln', 'TuS Koblenz 2008-2010, ',
                        '1. FSV Mainz 05 2010-2012, ', 'TSG Hoffenheim 2012-2017, ',
                        '1. FC Heidenheim 1846 2017-2019, ', 'FC Homburg 2019-2020 and has played ',
                        '1. FC Köln since 2020'
    bundesliga.add_node(176, name='Dejan Ljubicic', club='1. FC Köln', 'Favoritner AC 2004-2006, ',
                        'SK Rapid Wien 2006-2017, ', 'SC Wiener Neustadt 2017-2017, ',
                        'SK Rapid Wien 2017-2021 and has played ', '1. FC Köln since 2021'
    bundesliga.add_node(177, name='Serge Gnabry', club='FC Bayern München', 'TSV Weissach 1999-2000, ',
                        'GSV Hemmingen 2000-2001, ', 'TSF Ditzingen 2001-2003, ', 'Sportvg Feuerbach 2003-2005, ',
                        'SV Stuttgarter Kickers 2005-2006, ', 'VfB Stuttgart 2006-2011, ', 'Arsenal FC 2011-2015, ',
                        'West Bromwich Albion FC 2015-2016, ', 'Arsenal FC 2016-2016, ', 'SV Werder Bremen 2016-2017, ',
                        'FC Bayern München 2017-2017, ', 'TSG Hoffenheim 2017-2018 and has played ',
                        'FC Bayern München since 2018'
    bundesliga.add_node(178, name='Rafał Gikiewicz', club='FC Augsburg', 'KKS Warmia Olsztyn 1993-2000, ',
                        'KS Stomil Olsztyn 2000-2001, ', 'UKS Tempo Olsztyn 2001-2004, ',
                        'DKS Dobre Miasto 2004-2005, ', 'Sokol Ostroda 2006-2006, ', 'KS Drweca NML 2006-2007, ',
                        'KS Wigry Suwalki 2007-2008, ', 'SSA Jagiellonia Bialystok 2008-2010, ',
                        'KS Stomil Olsztyn 2010-2010, ', 'SSA Jagiellonia Bialystok 2011-2011, ',
                        'WKS Slask Wroclaw 2011-2014, ', 'Eintracht Braunschweig 2014-2016, ',
                        'SC Freiburg 2016-2018, ', '1. FC Union Berlin 2018-2020 and has played ',
                        'FC Augsburg since 2020'
    bundesliga.add_node(179, name='Tom Rothe', club='Borussia Dortmund', 'Rendsburger TSV 2010-2012, ',
                        'Büdelsdorfer TSV 2012-2016, ', 'SC Nienstedten 2016-2018, ', 'FC St. Pauli 2018-2021, ',
                        'Borussia Dortmund since 2021 and has played ', 'Borussia Dortmund II since 2021'
    bundesliga.add_node(180, name='Patrick Osterhage', club='VfL Bochum', 'SC Marklohe 2010-2011, ',
                        'SV Werder Bremen 2011-2017, ', 'Borussia Dortmund 2017-2021 and has played ',
                        'VfL Bochum 1848 since 2021'
    bundesliga.add_node(181, name='Lasse Rieß', club='1. FSV Mainz 05'
    bundesliga.add_node(182, name='Manuel Gulde', club='Sport-Club Freiburg', 'VfL Neckarau 2006-2007, ',
                        'TSG Hoffenheim 2007-2012, ', 'SC Paderborn 07 2012-2013, ',
                        'Karlsruher SC 2013-2016 and has played ', 'SC Freiburg since 2016'
    bundesliga.add_node(183, name='Eder Balanta', club='FC Schalke 04', 'CA River Plate 2011-2016, ',
                        'FC Basel 2016-2019, ', 'Club Brügge KV 2019-2023 and has played ', 'FC Schalke 04 since 2023'
    bundesliga.add_node(184, name='Sanoussy Ba', club='RB Leipzig', 'SpVgg Bayern Hof 2015-2016 and has played ',
                        'RB Leipzig since 2016'
    bundesliga.add_node(185, name='Jeff Chabot', club='1. FC Köln', 'Eintracht Frankfurt 2011-2014, ',
                        'RB Leipzig 2014-2017, ', 'Sparta Rotterdam 2017-2018, ', 'FC Groningen 2018-2019, ',
                        'Sampdoria Genua 2019-2020, ', 'Spezia Calcio 2020-2021, ',
                        'Sampdoria Genua 2021-2022 and has played ', '1. FC Köln since 2022'
    bundesliga.add_node(186, name='Kiliann Sildillia', club='Sport-Club Freiburg', 'AS Montigny-les-Metz 2008-2009, ',
                        'APM Du FC Metz 2009-2010, ', 'FC Metz 2010-2020, ', 'SC Freiburg since 2020 and has played ',
                        'SC Freiburg II since 2020'
    bundesliga.add_node(187, name='Kristijan Jakić', club='Eintracht Frankfurt', 'NK Mracaj Runovic 2004-2009, ',
                        'NK Imotski 2009-2013, ', 'RNK Split 2013-2017, ', 'NK Lokomotiva Zagreb 2017-2018, ',
                        'NK Istra 1961 2018-2018, ', 'NK Lokomotiva Zagreb 2018-2020, ',
                        'GNK Dinamo Zagreb 2020-2021 and has played ', 'Eintracht Frankfurt since 2021'
    bundesliga.add_node(188, name='Florian Wirtz', club='Bayer 04 Leverkusen'
    bundesliga.add_node(189, name='Koen Casteels', club='VfL Wolfsburg', 'KAC Betekom 1996-2002, ',
                        'KRC Genk 2002-2011, ', 'TSG Hoffenheim 2011-2015, ',
                        'SV Werder Bremen 2015-2015 and has played ', 'VfL Wolfsburg since 2015'
    bundesliga.add_node(190, name='Gerrit Holtmann', club='VfL Bochum', 'OSC Bremerhaven 2009-2010, ',
                        'SV Werder Bremen 2010-2013, ', 'JFV Bremerhaven 2013-2013, ', 'OSC Bremerhaven 2013-2014, ',
                        'Eintracht Braunschweig 2014-2016, ', '1. FSV Mainz 05 2016-2019, ',
                        '1.FSV Mainz 05 II 2016-2019, ', 'SC Paderborn 07 2019-2020, ',
                        '1. FSV Mainz 05 2020-2020 and has played ', 'VfL Bochum 1848 since 2020'
    bundesliga.add_node(191, name='Mark Flekken', club='Sport-Club Freiburg', 'Roda JC Kerkrade 2008-2009, ',
                        'Alemannia Aachen 2009-2013, ', 'SpVgg Greuther Fürth 2013-2016, ',
                        'MSV Duisburg 2016-2018 and has played ', 'SC Freiburg since 2018'
    bundesliga.add_node(192, name='Mohammed Tolba', club='VfL Bochum', 'Essener SG 99 2010-2015 and has played ',
                        'VfL Bochum 1848 since 2015'
    bundesliga.add_node(193, name='Diogo Leite', club='1. FC Union Berlin', 'Leixoes SC Matosinhos 2007-2008, ',
                        'FC Porto 2008-2014, ', 'Padroense FC 2014-2014, ', 'FC Porto 2015-2021, ',
                        'Sporting Braga 2021-2022, ', 'FC Porto 2022-2022 and has played ',
                        '1. FC Union Berlin since 2022'
    bundesliga.add_node(194, name='Felix Nmecha', club='VfL Wolfsburg', 'Manchester City FC 2008-2021 and has played ',
                        'VfL Wolfsburg since 2021'
    bundesliga.add_node(195, name='Eduardo Dos Santos Haesler', club='SV Werder Bremen', 'FC Hennef 05 2009-2010, ',
                        " Borussia M'gladbach 2010-2012, ", 'Rot-Weiss Essen 2012-2013, ',
                        '1.FC Mönchengladbach 2013-2014, ', 'MSV Duisburg 2014-2018, ', 'SV Werder Bremen 2018-2021, ',
                        'FC Nordsjaelland 2021-2022 and has played ', 'SV Werder Bremen since 2022'
    bundesliga.add_node(196, name='Vincenzo Grifo', club='Sport-Club Freiburg', '1.CfR P', 'zheim 1996-2006, ',
                        'Germania Brötzingen 2006-2010, ', '1.CfR P', 'zheim 2010-2011, ', 'Karlsruher SC 2011-2012, ',
                        'TSG Hoffenheim 2012-2014, ', 'SG Dynamo Dresden 2014-2014, ', 'FSV Frankfurt 2014-2015, ',
                        'SC Freiburg 2015-2017, ', " Borussia M'gladbach 2017-2018, ", 'TSG Hoffenheim 2018-2019, ',
                        'SC Freiburg 2019-2019, ', 'TSG Hoffenheim 2019-2019 and has played ', 'SC Freiburg since 2019'
    bundesliga.add_node(197, name='Jeremie Frimpong', club='Bayer 04 Leverkusen', 'Manchester City FC 2010-2019, ',
                        'Celtic Glasgow FC 2019-2021 and has played ', 'Bayer 04 Leverkusen since 2021'
    bundesliga.add_node(198, name='Kevin Trapp', club='Eintracht Frankfurt', 'FC Brotdorf 1997-2000, ',
                        'SSV Bachem 1926 2000-2003, ', 'SV Mettlach 2003-2005, ', '1. FC Kaiserslautern 2005-2012, ',
                        'Eintracht Frankfurt 2012-2015, ', 'Paris Saint-Germain FC 2015-2018, ',
                        'Eintracht Frankfurt 2018-2019, ', 'Paris Saint-Germain FC 2019-2019 and has played ',
                        'Eintracht Frankfurt since 2019'
    bundesliga.add_node(199, name='Georg Strauch', club='1. FC Köln', 'FC Hennef 05 2013-2014 and has played ',
                        '1. FC Köln since 2014'
    bundesliga.add_node(200, name='Florian Schock', club='VfB Stuttgart'
    bundesliga.add_node(201, name='Kilian Fischer', club='VfL Wolfsburg', 'TuS Bad Aibling 2014-2015, ',
                        'TSV 1860 München 2015-2019, ', 'Türkgücü München 2019-2021, ',
                        '1. FC Nürnberg 2021-2022 and has played ', 'VfL Wolfsburg since 2022'
    bundesliga.add_node(202, name='Wooyeong Jeong', club='Sport-Club Freiburg', 'Incheon United FC 2010-2017, ',
                        'FC Bayern München 2018-2019, ', 'SC Freiburg 2019-2020, ', 'FC Bayern München 2020-2020, ',
                        'FC Bayern München II 2020-2020 and has played ', 'SC Freiburg since 2020'
    bundesliga.add_node(203, name='Jonas Omlin', club='Borussia Mönchengladbach', 'FC Luzern 2011-2012, ',
                        'SC Kriens 2012-2014, ', 'FC Luzern 2014-2015, ', 'FC Le Mont LS 2015-2016, ',
                        'FC Luzern 2016-2018, ', 'FC Basel 2018-2020, ',
                        'Montpellier Herault SC 2020-2023 and has played ', " Borussia M'gladbach since 2023."
    bundesliga.add_node(204, name='Evan Ndicka', club='Eintracht Frankfurt', 'FCA Paris 19eme 2006-2009, ',
                        'FC Solitaires Paris-Est 2009-2012, ', 'AJ Auxerre 2012-2018 and has played ',
                        'Eintracht Frankfurt since 2018'
    bundesliga.add_node(205, name='Gregor Kobel', club='Borussia Dortmund', 'FC Seefeld Zürich 2004-2005, ',
                        'Grasshopper Zürich 2005-2014, ', 'TSG Hoffenheim 2014-2019, ', 'FC Augsburg 2019-2019, ',
                        'VfB Stuttgart 2019-2020, ', 'TSG Hoffenheim 2020-2020, ',
                        'VfB Stuttgart 2020-2021 and has played ', 'Borussia Dortmund since 2021'
    bundesliga.add_node(206, name='Oliver Baumann', club='TSG 1899 Hoffenheim', 'FC Bad Krozingen 1996-2000, ',
                        'SC Freiburg 2000-2014 and has played ', 'TSG Hoffenheim since 2014'
    bundesliga.add_node(207, name='Paul Wanner', club='FC Bayern München',
                        'FV 1893 Ravensburg 2017-2018 and has played ', 'FC Bayern München since 2018'
    bundesliga.add_node(208, name='Odilon Kossounou', club='Bayer 04 Leverkusen', 'ASEC Mimosas 2018-2019, ',
                        'Hammarby IF 2019-2019, ', 'Club Brügge KV 2019-2021 and has played ',
                        'Bayer 04 Leverkusen since 2021'
    bundesliga.add_node(209, name='Sardar Azmoun', club='Bayer 04 Leverkusen', 'Oghab Gonbad 2004-2008, ',
                        'Shamoushak Gorgan 2008-2009, ', 'Etka Gorgan FC 2009-2010, ', 'Sepahan Isfahan FC 2010-2012, ',
                        'FC Rubin Kazan 2013-2015, ', 'FK Rostov 2015-2017, ', 'FC Rubin Kazan 2017-2019, ',
                        'FC Zenit St. Petersburg 2019-2022 and has played ', 'Bayer 04 Leverkusen since 2022'
    bundesliga.add_node(210, name='Luca Netz', club='Borussia Mönchengladbach', 'FSV Bernau 2009-2010, ',
                        'Hertha BSC 2010-2021 and has played ', " Borussia M'gladbach since 2021."
    bundesliga.add_node(211, name='Stefan Bell', club='1. FSV Mainz 05', 'JSG Rieden/Wehr/Volkesfeld 1995-2006, ',
                        'TuS Mayen 2006-2007, ', '1. FSV Mainz 05 2007-2010, ', 'TSV 1860 München 2010-2011, ',
                        'Eintracht Frankfurt 2011-2012 and has played ', '1. FSV Mainz 05 since 2012'
    bundesliga.add_node(212, name='Josha Vagnoman', club='VfB Stuttgart', 'SC Poppenbüttel 2009-2009, ',
                        'Hummelsbütteler SV 2009-2010, ', 'Hamburger SV 2010-2022 and has played ',
                        'VfB Stuttgart since 2022'
    bundesliga.add_node(213, name='Eduardo Quaresma', club='TSG 1899 Hoffenheim', 'Sporting CP Lissabon 2012-2021, ',
                        'CD Tondela 2021-2022, ', 'Sporting CP Lissabon 2022-2022 and has played ',
                        'TSG Hoffenheim since 2022'
    bundesliga.add_node(214, name='Robert Gumny', club='FC Augsburg', 'KKS Lech Posen 2013-2017, ',
                        'TS Podbeskidzie Bielsko-Biala 2017-2017, ', 'KKS Lech Posen 2017-2020 and has played ',
                        'FC Augsburg since 2020'
    bundesliga.add_node(215, name='Niklas Schmidt', club='SV Werder Bremen', 'SpVgg Olympia Kassel 2006-2007, ',
                        'OSC Vellmar 2007-2011, ', 'FC Rot-Weiß Erfurt 2011-2012, ', 'SV Werder Bremen 2012-2018, ',
                        'Werder Bremen II 2012-2018, ', 'SV Wehen Wiesbaden 2018-2019, ',
                        'VfL Osnabrück 2019-2021 and has played ', 'SV Werder Bremen since 2021'
    bundesliga.add_node(216, name='Sebastiaan Bornauw', club='VfL Wolfsburg', 'FCV Dender EH 2008-2009, ',
                        'RSC Anderlecht 2009-2019, ', '1. FC Köln 2019-2021 and has played ', 'VfL Wolfsburg since 2021'
    bundesliga.add_node(217, name='Tiago Tomás', club='VfB Stuttgart', 'GS Carcavelos 2010-2012, ',
                        'Colegio Marista 2012-2013, ', 'GD Estoril Praia 2013-2014, ',
                        'Sporting CP Lissabon 2014-2022 and has played ', 'VfB Stuttgart since 2022'
    bundesliga.add_node(218, name='Salih Özcan', club='Borussia Dortmund', 'SC West Köln 2006-2007, ',
                        '1. FC Köln 2007-2019, ', 'Holstein Kiel 2019-2020, ', '1. FC Köln 2020-2022 and has played ',
                        'Borussia Dortmund since 2022'
    bundesliga.add_node(219, name='Niklas Klinger', club='VfL Wolfsburg',
                        'SV Reislingen-Neuhaus 2002-2003 and has played ', 'VfL Wolfsburg since 2003'
    bundesliga.add_node(220, name='Felix Agu', club='SV Werder Bremen', 'Osnabrücker SC 2009-2010, ',
                        'VfL Osnabrück 2010-2020 and has played ', 'SV Werder Bremen since 2020'
    bundesliga.add_node(221, name='Silvère Ganvoula', club='VfL Bochum', 'Patronage Sainte-Anne 2009-2014, ',
                        'Raja Casablanca 2014-2015, ', 'Elazigspor K 2015-2016, ', 'KVC Westerlo 2016-2017, ',
                        'RSC Anderlecht 2017-2017, ', 'KV Mechelen 2017-2018, ', 'RSC Anderlecht 2018-2018, ',
                        'VfL Bochum 1848 2018-2022, ', 'Cercle Brügge KSV 2022-2022 and has played ',
                        'VfL Bochum 1848 since 2022'
    bundesliga.add_node(222, name='Keven Schlotterbeck', club='VfL Bochum', 'SV Stuttgarter Kickers 2011-2012, ',
                        'TSG Backnang 2012-2014, ', 'VfL Kirchheim/Teck 2014-2015, ', 'TSG Backnang 2015-2017, ',
                        'SC Freiburg 2017-2019, ', '1. FC Union Berlin 2019-2020, ', 'SC Freiburg 2020-2023, ',
                        'SC Freiburg II 2020-2023 and has played ', 'VfL Bochum 1848 since 2023'
    bundesliga.add_node(223, name='Thomas Müller', club='FC Bayern München'
    bundesliga.add_node(224, name='Leonardo Bittencourt', club='SV Werder Bremen', 'FC Energie Cottbus 1999-2012, ',
                        'Borussia Dortmund 2012-2013, ', 'Hannover 96 2013-2015, ', '1. FC Köln 2015-2018, ',
                        'TSG Hoffenheim 2018-2019 and has played ', 'SV Werder Bremen since 2019'
    bundesliga.add_node(225, name='Dimitrios Limnios', club='1. FC Köln', 'Niki Volos FC 2002-2012, ',
                        'Atromitos FC 2012-2017, ', 'PAOK FC Thessaloniki 2017-2020, ', '1. FC Köln 2020-2021, ',
                        'FC Twente Enschede 2021-2022 and has played ', '1. FC Köln since 2022'
    bundesliga.add_node(226, name='Kaito Mizuta', club='1. FSV Mainz 05', 'Maebashi Ikuei High School 2018-2019, ',
                        'SV Straelen 2019-2021 and has played ', '1. FSV Mainz 05 since 2021'
    bundesliga.add_node(227, name='Nico Schlotterbeck', club='Borussia Dortmund', 'SG Weinstadt 2006-2007, ',
                        'SV Stuttgarter Kickers 2007-2014, ', 'VfR Aalen 2014-2015, ', 'Karlsruher SC 2015-2017, ',
                        'SC Freiburg 2017-2020, ', '1. FC Union Berlin 2020-2021, ',
                        'SC Freiburg 2021-2022 and has played ', 'Borussia Dortmund since 2022'
    bundesliga.add_node(228, name='Florian Dimmer', club='Borussia Mönchengladbach. He has played ',
                        " Borussia M'gladbach since 2019."
    bundesliga.add_node(229, name='Kerem Demirbay', club='Bayer 04 Leverkusen', 'FC Schalke 04 1999-2007, ',
                        'Borussia Dortmund 2007-2008, ', 'SG Wattenscheid 09 2008-2011, ',
                        'Borussia Dortmund 2011-2013, ', 'Borussia Dortmund II 2011-2013, ', 'Hamburger SV 2013-2014, ',
                        '1. FC Kaiserslautern 2014-2015, ', 'Hamburger SV 2015-2015, ',
                        'Fortuna Düsseldorf 2015-2016, ', 'Hamburger SV 2016-2016, ',
                        'TSG Hoffenheim 2016-2019 and has played ', 'Bayer 04 Leverkusen since 2019'
    bundesliga.add_node(230, name='Ryan Gravenberch', club='FC Bayern München', 'AVV Zeeburgia 2009-2010, ',
                        'Ajax Amsterdam 2010-2022 and has played ', 'FC Bayern München since 2022'
    bundesliga.add_node(231, name='Sebastian Rode', club='Eintracht Frankfurt', 'SKV Hähnlein 1994-1998, ',
                        'Alsbach FC 1998-2002, ', 'SC Viktoria Griesheim 2002-2004, ', 'SV Darmstadt 98 2004-2005, ',
                        'Kickers Offenbach 2005-2010, ', 'Eintracht Frankfurt 2010-2014, ',
                        'FC Bayern München 2014-2016, ', 'Borussia Dortmund 2016-2018, ',
                        'Eintracht Frankfurt 2019-2019, ', 'Borussia Dortmund 2019-2019 and has played ',
                        'Eintracht Frankfurt since 2019'
    bundesliga.add_node(232, name='Enzo Millot', club='VfB Stuttgart', 'Etoile de Brou 2008-2010, ',
                        " C'Chartres Footbal 2010-2015, ", 'FC Drouais 2015-2017, ',
                        'AS Monaco FC 2017-2021 and has played ', 'VfB Stuttgart since 2021'
    bundesliga.add_node(233, name='Munas Dabbur', club='TSG 1899 Hoffenheim', 'Maccabi Ahi Nazareth FC 2003-2010, ',
                        'Maccabi Tel Aviv FC 2010-2014, ', 'Grasshopper Zürich 2014-2016, ',
                        'FC Red Bull Salzburg 2016-2017, ', 'Grasshopper Zürich 2017-2017, ',
                        'FC Red Bull Salzburg 2017-2019, ', 'Sevilla FC 2019-2020 and has played ',
                        'TSG Hoffenheim since 2020'
    bundesliga.add_node(234, name='Ruwen Werthmüller', club='Hertha Berlin',
                        'SV Empor Berlin 2009-2010 and has played ', 'Hertha BSC since 2010'
    bundesliga.add_node(235, name='Edmond Tapsoba', club='Bayer 04 Leverkusen', 'Salitas FC 2014-2015, ',
                        'US Ouagadougou 2015-2017, ', 'Leixoes SC Matosinhos 2017-2018, ',
                        'Vitoria SC Guimaraes 2018-2020 and has played ', 'Bayer 04 Leverkusen since 2020'
    bundesliga.add_node(236, name='Ansgar Knauff', club='Eintracht Frankfurt', 'SVG Göttingen 07 2006-2015, ',
                        'Hannover 96 2015-2016, ', 'Borussia Dortmund 2016-2022, ',
                        'Borussia Dortmund II 2016-2022 and has played ', 'Eintracht Frankfurt since 2022'
    bundesliga.add_node(237, name='Silas Katompa', club='VfB Stuttgart', 'La Grace 2012-2014, ',
                        'AC Matonge 2014-2015, ', 'FC MK Etancheite 2015-2017, ', 'Olympique Ales 2017-2018, ',
                        'Paris FC 2018-2019 and has played ', 'VfB Stuttgart since 2019'
    bundesliga.add_node(238, name='Ellyes Skhiri', club='1. FC Köln', 'Gallia Club Lunel 1999-2010, ',
                        'Montpellier Herault SC 2010-2019 and has played ', '1. FC Köln since 2019'
    bundesliga.add_node(239, name='Mats Hummels', club='Borussia Dortmund', 'FC Bayern München 1995-2008, ',
                        'FC Bayern München II 1995-2008, ', 'Borussia Dortmund 2008-2016, ',
                        'FC Bayern München 2016-2019 and has played ', 'Borussia Dortmund since 2019'
    bundesliga.add_node(240, name='Rafael Borré', club='Eintracht Frankfurt', 'Deportivo Cali 2013-2016, ',
                        'Atletico Madrid 2016-2016, ', 'Villarreal CF 2016-2017, ', 'Atletico Madrid 2017-2017, ',
                        'CA River Plate 2017-2021 and has played ', 'Eintracht Frankfurt since 2021'
    bundesliga.add_node(241, name='Maya Yoshida', club='FC Schalke 04', 'Nagoya Grampus Eight 2001-2009, ',
                        'VVV Venlo 2010-2012, ', 'Southampton FC 2012-2020, ',
                        'Sampdoria Genua 2020-2022 and has played ', 'FC Schalke 04 since 2022'
    bundesliga.add_node(242, name='Jonathan Tah', club='Bayer 04 Leverkusen', 'FC Altona 93 2000-2009, ',
                        'SC Concordia Hamburg 2009-2009, ', 'Hamburger SV 2009-2014, ',
                        'Fortuna Düsseldorf 2014-2015, ', 'Hamburger SV 2015-2015 and has played ',
                        'Bayer 04 Leverkusen since 2015'
    bundesliga.add_node(243, name='Abdou Diallo', club='RB Leipzig', 'AS Monaco FC 2011-2015, ',
                        'SV Zulte-Waregem 2015-2016, ', 'AS Monaco FC 2016-2017, ', '1. FSV Mainz 05 2017-2018, ',
                        'Borussia Dortmund 2018-2019, ', 'Paris Saint-Germain FC 2019-2022 and has played ',
                        'RB Leipzig since 2022'
    bundesliga.add_node(244, name='Lucas Tousart', club='Hertha Berlin', 'US Pays Rignacois 2004-2010, ',
                        'Rodez Aveyron Football 2010-2013, ', 'Valenciennes FC 2013-2015, ',
                        'Olympique Lyonnais 2015-2020 and has played ', 'Hertha BSC since 2020'
    bundesliga.add_node(245, name='Jesper Lindström', club='Eintracht Frankfurt', 'Taastrup B.70 2003-2006, ',
                        'BSI fodbold 2007-2007, ', 'Vallensbaek IF 2007-2012, ', 'Bröndby IF 2012-2021 and has played ',
                        'Eintracht Frankfurt since 2021'
    bundesliga.add_node(246, name='Denis Huseinbašić', club='1. FC Köln', 'SpVgg Erbach 2009-2011, ',
                        'SV Darmstadt 98 2011-2013, ', 'Eintracht Frankfurt 2013-2018, ',
                        'Kickers Offenbach 2018-2022, ', 'Kickers Offenbach U 19 2018-2020 and has played ',
                        '1. FC Köln since 2022'
    bundesliga.add_node(247, name='Stefan Lainer', club='Borussia Mönchengladbach', 'SV Seekirchen 2000-2006, ',
                        'FC Red Bull Salzburg 2006-2011, ', 'SV Grödig 2011-2012, ', 'FC Liefering 2012-2014, ',
                        'SV Guntamatic Ried 2014-2015, ', 'FC Red Bull Salzburg 2015-2019 and has played ',
                        " Borussia M'gladbach since 2019."
    bundesliga.add_node(248, name='Nathan Ngoumou', club='Borussia Mönchengladbach',
                        'Toulouse FC 2006-2022 and has played ', " Borussia M'gladbach since 2022."
    bundesliga.add_node(249, name='Alexander Schwolow', club='FC Schalke 04', 'SV Allendorf/Berghausen 2004-2005, ',
                        'SV Wehen Wiesbaden 2005-2008, ', 'SC Freiburg 2008-2014, ',
                        'DSC Arminia Bielefeld 2014-2015, ', 'SC Freiburg 2015-2020, ',
                        'Hertha BSC 2020-2022 and has played ', 'FC Schalke 04 since 2022'
    bundesliga.add_node(250, name='Noah Mbamba', club='Bayer 04 Leverkusen', 'FC Vilvoorde 2014-2016, ',
                        'KV Woluwe-Zaventem 2016-2018, ', 'KRC Genk 2018-2020, ',
                        'Club Brügge KV 2020-2023 and has played ', 'Bayer 04 Leverkusen since 2023'
    bundesliga.add_node(251, name='Karim Bellarabi', club='Bayer 04 Leverkusen', 'FC Huchting 1997-1998, ',
                        'SV Werder Bremen 1998-2004, ', 'FC Oberneuland 2004-2008, ',
                        'Eintracht Braunschweig 2008-2011, ', 'Bayer 04 Leverkusen 2011-2013, ',
                        'Eintracht Braunschweig 2013-2014 and has played ', 'Bayer 04 Leverkusen since 2014'
    bundesliga.add_node(252, name='Daley Blind', club='FC Bayern München', 'Amsterdamsche FC 1995-1998, ',
                        'Ajax Amsterdam 1998-2010, ', 'FC Groningen 2010-2010, ', 'Ajax Amsterdam 2010-2014, ',
                        'Manchester United FC 2014-2018, ', 'Ajax Amsterdam 2018-2023 and has played ',
                        'FC Bayern München since 2023'
    bundesliga.add_node(253, name='Brajan Gruda', club='1. FSV Mainz 05', 'FC Speyer 09 2010-2015, ',
                        'Karlsruher SC 2015-2018 and has played ', '1. FSV Mainz 05 since 2018'
    bundesliga.add_node(254, name='Joe Scally', club='Borussia Mönchengladbach',
                        'New York City FC 2015-2020 and has played ', " Borussia M'gladbach since 2021."
    bundesliga.add_node(255, name='Joško Gvardiol', club='RB Leipzig', 'NK Tresnjevka Zagreb 2009-2010, ',
                        'GNK Dinamo Zagreb 2010-2021, ', 'GNK Dinamo Zagreb U 19 2019-2020 and has played ',
                        'RB Leipzig since 2021'
    bundesliga.add_node(256, name='Eric Martel', club='1. FC Köln', 'SSV Jahn Regensburg 2015-2017, ',
                        'RB Leipzig 2017-2021, ', 'FK Austria Wien 2021-2022 and has played ', '1. FC Köln since 2022'
    bundesliga.add_node(257, name='Micky van de Ven', club='VfL Wolfsburg', 'WSV 1930 Wormer 2012-2013, ',
                        'FC Volendam 2013-2021 and has played ', 'VfL Wolfsburg since 2021'
    bundesliga.add_node(258, name='Lukáš Hrádecký', club='Bayer 04 Leverkusen', 'Turun Pallokerho 1996-2000, ',
                        'FC TPS Turku 2001-2008, ', 'Abo IFK 2008-2008, ', 'Esbjerg fB 2009-2013, ',
                        'Bröndby IF 2013-2015, ', 'Eintracht Frankfurt 2015-2018 and has played ',
                        'Bayer 04 Leverkusen since 2018'
    bundesliga.add_node(259, name='Joao Cancelo', club='FC Bayern München', 'FC Barreirense 2002-2007, ',
                        'SL Benfica Lissabon 2007-2014, ', 'Valencia CF 2014-2017, ', 'Inter Mailand 2017-2018, ',
                        'Juventus FC Turin 2018-2019, ', 'Manchester City FC 2019-2023 and has played ',
                        'FC Bayern München since 2023'
    bundesliga.add_node(260, name='Miloš Pantović', club='1. FC Union Berlin', 'FC Rot-Weiß Oberföhring 2006-2007, ',
                        'FC Bayern München 2007-2018, ', 'VfL Bochum 1848 2018-2022 and has played ',
                        '1. FC Union Berlin since 2022'
    bundesliga.add_node(261, name='Nicolas Cozza', club='VfL Wolfsburg', 'FC Pays Viganais Aigoual 2005-2008, ',
                        'US Basses Cevennes 2008-2010, ', 'Montpellier Herault SC 2010-2023 and has played ',
                        'VfL Wolfsburg since 2023'
    bundesliga.add_node(262, name='Paxten Aaronson', club='Eintracht Frankfurt',
                        'Philadelphia Union 2015-2022 and has played ', 'Eintracht Frankfurt since 2023'
    bundesliga.add_node(263, name='Nathanaël Mbuku', club='FC Augsburg', 'US Ris Orangis 2012-2014, ',
                        'US Lusitanos Saint-Maur 2014-2016, ', 'Football Club Fleury 91 2016-2017, ',
                        'Stade de Reims 2017-2023 and has played ', 'FC Augsburg since 2023'
    bundesliga.add_node(264, name='Kevin Stöger', club='VfL Bochum', 'ATSV Steyr 1996-2007, ',
                        'SV Guntamatic Ried 2007-2009, ', 'VfB Stuttgart 2009-2013, ', 'VfB Stuttgart II 2009-2013, ',
                        '1. FC Kaiserslautern 2013-2015, ', 'VfB Stuttgart 2015-2015, ', 'SC Paderborn 07 2015-2016, ',
                        'VfL Bochum 1848 2016-2018, ', 'Fortuna Düsseldorf 2018-2020, ',
                        '1. FSV Mainz 05 2020-2022 and has played ', 'VfL Bochum 1848 since 2022'
    bundesliga.add_node(265, name='Marcus Ingvartsen', club='1. FSV Mainz 05', 'FC Nordsjaelland 2012-2017, ',
                        'KRC Genk 2017-2019, ', '1. FC Union Berlin 2019-2021 and has played ',
                        '1. FSV Mainz 05 since 2021'
    bundesliga.add_node(266, name='Manuel Riemann', club='VfL Bochum', 'TSV 1860 Rosenheim 2002-2003, ',
                        'SV Wacker Burghausen 2003-2010, ', 'VfL Osnabrück 2010-2013, ',
                        'SV Sandhausen 2013-2015 and has played ', 'VfL Bochum 1848 since 2015'
    bundesliga.add_node(267, name='Yannik Keitel', club='Sport-Club Freiburg', 'SV Breisach 2010-2011 and has played ',
                        'SC Freiburg since 2011'
    bundesliga.add_node(268, name='Agustín Rogel', club='Hertha Berlin', 'Club Nacional Montevideo 2015-2018, ',
                        'Krylya Sovetov Samara 2018-2019, ', 'Toulouse FC 2019-2021, ',
                        'Club Estudiantes de la Plata 2021-2022 and has played ', 'Hertha BSC since 2022'
    bundesliga.add_node(269, name='Florian Niederlechner', club='Hertha Berlin', 'SV Hohenlinden 2001-2002, ',
                        'TSV 1860 München 2002-2006, ', 'TSV 1877 Ebersberg 2006-2008, ',
                        'FC Falke Markt Schwaben 2008-2010, ', 'FC Ismaning 2010-2011, ',
                        'SpVgg Unterhaching 2011-2013, ', '1. FC Heidenheim 1846 2013-2015, ',
                        '1. FSV Mainz 05 2015-2016, ', 'SC Freiburg 2016-2019, ',
                        'FC Augsburg 2019-2023 and has played ', 'Hertha BSC since 2023'
    bundesliga.add_node(270, name='Marco Pašalić', club='Borussia Dortmund', 'TSG Hoffenheim 2015-2016, ',
                        'Karlsruher SC 2016-2019, ', 'VfB Stuttgart 2019-2021, ',
                        'Borussia Dortmund since 2021 and has played ', 'Borussia Dortmund II since 2021'
    bundesliga.add_node(271, name='Julian Ryerson', club='Borussia Dortmund', 'Lyngdal IL 2012-2013, ',
                        'Viking Stavanger 2013-2018, ', '1. FC Union Berlin 2018-2023 and has played ',
                        'Borussia Dortmund since 2023'
    bundesliga.add_node(272, name='David Raum', club='RB Leipzig', 'TuSpo Nürnberg 2002-2006, ',
                        'SpVgg Greuther Fürth 2006-2021, ', 'TSG Hoffenheim 2021-2022 and has played ',
                        'RB Leipzig since 2022'
    bundesliga.add_node(273, name='Arijon Ibrahimović ', club='FC Bayern München'
    bundesliga.add_node(274, name='Jens Stage', club='SV Werder Bremen', 'IF Lyseng Fodbold 2012-2013, ',
                        'Brabrand IF 2013-2016, ', 'Aarhus GF 2016-2019, ', 'FC Kopenhagen 2019-2022 and has played ',
                        'SV Werder Bremen since 2022'
    bundesliga.add_node(275, name='Josué Mbila', club='FC Augsburg', 'TSV 1860 München 2010-2010, ',
                        'SpVgg Unterhaching 2011-2014 and has played ', 'FC Augsburg since 2014'
    bundesliga.add_node(276, name='Robin Knoche', club='1. FC Union Berlin', 'TSV Germania Lamme 1996-2002, ',
                        'SV Olympia Braunschweig 2002-2005, ', 'VfL Wolfsburg 2005-2020 and has played ',
                        '1. FC Union Berlin since 2020'
    bundesliga.add_node(277, name='Oscar Fraulo', club='Borussia Mönchengladbach', 'Odense KS 2010-2017, ',
                        'FC Midtjylland 2017-2022 and has played ', " Borussia M'gladbach since 2022."
    bundesliga.add_node(278, name='Paul Jaeckel', club='1. FC Union Berlin', 'Eisenhüttenstädter FC Stahl 2003-2011, ',
                        'FC Energie Cottbus 2011-2014, ', 'VfL Wolfsburg 2014-2018, ',
                        'SpVgg Greuther Fürth 2018-2021 and has played ', '1. FC Union Berlin since 2021'
    bundesliga.add_node(279, name='Mitchell Weiser', club='SV Werder Bremen', 'TV Eintracht Veltenhof 2000-2005, ',
                        '1. FC Köln 2005-2012, ', 'FC Bayern München 2012-2013, ', '1. FC Kaiserslautern 2013-2013, ',
                        'FC Bayern München 2013-2015, ', 'Hertha BSC 2015-2018, ', 'Bayer 04 Leverkusen 2018-2021, ',
                        'SV Werder Bremen 2021-2022, ', 'Bayer 04 Leverkusen 2022-2022 and has played ',
                        'SV Werder Bremen since 2022'
    bundesliga.add_node(280, name='Tolga Cigerci', club='Hertha Berlin', 'SV Phiesewarden 1997-2000, ',
                        'TSV Arminia Vöhrum 2000-2005, ', 'VfL Wolfsburg 2005-2012, ',
                        " Borussia M'gladbach 2012-2013, ", 'VfL Wolfsburg 2013-2013, ', 'Hertha BSC 2013-2016, ',
                        'Galatasaray SK Istanbul 2016-2018, ', 'Fenerbahce SK Istanbul 2018-2021, ',
                        'Istanbul Basaksehir 2021-2022, ', 'MKE Ankaragücü SK 2022-2023 and has played ',
                        'Hertha BSC since 2023'
    bundesliga.add_node(281, name='Fisnik Asllani', club='TSG 1899 Hoffenheim', 'Berliner FC Dynamo 2008-2016, ',
                        '1. FC Union Berlin 2016-2020 and has played ', 'TSG Hoffenheim since 2020'
    bundesliga.add_node(282, name='Dominik Kohr', club='1. FSV Mainz 05', 'TuS Issel 2000-2008, ',
                        'Bayer 04 Leverkusen 2008-2014, ', 'FC Augsburg 2014-2017, ', 'Bayer 04 Leverkusen 2017-2019, ',
                        'Eintracht Frankfurt 2019-2021 and has played ', '1. FSV Mainz 05 since 2021'
    bundesliga.add_node(283, name='Marc-Oliver Kempf', club='Hertha Berlin', 'TSV Dorn-Assenheim 1998-2005, ',
                        'SV Bruchenbrücken 2005-2006, ', 'JSG Bad Nauheim 2006-2007, ',
                        'Eintracht Frankfurt 2007-2014, ', 'SC Freiburg 2014-2018, ',
                        'VfB Stuttgart 2018-2022 and has played ', 'Hertha BSC since 2022'
    bundesliga.add_node(284, name='Christopher Nkunku', club='RB Leipzig', 'AS Marolles 2003-2009, ',
                        'RCP Fontainebleau 2009-2010, ', 'Paris Saint-Germain FC 2010-2019 and has played ',
                        'RB Leipzig since 2019'
    bundesliga.add_node(285, name='Joshua Schwirten', club='1. FC Köln'
    bundesliga.add_node(286, name='Julien Duranville', club='Borussia Dortmund',
                        'RSC Anderlecht 2012-2023 and has played ', 'Borussia Dortmund since 2023'
    bundesliga.add_node(287, name='Kouadio Koné', club='Borussia Mönchengladbach', 'Villeneuve-la-Garenne 2007-2012, ',
                        'Paris FC 2012-2015, ', 'AC de Boulogne-Billancourt 2015-2016, ',
                        'Toulouse FC 2016-2021 and has played ', " Borussia M'gladbach since 2021."
    bundesliga.add_node(288, name='Alou Kuol', 'VfB Stuttgart', 'Goulburn Valley Suns FC 2014-2019, ',
                        'Central Coast Mariners FC 2019-2021, ', 'VfB Stuttgart 2021-2022, ',
                        'SV Sandhausen 2022-2022 and has played ', 'VfB Stuttgart since 2022'
    bundesliga.add_node(289, name='Jan Schroeder', club='Eintracht Frankfurt'
    bundesliga.add_node(290, name='Ramy Bensebaini', club='Borussia Mönchengladbach', 'CS Constantine 2005-2007, ',
                        'Paradou AC 2007-2014, ', 'Lierse SK 2014-2015, ', 'Montpellier Herault SC 2015-2016, ',
                        'Stade Rennais FC 2016-2019 and has played ', " Borussia M'gladbach since 2019."
    bundesliga.add_node(291, name='Jacob Bruun Larsen', club='TSG 1899 Hoffenheim', 'Lyngby BK 2013-2015, ',
                        'Borussia Dortmund 2015-2018, ', 'VfB Stuttgart 2018-2018, ', 'Borussia Dortmund 2018-2020, ',
                        'TSG Hoffenheim 2020-2021, ', 'RSC Anderlecht 2021-2021 and has played ',
                        'TSG Hoffenheim since 2021'
    bundesliga.add_node(292, name='Aljoscha Kemlein', club='1. FC Union Berlin. He has played ',
                        '1. FC Union Berlin since 2015'
    bundesliga.add_node(293, name='Ilia Gruev', club='SV Werder Bremen', 'FC Rot-Weiß Erfurt 2006-2015 and has played ',
                        'SV Werder Bremen since 2015'
    bundesliga.add_node(294, name='Donyell Malen', club='Borussia Dortmund', 'VV Succes 2004-2005, ',
                        'HVV Hollandia 2005-2008, ', 'Ajax Amsterdam 2008-2015, ', 'Arsenal FC 2015-2017, ',
                        'PSV Eindhoven 2017-2021 and has played ', 'Borussia Dortmund since 2021'
    bundesliga.add_node(295, name='Daniel Caligiuri', club='FC Augsburg', 'BSV 07 Schwenningen 1995-2001, ',
                        'SV Zimmern 2001-2005, ', 'SC Freiburg 2005-2013, ', 'VfL Wolfsburg 2013-2017, ',
                        'FC Schalke 04 2017-2020 and has played ', 'FC Augsburg since 2020'
    bundesliga.add_node(296, name='Marco Friedl', club='SV Werder Bremen'
    bundesliga.add_node(297, name='Marcel Wenig', club='Eintracht Frankfurt', '1. FC Nürnberg 2016-2017, ',
                        'FC Bayern München 2017-2022, ', 'FC Bayern München U 17 2019-2020 and has played ',
                        'Eintracht Frankfurt since 2022'
    bundesliga.add_node(298, name='Delano Burgzorg', club='1. FSV Mainz 05', 'AVV Zeeburgia 2014-2015, ',
                        'De Graafschap 2015-2019, ', 'Spezia Calcio 2019-2020, ',
                        'Heracles Almelo 2020-2022 and has played ', '1. FSV Mainz 05 since 2022'
    bundesliga.add_node(299, name='Amos Pieper', club='SV Werder Bremen', 'FC Nordkirchen 2002-2009, ',
                        'SC Union Lüdinghausen 2009-2010, ', 'Borussia Dortmund 2010-2019, ',
                        'DSC Arminia Bielefeld 2019-2022 and has played ', 'SV Werder Bremen since 2022'
    bundesliga.add_node(300, name='Mattis Hoppe', club='VfB Stuttgart'
    bundesliga.add_node(301, name='Ralf Fährmann', club='FC Schalke 04', 'VfB Chemnitz 1995-1998, ',
                        'Chemnitzer FC 1998-2003, ', 'FC Schalke 04 2003-2009, ', 'Eintracht Frankfurt 2009-2011, ',
                        'FC Schalke 04 2011-2019, ', 'Norwich City FC 2019-2020, ',
                        'SK Brann Bergen 2020-2020 and has played ', 'FC Schalke 04 since 2020'
    bundesliga.add_node(302, name='Emre Can', club='Borussia Dortmund', 'SV Blau-Gelb Frankfurt 2000-2006, ',
                        'Eintracht Frankfurt 2006-2009, ', 'FC Bayern München 2009-2013, ',
                        'Bayer 04 Leverkusen 2013-2014, ', 'Liverpool FC 2014-2018, ',
                        'Juventus FC Turin 2018-2020 and has played ', 'Borussia Dortmund since 2020'
    bundesliga.add_node(303, name='Ermedin Demirović', club='FC Augsburg', 'Hamburger SV 2004-2014, ',
                        'RB Leipzig 2014-2017, ', 'Deportivo Alaves 2017-2018, ', 'FC Sochaux 2018-2019, ',
                        'UD Almeria 2019-2019, ', 'Deportivo Alaves 2019-2019, ', 'FC Sankt Gallen 2019-2020, ',
                        'SC Freiburg 2020-2022 and has played ', 'FC Augsburg since 2022'
    bundesliga.add_node(304, name='Péter Gulácsi', club='RB Leipzig', 'BVSC Budapest 1995-2003, ',
                        'MTK Budapest 2003-2007, ', 'Liverpool FC 2007-2009, ', 'Here', 'd United FC 2009-2009, ',
                        'Liverpool FC 2009-2010, ', 'Tranmere Rovers 2010-2010, ', 'Liverpool FC 2010-2010, ',
                        'Tranmere Rovers 2010-2010, ', 'Liverpool FC 2010-2011, ', 'Hull City AFC 2011-2012, ',
                        'Liverpool FC 2012-2013, ', 'FC Red Bull Salzburg 2013-2015 and has played ',
                        'RB Leipzig since 2015'
    bundesliga.add_node(305, name='Timo Hübers', club='1. FC Köln', 'SV Hildesia Diekholzen 2007-2008, ',
                        'Hannover 96 2008-2015, ', '1. FC Köln 2015-2016, ', 'Hannover 96 2016-2021 and has played ',
                        '1. FC Köln since 2021'
    bundesliga.add_node(306, name='Marvin Plattenhardt', club='Hertha Berlin', '1. FC Frickenhausen 1999-2005, ',
                        'FV Nürtingen 2005-2006, ', 'SSV Reutlingen 2006-2008, ',
                        '1. FC Nürnberg 2008-2014 and has played ', 'Hertha BSC since 2014'
    bundesliga.add_node(307, name='Josuha Guilavogui', club='VfL Wolfsburg', 'USAM Toulon Marines 1997-2000, ',
                        'Sporting Toulon Var 2000-2005, ', 'AS Saint Etienne 2005-2013, ',
                        'Atletico Madrid 2013-2014, ', 'AS Saint Etienne 2014-2014, ', 'Atletico Madrid 2014-2014, ',
                        'VfL Wolfsburg 2014-2022, ', 'FC Girondins de Bordeaux 2022-2022 and has played ',
                        'VfL Wolfsburg since 2022'
    bundesliga.add_node(308, name='Janik Haberer', club='1. FC Union Berlin', 'FC Wangen 1999-2005, ',
                        'FV 1893 Ravensburg 2006-2009, ', 'FC Memmingen 2009-2010, ', 'SpVgg Unterhaching 2011-2014, ',
                        'TSG Hoffenheim 2014-2015, ', 'VfL Bochum 1848 2015-2016, ',
                        'SC Freiburg 2016-2022 and has played ', '1. FC Union Berlin since 2022'
    bundesliga.add_node(308, name='Mathys Tel', club='FC Bayern München', 'JS Villiers-le-Bel 2012-2016, ',
                        'Paris FC 2016-2017, ', 'AS Jeunesse Aubervilliers 2017-2019, ', 'Montrouge FC 92 2019-2020, ',
                        'Stade Rennais FC 2020-2022 and has played ', 'FC Bayern München since 2022'
    bundesliga.add_node(310, name='Christopher Antwi-Adjei', club='VfL Bochum', 'SV Fortuna Hagen 1999-2001, ',
                        'Hasper SV 2001-2009, ', 'MSV Duisburg 2009-2011, ', 'TSC Eintracht Dortmund 2011-2012, ',
                        'SC Westfalia Herne 2012-2014, ', 'TSG Sprockhövel 2014-2017, ',
                        'SC Paderborn 07 2017-2021 and has played ', 'VfL Bochum 1848 since 2021'
    bundesliga.add_node(311, name='Cédric Brunner', club='FC Schalke 04', 'FC Maur 2005-2006, ',
                        'FC Zürich 2006-2018, ', 'DSC Arminia Bielefeld 2018-2022 and has played ',
                        'FC Schalke 04 since 2022'
    bundesliga.add_node(312, name='Kevin Paredes', club='VfL Wolfsburg', 'D.C. United 2016-2019, ',
                        'Loudoun United FC 2019-2019, ', 'D.C. United 2019-2022 and has played ',
                        'VfL Wolfsburg since 2022'
    bundesliga.add_node(313, name='Nikolas Nartey', club='VfB Stuttgart', 'Akademisk Boldklub 2008-2013, ',
                        'FC Kopenhagen 2013-2017, ', '1. FC Köln 2017-2019, ', 'FC Hansa Rostock 2019-2020, ',
                        'VfB Stuttgart 2020-2020, ', 'SV Sandhausen 2020-2021 and has played ',
                        'VfB Stuttgart since 2021'
    bundesliga.add_node(314, name='Rijad Smajic', club='1. FC Köln', 'SC Fortuna Köln 2017-2019 and has played ',
                        '1. FC Köln since 2019'
    bundesliga.add_node(315, name='Danilho Doekhi', club='1. FC Union Berlin', 'SC Excelsior Rotterdam 2006-2016, ',
                        'Ajax Amsterdam 2016-2018, ', 'Vitesse Arnheim 2018-2022 and has played ',
                        '1. FC Union Berlin since 2022'
    bundesliga.add_node(316, name='Benjamin Henrichs', club='RB Leipzig', 'SpVgg Porz 2003-2004, ',
                        'Bayer 04 Leverkusen 2004-2018, ', 'AS Monaco FC 2018-2020 and has played ',
                        'RB Leipzig since 2020'
    bundesliga.add_node(317, name='Julian Brandt', club='Borussia Dortmund', 'SC Borgfeld 2001-2009, ',
                        'FC Oberneuland 2009-2011, ', 'VfL Wolfsburg 2011-2013, ',
                        'Bayer 04 Leverkusen 2014-2019 and has played ', 'Borussia Dortmund since 2019'
    bundesliga.add_node(318, name='Robert Wagner', club='Sport-Club Freiburg'
    bundesliga.add_node(319, name='Philipp Lienhart', club='Sport-Club Freiburg', 'SC Lilienfeld 2002-2007, ',
                        'SK Rapid Wien 2007-2014, ', 'Real Madrid CF 2014-2017 and has played ',
                        'SC Freiburg since 2017'
    bundesliga.add_node(320, name='Dayot Upamecano', club='FC Bayern München', 'VS Angers 2004-2007, ',
                        'FC Prey 2008-2009, ', 'Evreux FC 27 2009-2013, ', 'Valenciennes FC 2013-2015, ',
                        'FC Red Bull Salzburg 2015-2017, ', 'RB Leipzig 2017-2021 and has played ',
                        'FC Bayern München since 2021'
    bundesliga.add_node(321, name='Luca Kilian', club='1. FC Köln', 'Hombrucher SV 2004-2011, ',
                        'Borussia Dortmund 2011-2019, ', 'SC Paderborn 07 2019-2020, ',
                        '1. FSV Mainz 05 2020-2021 and has played ', '1. FC Köln since 2021'
    bundesliga.add_node(322, name='Tuta', club='Eintracht Frankfurt', 'Sao Paulo FC 2016-2019, ',
                        'Eintracht Frankfurt 2019-2019, ', 'KV Kortrijk 2019-2020 and has played ',
                        'Eintracht Frankfurt since 2020'
    bundesliga.add_node(323, name='Antonios Papadopoulos', club='Borussia Dortmund',
                        'SV Stuttgarter Kickers 2012-2013, ', 'FSV Waiblingen 2013-2015, ', 'VfR Aalen 2015-2019, ',
                        'Hallescher FC 2019-2021, ', 'Borussia Dortmund since 2021 and has played ',
                        'Borussia Dortmund II since 2021'
    bundesliga.add_node(324, name='Maximilian Eggestein', club='Sport-Club Freiburg',
                        'TSV Schloß Rickingen 1998-2004, ', 'TSV Havelse 2004-2011, ', 'SV Werder Bremen 2011-2021, ',
                        'Werder Bremen II 2011-2017 and has played ', 'SC Freiburg since 2021'
    bundesliga.add_node(325, name='Nico Schulz', club='Borussia Dortmund', 'BSC Rehberge Berlin 1997-2000, ',
                        'Hertha BSC 2000-2015, ', " Borussia M'gladbach 2015-2017, ",
                        'TSG Hoffenheim 2017-2019 and has played ', 'Borussia Dortmund since 2019'
    bundesliga.add_node(326, name='Lukas Klostermann', club='RB Leipzig', 'FSV Gevelsberg 2007-2008, ',
                        'SSV Hagen 2008-2010, ', 'VfL Bochum 1848 2010-2014 and has played ', 'RB Leipzig since 2014'
    bundesliga.add_node(327, name='Dominick Drexler', club='FC Schalke 04', '1. SF Brüser Berg 1995-2005, ',
                        'Bonner SC 2005-2006, ', 'Alemannia Aachen 2006-2007, ', 'Bayer 04 Leverkusen 2007-2010, ',
                        'FC Rot-Weiß Erfurt 2010-2013, ', 'SpVgg Greuther Fürth 2013-2014, ', 'VfR Aalen 2014-2016, ',
                        'Holstein Kiel 2016-2018, ', 'FC Midtjylland 2018-2018, ',
                        '1. FC Köln 2018-2021 and has played ', 'FC Schalke 04 since 2021'
    bundesliga.add_node(328, name='Mads Pedersen', club='FC Augsburg', 'Hörsholm Usseröd IK 2006-2009, ',
                        'Farum BK 2009-2015, ', 'FC Nordsjaelland 2015-2019, ', 'FC Augsburg 2019-2020, ',
                        'FC Zürich 2020-2020 and has played ', 'FC Augsburg since 2020'
    bundesliga.add_node(329, name='Kenneth Schmidt', club='Sport-Club Freiburg'
    bundesliga.add_node(330, name='Jiri Pavlenka', club='SV Werder Bremen', 'FC Hlucin 2002-2008, ',
                        'FC Banik Ostrava 2008-2011, ', 'FC Hlucin 2011-2012, ', 'FC Banik Ostrava 2012-2016, ',
                        'SK Slavia Prag 2016-2017 and has played ', 'SV Werder Bremen since 2017'
    bundesliga.add_node(331, name='Omar Marmoush', club='VfL Wolfsburg', 'Wadi Degla SC 2016-2017, ',
                        'VfL Wolfsburg 2017-2021, ', 'FC St. Pauli 2021-2021, ', 'VfL Wolfsburg 2021-2021, ',
                        'VfB Stuttgart 2021-2022 and has played ', 'VfL Wolfsburg since 2022'
    bundesliga.add_node(332, name='Fredrik Jensen', club='FC Augsburg', 'FC Honka Espoo 2008-2011, ',
                        'HJK Helsinki 2012-2013, ', 'FC Twente Enschede 2013-2018 and has played ',
                        'FC Augsburg since 2018'
    bundesliga.add_node(333, name='Thomas Kastanaras', club='VfB Stuttgart'
    bundesliga.add_node(334, name='Julian Baumgartlinger', club='FC Augsburg', 'USC Mattsee 1993-2001, ',
                        'TSV 1860 München 2001-2009, ', 'TSV München 1860 II 2001-2009, ',
                        'FK Austria Wien 2009-2011, ', '1. FSV Mainz 05 2011-2016, ',
                        'Bayer 04 Leverkusen 2016-2022 and has played ', 'FC Augsburg since 2022'
    bundesliga.add_node(335, name='Mahmoud Dahoud', club='Borussia Dortmund', 'SC Germania Reusrath 2004-2009, ',
                        'Fortuna Düsseldorf 2009-2010, ', " Borussia M'gladbach 2010-2017 and has played ",
                        'Borussia Dortmund since 2017'
    bundesliga.add_node(336, name='Robert Andrich', club='Bayer 04 Leverkusen', 'FV Turbine Potsdam 2000-2003, ',
                        'Hertha BSC 2003-2015, ', 'SG Dynamo Dresden 2015-2016, ', 'SV Wehen Wiesbaden 2016-2018, ',
                        '1. FC Heidenheim 1846 2018-2019, ', '1. FC Union Berlin 2019-2021 and has played ',
                        'Bayer 04 Leverkusen since 2021'
    bundesliga.add_node(337, name='Lukas Nmecha', club='VfL Wolfsburg', 'Manchester City FC 2007-2018, ',
                        'Preston North End 2018-2019, ', 'Manchester City FC 2019-2019, ', 'VfL Wolfsburg 2019-2020, ',
                        'Middlesbrough FC 2020-2020, ', 'Manchester City FC 2020-2020, ', 'RSC Anderlecht 2020-2021, ',
                        'Manchester City FC 2021-2021 and has played ', 'VfL Wolfsburg since 2021'
    bundesliga.add_node(338, name='Aissa Laidouni', club='1. FC Union Berlin', 'SCO Angers 2015-2016, ',
                        'Vendee Les Herbiers Football 2016-2017, ', 'SCO Angers 2017-2017, ',
                        'FC Chambly Oise 2017-2018, ', 'FC Voluntari 2018-2020, ',
                        'Ferencvaros Budapest 2020-2023 and has played ', '1. FC Union Berlin since 2023'
    bundesliga.add_node(339, name='Jérôme Roussillon', club='1. FC Union Berlin', 'Saint-Denis US 1999-2006, ',
                        'I.N.F. Clairefontaine 2006-2009, ', 'FC Sochaux 2009-2015, ',
                        'Montpellier Herault SC 2015-2018, ', 'VfL Wolfsburg 2018-2023 and has played ',
                        '1. FC Union Berlin since 2023'
    bundesliga.add_node(340, name='Simon Zoller', club='VfL Bochum', 'VfB Friedrichshafen 2004-2005, ',
                        'VfB Stuttgart 2005-2007, ', 'SSV Ulm 1846 2007-2008, ', 'Karlsruher SC 2008-2012, ',
                        'VfL Osnabrück 2012-2013, ', '1. FC Kaiserslautern 2013-2014, ', '1. FC Köln 2014-2015, ',
                        '1. FC Kaiserslautern 2015-2015, ', '1. FC Köln 2015-2019 and has played ',
                        'VfL Bochum 1848 since 2019'
    bundesliga.add_node(341, name='Hrvoje Smolčić', club='Eintracht Frankfurt', 'NK Gospic 91 2013-2014, ',
                        'HNK Rijeka 2014-2014, ', 'NK Gospic 91 2014-2015, ', 'HNK Rijeka 2015-2022 and has played ',
                        'Eintracht Frankfurt since 2022'
    bundesliga.add_node(342, name='Jonjoe Kenny', club='Hertha Berlin', 'Everton FC 2006-2015, ',
                        'Wigan Athletic FC 2015-2015, ', 'Everton FC 2015-2016, ', 'Ox', 'd United 2016-2016, ',
                        'Everton FC 2016-2019, ', 'FC Schalke 04 2019-2020, ', 'Everton FC 2020-2021, ',
                        'Celtic Glasgow FC 2021-2021, ', 'Everton FC 2021-2022 and has played ', 'Hertha BSC since 2022'
    bundesliga.add_node(343, name='Moussa Diaby', club='Bayer 04 Leverkusen',
                        'Esperance Sportive Parisienne 2009-2013, ', 'Paris Saint-Germain FC 2013-2018, ',
                        'FC Crotone 2018-2018, ', 'Paris Saint-Germain FC 2018-2019 and has played ',
                        'Bayer 04 Leverkusen since 2019'
    bundesliga.add_node(344, name='Charles Aránguiz', club='Bayer 04 Leverkusen', 'Universidad de Chile 2000-2001, ',
                        'CD Cobreloa 2002-2007, ', 'CD Cobresal 2007-2007, ', 'CD Cobreloa 2008-2009, ',
                        'CSD Colo-Colo 2009-2010, ', 'Quilmes Atletico Club 2010-2011, ',
                        'Universidad de Chile 2011-2013, ', 'Udinese Calcio 2014-2014, ',
                        'SC Internacional 2014-2015 and has played ', 'Bayer 04 Leverkusen since 2015'
    bundesliga.add_node(345, name='Sébastien Haller', club='Borussia Dortmund', 'FC Olympique de Vigneux 2003-2005, ',
                        'CS Bretigny Football 2005-2007, ', 'AJ Auxerre 2007-2014, ', 'FC Utrecht 2015-2017, ',
                        'Eintracht Frankfurt 2017-2019, ', 'West Ham United FC 2019-2021, ',
                        'Ajax Amsterdam 2021-2022 and has played ', 'Borussia Dortmund since 2022'
    bundesliga.add_node(346, name='Tim Fosu-Mensah', club='Bayer 04 Leverkusen', 'AVV Zeeburgia 2005-2006, ',
                        'Ajax Amsterdam 2006-2014, ', 'Manchester United FC 2014-2017, ',
                        'Crystal Palace FC 2017-2018, ', 'Manchester United FC 2018-2018, ', 'Fulham FC 2018-2019, ',
                        'Manchester United FC 2019-2021 and has played ', 'Bayer 04 Leverkusen since 2021'
    bundesliga.add_node(347, name='Florian Neuhaus', club='Borussia Mönchengladbach', 'VfL Kaufering 2003-2007, ',
                        'TSV 1860 München 2007-2017, ', 'Fortuna Düsseldorf 2017-2018 and has played ',
                        " Borussia M'gladbach since 2018."
    bundesliga.add_node(348, name='Rani Khedira', club='1. FC Union Berlin', 'TV Oeffingen 1897 2004-2005, ',
                        'VfB Stuttgart 2005-2014, ', 'VfB Stuttgart II 2005-2014, ', 'RB Leipzig 2014-2017, ',
                        'FC Augsburg 2017-2021 and has played ', '1. FC Union Berlin since 2021'
    bundesliga.add_node(349, name='Michael Frey', club='FC Schalke 04', 'FC Münsingen 2000-2006, ',
                        'FC Thun 2006-2010, ', 'Berner SC Young Boys 2010-2014, ', 'Lille OSC 2014-2016, ',
                        'FC Luzern 2016-2016, ', 'Berner SC Young Boys 2016-2017, ', 'FC Zürich 2017-2018, ',
                        'Fenerbahce SK Istanbul 2018-2019, ', '1. FC Nürnberg 2019-2020, ',
                        'Fenerbahce SK Istanbul 2020-2020, ', 'RS Waasland - SK Beveren 2020-2021, ',
                        'Royal Antwerpen FC 2021-2023 and has played ', 'FC Schalke 04 since 2023'
    bundesliga.add_node(350, name='Bouna Sarr', club='FC Bayern München', 'FC Gerland 1998-2005, ',
                        'Olympique Lyonnais 2005-2009, ', 'FC Metz 2009-2015, ',
                        'Olympique de Marseille 2015-2020 and has played ', 'FC Bayern München since 2020'
    bundesliga.add_node(351, name='Thomas Ouwejan', club='FC Schalke 04', 'SV De Foresters Heiloo 2006-2007, ',
                        'AZ Alkmaar 2007-2020, ', 'Udinese Calcio 2020-2021 and has played ', 'FC Schalke 04 since 2021'
    bundesliga.add_node(352, name='Aarón Martín', club='1. FSV Mainz 05', 'C.F. Montmelo Unio Esportiva 2003-2005, ',
                        'Espanyol Barcelona 2005-2018, ', '1. FSV Mainz 05 2018-2020, ',
                        'Celta Vigo 2021-2021 and has played ', '1. FSV Mainz 05 since 2021'
    bundesliga.add_node(353, name='Noah Weißhaupt', club='Sport-Club Freiburg'
    bundesliga.add_node(354, name='Maxim Leitsch', club='1. FSV Mainz 05', 'Essener SG 99 2003-2007, ',
                        'SG Wattenscheid 09 2007-2008, ', 'VfL Bochum 1848 2008-2022 and has played ',
                        '1. FSV Mainz 05 since 2022'
    bundesliga.add_node(355, name='Wataru Endo', club='VfB Stuttgart', 'Yokohama South Totsuka SC 1999-2004, ',
                        'Yokohama South Totsuka Jr HS 2005-2007, ', 'Shonan Bellmare 2008-2015, ',
                        'Urawa Red Diamonds 2016-2018, ', 'Sint-Truidense VV 2018-2019 and has played ',
                        'VfB Stuttgart since 2019'
    bundesliga.add_node(356, name='Kasper Dolberg', club='TSG 1899 Hoffenheim', 'GfG Voel fodbold klub 2005-2010, ',
                        'Silkeborg IF 2010-2015, ', 'Ajax Amsterdam 2015-2019, ', 'OGC Nice 2019-2022, ',
                        'Sevilla FC 2022-2022 and has played ', 'TSG Hoffenheim since 2023'
    bundesliga.add_node(357, name='Nils Petersen', club='Sport-Club Freiburg'
    bundesliga.add_node(358, name='Pascal Stenzel', club='VfB Stuttgart', 'DSC Arminia Bielefeld 2006-2011, ',
                        'VfL Osnabrück 2011-2013, ', 'Borussia Dortmund 2013-2016, ',
                        'Borussia Dortmund II 2013-2016, ', 'SC Freiburg 2016-2019 and has played ',
                        'VfB Stuttgart since 2019'
    bundesliga.add_node(359, name='Finn Becker', club='TSG 1899 Hoffenheim', 'Holsatia Elmshorn 2010-2011, ',
                        'FC St. Pauli 2011-2022 and has played ', 'TSG Hoffenheim since 2022'
    bundesliga.add_node(360, name='Aurélio Buta', club='Eintracht Frankfurt', 'RD Agueda 2005-2009, ',
                        'SC Beira Mar 2009-2011, ', 'SL Benfica Lissabon 2011-2017, ',
                        'Royal Antwerpen FC 2017-2022 and has played ', 'Eintracht Frankfurt since 2022'
    bundesliga.add_node(361, name='Sepp van den Berg', club='FC Schalke 04', " CSV '28 2008-2012, ",
                        'PEC Zwolle 2012-2019, ', 'Liverpool FC 2019-2021, ', 'Preston North End 2021-2022, ',
                        'Liverpool FC 2022-2022 and has played ', 'FC Schalke 04 since 2022'
    bundesliga.add_node(362, name='Renato Veiga', club='FC Augsburg', 'Sporting CP Lissabon 2010-2013, ',
                        'Real Sport Clube 2016-2019, ', 'Sporting CP Lissabon 2019-2023 and has played ',
                        'FC Augsburg since 2023'
    bundesliga.add_node(363, name='Sergio Córdova', club='FC Augsburg', 'Arroceros FC 2012-2013, ',
                        'Caracas FC 2013-2017, ', 'FC Augsburg 2017-2020, ', 'DSC Arminia Bielefeld 2020-2021, ',
                        'FC Augsburg 2021-2022, ', 'Real Salt Lake 2022-2022 and has played ', 'FC Augsburg since 2023'
    bundesliga.add_node(364, name='Kevin-Prince Boateng', club='Hertha Berlin', 'Hertha BSC 1994-1995, ',
                        'Reinickendorfer Füchse 1995-1996, ', 'Hertha BSC 1996-2007, ', 'Hertha BSC II 1996-2007, ',
                        'Tottenham Hotspur FC 2007-2009, ', 'Borussia Dortmund 2009-2009, ',
                        'Tottenham Hotspur FC 2009-2009, ', 'Portsmouth FC 2009-2010, ', 'Genua CFC 1893 2010-2010, ',
                        'AC Mailand 2010-2013, ', 'FC Schalke 04 2013-2015, ', 'AC Mailand 2016-2016, ',
                        'UD Las Palmas 2016-2017, ', 'Eintracht Frankfurt 2017-2018, ',
                        'US Sassuolo Calcio 2018-2019, ', 'FC Barcelona 2019-2019, ', 'US Sassuolo Calcio 2019-2019, ',
                        'ACF Florenz 2019-2020, ', 'Besiktas JK Istanbul 2020-2020, ',
                        'ACF Florenz 2020-2020 and has played ', 'Hertha BSC since 2021'
    bundesliga.add_node(365, name='Marco Richter', club='Hertha Berlin', 'SV Guntamatic Ried 2003-2004, ',
                        'FC Bayern München 2004-2011, ', 'FC Augsburg 2011-2021 and has played ',
                        'Hertha BSC since 2021'
    bundesliga.add_node(366, name='Kelian Nsona', club='Hertha Berlin', " Union Sportive d'Ivry 2009-2012, ",
                        'Paris FC 2012-2017, ', 'SM Caen 2017-2022 and has played ', 'Hertha BSC since 2022'
    bundesliga.add_node(367, name='Christian Günter', club='Sport-Club Freiburg',
                        'FV Tennenbronn 1997-2007 and has played ', 'SC Freiburg since 2007'
    bundesliga.add_node(368, name='Paul Seguin', club='1. FC Union Berlin', '1.FC Lok Stendal 1999-2007, ',
                        'VfL Wolfsburg 2007-2017, ', 'SG Dynamo Dresden 2017-2018, ', 'VfL Wolfsburg 2018-2019, ',
                        'SpVgg Greuther Fürth 2019-2022 and has played ', '1. FC Union Berlin since 2022'
    bundesliga.add_node(369, name='Ivan Ordets', club='VfL Bochum', 'FC Shakhtar Donetsk 2005-2010, ',
                        'FC Illichivets Mariupol 2011-2011, ', 'FC Shakhtar Donetsk 2011-2013, ',
                        'FC Illichivets Mariupol 2013-2014, ', 'FC Shakhtar Donetsk 2014-2019, ',
                        'Dinamo Moskau 2019-2022 and has played ', 'VfL Bochum 1848 since 2022'
    bundesliga.add_node(370, name='Abdoulaye Kamara', club='Borussia Dortmund', 'Paris Saint-Germain FC 2018-2021, ',
                        'Borussia Dortmund since 2021 and has played ', 'Borussia Dortmund II since 2021'
    https: // www.bundesliga.com / en / bundesliga / player
    bundesliga.add_node(371, name='Jamal Musiala', club='FC Bayern München'
    bundesliga.add_node(372, name='Soumaïla Coulibaly', club='Borussia Dortmund',
                        'Football Club de Montfermeil 2015-2018, ', 'Paris Saint-Germain FC 2018-2021, ',
                        'Borussia Dortmund since 2021 and has played ', 'Borussia Dortmund II since 2021'
    bundesliga.add_node(373, name='Ermin Bičakčić', club='TSG 1899 Hoffenheim', 'Spvgg Möckmühl 1995-2004, ',
                        'FC Heilbronn 2005-2006, ', 'VfB Stuttgart 2006-2012, ', 'VfB Stuttgart II 2006-2012, ',
                        'Eintracht Braunschweig 2012-2014 and has played ', 'TSG Hoffenheim since 2014'
    bundesliga.add_node(374, name='Tom Berger', club='SV Werder Bremen', 'MTV Walle 2011-2012, ',
                        'VfL Wolfsburg 2012-2020, ', 'VfL Wolfsburg U 19 2018-2020 and has played ',
                        'SV Werder Bremen since 2020'
    bundesliga.add_node(375, name='Justin Che', club='TSG 1899 Hoffenheim', 'FC Dallas 2009-2021, ',
                        'FC Bayern München 2021-2021, ', 'FC Bayern München II 2021-2021, ',
                        'FC Dallas 2021-2022 and has played ', 'TSG Hoffenheim since 2022'
    bundesliga.add_node(376, name='Tobias Strobl', club='FC Augsburg', 'SV Aubing 1996-2000, ',
                        'TSV 1860 München 2000-2011, ', 'TSG Hoffenheim 2011-2012, ', '1. FC Köln 2012-2013, ',
                        'TSG Hoffenheim 2013-2016, ', " Borussia M'gladbach 2016-2020 and has played ",
                        'FC Augsburg since 2020'
    bundesliga.add_node(377, name='Tanguy Coulibaly ', club='VfB Stuttgart',
                        'Paris Saint-Germain FC 2013-2019 and has played ', 'VfB Stuttgart since 2019'
    bundesliga.add_node(378, name='Suat Serdar', club='Hertha Berlin', 'FVgg Hassia Bingen 2003-2008, ',
                        '1. FSV Mainz 05 2008-2018, ', '1.FSV Mainz 05 II 2008-2018, ',
                        'FC Schalke 04 2018-2021 and has played ', 'Hertha BSC since 2021'
    bundesliga.add_node(379, name='Aymen Barkok', club='1. FSV Mainz 05', 'SG Praunheim 08 2008-2009, ',
                        'SG Rot-Weiss Frankfurt 2009-2011, ', 'Kickers Offenbach 2011-2013, ',
                        'Eintracht Frankfurt 2013-2018, ', 'Fortuna Düsseldorf 2018-2020, ',
                        'Eintracht Frankfurt 2020-2022 and has played ', '1. FSV Mainz 05 since 2022'
    bundesliga.add_node(380, name='Joshua Quarshie', club='TSG 1899 Hoffenheim', 'FC Schalke 04 2017-2019, ',
                        'Fortuna Düsseldorf 2019-2020, ', 'Rot-Weiss Essen 2020-2022 and has played ',
                        'TSG Hoffenheim since 2022'
    bundesliga.add_node(381, name='Karim Adeyemi', club='Borussia Dortmund', 'TSV Forstenried 2007-2009, ',
                        'FC Bayern München 2009-2011, ', 'TSV Forstenried 2011-2012, ',
                        'SpVgg Unterhaching 2012-2018, ', 'FC Liefering 2018-2019, ',
                        'FC Red Bull Salzburg 2020-2022 and has played ', 'Borussia Dortmund since 2022'
    bundesliga.add_node(382, name='Sargis Adamyan', club='1. FC Köln', '1.FC Neubrandenburg 04 2005-2009, ',
                        'FC Hansa Rostock 2009-2014, ', 'TSG Neustrelitz 2014-2016, ',
                        'TSV Steinbach Haiger 2016-2017, ', 'SSV Jahn Regensburg 2017-2019, ',
                        'TSG Hoffenheim 2019-2022, ', 'Club Brügge KV 2022-2022 and has played ',
                        '1. FC Köln since 2022'
    bundesliga.add_node(383, name='Eric Maxim Choupo-Moting', club='FC Bayern München', 'FC Teutonia 05 1999-2000, ',
                        'FC Altona 93 2000-2003, ', 'FC St. Pauli 2003-2004, ', 'Hamburger SV 2004-2009, ',
                        'Hamburger SV II 2004-2009, ', '1. FC Nürnberg 2009-2010, ', 'Hamburger SV 2010-2011, ',
                        '1. FSV Mainz 05 2011-2014, ', 'FC Schalke 04 2014-2017, ', 'Stoke City FC 2017-2018, ',
                        'Paris Saint-Germain FC 2018-2020 and has played ', 'FC Bayern München since 2020'
    bundesliga.add_node(384, name='Ludovic Ajorque', club='1. FSV Mainz 05', 'SCO Angers 2013-2014, ',
                        'Le Poire sur Vie VF 2014-2015, ', 'SCO Angers 2015-2015, ', 'Lucon Football Club 2015-2016, ',
                        'SCO Angers 2016-2016, ', 'Clermont Foot 63 2016-2018, ',
                        'RC Strasbourg Alsace 2018-2023 and has played ', '1. FSV Mainz 05 since 2023'
    bundesliga.add_node(385, name='Anthony Modeste', club='Borussia Dortmund',
                        'Etoile FC Frejus Saint-Raphael 1994-2003, ', 'OGC Nice 2003-2009, ', 'SCO Angers 2009-2010, ',
                        'OGC Nice 2010-2010, ', 'FC Girondins de Bordeaux 2010-2012, ',
                        'Blackburn Rovers FC 2012-2012, ', 'SC Bastia 2012-2013, ', 'TSG Hoffenheim 2013-2015, ',
                        '1. FC Köln 2015-2017, ', 'Tianjin Quanjian 2017-2018, ', '1. FC Köln 2018-2021, ',
                        'AS Saint Etienne 2021-2021, ', '1. FC Köln 2021-2022 and has played ',
                        'Borussia Dortmund since 2022'
    bundesliga.add_node(386, name='Jakub Kamiński', club='VfL Wolfsburg', 'TS Szombierki Bytom 2010-2015, ',
                        'KKS Lech Posen 2015-2022 and has played ', 'VfL Wolfsburg since 2022'
    bundesliga.add_node(387, name='Paulo Otávio', club='VfL Wolfsburg', 'Coritiba FC 2013-2014, ',
                        'EC Santo Andre 2014-2014, ', 'Coritiba FC 2015-2015, ', 'Paysandu Sport Club 2015-2015, ',
                        'Coritiba FC 2015-2016, ', 'Tombense FC 2016-2016, ', 'LASK Linz 2016-2017, ',
                        'FC Ingolstadt 04 2017-2019 and has played ', 'VfL Wolfsburg since 2019'
    bundesliga.add_node(388, name='Youssoufa Moukoko', club='Borussia Dortmund'
    bundesliga.add_node(389, name='Lukas Kübler', club='Sport-Club Freiburg', '1. FC Köln 2007-2008, ',
                        'SF Troisdorf 2008-2009, ', 'Bonner SC 2009-2011, ', '1. FC Köln 2011-2013, ',
                        'SV Sandhausen 2013-2015, ', 'SC Freiburg since 2015 and has played ',
                        'SC Freiburg II since 2022'
    bundesliga.add_node(390, name='Yvandro Borges Sanches', club='Borussia Mönchengladbach'
    bundesliga.add_node(391, name='Louis Lord', club='SV Werder Bremen', 'FC Gessel-Leerssen 2007-2008, ',
                        'TV Stuhr 2008-2015 and has played ', 'SV Werder Bremen since 2015'
    bundesliga.add_node(392, name='André Silva', club='RB Leipzig', 'SC Salgueiros Porto 2003-2007, ',
                        'Boavista FC Porto 2007-2008, ', 'SC Salgueiros Porto 2008-2010, ', 'Padroense FC 2010-2011, ',
                        'FC Porto 2011-2017, ', 'AC Mailand 2017-2018, ', 'Sevilla FC 2018-2019, ',
                        'AC Mailand 2019-2019, ', 'Eintracht Frankfurt 2019-2021 and has played ',
                        'RB Leipzig since 2021'
    bundesliga.add_node(393, name='Maximilian Bauer', club='FC Augsburg', 'SpVgg GW Deggendorf 2013-2014, ',
                        'SpVgg Greuther Fürth 2014-2022 and has played ', 'FC Augsburg since 2022'
    bundesliga.add_node(394, name='Soichiro Kozuki', club='FC Schalke 04', 'Kyoto Sanga FC 2018-2022, ',
                        '1. FC Düren 2022-2022 and has played ', 'FC Schalke 04 since 2022'
    bundesliga.add_node(395, name='Leo Greiml', club='FC Schalke 04', 'SV Horn 2006-2014, ',
                        'SKN St. Pölten 2014-2018, ', 'SK Rapid Wien 2018-2022 and has played ',
                        'FC Schalke 04 since 2022'
    bundesliga.add_node(396, name='Hannes Wolf', club='Borussia Mönchengladbach', 'SC Seiersberg 2004-2008, ',
                        'SV Gössendorf 2008-2012, ', 'USV Vasoldsberg 2012-2012, ', 'JAZ GU-Süd 2012-2014, ',
                        'FC Red Bull Salzburg 2014-2016, ', 'FC Liefering 2016-2017, ',
                        'FC Red Bull Salzburg 2017-2019, ', 'RB Leipzig 2019-2020, ',
                        " Borussia M'gladbach 2020-2022, ", 'Swansea City 2022-2022 and has played ',
                        " Borussia M'gladbach since 2022."
    bundesliga.add_node(397, name='Andreas Ivan', club='FC Schalke 04', 'Karlsruher SC 2011-2012, ',
                        'SV Stuttgarter Kickers 2012-2016, ', 'Rot-Weiss Essen 2016-2016, ',
                        'Wuppertaler SV 2017-2017, ', 'SV Waldhof Mannheim 2017-2018, ',
                        'New York Red Bulls 2018-2019, ', 'VfR Aalen 2020-2020, ',
                        'SG Sonnenhof Großaspach 2020-2021, ', 'Rot Weiss Ahlen 2021-2022 and has played ',
                        'FC Schalke 04 since 2022'
    bundesliga.add_node(398, name='Aaron Zehnter', club='FC Augsburg', 'Würzburger FV 2016-2017, ',
                        'FC Würzburger Kickers 2017-2019 and has played ', 'FC Augsburg since 2019'
    bundesliga.add_node(399, name='Alexander Hack', club='1. FSV Mainz 05'
    bundesliga.add_node(400, name='Daniel Katic', club='FC Augsburg'
    bundesliga.add_node(401, name='Nikola Soldo', club='1. FC Köln', 'GNK Dinamo Zagreb 2006-2010, ',
                        'NK Lokomotiva Zagreb 2010-2011, ', 'NK Zagreb 2011-2013, ', 'NK HASK Zagreb 2013-2014, ',
                        'NK Tekstilac Ravnice 2014-2015, ', 'NK Inter Zapresic 2015-2021, ',
                        'NK Lokomotiva Zagreb 2021-2022 and has played ', '1. FC Köln since 2022'
    bundesliga.add_node(402, name='Giovanni Reyna', club='Borussia Dortmund',
                        'New York City FC 2015-2019 and has played ', 'Borussia Dortmund since 2019'
    bundesliga.add_node(403, name='Maximilian Neutgens', club='Bayer 04 Leverkusen'
    bundesliga.add_node(404, name='Callum Hudson-Odoi', club='Bayer 04 Leverkusen',
                        'Chelsea FC 2007-2022 and has played ', 'Bayer 04 Leverkusen since 2022'
    bundesliga.add_node(405, name='Bartol Franjić', club='VfL Wolfsburg', 'GNK Dinamo Zagreb 2008-2022, ',
                        'GNK Dinamo Zagreb U 19 2019-2020 and has played ', 'VfL Wolfsburg since 2022'
    bundesliga.add_node(406, name='Serhou Guirassy', club='VfB Stuttgart', 'J3 Sports Amilly 2008-2009, ',
                        'USM Montargis 2009-2010, ', 'J3 Sports Amilly 2010-2011, ', 'Stade Lavallois MFC 2011-2015, ',
                        'Lille OSC 2015-2016, ', 'AJ Auxerre 2016-2016, ', 'Lille OSC 2016-2016, ',
                        '1. FC Köln 2016-2019, ', 'Amiens Sporting Club 2019-2020, ',
                        'Stade Rennais FC 2020-2022 and has played ', 'VfB Stuttgart since 2022'
    bundesliga.add_node(407, name='Xaver Schlager', club='RB Leipzig', 'SC St. Valentin 2003-2009, ',
                        'FC Red Bull Salzburg 2009-2019, ', 'VfL Wolfsburg 2019-2022 and has played ',
                        'RB Leipzig since 2022'
    bundesliga.add_node(408, name='Philipp Pentke', 'TSG 1899 Hoffenheim', 'BSC Freiberg 1994-1998, ',
                        'SG Dynamo Dresden 1998-2003, ', 'TSV 1860 München 2003-2007, ',
                        'TSV München 1860 II 2003-2007, ', 'FC Augsburg 2007-2008, ', 'FC Energie Cottbus 2008-2009, ',
                        'Chemnitzer FC 2009-2015, ', 'SSV Jahn Regensburg 2015-2019 and has played ',
                        'TSG Hoffenheim since 2019'
    bundesliga.add_node(409, name='Josip Juranovic', club='1. FC Union Berlin', 'NK Dubrava Tim Kabel 2004-2011, ',
                        'NK Sesvete Zagreb 2011-2011, ', 'NK Dubrava Tim Kabel 2011-2015, ',
                        'HNK Hajduk Split 2015-2020, ', 'Legia Warschau 2020-2021, ',
                        'Celtic Glasgow FC 2021-2023 and has played ', '1. FC Union Berlin since 2023'
    bundesliga.add_node(410, name='Luca Philipp', club='TSG 1899 Hoffenheim', 'SGV Freiberg 2012-2013 and has played ',
                        'TSG Hoffenheim since 2013'
    bundesliga.add_node(411, name='Danny da Costa', club='1. FSV Mainz 05', 'DJK Winfriedia Mülheim 1999-2001, ',
                        'Bayer 04 Leverkusen 2001-2012, ', 'FC Ingolstadt 04 2012-2016, ',
                        'Bayer 04 Leverkusen 2016-2017, ', 'Eintracht Frankfurt 2017-2021, ',
                        '1. FSV Mainz 05 2021-2021, ', 'Eintracht Frankfurt 2021-2022 and has played ',
                        '1. FSV Mainz 05 since 2022'
    bundesliga.add_node(412, name='Nahuel Noll', club='TSG 1899 Hoffenheim'
    bundesliga.add_node(413, name='Leandro Barreiro', club='1. FSV Mainz 05', 'FC 72 Erpeldange 2004-2012, ',
                        'RFC Union Luxembourg 2012-2015, ', 'FC 72 Erpeldange 2015-2016 and has played ',
                        '1. FSV Mainz 05 since 2016'
    bundesliga.add_node(414, name='Marlon Mustapha', club='1. FSV Mainz 05', 'SC Red Star Penzing 2016-2018, ',
                        'FC Red Bull Salzburg 2018-2018, ', '1. FSV Mainz 05 2018-2021, ',
                        '1.FSV Mainz 05 U 19 2018-2020, ', 'FC FLYERALARM Admira Wacker 2021-2022 and has played ',
                        '1. FSV Mainz 05 since 2022'
    bundesliga.add_node(415, name='Tomáš Koubek', club='FC Augsburg', 'TJ Sokol Ostretin 1998-2004, ',
                        'AFK Horni Jeleni 1922 2004-2007, ', 'SK Hradec Kralove 2007-2015, ',
                        'FC Slovan Liberec 2015-2016, ', 'AC Sparta Prag 2016-2017, ',
                        'Stade Rennais FC 2017-2019 and has played ', 'FC Augsburg since 2019'
    bundesliga.add_node(416, name='Emil Forsberg', club='RB Leipzig', 'GIF Sundsvall 1996-2008, ',
                        'Medskogsbrons BK 2009-2009, ', 'GIF Sundsvall 2009-2012, ',
                        'Malmö FF 2013-2015 and has played ', 'RB Leipzig since 2015'
    bundesliga.add_node(417, name='Mehmet Can', club='FC Schalke 04', 'VfL Boscheln 2009-2010, ',
                        " Borussia M'gladbach 2010-2014 and has played ", 'FC Schalke 04 since 2014'
    bundesliga.add_node(418, name='Danny Latza', club='FC Schalke 04', 'DJK Germania Ückendorf 1995-1998, ',
                        'FC Schalke 04 1998-2011, ', 'SV Darmstadt 98 2011-2013, ', 'VfL Bochum 1848 2013-2015, ',
                        '1. FSV Mainz 05 2015-2021 and has played ', 'FC Schalke 04 since 2021'
    bundesliga.add_node(419, name='Ritsu Dōan', club='Sport-Club Freiburg', 'Gamba Osaka 2011-2017, ',
                        'FC Groningen 2017-2019, ', 'PSV Eindhoven 2019-2020, ', 'DSC Arminia Bielefeld 2020-2021, ',
                        'PSV Eindhoven 2021-2022 and has played ', 'SC Freiburg since 2022'
    bundesliga.add_node(420, name='Lilian Egloff', club='VfB Stuttgart'
    bundesliga.add_node(421, name='Kenan Karaman', club='FC Schalke 04', 'SV Stuttgarter Kickers 2008-2009, ',
                        'TSG Hoffenheim 2009-2014, ', 'Hannover 96 2014-2018, ', 'Fortuna Düsseldorf 2018-2021, ',
                        'Besiktas JK Istanbul 2021-2022 and has played ', 'FC Schalke 04 since 2022'
    bundesliga.add_node(422, name='Tom Krauß', club='FC Schalke 04', 'FC Sachsen Leipzig 2010-2011, ',
                        'RB Leipzig 2011-2020, ', '1. FC Nürnberg 2020-2022 and has played ', 'FC Schalke 04 since 2022'
    bundesliga.add_node(423, name='Maximilian Mittelstädt', club='Hertha Berlin', 'SC Staaken 2009-2010, ',
                        'FC Hertha 03 Zehlendorf 2010-2012 and has played ', 'Hertha BSC since 2012'
    bundesliga.add_node(424, name='Philipp Hofmann', club='VfL Bochum', 'TSV Rot-Weiß Wenholthausen 2001-2007, ',
                        'SC Neheim 2007-2009, ', 'FC Schalke 04 2009-2012, ', 'SC Paderborn 07 2012-2013, ',
                        'FC Ingolstadt 04 2013-2014, ', '1. FC Kaiserslautern 2014-2015, ', 'Brent', 'd FC 2015-2017, ',
                        'SpVgg Greuther Fürth 2017-2018, ', 'Eintracht Braunschweig 2018-2019, ',
                        'Karlsruher SC 2019-2022 and has played ', 'VfL Bochum 1848 since 2022'
    bundesliga.add_node(425, name='Mateu Morey', club='Borussia Dortmund', 'RCD Mallorca 2014-2015, ',
                        'FC Barcelona 2015-2019, ', 'Borussia Dortmund since 2019 and has played ',
                        'Borussia Dortmund II since 2019'
    bundesliga.add_node(426, name='Tobias Mohr', club='FC Schalke 04', 'SuS Borussia 08 Brand 1998-2006, ',
                        'Alemannia Aachen 2006-2018, ', 'SpVgg Greuther Fürth 2018-2020, ',
                        '1. FC Heidenheim 1846 2020-2022 and has played ', 'FC Schalke 04 since 2022'
    bundesliga.add_node(427, name='Ruben Vargas', club='FC Augsburg', 'FC Adligenswil 2006-2008, ',
                        'FC Luzern 2008-2014, ', 'SC Kriens 2014-2015, ', 'FC Luzern 2015-2019 and has played ',
                        'FC Augsburg since 2019'
    bundesliga.add_node(428, name='Benjamin Pavard', club='FC Bayern München', 'US Jeumont 2002-2005, ',
                        'Lille OSC 2005-2016, ', 'VfB Stuttgart 2016-2019 and has played ',
                        'FC Bayern München since 2019'
    bundesliga.add_node(429, name='Stevan Jovetić', club='Hertha Berlin', 'FK Mladost Podgorica 2000-2003, ',
                        'FK Partizan Belgrad 2003-2008, ', 'ACF Florenz 2008-2013, ', 'Manchester City FC 2013-2015, ',
                        'Inter Mailand 2015-2017, ', 'Sevilla FC 2017-2017, ', 'Inter Mailand 2017-2017, ',
                        'AS Monaco FC 2017-2021 and has played ', 'Hertha BSC since 2021'
    bundesliga.add_node(430, name='Juan Jose Perea', club='VfB Stuttgart', 'FC Porto 2018-2019, ',
                        'Panathinaikos FC Athen 2019-2020, ', 'Volos NPS 2020-2021, ',
                        'PAS Giannina FC 2021-2022 and has played ', 'VfB Stuttgart since 2022'
    bundesliga.add_node(431, name='Anthony Caci', club='1. FSV Mainz 05', 'Stade Olympique de Merlebach 2003-2004, ',
                        'ES Petite-Rosselle 2004-2008, ', 'Etoile Naborienne Saint-Avold 2008-2009, ',
                        'SG Marienau Forbach 2009-2011, ', 'RC Strasbourg 2011-2012, ',
                        'RC Strasbourg Alsace 2012-2022 and has played ', '1. FSV Mainz 05 since 2022'
    bundesliga.add_node(432, name='Dennis Geiger', club='TSG 1899 Hoffenheim',
                        'SV Alemannia Sattelbach 2008-2009 and has played ', 'TSG Hoffenheim since 2009'
    bundesliga.add_node(433, name='Romano Schmid', club='SV Werder Bremen', 'USV Vasoldsberg 2005-2009, ',
                        'SK Puntigamer Sturm Graz 2009-2017, ', 'FC Red Bull Salzburg 2017-2019, ',
                        'SV Werder Bremen 2019-2019, ', 'RZ Pellets WAC 2019-2020 and has played ',
                        'SV Werder Bremen since 2020'
    bundesliga.add_node(434, name='Dion Beljo', 'FC Augsburg', 'HNK Cibalia Vinkovci 2010-2019, ',
                        'NK Osijek 2019-2021, ', 'NK Istra 1961 2021-2022, ', 'NK Osijek 2022-2023 and has played ',
                        'FC Augsburg since 2023'
    bundesliga.add_node(435, name='Niklas Stark', club='SV Werder Bremen', 'FSV Ipsheim 1998-2002, ',
                        'TSV Neustadt/Aisch 2002-2004, ', '1. FC Nürnberg 2004-2015, ',
                        'Hertha BSC 2015-2022 and has played ', 'SV Werder Bremen since 2022'
    bundesliga.add_node(436, name='Justin Heekeren', club='FC Schalke 04', 'SSV Rheintreu Lüttingen 2013-2014, ',
                        'VfB Homberg 2014-2015, ', " Borussia M'gladbach 2015-2017, ",
                        'Rot-Weiß Oberhausen 2017-2022 and has played ', 'FC Schalke 04 since 2022'
    bundesliga.add_node(437, name='Genki Haraguchi', club='VfB Stuttgart', 'Urawa Red Diamonds 2004-2014, ',
                        'Hertha BSC 2014-2018, ', 'Fortuna Düsseldorf 2018-2018, ', 'Hannover 96 2018-2021, ',
                        '1. FC Union Berlin 2021-2023 and has played ', 'VfB Stuttgart since 2023'
    bundesliga.add_node(438, name='Nicolas Glaus', club='VfB Stuttgart', 'FC Basel 2016-2021 and has played ',
                        'VfB Stuttgart since 2021'
    bundesliga.add_node(439, name='Jonathan Schmid', club='Sport-Club Freiburg'
    bundesliga.add_node(440, name='Dominique Heintz', club='VfL Bochum', 'SV Herta Kirrweiler 2000-2001, ',
                        '1. FC Kaiserslautern 2001-2015, ', '1. FC Köln 2015-2018, ', 'SC Freiburg 2018-2021, ',
                        '1. FC Union Berlin 2022-2022 and has played ', 'VfL Bochum 1848 since 2022'
    bundesliga.add_node(441, name='Jacob Italiano', club='Borussia Mönchengladbach',
                        'Perth Glory 2017-2019 and has played ', " Borussia M'gladbach since 2019."
    bundesliga.add_node(442, name='Pierre Kunde Malong', club='VfL Bochum', 'Best Stars Academy de Limbe 2007-2012, ',
                        'Alcobendas CF 2012-2013, ', 'Atletico Madrid 2013-2016, ', 'CF Extremadura 2016-2017, ',
                        'Atletico Madrid 2017-2017, ', 'Granada CF 2017-2018, ', 'Atletico Madrid 2018-2018, ',
                        '1. FSV Mainz 05 2018-2021, ', 'Olympiacos CF Piräus 2021-2023 and has played ',
                        'VfL Bochum 1848 since 2023'
    bundesliga.add_node(443, name='Angelo Stiller', club='TSG 1899 Hoffenheim', 'TSV Milbertshofen 2009-2010, ',
                        'FC Bayern München 2010-2021, ', 'FC Bayern München II 2010-2021, ',
                        'FC Bayern München U 19 2018-2020 and has played ', 'TSG Hoffenheim since 2021'
    bundesliga.add_node(444, name='Derry Scherhant', club='Hertha Berlin', 'FC Viktoria 1889 Berlin 2018-2019, ',
                        'Tennis Borussia Berlin 2019-2020, ', 'Berliner SC 2020-2020 and has played ',
                        'Hertha BSC since 2020'
    bundesliga.add_node(445, name='Merlin Röhl', club='Sport-Club Freiburg', 'SV Babelsberg 03 2015-2018, ',
                        'FC Ingolstadt 04 2018-2022, ', 'FC Ingolstadt 04 U 19 2019-2020, ',
                        'SC Freiburg since 2022 and has played ', 'SC Freiburg II since 2022'
    bundesliga.add_node(446, name='Marcin Kamiński', club='FC Schalke 04', 'Aluminium Konin 2001-2005, ',
                        'KKS Lech Posen 2005-2016, ', 'VfB Stuttgart 2016-2018, ', 'Fortuna Düsseldorf 2018-2019, ',
                        'VfB Stuttgart 2019-2021 and has played ', 'FC Schalke 04 since 2021'
    bundesliga.add_node(447, name='Jonas Nickisch', club='RB Leipzig', 'Soccer ',
                        'Kids Dresden 2016-2017 and has played ', 'RB Leipzig since 2017'
    bundesliga.add_node(448, name='Marco Reus', club='Borussia Dortmund', 'PTSV Dortmund 1993-1995, ',
                        'Borussia Dortmund 1995-2005, ', 'LR Ahlen 2005-2006, ', 'Rot Weiss Ahlen 2006-2009, ',
                        " Borussia M'gladbach 2009-2012 and has played ", 'Borussia Dortmund since 2012'
    bundesliga.add_node(449, name='Sebastian Rudy', club='TSG 1899 Hoffenheim', 'FC Dietingen 1996-2001, ',
                        'SV Zimmern 2001-2003, ', 'VfB Stuttgart 2003-2010, ', 'VfB Stuttgart II 2003-2010, ',
                        'TSG Hoffenheim 2010-2017, ', 'FC Bayern München 2017-2018, ', 'FC Schalke 04 2018-2019, ',
                        'TSG Hoffenheim 2019-2020, ', 'FC Schalke 04 2020-2020 and has played ',
                        'TSG Hoffenheim since 2020'
    bundesliga.add_node(450, name='Timothy Chandler', club='Eintracht Frankfurt',
                        'Sportfreunde Oberau 1951 2000-2001, ', 'Eintracht Frankfurt 2001-2010, ',
                        '1. FC Nürnberg 2010-2014 and has played ', 'Eintracht Frankfurt since 2014'
    bundesliga.add_node(451, name='Jamie Leweling', club='1. FC Union Berlin', '1.FC Schnaittach 2005-2010, ',
                        '1.SC Feucht 2010-2012, ', '1. FC Nürnberg 2012-2017, ', 'SpVgg Greuther Fürth 2017-2022, ',
                        'SpVgg Greuther Fürth U 19 2018-2020 and has played ', '1. FC Union Berlin since 2022'
    bundesliga.add_node(452, name='Andrey Lunev', club='Bayer 04 Leverkusen', 'Torpedo Moskau 2001-2011, ',
                        'FK Istra 2012-2012, ', 'Torpedo Moskau 2012-2013, ', 'FK Kaluga 2013-2014, ',
                        'Torpedo Moskau 2014-2014, ', 'FC Saturn Moskovskaya Oblast 2015-2015, ', 'FK Ufa 2015-2016, ',
                        'FC Zenit St. Petersburg 2017-2021 and has played ', 'Bayer 04 Leverkusen since 2021'
    bundesliga.add_node(453, name='Justin Njinmah', club='Borussia Dortmund', 'Eimsbütteler TV 2017-2018, ',
                        'Holstein Kiel 2018-2021, ', 'SV Werder Bremen 2021-2022, ',
                        'Borussia Dortmund since 2022 and has played ', 'Borussia Dortmund II since 2022'
    bundesliga.add_node(454, name='Lennart Grill', club='1. FC Union Berlin', '1. FSV Mainz 05 2013-2016, ',
                        '1. FC Kaiserslautern 2016-2020, ', 'Bayer 04 Leverkusen 2020-2021, ',
                        'SK Brann Bergen 2021-2021, ', 'Bayer 04 Leverkusen 2022-2022 and has played ',
                        '1. FC Union Berlin since 2022'
    bundesliga.add_node(455, name='Patrick Herrmann', club='Borussia Mönchengladbach', 'FC Uchtelfangen 1995-2004, ',
                        '1. FC Saarbrücken 2004-2008 and has played ', " Borussia M'gladbach since 2008."
    bundesliga.add_node(456, name='Tobias Sippel', club='Borussia Mönchengladbach', 'SV 1911 Bad Dürkheim 1993-1998, ',
                        '1. FC Kaiserslautern 1998-2015, ', '1.FC Kaiserslautern II 1998-2015 and has played ',
                        " Borussia M'gladbach since 2015."
    bundesliga.add_node(457, name='Anthony Losilla', club='VfL Bochum', 'FC Pont Salomon 1992-1993, ',
                        'FCO Firminy 1993-1994, ', 'AS Saint Etienne 1994-2006, ', 'AS Cannes 2006-2008, ',
                        'Paris FC 2008-2010, ', 'Stade Lavallois MFC 2010-2012, ',
                        'SG Dynamo Dresden 2012-2014 and has played ', 'VfL Bochum 1848 since 2014'
    bundesliga.add_node(458, name='Nadiem Amiri', club='Bayer 04 Leverkusen', '1. FC Kaiserslautern 2009-2010, ',
                        'SV Waldhof Mannheim 2010-2012, ', 'TSG Hoffenheim 2012-2019, ',
                        'Bayer 04 Leverkusen 2019-2022, ', 'Genua CFC 1893 2022-2022 and has played ',
                        'Bayer 04 Leverkusen since 2022'
    bundesliga.add_node(459, name='Jae-sung Lee', club='1. FSV Mainz 05', 'Ulsan Okdong Elementary School 1999-2004, ',
                        'Haksung Middle School 2005-2007, ', 'Haksung High School 2008-2010, ',
                        'Korea University 2011-2013, ', 'Jeonbuk Hyundai Motors FC 2014-2018, ',
                        'Holstein Kiel 2018-2021 and has played ', '1. FSV Mainz 05 since 2021'
    bundesliga.add_node(460, name='Timo Baumgartl', club='1. FC Union Berlin', 'GSV Maichingen 2009-2010, ',
                        'SSV Reutlingen 2010-2011, ', 'VfB Stuttgart 2011-2019, ', 'VfB Stuttgart II 2011-2016, ',
                        'PSV Eindhoven 2019-2021 and has played ', '1. FC Union Berlin since 2021'
    bundesliga.add_node(461, name='Vasileios Lampropoulos', club='VfL Bochum', 'AE Chalandriou 2004-2006, ',
                        'Olympiacos CF Piräus 2006-2008, ', 'Apollon Kalamarias FC 2008-2009, ',
                        'Asteras Tripolis FC 2009-2010, ', 'GS Ilioupolis 2011-2011, ', 'Ethnikos Asteras 2011-2012, ',
                        'Panionios GSS Athen 2012-2014, ', 'AEK Athen FC 2014-2019, ',
                        'Deportivo La Coruna 2019-2020, ', 'VfL Bochum 1848 2020-2020, ',
                        'Deportivo La Coruna 2020-2020 and has played ', 'VfL Bochum 1848 since 2020'
    bundesliga.add_node(462, name='Marvin Friedrich', club='Borussia Mönchengladbach', 'FSC Guxhagen 2002-2008, ',
                        'OSC Vellmar 2008-2010, ', 'SC Paderborn 07 2010-2011, ', 'FC Schalke 04 2011-2016, ',
                        'FC Augsburg 2016-2018, ', '1. FC Union Berlin 2018-2022 and has played ',
                        " Borussia M'gladbach since 2022."
    bundesliga.add_node(463, name='Leon Reichardt', club='VfB Stuttgart'
    bundesliga.add_node(464, name='Edimilson Fernandes', club='1. FSV Mainz 05', 'FC Fully 2004-2007, ',
                        'FC Sion 2007-2016, ', 'West Ham United FC 2016-2018, ', 'ACF Florenz 2018-2019, ',
                        '1. FSV Mainz 05 2019-2021, ', 'DSC Arminia Bielefeld 2021-2022, ',
                        'Berner SC Young Boys 2022-2022 and has played ', '1. FSV Mainz 05 since 2022'
    bundesliga.add_node(465, name='Makoto Hasebe', club='Eintracht Frankfurt',
                        'Fujieda Higashi High School 1999-2001, ', 'Urawa Red Diamonds 2002-2008, ',
                        'VfL Wolfsburg 2008-2013, ', '1. FC Nürnberg 2013-2014 and has played ',
                        'Eintracht Frankfurt since 2014'
    bundesliga.add_node(466, name='Ayman Azhil', club='Bayer 04 Leverkusen', 'Bayer 04 Leverkusen 2008-2020, ',
                        'Bayer 04 Leverkusen U-Team 2019-2020, ', 'RKC Waalwijk 2020-2022 and has played ',
                        'Bayer 04 Leverkusen since 2022'
    bundesliga.add_node(467, name='Marius Bülter', club='FC Schalke 04', 'SV Brukteria Dreierwalde 2008-2009, ',
                        'SC Preußen Münster 2009-2011, ', 'FC Eintracht Rheine 2011-2013, ',
                        'SuS Neuenkirchen 2013-2014, ', 'SV Rödinghausen 2014-2018, ', '1. FC Magdeburg 2018-2019, ',
                        '1. FC Union Berlin 2019-2021 and has played ', 'FC Schalke 04 since 2021'
    bundesliga.add_node(468, name='Eren Dinkçi', club='SV Werder Bremen', 'ATSV Sebaldsbrück 2015-2017, ',
                        'SC Borgfeld 2017-2019 and has played ', 'SV Werder Bremen since 2019'
    bundesliga.add_node(469, name='Leon Goretzka', club='FC Bayern München', 'Werner SV Bochum 1999-2001, ',
                        'VfL Bochum 1848 2001-2013, ', 'FC Schalke 04 2013-2018 and has played ',
                        'FC Bayern München since 2018'
    bundesliga.add_node(470, name='Philipp Schulze', club='VfL Wolfsburg'
    bundesliga.add_node(471, name='Piero Hincapie', club='Bayer 04 Leverkusen',
                        'Guayaquil CS Norte America 2014-2014, ', 'Deportivo Azogues 2014-2014, ',
                        'Guayaquil CS Norte America 2015-2015, ', 'Deportivo Azogues 2015-2016, ',
                        'Independiente del Valle 2016-2020, ',
                        'Club Atletico Talleres Cordoba 2020-2021 and has played ', 'Bayer 04 Leverkusen since 2021'
    bundesliga.add_node(472, name='Alphonso Davies', club='FC Bayern München'
    bundesliga.add_node(473, name='Manuel Neuer', club='FC Bayern München', 'FC Schalke 04 1991-2011, ',
                        'FC Schalke 04 II 1991-2011 and has played ', 'FC Bayern München since 2011'
    bundesliga.add_node(474, name='Philipp Max', club='Eintracht Frankfurt', 'SC Baldham 2000-2003, ',
                        'TSV 1860 München 2003-2007, ', 'FC Bayern München 2007-2010, ', 'FC Schalke 04 2010-2014, ',
                        'Karlsruher SC 2014-2015, ', 'FC Augsburg 2015-2020, ',
                        'PSV Eindhoven 2020-2023 and has played ', 'Eintracht Frankfurt since 2023'
    bundesliga.add_node(475, name='Leroy Sané', club='FC Bayern München', 'SG Wattenscheid 09 2001-2005, ',
                        'FC Schalke 04 2005-2008, ', 'Bayer 04 Leverkusen 2008-2011, ', 'FC Schalke 04 2011-2016, ',
                        'Manchester City FC 2016-2020 and has played ', 'FC Bayern München since 2020'
    bundesliga.add_node(476, name='Kristian Pedersen', club='1. FC Köln', 'Ringsted IF 2014-2014, ',
                        'HB Köge 2014-2016, ', '1. FC Union Berlin 2016-2018, ',
                        'Birmingham City FC 2018-2022 and has played ', '1. FC Köln since 2022'
    bundesliga.add_node(477, name='Pascal Klemens', club='Hertha Berlin. He has played ', 'Hertha BSC since 2019'
    bundesliga.add_node(478, name='Oliver Christensen', club='Hertha Berlin',
                        'Odense Boldklub 2010-2021 and has played ', 'Hertha BSC since 2021'
    bundesliga.add_node(479, name='Sidi Sané', club='FC Schalke 04', 'SG Wattenscheid 09 2008-2009, ',
                        'Bayer 04 Leverkusen 2009-2011 and has played ', 'FC Schalke 04 since 2011'
    bundesliga.add_node(480, name='Fabio Chiarodia', club='SV Werder Bremen', 'VfL Oldenburg 2013-2014 and has played ',
                        'SV Werder Bremen since 2014'
    bundesliga.add_node(481, name='Mohamed Simakan', club='RB Leipzig', 'Vivaux Marronniers 2006-2009, ',
                        'FC Bruz 2009-2010, ', 'FC Rouguiere 2010-2011, ', 'Olympique de Marseille 2011-2014, ',
                        'JO Saint Gabriel 2015-2015, ', 'Sporting Club Air Bel 2015-2017, ',
                        'RC Strasbourg Alsace 2017-2021 and has played ', 'RB Leipzig since 2021'
    bundesliga.add_node(482, name='Ørjan Nyland', club='RB Leipzig', 'Volda TI 2006-2006, ', 'IL Hödd 2007-2012, ',
                        'Molde FK 2013-2015, ', 'FC Ingolstadt 04 2015-2018, ', 'Aston Villa FC 2018-2020, ',
                        'Norwich City FC 2021-2021, ', 'Bournemouth AFC 2021-2022, ',
                        'Reading FC 2022-2022 and has played ', 'RB Leipzig since 2022'
    bundesliga.add_node(483, name='Jan Olschowsky', club='Borussia Mönchengladbach',
                        'SV Glehn 2008-2009 and has played ', " Borussia M'gladbach since 2009."
    bundesliga.add_node(484, name='Almamy Touré', club='Eintracht Frankfurt',
                        'Esperance Sportive de Stains 2003-2004, ', 'FC Bourget 2004-2010, ',
                        'AS Monaco FC 2010-2019 and has played ', 'Eintracht Frankfurt since 2019'
    bundesliga.add_node(485, name='Niklas Dorsch', club='FC Augsburg', '1. FC Baiersdorf 2002-2006, ',
                        'Deutsch-Tschechische FS 2006-2009, ', '1. FC Nürnberg 2009-2012, ',
                        'FC Bayern München 2012-2018, ', '1. FC Heidenheim 1846 2018-2020, ',
                        'KAA Gent 2020-2021 and has played ', 'FC Augsburg since 2021'
    bundesliga.add_node(486, name='Pavao Pervan', club='VfL Wolfsburg', 'Favoritner AC 1997-2000, ',
                        'SC Team Wiener Linien 2000-2005, ', 'SV Schwechat 2005-2007, ', 'FC Lustenau 2007-2010, ',
                        'FC Pasching 2010-2010, ', 'LASK Linz 2010-2018 and has played ', 'VfL Wolfsburg since 2018'
    bundesliga.add_node(487, name='Simon Terodde', club='FC Schalke 04', 'SV Krechting 1991-1998, ',
                        'VfL Rhede 1998-2001, ', '1.FC Bocholt 2001-2002, ', 'MSV Duisburg 2002-2009, ',
                        'Fortuna Düsseldorf 2009-2009, ', '1. FC Köln 2009-2011, ', '1. FC Köln II 2009-2011, ',
                        '1. FC Union Berlin 2011-2014, ', 'VfL Bochum 1848 2014-2016, ', 'VfB Stuttgart 2016-2017, ',
                        '1. FC Köln 2018-2020, ', 'Hamburger SV 2020-2021 and has played ', 'FC Schalke 04 since 2021'
    bundesliga.add_node(488, name='Mio Backhaus', club='SV Werder Bremen', 'Kawasaki Frontale 2015-2017, ',
                        'Alemannia Aachen 2017-2018 and has played ', 'SV Werder Bremen since 2018'
    bundesliga.add_node(489, name='Jamie Bynoe-Gittens', club='Borussia Dortmund', 'Reading FC 2017-2018, ',
                        'Manchester City FC 2018-2020 and has played ', 'Borussia Dortmund since 2020'
    bundesliga.add_node(490, name='Henning Matriciani', club='FC Schalke 04', 'SuS Bad Westernkotten 2006-2014, ',
                        'DSC Arminia Bielefeld 2014-2016, ', 'SV Lippstadt 08 2016-2020 and has played ',
                        'FC Schalke 04 since 2020'
    bundesliga.add_node(491, name='Paul Grave', club='VfL Bochum', 'SV Westfalia Gemen 2006-2014 and has played ',
                        'VfL Bochum 1848 since 2014'
    bundesliga.add_node(492, name='Thomas Delaney', club='TSG 1899 Hoffenheim', 'KB Kopenhagen 1993-2009, ',
                        'FC Kopenhagen 2009-2016, ', 'SV Werder Bremen 2017-2018, ', 'Borussia Dortmund 2018-2021, ',
                        'Sevilla FC 2021-2023 and has played ', 'TSG Hoffenheim since 2023'
    bundesliga.add_node(493, name='Kingsley Coman', club='FC Bayern München', 'US Senart-Moissy 2002-2005, ',
                        'Paris Saint-Germain FC 2005-2014, ', 'Juventus FC Turin 2014-2015 and has played ',
                        'FC Bayern München since 2015'
    bundesliga.add_node(494, name='Ridle Baku', club='VfL Wolfsburg', '1. FSV Mainz 05 2007-2020 and has played ',
                        'VfL Wolfsburg since 2020'
    bundesliga.add_node(495, name='Eniss Shabani', club='1. FSV Mainz 05'
    bundesliga.add_node(496, name='Jean-Paul Boëtius', club='Hertha Berlin', 'Feyenoord Rotterdam 2000-2015, ',
                        'FC Basel 2015-2017, ', 'KRC Genk 2017-2017, ', 'Feyenoord Rotterdam 2017-2018, ',
                        '1. FSV Mainz 05 2018-2022 and has played ', 'Hertha BSC since 2022'
    bundesliga.add_node(497, name='András Schäfer', club='1. FC Union Berlin', 'Grundball PFC 2009-2010, ',
                        'VFC Haladas Szombathely 2010-2014, ', 'MTK Budapest 2014-2019, ', 'Genua CFC 1893 2019-2019, ',
                        'AC Chievo Verona 2019-2020, ', 'Genua CFC 1893 2020-2020, ',
                        'DAC Dunajska Streda 2020-2022 and has played ', '1. FC Union Berlin since 2022'
    bundesliga.add_node(498, name='Florian Dietz', club='1. FC Köln', 'TSV Großbardorf 2012-2013, ',
                        'FC Carl Zeiss Jena 2013-2018, ', 'SV Werder Bremen 2018-2019, ',
                        'SpVgg Unterhaching 2019-2020 and has played ', '1. FC Köln since 2020'
    bundesliga.add_node(499, name='Dikeni Salifou', club='SV Werder Bremen', 'FC Augsburg 2017-2022, ',
                        'FC Augsburg U 17 2019-2020 and has played ', 'SV Werder Bremen since 2022'
    bundesliga.add_node(500, name='Sebastian Andersson', club='1. FC Köln', 'Helsingborgs IF 2006-2007, ',
                        'Ängelholms FF 2008-2011, ', 'Kalmar FF 2012-2014, ', 'Djurgardens IF 2014-2016, ',
                        'IFK Norrköping 2016-2017, ', '1. FC Kaiserslautern 2017-2018, ',
                        '1. FC Union Berlin 2018-2020 and has played ', '1. FC Köln since 2020'
    bundesliga.add_node(501, name='Morten Thorsby', club='1. FC Union Berlin', 'IL Heming 2009-2009, ',
                        'FK Lyn Oslo 2010-2012, ', 'Stabaek IF 2012-2014, ', 'SC Heerenveen 2014-2019, ',
                        'Sampdoria Genua 2019-2022 and has played ', '1. FC Union Berlin since 2022'
    bundesliga.add_node(502, name='Alex Kral', club='FC Schalke 04', 'SK Moravska Slavia Brno 2004-2007, ',
                        'FC Zbrojovka Brno 2007-2012, ', 'SK Slavia Prag 2012-2017, ', 'FK Teplice 2017-2019, ',
                        'SK Slavia Prag 2019-2019, ', 'FC Spartak Moskau 2019-2021, ', 'West Ham United FC 2021-2022, ',
                        'FC Spartak Moskau 2022-2022 and has played ', 'FC Schalke 04 since 2022'
    bundesliga.add_node(503, name='Willi Orban', club='RB Leipzig', '1. FC Kaiserslautern 1997-2015 and has played ',
                        'RB Leipzig since 2015'
    bundesliga.add_node(504, name='Laurin Ulrich', club='VfB Stuttgart'
    bundesliga.add_node(504, name='Maxence Lacroix', club='VfL Wolfsburg', 'A.S. Les Croquants de Limeyrat 2006-2008, ',
                        'Esperance Sport. Montignacoise 2008-2011, ', 'FC Thenon Limeyrat Fossemagne 2011-2012, ',
                        'Trelissac Football Club 2012-2015, ', 'FC Sochaux 2015-2020 and has played ',
                        'VfL Wolfsburg since 2020'
    bundesliga.add_node(506, name='Gil Dias', club='VfB Stuttgart', 'Sporting CP Lissabon 2007-2008, ',
                        'Associacao Desportiva Sanjoane 2008-2013, ', 'Sporting Braga 2013-2014, ',
                        'AS Monaco FC 2014-2016, ', 'Varzim SC 2016-2016, ', 'Rio Ave FC 2016-2017, ',
                        'AS Monaco FC 2017-2017, ', 'ACF Florenz 2017-2018, ', 'Nottingham Forest FC 2018-2019, ',
                        'Olympiacos CF Piräus 2019-2019, ', 'AS Monaco FC 2019-2020, ', 'Granada CF 2020-2020, ',
                        'AS Monaco FC 2020-2020, ', 'Futebol Clube de Famalicao 2020-2021, ',
                        'SL Benfica Lissabon 2021-2023 and has played ', 'VfB Stuttgart since 2023'
    bundesliga.add_node(507, name='Silas Ostrzinski', club='Borussia Dortmund'
    bundesliga.add_node(508, name='Luca Unbehaun', club='Borussia Dortmund', 'Union Bergen 2006-2009, ',
                        'VfL Bochum 1848 2009-2016, ', 'Borussia Dortmund since 2016 and has played ',
                        'Borussia Dortmund II since 2016'
    bundesliga.add_node(509, name='Göktan Gürpüz', club='Borussia Dortmund'
    bundesliga.add_node(510, name='Éric Dina Ebimbe', club='Eintracht Frankfurt', 'AAS Sarcelles 2006-2012, ',
                        'Paris Saint-Germain FC 2012-2019, ', 'Le Havre AC 2019-2020, ', 'Dijon FCO 2020-2021, ',
                        'Paris Saint-Germain FC 2021-2022 and has played ', 'Eintracht Frankfurt since 2022'
    bundesliga.add_node(511, name='Niklas Süle', club='Borussia Dortmund', 'Rot-Weiss Walldorf 2005-2006, ',
                        'Eintracht Frankfurt 2006-2009, ', 'SV Darmstadt 98 2009-2009, ', 'TSG Hoffenheim 2010-2017, ',
                        'FC Bayern München 2017-2022 and has played ', 'Borussia Dortmund since 2022'
    bundesliga.add_node(512, name='Rune Jarstein', club='Hertha Berlin', 'Herkules IF 2001-2001, ',
                        'ODD Grenland 2002-2007, ', 'Rosenborg Trondheim 2008-2010, ',
                        'Viking Stavanger 2010-2013 and has played ', 'Hertha BSC since 2014'
    bundesliga.add_node(513, name='Ivan Sunjic', club='Hertha Berlin', 'NK Spansko Zagreb 2008-2009, ',
                        'NK Zagreb 2009-2012, ', 'GNK Dinamo Zagreb 2012-2016, ', 'NK Lokomotiva Zagreb 2016-2018, ',
                        'GNK Dinamo Zagreb 2018-2019, ', 'Birmingham City FC 2019-2022 and has played ',
                        'Hertha BSC since 2022'
    bundesliga.add_node(514, name='Randal Kolo', club='Eintracht Frankfurt', 'FC Villepinte 2004-2009, ',
                        'Tremblay Football Club 2009-2011, ', 'US Torcy 2012-2015, ', 'FC Nantes 2015-2019, ',
                        'US Boulogne 2019-2020, ', 'FC Nantes 2020-2022 and has played ',
                        'Eintracht Frankfurt since 2022'
    bundesliga.add_node(515, name='Nicolas Höfler', club='Sport-Club Freiburg', 'Herdwanger SV 2000-2001, ',
                        'SC Pfullendorf 2001-2005, ', 'SC Freiburg 2005-2011, ',
                        'FC Erzgebirge Aue 2011-2013 and has played ', 'SC Freiburg since 2013'
    bundesliga.add_node(516, name='Florian Kainz', club='1. FC Köln', 'FC Stattegg 1999-2000, ',
                        'SK Puntigamer Sturm Graz 2000-2014, ', 'SK Rapid Wien 2014-2016, ',
                        'SV Werder Bremen 2016-2019 and has played ', '1. FC Köln since 2019'
    bundesliga.add_node(517, name='Jordi Osei-Tutu', club='VfL Bochum', 'Reading FC 2014-2015, ',
                        'Arsenal FC 2015-2019, ', 'VfL Bochum 1848 2019-2020, ', 'Arsenal FC 2020-2020, ',
                        'Cardiff City 2020-2021, ', 'Arsenal FC 2021-2021, ', 'Nottingham Forest FC 2021-2022, ',
                        'Arsenal FC 2022-2022, ', 'Rotherham United FC 2022-2022, ',
                        'Arsenal FC 2022-2022 and has played ', 'VfL Bochum 1848 since 2022'
    bundesliga.add_node(518, name='Mehdi Loune', club='Eintracht Frankfurt'
    bundesliga.add_node(519, name='Jacek Góralski', club='VfL Bochum', 'Zawisza Bydgoszcz 2009-2011, ',
                        'MGLKS Victoria Koronowo 2011-2011, ', 'MKS Blekitni Gabin 2011-2011, ',
                        'Wisla Plock 2011-2015, ', 'SSA Jagiellonia Bialystok 2015-2017, ',
                        'PFC Ludogorets Razgrad 2017-2020, ', 'FC Kairat Almaty 2020-2022 and has played ',
                        'VfL Bochum 1848 since 2022'
    bundesliga.add_node(520, name='Davie Selke', club='1. FC Köln', '1.FC Normannia Gmünd 2008-2009, ',
                        'TSG Hoffenheim 2009-2013, ', 'SV Werder Bremen 2013-2015, ', 'RB Leipzig 2015-2017, ',
                        'Hertha BSC 2017-2020, ', 'SV Werder Bremen 2020-2021, ',
                        'Hertha BSC 2021-2023 and has played ', '1. FC Köln since 2023'
    bundesliga.add_node(521, name='Jere Uronen', club='FC Schalke 04', 'FC TPS Turku 2010-2011, ',
                        'Helsingborgs IF 2012-2016, ', 'KRC Genk 2016-2021, ',
                        'Stade Brestois 2021-2023 and has played ', 'FC Schalke 04 since 2023'
    bundesliga.add_node(522, name='Lucas Alario', club='Eintracht Frankfurt', 'Club San Lorenzo de Tostado 2007-2010, ',
                        'CA Colon de Santa Fe 2011-2015, ', 'CA River Plate 2015-2017, ',
                        'Bayer 04 Leverkusen 2017-2022 and has played ', 'Eintracht Frankfurt since 2022'
    bundesliga.add_node(523, name='Kevin Behrens', club='1. FC Union Berlin', 'ATS Buntentor 1995-2004, ',
                        'SC Weyhe 2004-2008, ', 'SV Werder Bremen 2008-2011, ', 'SV Wilhelmshaven 92 2011-2012, ',
                        'Hannover 96 2012-2014, ', 'Alemannia Aachen 2014-2015, ', 'Rot-Weiss Essen 2015-2015, ',
                        '1. FC Saarbrücken 2016-2018, ', 'SV Sandhausen 2018-2021 and has played ',
                        '1. FC Union Berlin since 2021'
    bundesliga.add_node(524, name='Chris Führich', club='VfB Stuttgart', 'SG Suderwich 2005-2006, ',
                        'FC Schalke 04 2006-2013, ', 'Borussia Dortmund 2013-2014, ', 'VfL Bochum 1848 2015-2015, ',
                        'Rot-Weiß Oberhausen 2015-2017, ', '1. FC Köln 2017-2019, ', 'Borussia Dortmund 2019-2020, ',
                        'SC Paderborn 07 2020-2021 and has played ', 'VfB Stuttgart since 2021'
    bundesliga.add_node(525, name='Timothée Kolodziejczak', club='FC Schalke 04',
                        'US St. Maurice Loos en Gohelle 1999-1999, ', 'CF Avion 1999-2000, ', 'RC Lens 2000-2008, ',
                        'Olympique Lyonnais 2008-2012, ', 'OGC Nice 2012-2014, ', 'Sevilla FC 2014-2017, ',
                        " Borussia M'gladbach 2017-2017, ", 'Tigres UANL 2017-2018, ',
                        'AS Saint Etienne 2018-2022 and has played ', 'FC Schalke 04 since 2022'
    bundesliga.add_node(526, name='Djibril Sow', club='Eintracht Frankfurt', 'BC Albisrieden 2007-2008, ',
                        'FC Zürich 2008-2015, ', " Borussia M'gladbach 2015-2017, ",
                        'Berner SC Young Boys 2017-2019 and has played ', 'Eintracht Frankfurt since 2019'
    bundesliga.add_node(527, name='Jeffrey Gouweleeuw', club='FC Augsburg', 'SC Heerenveen 2006-2013, ',
                        'AZ Alkmaar 2013-2016 and has played ', 'FC Augsburg since 2016'
    bundesliga.add_node(528, name='Jude Bellingham', club='Borussia Dortmund',
                        'Birmingham City FC 2010-2020 and has played ', 'Borussia Dortmund since 2020'
    bundesliga.add_node(529, name='Julius Schell', club='FC Schalke 04', 'TuS Graf Kobbo Tecklenburg 2006-2010, ',
                        'SC Preußen Lengerich 2010-2012, ', 'Borussia Dortmund 2012-2020, ',
                        'Rot-Weiß Koblenz 2020-2021 and has played ', 'FC Schalke 04 since 2021'
    bundesliga.add_node(530, name='Kingsley Schindler', club='1. FC Köln', 'SC Concordia Hamburg 2009-2011, ',
                        'Hannover 96 2011-2012, ', 'TSG Neustrelitz 2012-2013, ', 'TSG Hoffenheim 2013-2016, ',
                        'Holstein Kiel 2016-2019, ', '1. FC Köln 2019-2020, ', 'Hannover 96 2020-2021 and has played ',
                        '1. FC Köln since 2021'
    bundesliga.add_node(531, name='Faride Alidou', club='Eintracht Frankfurt', 'ESV Einigkeit Wilhelmsburg 2011-2012, ',
                        'Hamburger SV 2012-2022 and has played ', 'Eintracht Frankfurt since 2022'
    bundesliga.add_node(532, name='Danilo Soares', club='VfL Bochum', 'Gremio FB Porto Alegrense 2009-2010, ',
                        'SC Austria Lustenau 2010-2013, ', 'FC Ingolstadt 04 2013-2016, ',
                        'TSG Hoffenheim 2016-2017 and has played ', 'VfL Bochum 1848 since 2017'
    bundesliga.add_node(533, name='Jonathan Burkardt', club='1. FSV Mainz 05',
                        'SV Darmstadt 98 2009-2014 and has played ', '1. FSV Mainz 05 since 2014'
    bundesliga.add_node(534, name='Arne Maier', club='FC Augsburg', 'Ludwigsfelder FC 2006-2007, ',
                        'Hertha BSC 2007-2020, ', 'DSC Arminia Bielefeld 2020-2021, ',
                        'Hertha BSC 2021-2021 and has played ', 'FC Augsburg since 2021'
    bundesliga.add_node(535, name='Borna Sosa', club='VfB Stuttgart', 'GNK Dinamo Zagreb 2006-2018 and has played ',
                        'VfB Stuttgart since 2018'
    bundesliga.add_node(536, name='Karim Onisiwo', club='1. FSV Mainz 05'
    """

    numbernodes = bundesliga.number_of_nodes()
    print(numbernodes)

    for i in range(1, numbernodes+1):
        for j in range(1, numbernodes+1):

            if (bundesliga._node[i] == bundesliga._node[j]):
                break

            if (bundesliga._node[i].get('club') == bundesliga._node[j].get('club')):
                bundesliga.add_edge(i,j)
            if (bundesliga._node[i].get('y2013') == bundesliga._node[j].get('y2013')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2014') == bundesliga._node[j].get('y2014')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2015') == bundesliga._node[j].get('y2015')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2016') == bundesliga._node[j].get('y2016')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2017') == bundesliga._node[j].get('y2017')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2018') == bundesliga._node[j].get('y2018')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2019') == bundesliga._node[j].get('y2019')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2020') == bundesliga._node[j].get('y2020')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2021') == bundesliga._node[j].get('y2021')):
                bundesliga.add_edge(i, j)
            if (bundesliga._node[i].get('y2022') == bundesliga._node[j].get('y2022')):
                bundesliga.add_edge(i, j)

    playergroups=asyn_lpa_communities(bundesliga)
    players = []
    color_map = []

    position = nx.spring_layout(bundesliga)

    for player in playergroups:
        players.append(player)
    print(len(players))

    for node in bundesliga:
        if node in players[0]:
            color_map.append('blue')
        elif node in players[1]:
            color_map.append('red')
        elif node in players[2]:
            color_map.append('green')
        elif node in players[3]:
            color_map.append('yellow')
        elif node in players[4]:
            color_map.append('magenta')
        elif node in players[5]:
            color_map.append('pink')
        elif node in players[6]:
            color_map.append('brown')
        elif node in players[7]:
            color_map.append('cyan')
        elif node in players[8]:
            color_map.append('orange')
        elif node in players[9]:
            color_map.append('#228B22')
        elif node in players[10]:
            color_map.append('#F4A460')
        elif node in players[11]:
            color_map.append('#A020F0')

    nx.draw(bundesliga, pos=nx.spring_layout(bundesliga),node_color=color_map, with_labels=True)
    plt.show()
