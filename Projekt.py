# assignment2.py
import pandas as pd

def get_user_weights_phones(criteria_for_decision_phones, normalized_phone_specs): #prev min_max_values
    """
    Prompts the user to input weights for each criterion and normalizes them.
    Students must implement the logic to get input and normalize the weights.
    """
    def get_integer_input(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value:
                    return value
                else:
                    print("Please enter a value between 1 and 5.")
            except ValueError:
                print("Only integer values are accepted. Please try again.")
     #criteria_for_decision_phones = [
    # "Weight", 
    # "RAM", 
    # "Battery mAh", 
    # "Price", 
    # "Front Camera", 
    # "Back Camera"]
    
    min_max_values = {
        "min": {
            "Weight": min(phone['Weight'] for phone in phone_specs),
            "RAM": min(phone['RAM'] for phone in phone_specs),
            "Battery mAh": min(phone['Battery mAh'] for phone in phone_specs),
            "Price": min(phone['Price'] for phone in phone_specs),
            "Front Camera": min(phone['Front Camera'] for phone in phone_specs),
            "Back Camera": min(phone['Back Camera'] for phone in phone_specs),
            "Screen Size": min(phone['Screen Size'] for phone in phone_specs)
        },
        "max": {
            "Weight": max(phone['Weight'] for phone in phone_specs),
            "RAM": max(phone['RAM'] for phone in phone_specs),
            "Battery mAh": max(phone['Battery mAh'] for phone in phone_specs),
            "Price": max(phone['Price'] for phone in phone_specs),
            "Front Camera": max(phone['Front Camera'] for phone in phone_specs),
            "Back Camera": max(phone['Back Camera'] for phone in phone_specs),
            "Screen Size": max(phone['Screen Size'] for phone in phone_specs)
        }
    }
    
    print("Enter your absolute maximum budget. Devices above this price will be excluded:")
    max_budget = get_integer_input(f"Maximum Budget ($" + str(min_max_values["min"]["Price"]) + " - " + str(min_max_values["max"]["Price"]) + "): ")
    
    print("Enter minimum RAM required (GB). Devices with less RAM will be excluded:")
    min_ram = get_integer_input(f"Minimum RAM (" + str(min_max_values["min"]["RAM"]) + " - " + str(min_max_values["max"]["RAM"]) + " GB): ")
    
    print("Enter minimum battery capacity (mAh). Devices with smaller batteries will be excluded:")  
    min_battery = get_integer_input(f"Minimum Battery (" + str(min_max_values["min"]["Battery mAh"]) + " - " + str(min_max_values["max"]["Battery mAh"]) + " mAh): ")

    print("Please enter your priority (weight 1-10) for each criterion:")
    Weight          = get_integer_input(criteria_for_decision_phones[0] + " (" + str(min_max_values["min"]["Weight"]) + " - " + str(min_max_values["max"]["Weight"]) + ")")
    Ram             = get_integer_input(criteria_for_decision_phones[1] + " (" + str(min_max_values["min"]["RAM"]) + " - " + str(min_max_values["max"]["RAM"]) + ")")
    Front_Camera    = get_integer_input(criteria_for_decision_phones[4] + " (" + str(min_max_values["min"]["Front Camera"]) + " - " + str(min_max_values["max"]["Front Camera"]) + ")")
    Back_Camera     = get_integer_input(criteria_for_decision_phones[5] + " (" + str(min_max_values["min"]["Back Camera"]) + " - " + str(min_max_values["max"]["Back Camera"]) + ")")
    Battery_mAh     = get_integer_input(criteria_for_decision_phones[2] + " (" + str(min_max_values["min"]["Battery mAh"]) + " - " + str(min_max_values["max"]["Battery mAh"]) + ")")
    Screen_Size     = get_integer_input(criteria_for_decision_phones[6] + " (" + str(min_max_values["min"]["Screen Size"]) + " - " + str(min_max_values["max"]["Screen Size"]) + ")")
    Price           = get_integer_input(criteria_for_decision_phones[3] + " (" + str(min_max_values["min"]["Price"]) + " - " + str(min_max_values["max"]["Price"]) + ")")
    
    
    
    
    
    



    # Normalize the weights
    #total = int(Weight) + int(Ram) + int(Battery_mAh) + int(Price) + int(Front_Camera)
    total = float(Weight) + float(Ram) + float(Battery_mAh) + float(Price) + float(Front_Camera)
    
    """"
    if total > 0:
        Weight          =   int(Weight) / total
        Ram             =   int(Ram) / total
        Battery_mAh     =   int(Battery_mAh) / total
        Price           =   int(Price) / total
        Front_Camera    =   int(Front_Camera) / total"""

    if total > 0:
        Weight          =   float(Weight) / total
        Ram             =   float(Ram) / total
        Battery_mAh     =   float(Battery_mAh) / total
        Price           =   float(Price) / total
        Front_Camera    =   float(Front_Camera) / total
        Back_Camera     =   float(Back_Camera) / total
        Screen_Size     =   float(Screen_Size) / total

    normalized_weights = {
        "Weight":        Weight,
        "RAM":           Ram,
        "BatterymAh":   Battery_mAh,    # Changed from "BatterymAh" 
        "Price":         Price,
        "Front_Camera":  Front_Camera,
        "Back_Camera":   Back_Camera,
        "Screen_Size":   Screen_Size
    }
    #print("Normalized Weights:", normalized_weights)
    # print("\n--- Your normalized weights ---")
    # for n in normalized_weights:
    #     print(f"{n}: {normalized_weights[n]:.2f}" + "\n")

    return normalized_weights




def calculate_alternative_score(phone_specs, normalized_weights_phones): # MOBILE------------------------------------MOBILE
    """
    Calculates the total weighted score for a single alternative.
    Students must implement the scoring logic.
    """
    # TODO
    # score = (alternative['reliability_score'] * normalized_weights['reliability']) + ...
    #criteria_for_decision_phones = ["Weight", "RAM", "Battery mAh", "Price", "Front Camera", "Back Camera"]
    total_score = {}
    for x in phone_specs:
        score = (
            x['Weight']         * normalized_weights_phones['Weight'] +
            x['RAM']            * normalized_weights_phones['RAM'] +
            x['Battery mAh']    * normalized_weights_phones['BatterymAh'] +
            x['Price']          * normalized_weights_phones['Price'] +
            x['Front Camera']   * normalized_weights_phones['Front_Camera']+
            x['Back Camera']    * normalized_weights_phones['Back_Camera'] +
            x['Screen Size']    * normalized_weights_phones['Screen_Size']
        )
        
        total_score[x['Model Name']] = score
    #print("Alternative Scores:", total_score)
    return total_score




def analyze_phone_specs_test(phone_specs):
    """Analyze the min/max of your test data"""
    
    # Extract numeric values from your data
    weights = [phone['Weight'] for phone in phone_specs]
    rams = [phone['RAM'] for phone in phone_specs]
    batteries = [phone['Battery mAh'] for phone in phone_specs]
    prices = [phone['Price'] for phone in phone_specs]
    front_cameras = [phone['Front Camera'] for phone in phone_specs]
    back_cameras = [phone['Back Camera'] for phone in phone_specs]
    screen_sizes = [phone['Screen Size'] for phone in phone_specs]

    min_values = {
        'Weight': min(weights),
        'RAM': min(rams),
        'Battery mAh': min(batteries),
        'Price': min(prices),
        'Front Camera': min(front_cameras),
        'Back Camera': min(back_cameras),
        'Screen Size': min(screen_sizes)
    }

    max_values = {
        'Weight': max(weights),
        'RAM': max(rams),
        'Battery mAh': max(batteries),
        'Price': max(prices),
        'Front Camera': max(front_cameras),
        'Back Camera': max(back_cameras),
        'Screen Size': max(screen_sizes)
    }

    return {'min': min_values, 'max': max_values}


def normalize_phone_specs(phone_specs):
    """Normalize all phone specifications to 0-1 scale"""
    
    # Get min/max for normalization
    min_max = analyze_phone_specs_test(phone_specs) # ger lägsta och högsta värdet för varje kolumn
    
    normalized_specs = []
    
    for phone in phone_specs:
        # For "lower is better" criteria (Weight, Price), invert the normalization
        #tog bort = 1 - (phone...
        
        # låg vikt = högt värde
        weight_norm = 1 - (phone['Weight'] - min_max['min']['Weight']) / (min_max['max']['Weight'] - min_max['min']['Weight'])
        price_norm = 1 - (phone['Price'] - min_max['min']['Price']) / (min_max['max']['Price'] - min_max['min']['Price'])
        
        # For "higher is better" criteria (RAM, Battery, Camera)
        ram_norm = (phone['RAM'] - min_max['min']['RAM']) / (min_max['max']['RAM'] - min_max['min']['RAM'])
        battery_norm = (phone['Battery mAh'] - min_max['min']['Battery mAh']) / (min_max['max']['Battery mAh'] - min_max['min']['Battery mAh'])
        camera_norm = (phone['Front Camera'] - min_max['min']['Front Camera']) / (min_max['max']['Front Camera'] - min_max['min']['Front Camera'])
        back_camera_norm = (phone['Back Camera'] - min_max['min']['Back Camera']) / (min_max['max']['Back Camera'] - min_max['min']['Back Camera'])
        screen_size_norm = (phone['Screen Size'] - min_max['min']['Screen Size']) / (min_max['max']['Screen Size'] - min_max['min']['Screen Size'])

        normalized_phone = {
            'Model Name': phone['Model Name'],
            'Company name': phone['Company name'],
            'Weight': weight_norm,
            'RAM': ram_norm,
            'Battery mAh': battery_norm,
            'Price': price_norm,
            'Front Camera': camera_norm,
            'Back Camera': back_camera_norm,
            'Screen Size': screen_size_norm
        }
        normalized_specs.append(normalized_phone)

        #Detta normaliserar varje skild telefon, så alla värden är mellan 0-1
    
    return normalized_specs

def run_mcdm_analysis_mobile(phone_specs, criteria_for_decision_phones): #NEW MOBILE
    """
    Orchestrates the MCDA process.
    For this to be testable, it should RETURN the ranked list of alternatives.
    """
    # TODO
    phone_specs, criteria_for_decision_phones

    min_max_values = analyze_phone_specs_test(phone_specs)
    #print("Min/Max Values:", min_max_values)
    
    normalized_phone_specs = normalize_phone_specs(phone_specs)
    #normalized_weights_phones = get_user_weights_phones(criteria_for_decision_phones, min_max_values) # + min max values

    #print(normalized_phone_specs[0:5])  # Print first 5 normalized specs to verify

    normalized_weights_phones_user = get_user_weights_phones(criteria_for_decision_phones, normalized_phone_specs) # + min max values

    #Här sker Weight felet

    #scores = calculate_alternative_score(phone_specs, normalized_weights_phones)
    scores = calculate_alternative_score(normalized_phone_specs, normalized_weights_phones_user)
    #print("End Scores:", scores)


    return [{'name': name, 'score': score} for name, score in sorted(scores.items(), key=lambda item: item[1], reverse=True)]



def get_phone_specs():

    df = pd.read_csv('PhonesNew.csv', encoding='UTF-8', on_bad_lines='skip')

    phone_specs = []

    for i in range(len(df)):
            phone_dict = {
                'Company name': str(df["Company Name"].iloc[i]), 
                'Model Name': str(df["Model Name"].iloc[i]), 
                'Weight': int(df["Mobile Weight"].iloc[i]), 
                'RAM': int(df["RAM"].iloc[i]),
                'Front Camera': float(df["Front Camera"].iloc[i]),  
                'Back Camera': float(df["Back Camera"].iloc[i]), 
                'Battery mAh': int(df["Battery Capacity"].iloc[i]),
                'Screen Size': float(df["Screen size"].iloc[i]),  
                'Price': int(df["Launched Price (USA)"].iloc[i])
            }
            phone_specs.append(phone_dict)
    
    return phone_specs

# --- Main ---
if __name__ == "__main__":

    # phone_specs_test = [
    #     {'Company name': 'Poco', 'Model Name': 'Pad 5G 128GB', 'Weight': 571, 'RAM': 8, 'Front Camera': 8.0, 'Back Camera': 8.0, 'Battery mAh': 10000, 'Screen Size': 12.1, 'Price': 280}, 
    #     {'Company name': 'Poco', 'Model Name': 'Pad 5G 256GB', 'Weight': 571, 'RAM': 8, 'Front Camera': 8.0, 'Back Camera': 8.0, 'Battery mAh': 10000, 'Screen Size': 12.1, 'Price': 300}, 
    #     {'Company name': 'Huawei', 'Model Name': 'MatePad Pro 12.2 512GB', 'Weight': 508, 'RAM': 12, 'Front Camera': 16.0, 'Back Camera': 13.0, 'Battery mAh': 10100, 'Screen Size': 12.2, 'Price': 999}, 
    #     {'Company name': 'Huawei', 'Model Name': 'MatePad Pro 13.2 512GB', 'Weight': 580, 'RAM': 12, 'Front Camera': 16.0, 'Back Camera': 13.0, 'Battery mAh': 10100, 'Screen Size': 13.2, 'Price': 877}
    #     ]

    phone_specs = get_phone_specs() # this is good

    if(phone_specs):
        print("Successfully loaded phone specifications.")

    #print("Phone specs=", phone_specs[0:5])  # Print the first 5 phone specifications to verify


    #criteria_for_decision = ["Reliability", "Speed", "Maintenance Ease", "Energy Efficiency", "Cost"]
    criteria_for_decision_phones = ["Weight", "RAM", "Battery mAh", "Price", "Front Camera", "Back Camera", "Screen Size"]
    
    print("Running the MCDM Analysis:")
    #ranked_results = run_mcdm_analysis(espresso_machines, criteria_for_decision)
    ranked_results_phones = run_mcdm_analysis_mobile(phone_specs, criteria_for_decision_phones)

if ranked_results_phones:
    print("\n--- Top 5 Recommendations ---")
    for i, result in enumerate(ranked_results_phones[:5]):  # First 5 items
        print(f"{i+1}. {result['name']} (Score: {result['score']:.2f})")
    
    print("\n--- Bottom 5 Recommendations ---")
    for i, result in enumerate(ranked_results_phones[-5:]):  # Last 5 items
        rank = len(ranked_results_phones) - 4 + i  # Calculate actual rank
        print(f"{rank}. {result['name']} (Score: {result['score']:.2f})")
        #print(f"\nBased on your priorities, the **{ranked_results_phones[0]['name']}** is the recommended choice!")