# assignment2.py

def get_user_weights(criteria_names):
    """
    Prompts the user to input weights for each criterion and normalizes them.
    Students must implement the logic to get input and normalize the weights.
    """
    # TODO
    # Hämta användarens inputs
    # Kom ihåg att normalizera dem efter!

    # Hjälpfunktion för att validera heltalsinput
    def get_integer_input(prompt):
        while True:
            try:
                value = int(input(prompt))
                if 1 <= value <= 10: 
                    return value
                else:
                    print("Please enter a value between 1 and 5.")
            except ValueError:
                print("Only integer values are accepted. Please try again.")

    print("Please enter your priority (weight 1-10) for each criterion:")
    reliability     = get_integer_input(criteria_names[0] + " (1-10): ") 
    speed           = get_integer_input(criteria_names[1] + " (1-10): ")
    maintenance     = get_integer_input(criteria_names[2] + " (1-10): ")
    energy          = get_integer_input(criteria_names[3] + " (1-10): ")
    cost            = get_integer_input(criteria_names[4] + " (1-10, 10 being very low-cost priority): ")

    # Normalize the weights
    total = int(reliability) + int(speed) + int(maintenance) + int(energy) + int(cost)
    if total > 0:
        reliability     =   int(reliability) / total
        speed           =   int(speed) / total
        maintenance     =   int(maintenance) / total
        energy          =   int(energy) / total
        cost            =   int(cost) / total

    normalized_weights = {
        "reliability":  reliability,
        "speed":        speed,
        "maintenance":  maintenance,
        "energy":       energy,
        "cost":         cost
    }
    #print("Normalized Weights:", normalized_weights)
    print("\n--- Your normalized weights ---")
    for n in normalized_weights:
        print(f"{n}: {normalized_weights[n]:.2f}" + "\n")

    return normalized_weights




def calculate_alternative_score(alternatives, normalized_weights):
    """
    Calculates the total weighted score for each alternative.
    Students must implement the scoring logic.
    """
    # TODO
    # score = (alternative['reliability_score'] * normalized_weights['reliability']) + ...
    total_score = {}
    for machine in alternatives:
        score = (
            machine['reliability_score']        * normalized_weights['reliability'] +
            machine['speed_score']              * normalized_weights['speed'] +
            machine['maintenance_ease_score']   * normalized_weights['maintenance'] +
            machine['energy_efficiency_score']  * normalized_weights['energy'] +
            machine['cost_score']               * normalized_weights['cost']
        )
        total_score[machine['name']] = score
    #print("Alternative Scores:", total_score)
    return total_score


def run_mcdm_analysis(alternatives, criteria_names):
    """
    Orchestrates the MCDA process.
    For this to be testable, it should RETURN the ranked list of alternatives.
    """
    # TODO
    alternatives # = phoneSpecs
    criteria_names # namn på input variabler 
    normalized_weights = get_user_weights(criteria_names)
    scores = calculate_alternative_score(alternatives, normalized_weights)
    #print("End Scores:", scores)


    return [{'name': name, 'score': score} for name, score in sorted(scores.items(), key=lambda item: item[1], reverse=True)]



# --- Main ---
if __name__ == "__main__":

    # "The alternatives" - I.e., vad som finns att välja bland
    espresso_machines = [
        {'name': "EspressoMaster 3000", 'cost_score': 4, 'reliability_score': 5, 'speed_score': 4, 'maintenance_ease_score': 4, 'energy_efficiency_score': 3},
        {'name': "BrewBot Pro", 'cost_score': 3, 'reliability_score': 4, 'speed_score': 5, 'maintenance_ease_score': 3, 'energy_efficiency_score': 4},
        {'name': "CafeMax Deluxe", 'cost_score': 5, 'reliability_score': 3, 'speed_score': 3, 'maintenance_ease_score': 5, 'energy_efficiency_score': 2},
        {'name': "GrindGuru Elite", 'cost_score': 2, 'reliability_score': 5, 'speed_score': 5, 'maintenance_ease_score': 2, 'energy_efficiency_score': 5}
    ]

    criteria_for_decision = ["Reliability", "Speed", "Maintenance Ease", "Energy Efficiency", "Cost"]
    
    print("Running the MCDM Analysis:")
    ranked_results = run_mcdm_analysis(espresso_machines, criteria_for_decision)

    if ranked_results:
        print("\n--- Ranked Recommendations ---")
        for i, result in enumerate(ranked_results):
            print(f"{i+1}. {result['name']} (Score: {result['score']:.2f})")
        print(f"\nBased on your priorities, the **{ranked_results[0]['name']}** is the recommended choice!")