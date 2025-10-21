# Debug test for BrewBot Pro scoring
espresso_machines = [
    {'name': "EspressoMaster 3000", 'cost_score': 4, 'reliability_score': 5, 'speed_score': 4, 'maintenance_ease_score': 4, 'energy_efficiency_score': 3},
    {'name': "BrewBot Pro", 'cost_score': 3, 'reliability_score': 4, 'speed_score': 5, 'maintenance_ease_score': 3, 'energy_efficiency_score': 4},
    {'name': "CafeMax Deluxe", 'cost_score': 5, 'reliability_score': 3, 'speed_score': 3, 'maintenance_ease_score': 5, 'energy_efficiency_score': 2},
    {'name': "GrindGuru Elite", 'cost_score': 2, 'reliability_score': 5, 'speed_score': 5, 'maintenance_ease_score': 2, 'energy_efficiency_score': 5}
]

# Simulate BrewBot Pro exact input: reliability=4, speed=5, maintenance=3, energy=4, cost=3
# Total = 4+5+3+4+3 = 19
# Normalized weights:
reliability_weight = 4/19
speed_weight = 5/19
maintenance_weight = 3/19
energy_weight = 4/19
cost_weight = 3/19

print("BrewBot Pro exact weights:")
print(f"Reliability: {reliability_weight:.4f}")
print(f"Speed: {speed_weight:.4f}")
print(f"Maintenance: {maintenance_weight:.4f}")
print(f"Energy: {energy_weight:.4f}")
print(f"Cost: {cost_weight:.4f}")
print()

# Calculate scores for each machine
for machine in espresso_machines:
    score = (
        machine['reliability_score'] * reliability_weight +
        machine['speed_score'] * speed_weight +
        machine['maintenance_ease_score'] * maintenance_weight +
        machine['energy_efficiency_score'] * energy_weight +
        machine['cost_score'] * cost_weight
    )
    print(f"{machine['name']}: {score:.4f}")
    
    # Show calculation for BrewBot Pro
    if machine['name'] == "BrewBot Pro":
        print(f"  BrewBot Pro calculation:")
        print(f"  {machine['reliability_score']} * {reliability_weight:.4f} = {machine['reliability_score'] * reliability_weight:.4f}")
        print(f"  {machine['speed_score']} * {speed_weight:.4f} = {machine['speed_score'] * speed_weight:.4f}")
        print(f"  {machine['maintenance_ease_score']} * {maintenance_weight:.4f} = {machine['maintenance_ease_score'] * maintenance_weight:.4f}")
        print(f"  {machine['energy_efficiency_score']} * {energy_weight:.4f} = {machine['energy_efficiency_score'] * energy_weight:.4f}")
        print(f"  {machine['cost_score']} * {cost_weight:.4f} = {machine['cost_score'] * cost_weight:.4f}")