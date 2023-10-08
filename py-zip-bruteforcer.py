import zipfile

def unzip_with_password(zip_file_path, output_folder, password):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Set the password to extract files from the ZIP archive
            zip_ref.setpassword(password)
            
            # Extract all files to the specified output folder
            zip_ref.extractall(output_folder)
            
        return True
    except zipfile.BadZipFile:
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    zip_file_path = input("Enter the path to the ZIP file: ")
    password_list_path = input("Enter the path to the password list file: ")
    output_folder = "out"

    # Try each password from the list
    with open(password_list_path, 'r') as password_file:
        for line in password_file:
            password = line.strip()
            print(f"Trying password: {password}")
            if unzip_with_password(zip_file_path, output_folder, password):
                print(f"Extraction successful with password: {password}")
                break
        else:
            print("Extraction failed. None of the passwords worked.")

if __name__ == "__main__":
    main()
