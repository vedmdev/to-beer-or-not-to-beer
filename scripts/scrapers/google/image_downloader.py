from google_images_download import google_images_download

def image_download(output_dir, keywords , number_images):
    
    """
    arguments:
        keywords : it refers to the keywords being searched
        
        number_images : Total number of images to be downloaded
    """

    response = google_images_download.googleimagesdownload() 

    arguments = {"keywords":keywords,"limit":number_images,"print_urls":True, "output_directory": output_dir}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)   #printing absolute paths of the downloaded images
    



image_download('./data/datasets/beer/train', 'beer beach', 100)

# beer 100
# beer people 100
# beer party 100
# beer people holding 100
# beer local 100
# beer outside 100
# beer drink 100
# beer summer 100
# beer beach 100
# beer girl images 100