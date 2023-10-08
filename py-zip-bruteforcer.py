import zipfile
import threading

def unzip_with_password(zip_file_path, output_folder, password):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.setpassword(password)
            zip_ref.extractall(output_folder)
        return True
    except zipfile.BadZipFile:
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def try_passwords(zip_file_path, output_folder, password_list, thread_num, num_threads):
    password_count = len(password_list)
    start_index = thread_num * (password_count // num_threads)
    end_index = (thread_num + 1) * (password_count // num_threads)
    
    for i in range(start_index, end_index):
        password = password_list[i].strip()
        print(f"Thread-{thread_num} trying password: {password}")
        if unzip_with_password(zip_file_path, output_folder, password):
            print(f"Thread-{thread_num} extraction successful with password: {password}")
            return

def main():
    zip_file_path = input("Enter the path to the ZIP file: ")
    password_list_path = input("Enter the path to the password list file: ")
    output_folder = "out"

    # Read the password list
    with open(password_list_path, 'r') as password_file:
        password_list = password_file.readlines()

    num_threads = int(input("Enter the number of threads to use: "))
    threads = []
    
    for i in range(num_threads):
        thread = threading.Thread(target=try_passwords, args=(zip_file_path, output_folder, password_list, i, num_threads))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Extraction failed. None of the passwords worked.")

if __name__ == "__main__":
    main()
