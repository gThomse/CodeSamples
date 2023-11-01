import sys
import requests
from bs4 import BeautifulSoup
import re
import webbrowser
# import numba as njit

url = 'https://www.homecookingadventure.com/15-lemon-desserts/'

url = 'https://www.homecookingadventure.com/15-cake-roll-recipes/'

url = 'https://www.homecookingadventure.com/25-best-potato-recipes/'

url =  'https://www.homecookingadventure.com/25-healthy-recipes-to-try-in-2023/'

url = 'https://www.homecookingadventure.com/35-french-desserts/'

url = 'https://www.homecookingadventure.com/40-gorgeous-easter-cakes/'

# url = 'https://natashaskitchen.com/'


url = 'https://www.homecookingadventure.com/35-mouthwatering-gluten-free-desserts/'

url = 'https://www.homecookingadventure.com/35-easy-spring-desserts/'

url = 'https://www.homecookingadventure.com/30-irresistible-custard-desserts/'

url = 'https://www.homecookingadventure.com/20-heavenly-eggless-cake-recipes/'

url = 'https://www.homecookingadventure.com/30-brunch-ideas/'

url = 'https://www.homecookingadventure.com/30-unique-4th-of-july-desserts/'

url = "https://www.homecookingadventure.com/25-best-brownie-recipes/"

url = "https://www.homecookingadventure.com/20-delightful-chicken-recipes/"

# url = 'C:\Users\gThom\Documents\code\Python programs\Recipe Web Scrapes\Test\Preppy Kitchen desserts.htm'

url = "https://www.homecookingadventure.com/20-easy-homemade-ice-cream-recipes/"

url = "https://www.homecookingadventure.com/8-easy-must-try-zucchini-recipes/"

url = 'https://www.homecookingadventure.com/30-best-caramel-recipes/'

url = 'https://www.homecookingadventure.com/50-must-try-fall-desserts/'


def extract_characters(input_string):
    return re.sub(r'[^a-zA-Z]', '', input_string)

def main():

    try:
        if len(sys.argv[1]) > 0:
            x = sys.argv[1]
            # print ("Has value")
    except:
        print('Enter Starting link (line no): ', end='')

        x = input()

    try:
      xint = int(x)
    except:
      try:
        if len(x) == 0:
           xint = 0
      except:
        print("Invalid Entry")
        quit()

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    lnk_dict = {}
    check_out = {}

    input_tag = soup.findAll('p', class_="site-title")
    for i in input_tag:
        site_name = extract_characters(i.text)
        break

    max_l = 0

    for link in soup.find_all('a'):
        lnk = link.get('href')
        lnk_text = link.getText().strip()

        # Check_out is all the links in the document that are recipes...
        if lnk_text.strip() == "Check out this recipe":
            check_out [lnk] = ["A recipe"]
        else:
            lnk_dict[lnk] = [lnk_text.strip()]
            # The link is the key, the text is the value ..

    # An Example of inline dictionary operations.
        # my_dict = {'a': 1, 'b': 2, 'c': 3}
    # new_dict = {value * 2 if key == 'b' else value: key for key, value in my_dict.items()}
    # print([value for key, value in lnk_dict.items()])


    # The value in lnk_dict is a list...
    max_l = max([len(lnk_dict[key][0]) for key, _ in check_out.items()])

    # For clarity uncomment next 5 lines
    # print([key for key, _ in check_out.items()])
    # print([lnk_dict[key] for key, _ in check_out.items()])
    # print([len(lnk_dict[key][0]) for key, _ in check_out.items()])
    # print(max([len(lnk_dict[key][0]) for key, _ in check_out.items()]))
    # quit()

    max_l += 1
    site_name = site_name.replace("eC","e C").replace("gA","g A")
    offset = max_l + 3 + 1 + len(site_name.strip())

    # print(offset)
    print(f'{site_name: >{offset}}')

    title = soup.find('title')
    print(f'{title.get_text():>{max_l + 3 + 1 + len(title.get_text())}}')

    # check_out provides the key for lnk_dict
    for i, (k, v) in enumerate(check_out.items()):
        str_value = ""
        # xint is user input
        if i+1 >= xint:
            for ele in lnk_dict[k]:
                str_value += ele
            # print (i+1,k,str_value)

            print(f'{i+1:<3}{str_value: <{max_l}} {k}')
            # webbrowser.open_new(k)

if __name__ == '__main__':
    main()