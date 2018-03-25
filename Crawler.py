import requests
import shutil

subscription_key = "****************************"
assert subscription_key

#URL for Bing Image Search Api
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

#Search Query
search_term = "Cristiano Ronaldo Face"

#Method for dawnloading image
def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

#Setting of this Api
for offset in range(3):
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "count": 150}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

#URLs in this variable
thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:150]]

#Downloading images
imageNum = 1
for w in thumbnail_urls:
    download_img(thumbnail_urls[imageNum],r"C:\Users\Face_Judge_001\Images\Image" + str(imageNum)+".png")
    imageNum += 1
    
    if imageNum > 100:
        break
    


