# Whole Foods/Amazon Fresh Delivery Slot Automated Script
Let's stay home as much as possible during this difficult time.
This is intended to help you find a delivery slot on Amazon.


## Usage:
Supports **MacOS**.

The script works on **Chrome** (```whole_foods_delivery_slot_chrome.py``` for Whole Foods) (```amazon_fresh_delivery_slot_chrome.py``` for Amazon Fresh). 
It initializes a  webdriver, for which if you don't have one install it from: https://chromedriver.chromium.org/ for Chrome.

You'll have to update the path of the this installed webdriver under: ```python driver = webdriver.Chrome()``` if its not the default location your OS needs. Similarly, for FireFox ```python driver = webdriver.Firefox(executable_path="<your-webdriver-path>")```

Script was written on Python 2.7.10
(install Python 2.7.10 with command ```brew install python@2``)




_The script works after you have added all the items to your cart! Note, have your cart ready before running this script! Also, please don't let your computer sleep. Let your computer do the work, while you sleep_



### After you clone the project:
_Walkthrough for Chrome for Whole Foods, follow same steps if running on FireFox with the FireFox script_

1. Run the requirements.txt (```$ pip install -r requirements.txt```)
   1. install pip with ```sudo easy_install pip``` if you don't have it already.
2. Run whole_foods_delivery_slot_chrome.py (``` $ python amazon_fresh_delivery.py```)
3. The first time you run this script, website will ask you to login. After you login, go to the "Shipping and Payment" window. Its titled: _Schedule your order_. Leave the script running.
4. Get a nice warm Tea, browse reddit, do something on Xbox, etc.
5. Once a slot opens the script will verbally notify you of an open slot.
6. Proceed to checkout once you select a time slot. Stay Safe!

> __Screen 1__
![alt text](https://github.com/GentleWen/amazon-grocery-slots/blob/master/instruction_img/step1.png)

> __Screen 2__
![alt text](https://github.com/GentleWen/amazon-grocery-slots/blob/master/instruction_img/step2.png)

> __Screen 3__
![alt text](https://github.com/GentleWen/amazon-grocery-slots/blob/master/instruction_img/step3.png)

> __Screen 4__
![alt text](https://github.com/GentleWen/amazon-grocery-slots/blob/master/instruction_img/step4.png)

> __Screen 5__
![alt text](https://github.com/GentleWen/amazon-grocery-slots/blob/master/instruction_img/step5.png)
>
> __Screen 6: Leave script running on this screen!__
![alt text](https://github.com/GentleWen/amazon-grocery-slots/blob/master/instruction_img/step6.png)
>
> __Show case!__
![alt text](https://github.com/GentleWen/amazon-grocery-slots/blob/master/instruction_img/showcase.mov)
>
