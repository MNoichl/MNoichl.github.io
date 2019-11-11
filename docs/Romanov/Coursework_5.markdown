---
layout: page
title: Homework No. 5
has_children: false
parent: DH, Romanov, 2019
---


# Homework no. 5

Here's another Python-Screenshot.
![](2019-11-11.png)

## Regular expressions:

*A lot of these really depend on context. I think my solutions work reasonably well in the given document, but might yield false positives in other corpora.*

* \w*at\w*
* M[\w']*m\w+[\s\w-]{1,4}[GK][\w]+
* [IEH]\w+h[aā]n
* (Vienna\|Graz\|Linz\|Salzburg\|Innsbruck\|Klagenfurt\|Villach\|Wels\|Sankt Pölten\|Dornbirn\|Wiener Neustadt\|Steyr\|Feldkirch\|Bregenz\|Leonding\|  Klosterneuburg\|Baden bei Wien\|Wolfsberg\|Leoben\|Krems\|Traun\| Amstetten\|Lustenau\|Kapfenberg\|Mödling\|Hallein\|Kufstein\| Traiskirchen\|Schwechat\|Braunau am Inn\|Stockerau\|Saalfelden\| Ansfelden\|Tulln\|Hohenems\|Spittal an der Drau\|Telfs\|Ternitz\| Perchtoldsdorf\|Feldkirchen\|Bludenz\|Bad Ischl\|Eisenstadt\|Schwaz\|Hall in Tirol\|Gmunden\|Wörgl\|Wals-Siezenheim\| Marchtrenk\|Bruck an der Mur\|Sankt Veit an der Glan\| Korneuburg\|Neunkirchen\|Hard\|Vöcklabruck\|Lienz\|Rankweil\| Hollabrunn\|Enns\|Brunn am Gebirge\|Ried im Innkreis\|  Bad Vöslau\|Waidhofen\|Knittelfeld\|Trofaiach\|Mistelbach\|Zwettl\|Völkermarkt\|Götzis\|Sankt Johann im Pongau\| Gänserndorf\|Gerasdorf bei Wien\|Ebreichsdorf\|Bischofshofen\|  Groß-Enzersdorf\|Seekirchen am Wallersee\|Sankt Andrä)
* (Vienna\|Graz\|Linz\|    Salzburg\|Innsbruck\|Klagenfurt\|Villach\|Wels\|Sankt Pölten\|    Dornbirn\|Wiener Neustadt\|Steyr\|Feldkirch\|Bregenz\|Leonding\|  Klosterneuburg\|Baden bei Wien\|Wolfsberg\|Leoben\|Krems\|Traun\| Amstetten\|Lustenau\|Kapfenberg\|Mödling\|Hallein\|Kufstein\| Traiskirchen\|Schwechat\|Braunau am Inn\|Stockerau\|Saalfelden\| Ansfelden\|Tulln\|Hohenems\|Spittal an der Drau\|Telfs\|Ternitz\| Perchtoldsdorf\|Feldkirchen\|Bludenz\|Bad Ischl\|Eisenstadt\|    Schwaz\|Hall in Tirol\|Gmunden\|Wörgl\|Wals-Siezenheim\| Marchtrenk\|Bruck an der Mur\|Sankt Veit an der Glan\| Korneuburg\|Neunkirchen\|Hard\|Vöcklabruck\|Lienz\|Rankweil\| Hollabrunn\|Enns\|Brunn am Gebirge\|Ried im Innkreis\|  Bad Vöslau\|Waidhofen\|Knittelfeld\|Trofaiach\|Mistelbach\|Zwettl\|Völkermarkt\|Götzis\|Sankt Johann im Pongau\| Gänserndorf\|Gerasdorf bei Wien\|Ebreichsdorf\|Bischofshofen\|  Groß-Enzersdorf\|Seekirchen am Wallersee\|Sankt Andrä).{0,3}(Lower Austria\|Salzburg)