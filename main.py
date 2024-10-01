import os
import sys
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# # linux
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service


# windows
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

# # linux
# options = Options()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()), options=options
# )


def main():
    def rem_chars(arg):
        return arg.split(", ")

    emailAdd = "redeks123456@gmail.com"
    pwd = "blessedacademy"

    if not len(sys.argv) > 1:
        print("no project number assigned")
        return

    def get_web_content():
        url = f"https://intranet.alxswe.com/projects/{sys.argv[1]}"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print("invalid url")
            return None
        driver.get(url)
        email = driver.find_element(By.ID, "user_email")
        password = driver.find_element(By.ID, "user_password")
        email.send_keys(emailAdd)
        password.send_keys(pwd)
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        folders = driver.find_elements(By.XPATH, '//li[contains(text(), "Directory:")]')
        files = driver.find_elements(By.XPATH, '//li[contains(text(), "File:")]')
        if not folders:
            folders = ["." for n in files]
        task_topics = driver.find_elements(
            By.XPATH, '//div[contains(@id, "task-num-")]'
        )
        comment_find = driver.find_elements(
            By.XPATH,
            '//li[contains(text(), "The first line of all your files should be exactly")]',
        )
        h1 = driver.find_element(By.CSS_SELECTOR, "h1")
        if comment_find:
            comment = comment_find[0].find_element(By.CSS_SELECTOR, "code")
        else:
            comment = {}
        for a, b in zip(folders, files):
            if a == ".":
                folder_p = "."
            else:
                folder_p = a.find_element(By.CSS_SELECTOR, "code").text
            file_p = b.find_element(By.CSS_SELECTOR, "code").text

            flp = rem_chars(file_p)
            for fileee in flp:
                path_parts = fileee.split("/")

                current_path = ""

                if len(path_parts) == 1:
                    if not os.path.exists(f"{folder_p}/{current_path}"):
                        os.mkdir(f"{folder_p}/{current_path}")
                        print("\n-------------FOLDER-------------")
                        print(f"{folder_p}/{current_path}")
                else:
                    for pthhh in path_parts[:-1]:
                        current_path = os.path.join(current_path, pthhh)
                        print(f"{folder_p}/{current_path}")
                        if not os.path.exists(f"{folder_p}/{current_path}"):
                            print("\n-------------FOLDER-------------")
                            os.makedirs(f"{folder_p}/{current_path}")

                filePath = os.path.join(*path_parts)
                completed_pth = f"{folder_p}/{filePath}"
                if not os.path.exists(completed_pth):
                    print(completed_pth)
                    with open(completed_pth, "w") as f:
                        try:
                            f.write(f"{comment.text}\n")
                        except AttributeError:
                            pass
                        if filePath.endswith(".py"):
                            f.write("'''")
                            f.write(h1.text)
                            f.write("'''\n")
                        elif filePath.endswith(".sql"):
                            f.write("-- ")
                            f.write(h1.text)
                            f.write("\n")
                    os.chmod(completed_pth, os.stat(completed_pth).st_mode | 0o100)

        with open(f"{folder_p}/README.md", "w") as f:
            f.write(f"# {h1.text}\n")
            f.write(f"Tasks\n")
            [
                f.write(f"### `{topic.find_element(By.CSS_SELECTOR, 'h3').text}`\n")
                for topic in task_topics
            ]

        driver.quit()

    get_web_content()


main()
