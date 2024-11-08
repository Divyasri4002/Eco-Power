# cloud_analytics.py
import time

def send_data_to_cloud(data):
    print("Connecting to cloud...")
    time.sleep(1)
    print(f"Data sent to cloud: {data}")

if __name__ == "__main__":
    from biogas_production import ferment_materials
    data = {
        "filtered_emissions": ["NOx", "SOx"],
        "biogas": "biogas",
        "pest_control": "Natural pest control"
    }
    send_data_to_cloud(data)
