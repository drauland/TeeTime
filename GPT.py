from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
import schedule
import time
import datetime as dt
import dateutil.relativedelta as rel

eightAM = dt.time(8, 31, 00)

# Create options object to launch Chrome with
options = Options()
options.add_argument("--start-maximized")

# Create webdriver object
browser = webdriver.Chrome(options=options)


# Get the formatted date of the next Saturday
def get_next_saturday():
    today = dt.date.today()
    rd = rel.relativedelta(days=7, weekday=rel.SA)
    next_saturday = today + rd
    formatted_date = dt.date.strftime(next_saturday, "%m-%d-%Y")
    return formatted_date


def get_next_sunday():
    today = dt.date.today()
    rd = rel.relativedelta(days=7, weekday=rel.SU)
    next_sunday = today + rd
    formatted_date = dt.date.strftime(next_sunday, "%m-%d-%Y")
    return formatted_date


# Open website
def job():
    # Go to website
    browser.get('https://foreupsoftware.com/index.php/booking/20173/3927#/teetimes')
    time.sleep(1)
    # Log In
    browser.find_element("xpath", "//button[normalize-space()='Rec 18 Resident Card Times']").click()
    time.sleep(1)
    browser.find_element("xpath", "//button[@class='btn btn-lg btn-primary login']").click()
    time.sleep(1)
    browser.find_element("name", "email").send_keys("djrauland@gmail.com")
    browser.find_element("name", "password").send_keys("dj1216445")
    browser.find_element("xpath", "//button[@class='btn btn-primary login col-xs-12 col-md-2']").click()
    time.sleep(2)
    browser.find_element("name", "date").send_keys(Keys.CONTROL, 'a')
    browser.find_element("name", "date").send_keys(Keys.BACKSPACE)
    # Enter next Saturday
    browser.find_element("name", "date").send_keys(get_next_saturday())
    # Enter next Sunday
    # browser.find_element("name", "date").send_keys(get_next_sunday())
    browser.find_element("xpath", "//a[@data-value='4']").click()
    browser.find_element("xpath", "//a[@data-value='4']").click()
    time.sleep(1)
    first_time = browser.find_element("class name", "booking-start-time-label").text
    date_format = '%I:%M%p'
    datetime_str = dt.datetime.strptime(first_time, date_format)
    print(browser.find_element("class name", "booking-start-time-label"[2]).text)
    if datetime_str.time() < eightAM:
        browser.find_element("class name", "booking-start-time-label").click()
        time.sleep(2)
        browser.find_element("xpath", "//button[normalize-space()='Book Time']").click()
        time.sleep(2)
        browser.find_element("xpath", "//button[@class='btn btn-success col-xs-12 col-md-3 continue']").click()
        time.sleep(1)
        browser.find_element("xpath", "//button[@class='btn btn-success set-card col-xs-12 col-md-3']").click()
        print('Booked ' + first_time + ' tee time. ')
        time.sleep(3)
    else:
        print('Couldn\'t find a time before 8. The earliest time was ' + first_time + ' booking for testing purposes.')
        browser.find_element("class name", "booking-start-time-label").click()
        time.sleep(2)
        browser.find_element("xpath", "//button[normalize-space()='Book Time']").click()
        time.sleep(2)
        browser.find_element("xpath", "//button[@class='btn btn-success col-xs-12 col-md-3 continue']").click()
        time.sleep(1)
        #browser.find_element("xpath", "//button[@class='btn btn-success set-card col-xs-12 col-md-3']").click()
        print('Booked ' + first_time + ' tee time. ')
        time.sleep(3)
        # print('Couldn\'t find a time at or before 8:30. The earliest time was ' + first_time)
    # Close browser
    browser.quit()
    exit()


def timecheck():

# Schedule job to run every Wednesday at 6am
# schedule.every().friday.at("12:28:00").do(job)
job()

# Run continuously
#while True:
#    schedule.run_pending()
#    time.sleep(1)




