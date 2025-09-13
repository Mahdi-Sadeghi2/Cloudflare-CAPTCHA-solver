import pyautogui
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc


def human_like_mouse_movement(start_x, start_y, end_x, end_y, duration=1.0):
    """Simulate natural mouse movement from current position to target position"""
    # Get current mouse position
    current_x, current_y = pyautogui.position()

    # If start point not specified, use current position
    if start_x is None:
        start_x = current_x
    if start_y is None:
        start_y = current_y

    # Calculate distance and direction
    distance = ((end_x - start_x) ** 2 + (end_y - start_y) ** 2) ** 0.5

    # If distance is very small, move directly
    if distance < 50:
        pyautogui.moveTo(end_x, end_y, duration=duration)
        return

    # Create curved path with intermediate points
    # Number of intermediate points based on distance
    num_points = max(3, int(distance / 50))
    points = []

    for i in range(1, num_points):
        # Calculate intermediate position with random deviation
        t = i / num_points
        mid_x = start_x + (end_x - start_x) * t
        mid_y = start_y + (end_y - start_y) * t

        # Add random deviation for more natural movement
        deviation = random.randint(-30, 30)
        mid_x += deviation
        mid_y += deviation

        points.append((mid_x, mid_y))

    # Move through intermediate points
    for point in points:
        pyautogui.moveTo(point[0], point[1], duration=duration / len(points))

    # Move to final point
    pyautogui.moveTo(end_x, end_y, duration=duration / 3)


def click_with_human_like_movement(x, y):
    """Click with natural mouse movement"""
    # Get current mouse position
    current_x, current_y = pyautogui.position()

    # Natural movement to target
    human_like_mouse_movement(current_x, current_y, x,
                              y, duration=random.uniform(0.7, 1.5))

    # Short delay before clicking
    time.sleep(random.uniform(0.1, 0.3))

    # Click
    pyautogui.click()

    print(f"Clicked at position ({x}, {y})")


def setup_browser(url):
    """Set up browser and open URL"""
    options = uc.ChromeOptions()
    options.add_argument("--window-size=1280,720")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = uc.Chrome(options=options, headless=False)
    driver.get(url)

    # Wait for page to load
    time.sleep(3)

    return driver


def switch_to_cloudflare_iframe(driver):
    """Switch to Cloudflare challenge iframe"""
    try:
        # Find Cloudflare challenge iframe
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "iframe[src*='challenge'], iframe[src*='cloudflare']"))
        )

        # Switch to iframe
        driver.switch_to.frame(iframe)
        print("Switched to Cloudflare iframe")
        return True
    except Exception as e:
        print(f"Error finding iframe: {e}")
        return False


def find_and_click_checkbox(driver):
    """Find and click checkbox in iframe"""
    try:
        # Find checkbox
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[type='checkbox'], .checkbox, #challenge-stage, [role='checkbox']"))
        )

        # Click checkbox with JavaScript
        driver.execute_script("arguments[0].click();", checkbox)
        print("Clicked on checkbox")
        return True
    except Exception as e:
        print(f"Error clicking checkbox: {e}")
        return False


def main():
    # Checkbox center coordinates (from OpenCV output)
    center_x, center_y = 460, 685  # Change according to your screen size and monitor

    # Target website URL
    target_url = "https://dash.cloudflare.com/login"

    # Set up browser and open website
    print("Setting up browser...")
    driver = setup_browser(target_url)

    try:
        # Switch to Cloudflare iframe
        if switch_to_cloudflare_iframe(driver):
            # Click checkbox with Selenium
            if find_and_click_checkbox(driver):
                print("Checkbox clicked successfully")
            else:
                # If Selenium click doesn't work, use coordinates and pyautogui
                print("Using coordinate click method...")

                # Switch back to main page
                driver.switch_to.default_content()

                # Wait for browser window to activate
                print("Waiting for browser window to activate...")
                time.sleep(3)

                # Click with natural mouse movement
                print("Moving mouse and clicking on checkbox...")
                click_with_human_like_movement(center_x, center_y)
        else:
            print("If iframe not found, using coordinates directly...")
            # Wait for browser window to activate
            time.sleep(3)
            click_with_human_like_movement(center_x, center_y)

        # Wait for click to be processed
        print("Waiting for click to be processed...")
        time.sleep(5)

        # Check status
        current_url = driver.current_url
        page_source = driver.page_source.lower()

        if "challenge" not in current_url and "challenge" not in page_source:
            print("Challenge solved successfully!")
        else:
            print("Challenge may not be solved.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close browser
        input("Press Enter to exit...")
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    main()
