from FileModule.file_reading import FileReading
from Module.cart import Cart
from Module.filtering import Filtering
from Module.checkout import CheckOut
import requests
from bs4 import BeautifulSoup

file_reader = FileReading()
categories = file_reader.read_file_and_get_categories()
# print("Categories:", categories)
cart = Cart()  # Instantiate the Cart class
URL = "https://www.ikea.lt/lt"
itm_links = []

# Scraping links from multiple pages
for x in range(1, 3):
    page = requests.get(f'{URL}/workspace-news/?page={x}')
    soup = BeautifulSoup(page.content, "html.parser")
    itm_elements = soup.find_all("div", class_="col-6 col-md-4 col-lg-3 p-0 itemBlock")
    
    for item in itm_elements:
        for link in item.find_all('a', href=True):
            # Append the full URL to the scraped links
            full_link = f"https://www.ikea.lt{link['href']}"
            itm_links.append(full_link)

            
# Limiting to 50 items
limited_links = itm_links[:5]

scraped_data = []

# Scraping data from the limited links
for link in limited_links:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        item_name = soup.find("h3", class_="display-7 mr-2").get_text(strip=True)
        # print(item_name)
        desc = soup.find("h4", class_="itemFacts font-weight-normal").get_text(strip=True)
        # print(desc)
        price = soup.find("span", {"data-price": True}).get_text(strip=True)
        item_data = {'name': item_name, 'price': price, 'description':desc}  # Construct dictionary for each item
        scraped_data.append(item_data)  # Append item data to the list
    except Exception as e:
        print(f"error {e}")
print(scraped_data)
file_reader.save_scraped_data('scraped_data.csv', scraped_data)
while True:
    choice = input("Select an action: 1 - Add to cart, 2 - Remove from cart, 3 - Filter and shop again, 4 - See the new additions, exit - Finish shopping: ")
    if choice.lower() == 'exit':
        break
    elif choice == '1':
        cart.add_to_cart(categories)
    elif choice == '2':
        loaded_data = file_reader.load_from_csv('checkout_info.csv')
        cart.remove_from_cart(loaded_data)
        FileReading.save_to_csv('checkout_info.csv', cart)
    elif choice == '3':
        filter_instance = Filtering(file_reader.data)  # Instantiate the Filtering class
        filter_by = input("Enter category to filter by: ")
        filtered_items = filter_instance.filter_items_by_category(filter_by)
        for item in filtered_items:
            if 'name' in item:
                print(item['name'], item['no'])
            else:
                print("Item missing name:", item)
    elif choice =='4':
        itms = file_reader.read_file_and_get_categories()
        print(itms)
    else:
        print("Invalid choice.")

CheckOut.view_cart(cart)

