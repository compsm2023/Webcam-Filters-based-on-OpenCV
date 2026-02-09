# load the imig , convert into grayscale,show the img, save the img
# take the input of the img from the user 
# if the user want to see the img then display it 
# if user want to save the img save it and take the output name from the user
# after that display the msg " file name saved succesfully"
# if the user want to convert the img  into grayscale then create it
import cv2 
load_img=str(input("enter the image location: "))
read_img=cv2.imread(load_img)
if read_img is None:
    print("not loaded")
else:
    print("loaded")

    def save_img():
        if read_img is not None:
            save=cv2.imwrite(str(input("Please give the name to image for saving: ")),read_img)
            if save:
                print("Image saved succesfully as 'output_naruto.png'")
            else:
                print("Failed to save an image")
        else:
            print("Error:Could not load image")

    b=str(input("if you want the image to display on windows, convert it into grayscale or save the image so please enter the 'yes': "))
    while b=="yes":
        a=str(input("write 'yes' if you want to display the image otherwise write 'No': "))
        if a=="yes":
            cv2.imshow(str(input("Please enter the title of the image: ")),read_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        elif a=="no":
            print("Thank you!")
    
        c=str(input("write 'yes' if you want to save  the image otherwise write 'No': "))
        if c=="yes":
            save_img()
        elif c=="no":
            print("Thank you!")
    
        d=str(input("If you want to create the image in to grayscale enter the 'yes',else 'no': "))
        if d=="yes":
            if read_img is not None:
                gray=cv2.cvtColor(read_img, cv2.COLOR_BGR2GRAY)
                cv2.imshow(str(input("Please enter the tile of the image: ")),read_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("Error:image is not Loaded to covert into the grayscale ")

        b=str(input("if you want the image to display on windows, convert it into grayscale or save the image so please enter the 'yes': "))