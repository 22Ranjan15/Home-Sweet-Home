import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, WebDriverException

# Define a list of cities to scrape
cities = [
    # States
    "Andhra-Pradesh", "Arunachal-Pradesh", "Assam", "Bihar", "Goa", 
    "Gujarat","Himachal-Pradesh", "Jharkhand", 
    "Karnataka",
    "Maharashtra","Kerala", "Madhya-Pradesh",
     "Manipur", "Meghalaya",  "Punjab", "Rajasthan", "Sikkim", "Tamil-Nadu", 
    "Telangana", "Tripura", 
    "Uttar-Pradesh", "Uttarakhand", "West-Bengal", "Haryana","Chhattisgarh", "Mizoram","Nagaland", "Odisha",

    # Union Territories
    "Andaman-and-Nicobar-Islands", "Chandigarh", "Dadra-and-Nagar-Haveli-and-Daman-and-Diu", 
    "Lakshadweep", "Delhi"
]

# Dictionary to store the name and number of pages scraped for each city
data_scraped = {}

# Function to set up the WebDriver
def setup_driver():
    options = Options()
    # options.add_argument("--headless")  # Uncomment to run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)
    return driver, wait

# Function to extract text from an element with retries
def extract_text(container, by, value):
    for _ in range(3):  # Try 3 times
        try:
            element = container.find_element(by, value)
            return element.text.strip()
        except NoSuchElementException:
            return None
        except StaleElementReferenceException:
            time.sleep(1)
    return None

# Function to extract image and video URLs from the container with retries
def extract_media(container):
    media_urls = []
    
    def extract_images_and_videos(elements):
        for elem in elements:
            # Extract images
            img_elements = elem.find_elements(By.TAG_NAME, "img")
            for img_elem in img_elements:
                img_url = img_elem.get_attribute("src")
                if img_url and not img_url.endswith(".svg") and img_url != "https://static.99acres.com/universalapp/img/Shortlist.png":
                    media_urls.append(img_url)
            # Extract videos
            video_elements = elem.find_elements(By.CLASS_NAME, "reel__videocontainer")
            for video_elem in video_elements:
                video_url = video_elem.get_attribute("src")
                if video_url:
                    media_urls.append(video_url)
    
    for _ in range(3):  # Try 3 times
        try:
            infinity_elements = container.find_elements(By.CLASS_NAME, "tupleNew__imgWrap.tupleNew__infinity")
            extract_images_and_videos(infinity_elements)
            platinum_elements = container.find_elements(By.CLASS_NAME, "tupleNew__imgWrap.tupleNew__platinum")
            extract_images_and_videos(platinum_elements)
            break
        except StaleElementReferenceException:
            time.sleep(1)

    return ", ".join(media_urls) if media_urls else None

# Function to click the next button
def click_next(driver, current_page):
    try:
        # Use different XPath for first page and subsequent pages
        if current_page == 1:
            next_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[4]/div[3]/div[3]/div[3]/a')
        else:
            next_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[4]/div[3]/div[3]/div[4]/a')
        
        # Scroll the "Next" button into view
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        time.sleep(1)  # Give it a moment to scroll
        
        # Wait until the button is clickable
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[4]/div[3]/div[3]/div[3]/a' if current_page == 1 else '//*[@id="app"]/div/div/div[4]/div[3]/div[3]/div[4]/a')))
        
        # Use JavaScript to click the button
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)  # Wait for the page to load
        return True
    except NoSuchElementException:
        print("Next button not found")
        return False
    except WebDriverException as e:
        print(f"WebDriverException: {e}")
        return False

# Loop over each city
for city in cities:
    all_data = []  # Initialize an empty list to store data for the current city
    
    driver, wait = setup_driver()  # Set up the WebDriver for the current city

    # Construct the URL for the first page
    url = f"https://www.99acres.com/commercial-property-for-rent-in-{city.lower()}-ffid"
    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    current_page = 1
    while True:
        print(f"Scraping city: {city}, page: {current_page}")
        print(f"Current URL: {driver.current_url}")

        # Scroll down to load all the containers
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait to load the page
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        # Extract data
        try:
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "tupleNew__outerTupleWrap")))
            property_containers = driver.find_elements(By.CLASS_NAME, "tupleNew__outerTupleWrap")
        except TimeoutException:
            print(f"TimeoutException: No containers found on page {current_page} for city {city}")
            break

        # Print the count of containers
        container_count = len(property_containers)
        print(f"Number of property containers found on page {current_page} for city {city}: {container_count}")
        
        for container in property_containers:
            address = extract_text(container, By.CLASS_NAME, "tupleNew__locationName")
            property_type = extract_text(container, By.CLASS_NAME, "tupleNew__bOld")
            micromarket = extract_text(container, By.CLASS_NAME, "tupleNew__propertyHeading.ellipsis")
            price = extract_text(container, By.CLASS_NAME, "tupleNew__priceWrap")
            area = extract_text(container, By.CLASS_NAME, "tupleNew__areaWrap")
            about = extract_text(container, By.CLASS_NAME, "tupleNew__descText")
            media = extract_media(container)
            
            all_data.append({
                "Address": address,
                "Type": property_type,
                "Micromarket": micromarket,
                "Price": price,
                "Area": area,
                "About": about,
                "Images": media,
                "City": city
            })

        # Click next page
        if not click_next(driver, current_page):
            break
        current_page += 1

    # Save data to CSV for each city
    df = pd.DataFrame(all_data)
    df.to_csv(f"{city}_99acres.csv", index=False)

    # Store the city and number of pages scraped
    data_scraped[city] = current_page

    # Close the WebDriver for the current city
    driver.quit()

# Print the dictionary with the scraped data
print("Data scraped summary:")
print(data_scraped)
