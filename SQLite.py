import sqlite3

db = sqlite3.connect("app.db")

cr = db.cursor()

def commit_and_close():
    
    db.commit()
    db.close()
    print("Connection To Database Is Closed")

uid = 1

input_message = """
What do you want to do?
"s" => Show all Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

user_input = input(input_message).strip().lower()

commands_list = ["s", "a", "d", "u", "q"]

def show_skills():
    cr.execute(f"select * from skills where user_id = '{uid}'")

    results = cr.fetchall()

    print(f"You have {len(results)} Skills.")

    if len(results) > 0:
        
        print("Showing Skills with Progress: ")

    for row in results:
        print(f"Skill => {row[0]},", end=" ")

        print(f"Progress => {row[1]}%")

    commit_and_close()

def add_skills():
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")

    results = cr.fetchone()

    if results == None:
        prog = input("Write Skill Progress").strip()
        cr.execute(
            f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")

    else:
        print("You Can Not Add It")
    prog = input("Write Skill Progress").strip()
    cr.execute(
        f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")
    
    commit_and_close()

    

def delete_skills():
    sk = input("Write Skill Name: ").strip().capitalize()
    
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
    
    commit_and_close()

def update_skills():
    sk = input("Write Skill Name: ").strip().capitalize()
    prog = input("Write The New Skill Progress").strip()
    cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
    
    commit_and_close()



if user_input in commands_list:
    print(f"Commands Found {user_input}")

    if user_input =="s":
        show_skills()

    elif user_input == "a":
        add_skills()

    elif user_input == "d":
        delete_skills()

    elif user_input == "u":
        update_skills()

    else :
        print("App is Closed.")
        commit_and_close()

else:
    print(f"Sorry This Command \"{user_input}\" Is Not Found")

my_tuple = ('Pascal', '65', 4)

cr.execute("insert into skills values(?, ?, ?)", my_tuple)

cr.execute("select * from skills where user_id not in(1, 2, 3)")

results = cr.fetchall()

for row in results:
    print(f"Skill Name => {row[0]},", end=" ")
    print(f"Skill Progress => {row[1]},", end=" ")
    print(f"User ID => {row[2]}")

db.commit()

db.close()

import string 
import random

print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
def make_serial(count):
    all_chars = string.ascii_letters + string.digits
    print(all_chars)

    chars_count = len(all_chars)
    print(chars_count)

    serial_list = []

    while count > 0:
        random_number = random.randint(0, chars_count - 1)

        random_character = all_chars[random_number]

        serial_list.append(random_character)

        count -= 1

    print("".join(serial_list))







make_serial(10)

############ WEBSCRAPING CONTROL BROWSER #################

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
options = Options()
options.add_argument("--window-size=1200,800")

# Start Chrome browser
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

# Open Wikipedia
browser.get("https://www.wikipedia.org")

try:
    wait = WebDriverWait(browser, 10)

    # ✅ Wait for the search input to appear and type in it
    search_input = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_input.send_keys("Front-End Developer")
    print("✅ Typed into search.")

    time.sleep(5)  # Wait before clicking search

    # ✅ Wait for the search button and click it
    search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    search_btn.click()
    print("✅ Clicked search button.")

    time.sleep(5)  # Wait before clicking the search result

    # ✅ Wait and click the first search result (if redirected to search results page)
    first_result = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.mw-search-results li.mw-search-result a"))
    )
    first_result.click()
    print("✅ Clicked first search result.")

    time.sleep(5)  # Wait before scraping content

    # ✅ Get the article title
    title = wait.until(EC.presence_of_element_located((By.ID, "firstHeading")))
    print("📘 Article title:", title.text)

    # ✅ Get the first paragraph
    first_paragraph = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.mw-parser-output > p"))
    )
    print("📝 First paragraph:\n", first_paragraph.get_attribute('innerText'))

except Exception as e:
    print("❌ Error:", e)

# Close the browser and end the session
browser.quit()





