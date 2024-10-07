import PyPDF2

def decrypt_pdf(input_pdf, output_pdf, password):
    # Open the input PDF file in read-binary mode
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Check if the PDF is encrypted
        if reader.is_encrypted:
            # Try to decrypt the PDF with the given password
            reader.decrypt(password)
        
        # Create a new PDF writer object
        writer = PyPDF2.PdfWriter()
        
        # Add all the pages to the writer
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])
        
        # Write the output PDF file without the password
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)
    
    print(f"Decrypted PDF saved as '{output_pdf}'.")

# Example usage
input_pdf = "encrypted.pdf"
output_pdf = "decrypted.pdf"
password = "your_password"

decrypt_pdf(input_pdf, output_pdf, password)
