import pandas as pd

def get_normalized_input(weightType: str, min_val: float, max_val: float) -> float:
    
    #Get user's desired value and convert it to importance weight
    
    # Prints current operation
    print(f"\n{weightType} specification range: {min_val:.1f} - {max_val:.1f}")
    
    while True:
        try:
            value = float(input(f"Enter your desired {weightType} value: ")) # Enter weight
            if min_val <= value <= max_val:
                
                # Convert desired value to normalized preference (0-1 scale)
                if weightType in ["Weight", "Price"]:  # Lower is better
                    # If user wants low value, give high importance weight
                    norm_preference = 1 - (value - min_val) / (max_val - min_val)
                
                else:  # Higher is better (RAM, Battery, Cameras, Screen)
                    # If user wants high value, give high importance weight  
                    norm_preference = (value - min_val) / (max_val - min_val)
                
                # Scale to 1-10 for weight calculation
                weight = 1 + (norm_preference * 9)  # 1-10 scale
                
                print(f"Your {weightType} preference: {value}")
                print(f"Converted to importance weight: {weight:.2f}/10")
                
                return weight
            
            else:
                print(f"Value out of range. Please enter between {min_val} and {max_val}")
        
        except ValueError:
            print("Please enter a valid number.")

def get_user_weights_phones(criteria_for_decision_phones, phone_specs):
    
    #Get user's desired phone specifications and convert to MCDM weights
    
    print("=== Phone Specification Input ===")
    print("Enter your desired specifications for each criterion.")
    print("The system will find phones that best match your preferences.\n")
    
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

    Weight = get_normalized_input("Weight", min_max_values["min"]["Weight"], min_max_values["max"]["Weight"])
    Ram = get_normalized_input("RAM", min_max_values["min"]["RAM"], min_max_values["max"]["RAM"])
    Battery_mAh = get_normalized_input("Battery mAh", min_max_values["min"]["Battery mAh"], min_max_values["max"]["Battery mAh"])
    #Price = get_normalized_input("Price", min_max_values["min"]["Price"], min_max_values["max"]["Price"])
    Front_Camera = get_normalized_input("Front Camera", min_max_values["min"]["Front Camera"], min_max_values["max"]["Front Camera"])
    Back_Camera = get_normalized_input("Back Camera", min_max_values["min"]["Back Camera"], min_max_values["max"]["Back Camera"])
    Screen_Size = get_normalized_input("Screen Size", min_max_values["min"]["Screen Size"], min_max_values["max"]["Screen Size"])

    # Normalize weights to sum to 1.0
    total = Weight + Ram + Battery_mAh + Front_Camera + Back_Camera + Screen_Size #+ Price
    
    normalized_weights = {
        "Weight": Weight / total,
        "RAM": Ram / total,
        "Battery mAh": Battery_mAh / total,
        #"Price": Price / total,
        "Front_Camera": Front_Camera / total,
        "Back_Camera": Back_Camera / total,
        "Screen_Size": Screen_Size / total
    }
    
    print("\n--- Your Preference Weights ---")
    for criterion, weight in normalized_weights.items():
        print(f"{criterion}: {weight:.3f} ({weight*100:.1f}%)")
    
    return normalized_weights




def calculate_alternative_score(phone_specs, normalized_weights_phones): # MOBILE------------------------------------MOBILE
    
    #Calculates the total weighted score for a single alternative.
    
    
    # 
    # score = (alternative['reliability_score'] * normalized_weights['reliability']) + ...
    #criteria_for_decision_phones = ["Weight", "RAM", "Battery mAh", "Price", "Front Camera", "Back Camera"]
    total_score = {}
    for x in phone_specs:
        score = (
            x['Weight']         * normalized_weights_phones['Weight'] +
            x['RAM']            * normalized_weights_phones['RAM'] +
            x['Battery mAh']    * normalized_weights_phones['Battery mAh'] +
            #x['Price']          * normalized_weights_phones['Price'] +
            x['Front Camera']   * normalized_weights_phones['Front_Camera']+
            x['Back Camera']    * normalized_weights_phones['Back_Camera'] +
            x['Screen Size']    * normalized_weights_phones['Screen_Size']
        )
        
        total_score[x['Model Name']] = score
    #print("Alternative Scores:", total_score)
    return total_score

     #Tidigare kod SLUT


def analyze_phone_specs_test(phone_specs):
    """Analyze the min/max of your test data"""
    
    # Extract numeric values from your data
    weights = [phone['Weight'] for phone in phone_specs]
    rams = [phone['RAM'] for phone in phone_specs]
    batteries = [phone['Battery mAh'] for phone in phone_specs]
    #prices = [phone['Price'] for phone in phone_specs]
    front_cameras = [phone['Front Camera'] for phone in phone_specs]
    back_cameras = [phone['Back Camera'] for phone in phone_specs]
    screen_sizes = [phone['Screen Size'] for phone in phone_specs]

    min_values = {
        'Weight': min(weights),
        'RAM': min(rams),
        'Battery mAh': min(batteries),
       # 'Price': min(prices),
        'Front Camera': min(front_cameras),
        'Back Camera': min(back_cameras),
        'Screen Size': min(screen_sizes)
    }

    max_values = {
        'Weight': max(weights),
        'RAM': max(rams),
        'Battery mAh': max(batteries),
       # 'Price': max(prices),
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
       
        #handle division by zero
        # low weight is valuable, 
        
        weight_norm = 0.5 if min_max['max']['Weight'] == min_max['min']['Weight'] else 1 - (phone['Weight'] - min_max['min']['Weight']) / (min_max['max']['Weight'] - min_max['min']['Weight'])
        #price_norm = 1 - (phone['Price'] - min_max['min']['Price']) / (min_max['max']['Price'] - min_max['min']['Price'])
        
        # High number is valuable
        # Handle division by zero when min == max
        ram_norm = 0.5 if min_max['max']['RAM'] == min_max['min']['RAM'] else (phone['RAM'] - min_max['min']['RAM']) / (min_max['max']['RAM'] - min_max['min']['RAM'])
        battery_norm = 0.5 if min_max['max']['Battery mAh'] == min_max['min']['Battery mAh'] else (phone['Battery mAh'] - min_max['min']['Battery mAh']) / (min_max['max']['Battery mAh'] - min_max['min']['Battery mAh'])
        camera_norm = 0.5 if min_max['max']['Front Camera'] == min_max['min']['Front Camera'] else (phone['Front Camera'] - min_max['min']['Front Camera']) / (min_max['max']['Front Camera'] - min_max['min']['Front Camera'])
        back_camera_norm = 0.5 if min_max['max']['Back Camera'] == min_max['min']['Back Camera'] else (phone['Back Camera'] - min_max['min']['Back Camera']) / (min_max['max']['Back Camera'] - min_max['min']['Back Camera'])
        screen_size_norm = 0.5 if min_max['max']['Screen Size'] == min_max['min']['Screen Size'] else (phone['Screen Size'] - min_max['min']['Screen Size']) / (min_max['max']['Screen Size'] - min_max['min']['Screen Size'])

        normalized_phone = {
            'Model Name': phone['Model Name'],
            'Company name': phone['Company name'],
            'Weight': weight_norm,
            'RAM': ram_norm,
            'Battery mAh': battery_norm,
           # 'Price': price_norm,
            'Front Camera': camera_norm,
            'Back Camera': back_camera_norm,
            'Screen Size': screen_size_norm
        }
        normalized_specs.append(normalized_phone)

        #Detta normaliserar varje skild telefon, så alla värden är mellan 0-1
    
    return normalized_specs




def run_mcdm_analysis_mobile(phone_specs, criteria_for_decision_phones): #NEW MOBILE
        
    #get notmalized Phone specs
    normalized_phone_specs = normalize_phone_specs(phone_specs)
    
    #Get user weights
    normalized_weights_phones_user = get_user_weights_phones(criteria_for_decision_phones, phone_specs) # + min max values

    #Calculate score
    scores = calculate_alternative_score(normalized_phone_specs, normalized_weights_phones_user)
    
    return [{'name': name, 'score': score} for name, score in sorted(scores.items(), key=lambda item: item[1], reverse=True)]


def filter_phones_by_price(phone_specs, max_price):
    
    #Get rows at- or below max price
    filtered_phones = [phone for phone in phone_specs if phone['Price'] <= max_price]
        
    return filtered_phones

def get_max_budget(phoneData):
    #Get min and max price from data
    prices = [phone['Price'] for phone in phoneData]
    
    # second lowest price to avoid Division by zero
    min_price = float(sorted(set(prices))[1])

    while True:
        try:
            budget = float(input(f"Enter your maximum budget. \n Smallest accepted value is {min_price}$:"))
            if min_price <= budget: #Check that budget is above minimum
                return budget
            else:
                print(f"Price too low\n Price automatically set to minimum value: {min_price}$")
                return min_price #Forcefully set budget to minimum
        except ValueError:
            print("Please enter a valid number.")




def get_phone_specs(): #Load in phone data

    #Create dataframe from CSV-file
    df = pd.read_csv('PhonesNew.csv', encoding='UTF-8', on_bad_lines='skip')

    #Create list of dictionaries from dataframe
    phone_specs_dict = []

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
            phone_specs_dict.append(phone_dict)


    return phone_specs_dict

# --- Main ---
if __name__ == "__main__":
    #Get phone specifications from CSV-file
    phone_specs_raw = get_phone_specs()

    #Set Max budget. All considered phones will be under this price 
    max_budget =get_max_budget(phone_specs_raw)

    #Filter phones by price, "phone_specs" contains the filtered listgit DD .
    phone_specs = filter_phones_by_price(phone_specs_raw, max_budget) 
    
    #Columns which will be used for evaluation
    criteria_for_decision_phones = ["Weight", "RAM", "Battery mAh", "Front Camera", "Back Camera", "Screen Size"] 
    
    print("Running the MCDM Analysis:")
    ranked_results_phones = run_mcdm_analysis_mobile(phone_specs, criteria_for_decision_phones)
    
    
    if ranked_results_phones:
        print("\n--- Top 5 Recommendations ---")
        for i, result in enumerate(ranked_results_phones[:5]):
            print(f"{i+1}. {result['name']} (Score: {result['score']:.2f})")
        
        print("\n--- Bottom 3 Recommendations ---")
        for i, result in enumerate(ranked_results_phones[-3:]):
            rank = len(ranked_results_phones) - 2 + i
            print(f"{rank}. {result['name']} (Score: {result['score']:.2f})")
        
        print(f"\nBased on your priorities, the **{ranked_results_phones[0]['name']}** is the recommended choice!")
       