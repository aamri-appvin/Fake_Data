import time
import asyncio
import nltk
import os
from pii_scanner.scanner import PIIScanner
from pii_scanner.constants.patterns_countries import Regions

# Ensure the necessary nltk datasets are downloaded
nltk.data.path.extend([
    os.path.expanduser('~/nltk_data'),
    '/usr/share/nltk_data',
    '/usr/local/share/nltk_data',
    os.path.join(os.path.dirname(__file__), 'nltk_data')
])

def verify_nltk_requirements():
    required = [
        'punkt',
        'averaged_perceptron_tagger',
        'maxent_ne_chunker',
        'words',
        'averaged_perceptron_tagger_eng'
    ]
    for package in required:
        try:
            print(f"Verifying {package}...")
            nltk.download(package, quiet=True)
        except Exception as e:
            print(f"Error downloading {package}: {str(e)}")

async def scan_csv_file(file_path, scanner):
    """Scan a single CSV file and print results."""
    try:
        print(f"\nScanning file: {file_path}")
        results = await scanner.scan(
            file_path=file_path,
            sample_size=50,  
            region=Regions.IN 
        )
        
        # Updated result handling logic
        print(f"\nResults for {file_path}:")
        for pii_type, details in results.items():
            print(f"\n{pii_type}:")
            # Check if results are string-based or a list of dicts
            if isinstance(details, list):
                for item in details:
                    if isinstance(item, dict) and 'value' in item and 'score' in item:
                        print(f"  - Value: {item['value']}, Score: {item['score']}")
                    else:
                        print(f"  - {item}")  # If it's just a string, print directly
            else:
                print(f"  - {details}")  # If results are not lists, print directly

    except Exception as e:
        print(f"Error scanning {file_path}: {e}")
        import traceback
        traceback.print_exc()

async def run_scan():
    start_time = time.time()
    verify_nltk_requirements()

    # Initialize PIIScanner
    pii_scanner = PIIScanner()

    # List of CSV files to scan
    csv_files = [
        "Biometric_Data.csv",
        "Demographic_Data.csv",
        "Contact_Data.csv",
        "Financial_Data.csv",
        "Health_Data.csv",
        "Personal_Data.csv",
        "System_Data.csv",
        "Vehicle_Data.csv"
    ]

    # Base directory where the CSV files are stored
    base_dir = "/home/dell/Documents/Task2/"

    # Loop through each CSV and scan it
    tasks = []
    for file_name in csv_files:
        file_path = os.path.join(base_dir, file_name)
        if os.path.exists(file_path):
            tasks.append(scan_csv_file(file_path, pii_scanner))
        else:
            print(f"File not found: {file_path}")

    # Execute all scans concurrently
    await asyncio.gather(*tasks)

    print(f"\nTotal Execution Time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(run_scan())
