[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sivoe5-y)
### **Uppgift 2: Upgradering! - Multi-Criteria Decision Analysis (MCDA)** 

 

**Mål:** DSS ska bli bättre, *The Daily Grind* måste köpa en ny Espresso maskin men behöver hjälp av oss för att ta beslutet av vilken det ska bli! Presentera era resultat och en kort reflektion i en `report.md` fil. 

 

**Krav:** 

 

1.  **Espresso maskiner (espresso_machines):** *finns färdigt* 

*	En dict av några maskiner 

 

2.  **Kriterier och vikter (criteria_for_decision):** *finns färdigt* 

    *   En lista på vad som är relevant 

 

 

    *   **`get_user_weights`:** Fråga användaren vad de prioriterar i sin espresso maskin (input) 

	* Kom ihåg att normalisera värderna (så de uppnår 1/100%). 

 

3.  **`calculate_alternative_score(alternative, weights)` Function:** 

    *   Funktionen tar emot `alternative` dict/object och de `normalized_weights` (från användaren). 

    *   Den beröknar sedan ett viktat värde för alla alternativ. 

    *   *Viktigt!:* `cost_score` (1-5, 5 är bästa värdet för enkelhetens skull). 

    *   `total_score = (alternative['reliability_score'] * weights['Reliability']) + ...` 

    *   Returnera `total_score`. 

 

4.  **`run_mcdm_analysis(alternatives, criteria_names)` Function:** 

	* *Multi-Criteria Decision-Making* 

    *   Kör allt: 

        *   Ta emot användarens preferenser. 

        *   Normalisera vikterna. 

        *   Gå igenom varje produkt/`alternative`: 

            *   Beräkna `total_score` med `calculate_alternative_score()`. 

            *   Spara namn och poäng, sortera, presentera och rekommendera det “bästa” (högst poäng) alternativet. 

 

**Example:** 

 

``` 

--- Espresso Machine Selection DSS --- 

Please enter your priority (weight 1-10) for each criterion: 

Reliability (1-10): 9 

Speed (1-10): 7 

Maintenance Ease (1-10): 8 

Energy Efficiency (1-10): 6 

Cost (1-10, 10 being very low-cost priority): 5 

 

Normalized Weights: 

  Reliability: 0.25 

  Speed: 0.19 

  Maintenance Ease: 0.22 

  Energy Efficiency: 0.17 

  Cost: 0.14 

 

Calculating scores for alternatives... 

 

Ranked Recommendations: 

1. EspressoMaster 3000 (Score: 4.25) 

2. BrewBot Pro (Score: 3.90) 

3. CafeMax Deluxe (Score: 3.50) 

 

Based on your priorities, the **EspressoMaster 3000** is the recommended choice! 

``` 