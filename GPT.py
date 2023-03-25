from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
import schedule
import time
import datetime as dt
import dateutil.relativedelta as rel

eightAM = dt.time(8, 31, 00)
sevenAM = dt.time(6, 59, 00)

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
    # browser.find_element("name", "date").send_keys(get_next_saturday())
    # Enter next Sunday
    browser.find_element("name", "date").send_keys(get_next_sunday())
    browser.find_element("xpath", "//a[@data-value='4']").click()
    browser.find_element("xpath", "//a[@data-value='4']").click()
    time.sleep(1)
    # Get a time if it's between 7 and 8:30, otherwise return the latest time
    my_time = get_times()
    print(my_time + ' is my time')
    date_format = '%I:%M%p'
    my_time_str = dt.datetime.strptime(my_time, date_format)
    # Try and click my time
    my_xpath = "//div[normalize-space()='" + my_time + "']"
    time.sleep(1)
    if (my_time_str.time() < eightAM) and my_time_str.time() > sevenAM:
        browser.find_element("xpath", my_xpath).click()
        time.sleep(2)
        browser.find_element("xpath", "//button[normalize-space()='Book Time']").click()
        time.sleep(2)
        browser.find_element("xpath", "//button[@class='btn btn-success col-xs-12 col-md-3 continue']").click()
        time.sleep(1)
        browser.find_element("xpath", "//button[@class='btn btn-success set-card col-xs-12 col-md-3']").click()
        print('Booked ' + my_time + ' tee time. ')
        time.sleep(3)
    else:
        print('Couldn\'t find a time between 7 and 8:30.')
    # Close browser
    browser.quit()
    exit()


# Get the times from the page
def get_times():
    list_of_elements = browser.find_elements("class name", "booking-start-time-label")
    count = 0
    date_format = '%I:%M%p'
    while count < len(list_of_elements):
        datetime_str = dt.datetime.strptime(list_of_elements[count].text, date_format)
        if (datetime_str.time() < eightAM) and datetime_str.time() > sevenAM:
            print(datetime_str)
            return datetime_str
        else:
            print(list_of_elements[count].text + ' is not in between 7 and 8:30am')
        count = count + 1
    return list_of_elements[count-1].text


# Schedule job to run every Wednesday at 6am
schedule.every().saturday.at("6:00:00").do(job)

# Run continuously
while True:
    schedule.run_pending()
    time.sleep(1)




