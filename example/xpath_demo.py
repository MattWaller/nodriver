from nodriver import *
from pathlib import Path

"""

Just a basic example of how to use xpath find_element(BY.XPATH, xpath) / find_elements(BY.XPATH, xpath) port from Selenium.

driver.find_element(By.XPATH, xpath) is now: 
await tab.find_element_by_text(xpath)

driver.find_elements(BY.XPATH, xpath) is now:
await tab.find_element_by_texts(xpath)



"""
DELAY = 2


async def main():

    browser = await start()
    tab = await browser.get("https://google.com")

    await tab.wait(DELAY)

    selector = "//textarea" # basic xpath selector

    xpath_element = await tab.find_element_by_text(selector)

    await xpath_element.send_keys('nodriver github')

    # Google Search button, advanced xpath search
    selector = """//input[@value="I'm Feeling Lucky"]//preceding-sibling::input"""
    xpath_elements = await tab.find_elements_by_text(selector)

    for xe in xpath_elements:
        await xe.click()    
        break
    
    await tab.wait(DELAY)

    github_href_xpath = await tab.find_element_by_text('//a[contains(@href,"ultrafunkamsterdam")]')

    github_href = github_href_xpath.attrs.href

    print(f'Got Github href: {github_href}')


    await tab.get(github_href)

    await tab.wait(DELAY)

    await tab




if __name__ == "__main__":
    loop = loop()
    loop.run_until_complete(main())
