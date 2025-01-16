import random
import string
from faker import Faker
import pandas as pd 

fake = Faker()
#Comment for MINOR CHANGES for semantic versioning
#Function to generate rupay card number in financial data
def generate_rupay_card():
    return "RU" + ''.join(random.choices("0123456789", k=16)) 

#Function to generate vehicle identification number
def generate_vin():
    allowed_characters = string.ascii_uppercase.replace('I', '').replace('O', '').replace('Q', '') + string.digits
    return ''.join(random.choices(allowed_characters, k=17))


# Function to generate personal identification data
def personal_Identification(n=4000):
    personal_identification_formats = {
        "AADHAAR": lambda: f"{fake.random_int(min=100000000000, max=999999999999)}",
        "PASSPORT": lambda: f"{fake.random_int(min=100000, max=999999)}", 
        "DRIVERLICENSE": lambda: fake.bothify(text='??######??'),
        "VOTERID": lambda: f"{fake.random_int(min=100000000000, max=999999999999)}",
        "SSN": lambda: f"{fake.ssn()}",
        "UID": lambda: f"{fake.random_int(min=100000000, max=999999999)}",
        "PAN": lambda: fake.bothify(text='?????######'),
        "VID": lambda: fake.random_int(min=1000000000, max=9999999999),
        "RATION_CARD_NUMBER": lambda: fake.random_int(min=1000000, max=9999999),
    }
    return pd.DataFrame([
        {key: value() for key, value in personal_identification_formats.items()}
        for i in range(n)
    ])

#Function to generate contact data
def contact_info(n=4000):
    fake_contact_data = {
        "ADDRESS": lambda: fake.address(),
        "EMAIL_ADDRESS": lambda: fake.email(),
        "PHONE_NUMBER": lambda: fake.phone_number(),
        "POBOX": lambda: fake.zipcode(),
        "ZIPCODE": lambda: fake.zipcode(),
        "LOCATION": lambda: fake.city(),
    }
    
    return pd.DataFrame([
        {key: value() for key, value in fake_contact_data.items()}
        for i in range(n)
    ])


# Function to generate biometric data
def biometric_data(n=4000):
    biometric_data_formats = {
        "BIOMETRIC": lambda: fake.uuid4(),
        "IMEI": lambda: ''.join(random.choices(string.digits, k=15)),
        "IMSI": lambda: ''.join(random.choices(string.digits, k=15)),
    }

    return pd.DataFrame([
        {key: value() for key, value in biometric_data_formats.items()}
        for i in range(n)
    ])

# Function to generate financial information
def financial_info(n=4000):
    financial_data_formats = {
        "BANK_ACCOUNT_NUMBER": lambda: fake.iban(),
        "BANK_CARD": lambda: fake.credit_card_number(),
        "CREDIT_CARD": lambda: fake.credit_card_number(),
        "AMEX_CARD": lambda: fake.credit_card_number(card_type='amex'),
        "MAESTRO_CARD": lambda: fake.credit_card_number(card_type='maestro'),
        "RUPAY_CARD": lambda: generate_rupay_card(),
        "VISA_CARD": lambda: fake.credit_card_number(card_type='visa'),
        "MASTER_CARD": lambda: fake.credit_card_number(card_type='mastercard'),
        "CVV": lambda: fake.credit_card_security_code(),
        "PAYMENTCARD": lambda: fake.credit_card_number(),
        "UPI_ID": lambda: fake.user_name(),
        "GST_NUMBER": lambda: fake.bothify(text='##????###'),
        "IFSC": lambda: fake.bothify(text='???#####'),
    }
    return pd.DataFrame([
        {key: value() for key, value in financial_data_formats.items()}
        for _ in range(n)
    ])

# Function to generate system data
def system_data(n=4000):
    system_data_formats = {
        "IP_ADDRESS": lambda: fake.ipv4(),
        "MAC_ADDRESS": lambda: fake.mac_address(),
        "DATE_TIME": lambda: fake.date_time(),
        "USERNAME": lambda: fake.user_name(),
        "USER_NAME": lambda: fake.user_name(),
        "PASSWORD": lambda: fake.password(),
    }
    return pd.DataFrame([
        {key: value() for key, value in system_data_formats.items()}
        for _ in range(n)
    ])

# Function to generate demographic data
def demographic_data(n=4000):
    demographic_data_formats = {
        "GENDER": lambda: fake.random_element(['Male', 'Female']),
        "NATIONALITY": lambda: fake.country(),
        "RELIGION": lambda: fake.random_element(['Christianity', 'Islam', 'Hinduism', 'Buddhism']),
        "POLITICAL_OPINION": lambda: fake.random_element(['Liberal', 'Conservative', 'Libertarian']),
        "SEXUAL_ORIENTATION": lambda: fake.random_element(['Heterosexual', 'Homosexual', 'Bisexual']),
        "TITLE": lambda: fake.prefix(),
        "PERSON": lambda: fake.name(),
    }
    return pd.DataFrame([
        {key: value() for key, value in demographic_data_formats.items()}
        for _ in range(n)
    ])

# Function to generate health data
def health_data(n=4000):
    health_data_formats = {
        "MEDICAL_LICENSE": lambda: fake.bothify(text='??####???'),
    }
    return pd.DataFrame([
        {key: value() for key, value in health_data_formats.items()}
        for _ in range(n)
    ])

# Function to generate vehicle data
def vehicle_data(n=4000):
    vehicle_data_formats = {
        "VEHICLE_IDENTIFICATION_NUMBER": lambda: generate_vin(),
    }
    return pd.DataFrame([
        {key: value() for key, value in vehicle_data_formats.items()}
        for _ in range(n)
    ])

# Getting the datasets
personal_data = personal_Identification()
contact_data = contact_info()
biometric_info = biometric_data()
financial_data = financial_info()
system_info = system_data()
demographic_info = demographic_data()
health_info = health_data()
vehicle_info = vehicle_data()

# Converting to required formats
personal_data.to_csv("Personal_Data.csv")
contact_data.to_csv("Contact_Data.csv")
biometric_info.to_csv("Biometric_Data.csv")
financial_data.to_csv("Financial_Data.csv")
system_info.to_csv("System_Data.csv")
demographic_info.to_csv("Demographic_Data.csv")
health_info.to_csv("Health_Data.csv")
vehicle_info.to_csv("Vehicle_Data.csv")