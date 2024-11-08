# biogas_production.py
import time

def ferment_materials(filtered_emissions, cow_dung="cow_dung", garlic="garlic"):
    print("Starting fermentation process...")
    materials = filtered_emissions + [cow_dung, garlic]
    time.sleep(1)
    biogas = "biogas"
    print(f"Biogas produced from {materials}: {biogas}")
    return biogas

if __name__ == "__main__":
    from emission_filtration import filter_emissions, capture_emissions
    emissions = capture_emissions()
    filtered_emissions = filter_emissions(emissions)
    biogas = ferment_materials(filtered_emissions)
