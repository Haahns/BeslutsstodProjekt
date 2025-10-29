# Beslutsstödsystem och verifikation (2025-2026)
# Projekt Rapport<br> Jakob Hahnsson<br>22.10.2025

## Innehåll <br> <br> 1. Data <br>2. Exploratory Data Analysis (EDA)<br>     3. Rekommendationssystem (MCDA) <br> 4. Reflektion

# 1. Data

Mitt projekt baserar sig på ett dataset med 888 mobiltelefoner och surfplattor.
https://www.kaggle.com/datasets/abdulmalik1518/mobiles-dataset-2025<br>
Uppdaterat 18.02.2025<br><br>
Datan omfattar: <br>
> Företag (Namn)<br>
Modell (Namn)<br>
Vikt (g)<br>
RAM (GB)<br>
Framkamera (Mp)<br>
Bakkamera (Mp)<br>
Processor (Namn)<br>
Skärmstorlek (tum)<br>
Lanseringspris ($)<br>
Utgivningsår<br>

# 2. Exploratory Data Analysis (EDA)
## Fördelningen av märken
Det är tydligt att Alla märken på marknaden inte representeras korrekt.<br>
Google Pixel representeras t.ex endast med två modeller i datasettet. 
<br><img src="EDA\Företag.png" alt="Scatter Plot">

# <br>
## Utgivningsår
Datasettet är utgivet i februari 2025.<br>
Telefoner från år 2024 framkommer mest, medan tidigare års representation gradvis minskar 
<br><img src="EDA\Year.png" alt="Scatter Plot">

## Samband

### Låt oss titta på hur olika förhållanden mellan två parametrar <br> ser ut i ett sambandsdiagram (Scatterplot)<br>

Här ser vi Y: Pris och X: skärmstorlek<br>
Telefoner och surefplattor skiljer sig tydligt.<br>
Vi ser även att den mest representerade sektorn omfattar telefoner kring ~6,5" för ~300-400$<br>
Märk hur det finns tydliga linjer i både X- och Y-led
<br><img src="EDA\pris_skärm.png" alt="Scatter Plot"><br>

Om vi zoomar in på intervallen 500-1000€ ser vi tydliga prisområden för varje 50$, där majoriteten är prissatta på jämna hundratal. (..49$ och ..99$ i själva verket).<br>
Även skärmstorleken tenderar gå i hopp mellan jämna eller .5 tum
<br><img src="EDA\pris_skärm_500-1000.png" alt="Scatter Plot">

### Andra samband
Skärmstorlek i förhållande till vikt följer en klar linje
<br><img src="EDA\skärm_vikt.png" alt="Scatter Plot">
<br><br>Skärmstorlek i förhållande till batteri följer även en linje, <br>

Med undantag för batteri satsningen för ~7" telefoner
<br><img src="EDA\skärm_batteri.png" alt="Scatter Plot">
<br> Pris i förhållande till batteri sprider sig brett
<br><img src="EDA\pris_batterimAh.png" alt="Scatter Plot">

# <br>3. Rekommendationssystem (MCDA)

Mitt rekommendationsystem är till grunden ett MCDA System.
programmet frågar användaren efter en max budget och sedan telefonspecs.
Programmet ger användaren den bästa telefonen inom budgeten.

<br>
Programmet fungerar helt okej.<br>
I MCDA kan det finnas object som ofta får mycket höga betyg.<br> Detta har jag kunna eliminera med budgeten, då de största tabbarna alltid fick mest poäng oberoende användarens önskemål<br>