# pest_control.py
def produce_pest_control(byproduct="biogas_residue"):
    print("Processing byproduct for pest control...")
    pest_control_product = f"Natural pest control from {byproduct}"
    print(f"Pest control product created: {pest_control_product}")
    return pest_control_product

if __name__ == "__main__":
    byproduct = "biogas_residue"
    pest_control_product = produce_pest_control(byproduct)
