import os
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

def log_to_excel(email, message):
    data = {
        'Timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        'Email': [email],
        'Message': [message]
    }

    df_new = pd.DataFrame(data)
    file_path = 'contact_submissions.xlsx'

    if os.path.exists(file_path):
        # Append without overwriting
        df_existing = pd.read_excel(file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_excel(file_path, index=False)
    else:
        # Create new file
        df_new.to_excel(file_path, index=False)