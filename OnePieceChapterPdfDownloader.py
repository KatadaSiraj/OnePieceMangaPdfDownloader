import requests
import os
from PIL import Image
from io import BytesIO
import img2pdf

print('Welcome to One Piece Chapter downloader');
print('Please type chapter number you\'d like to download');
episode = ''.join(filter(str.isdigit, input('Chapter Number?\n')));

episode = int(episode);

imageFound = True;
i = 1;

directory = "OnePiece"+ str(episode);
file_list = list [str] ();
os.makedirs(directory, exist_ok = True)
while imageFound :
    # URL of the image to be downloaded
    image_url = f"https://cdn.readonepiece.com/file/mangap/2/1{episode}000/{i}.jpeg";
    if episode < 1000:
        image_url = f"https://cdn.readonepiece.com/file/mangap/2/10{episode}000/{i}.jpeg";
    if episode < 100:
        image_url = f"https://cdn.readonepiece.com/file/mangap/2/100{episode}000/{i}.jpeg";
    if episode < 10:
        image_url = f"https://cdn.readonepiece.com/file/mangap/2/1000{episode}000/{i}.jpeg";


    
    # Send a HTTP request to the image URL
    response = requests.get(image_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the image
        image = Image.open(BytesIO(response.content))
        file_location = directory + f"\\OnePiece{episode}_{i}.jpg";
        # Save the image
        image.save(file_location);
        file_list.append(file_location);
        
        print(f"Image downloaded and saved as OnePiece{episode}_{i}.jpg")
    else:
        print("Complete")
        imageFound = False;
    
    i += 1;
if len(file_list) > 0:
    pdf_path = (f"OnePiece{episode}.pdf")
    with open(pdf_path, "wb") as f:
        f.write(img2pdf.convert(file_list))

    print(f"PDF saved as {pdf_path}")

    for fi in file_list:
        os.remove(fi)
    os.rmdir(directory)
else:
    print("Chapter does not exist yet");
    os.rmdir(directory)


