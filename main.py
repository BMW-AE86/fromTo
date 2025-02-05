import boto3
from fpdf import FPDF

# Step 1: Read email list from list.txt
with open("list.txt", "r") as file:
    email_list = file.read()

# Step 2: Format the email list (one per line)
formatted_emails = ",\n".join(email.strip() for email in email_list.split(",")) + ","

# Step 3: Generate a PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(200, 10, txt=formatted_emails, align='L')

# Save the PDF file
pdf_file_name = "Validate2,space.pdf"
pdf.output(pdf_file_name)

# Step 4: Upload PDF to Wasabi
wasabi_s3 = boto3.client(
    's3',
    endpoint_url='https://s3.wasabisys.com',  # Wasabi's S3 endpoint
    aws_access_key_id='ANLDS76GW5KOK4REGUYC',  # Replace with your Wasabi Access Key
    aws_secret_access_key='MmiG5F1DwpNMbtQQsD7Zkw95AhIJHzqXnIfXzimQ'  # Replace with your Wasabi Secret Key
)

bucket_name = "houssem"  # Replace with your Wasabi bucket name

try:
    wasabi_s3.upload_file(pdf_file_name, bucket_name, pdf_file_name)
    print(f"PDF '{pdf_file_name}' uploaded successfully to Wasabi bucket '{bucket_name}'.")
except Exception as e:
    print(f"Failed to upload PDF to Wasabi: {e}")

