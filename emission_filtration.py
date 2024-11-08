# emission_filtration.py
import time

def capture_emissions():
    print("Capturing emissions...")
    emissions = ["CO2", "NOx", "SOx"]
    print(f"Emissions captured: {emissions}")
    return emissions

def filter_emissions(emissions):
    print("Filtering emissions...")
    filtered = [emission for emission in emissions if emission != "CO2"]
    print(f"Filtered emissions: {filtered}")
    return filtered

if __name__ == "__main__":
    emissions = capture_emissions()
    filtered_emissions = filter_emissions(emissions)
