# py-zip-bruteforcer

py-zip-bruteforcer is a Python script designed to brute force the password for a password-protected ZIP file. This tool allows you to recover the contents of a ZIP archive when you have a list of potential passwords.

## How it Works

The tool uses a simple brute force approach by trying each password from a provided password list until it successfully extracts the ZIP file or exhausts all the passwords in the list.

## Prerequisites

Before using py-zip-bruteforcer, make sure you have the following:

- Python installed on your system (version 3.x recommended).
- A password-protected ZIP file that you want to extract.
- A text file containing a list of potential passwords (one password per line) that you believe could unlock the ZIP file.

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where you have saved the "py-zip-bruteforcer" script.

4. Run the script by executing the following command:

   ```
   python py-zip-bruteforcer.py
   ```

5. Follow the prompts:

   - Enter the path to the ZIP file you want to extract.
   - Enter the path to the password list file (text file with one password per line).
   
   Example:
   
   ```
   Enter the path to the ZIP file: sample.zip
   Enter the path to the password list file: passwords.txt
   ```

6. The tool will start trying each password from the list. If a correct password is found, it will extract the contents of the ZIP file to a folder named "out."

7. If a successful password is found, the tool will display a message indicating the password that worked. If none of the passwords work, it will indicate that the extraction failed.

## Important Notes

- It's important to use this tool responsibly and only on ZIP files for which you have permission to attempt to recover the password.

- Make sure to have the necessary permissions to read the ZIP file and password list file.

- Be prepared to wait if the password list is extensive, as the tool will try each password one by one.

- This tool is designed for educational and ethical purposes. Unauthorized use of this tool to access protected content is illegal and unethical.

## Disclaimer

The author is not responsible for any misuse of this tool or any legal consequences that may arise from its use. Use this tool responsibly and only on files you have permission to access.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, or suggest improvements!

## Author
- Kepardev
- discord: `kepardev`
