# Fake Data Generation, PII Scanning, and MySQL Loading

This repository automates the generation of synthetic data using the `Faker` library, scans for PII using `PIIScanner`, and loads the data into a MySQL database for secure storage and analysis.

---

## 📦 Features
- **Data Generation:** The `main.py` script generates synthetic data in CSV format across the following categories:
  - **Personal Data:** Aadhaar, PAN, SSN, Passport, UID, etc.
  - **Contact Data:** Email, Phone Number, Address, ZIP Code.
  - **Biometric Data:** IMEI, IMSI, UUID.
  - **Financial Data:** Credit Cards, Bank Accounts, GST, IFSC, UPI IDs.
  - **System Data:** IP, MAC Address, Username, Password.
  - **Demographic Data:** Gender, Nationality, Religion, Political Opinion.
  - **Health Data:** Medical License.
  - **Vehicle Data:** VIN.
  
- **PII Detection:** The `data_testing.py` script scans the CSV files for sensitive data using `PIIScanner`.
- **Database Loading:** The scanned data is loaded into a MySQL database (`faker_data`) with separate tables for each data type.

---

## 📊 Project Workflow
1. **Generate Data:** Run `main.py` to generate CSV files for each data category.
2. **Scan for PII:** Use `data_testing.py` to scan the generated CSV files.
3. **Load Data into MySQL:** Data is stored in a MySQL database named `faker_data`.

---

## 🛠️ Setup and Installation

### Prerequisites:
- Python 3.10+
- MySQL Server
- `pip` for Python packages

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
