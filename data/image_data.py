from selenium import webdriver
from selenium.webdriver.common.by import By


# # driver = webdriver.Edge('msedgedriver.exe')
# # driver.get("https://drive.google.com/drive/u/0/folders/1jcdmWfgHbphsEdQkSrgI9jFOpFt3jij2")
# # # a = driver.find_elements(By.CSS_SELECTOR, "td a")
# # # photo_urls = []
# # # for photo in a:
# # #     photo_urls.append(photo.get_attribute('href'))
# # # for photo in photo_urls:
# # #     driver.get(photo)
# # #     image = driver.find_elements(By.CSS_SELECTOR, "div img")
# # #     print(image)
# # #     with open("photo_url.txt", 'a') as file:
# # #         file.write(f"'{image[0].get_attribute('src')}',\n")
# # driver.implicitly_wait(60)
# driver.quit()
photos=\
    [
"https://hosting.photobucket.com/images/i/dmobley0608/DSC03050.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC03045.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC03032.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC03016.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC03009.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC03000.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02991.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02961.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02947.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02940.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02911.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02888.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02878.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02859.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02841.jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02744(1).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02705(1).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02642(1).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02628(1).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02598(2).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02572(1).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02559(1).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02550(2).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02545(2).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02491(2).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02471(2).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02436(2).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02386(2).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02366(2).jpg",
"https://hosting.photobucket.com/images/i/dmobley0608/DSC02358(3).jpg",

    ]
# with open("photo_url.txt", 'r') as file:
#     images = file.read()
#
#     for image in images.split("\n"):
#         photos.append(f'"{image}",\n')
#
# with open("photo_url.txt", 'w') as file:
#     for image in photos:
#         file.write(image)
