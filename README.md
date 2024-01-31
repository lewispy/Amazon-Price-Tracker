# Amazon Price Tracker

## Overview
This repository hosts a versatile Python script designed for tracking product prices on Amazon and sending email notifications when the price drops below a predefined target.
## Components
The project consists of three key components:
+ priceTracker.py: Harnessing web scraping prowess, this script extracts the current price of a specified Amazon product. It utilizes the requests library to retrieve the HTML content and employs BeautifulSoup for seamless parsing.
+ mailer.py: The email notifier script comes into play when the product's price hits or dips below the target. It reads a customizable message template from message.txt, dynamically inserts the actual price and product link, and promptly dispatches an email alert using the smtplib library.
+ main.py: Serving as the orchestrator, the main script integrates the functionalities of the tracker and mailer. After initializing the Tracker class to fetch the current Amazon price, it checks if the price is below a specified target and, if so, employs the Mailer class to dispatch an email notification.

## Main Features
+ Amazon Price Tracking: Stay informed about the current price of your favorite products on Amazon without manually checking.
+ Email Notifications: Receive timely email alerts when the product's price drops below your predefined target, ensuring you never miss a great deal.
+ Customizable Message Template: Tailor the content of your email notifications by editing the message.txt template to suit your preferences.
+ Ease of Use: Simply run the main.py script, and the system will handle the rest, providing a seamless and effortless experience.
+ Configurability: Easily adapt the script to your specific needs by customizing the Amazon URL, headers, target price, and other parameters in the main.py file.

## Getting Started
+ Clone the repository:
  git clone https://github.com/yourusername/your-repo.git
  cd your-repo
+ Install the required Python packages:
  pip install -r requirements.txt
+ Set up a Gmail App Password and set it as an environment variable named MAIL_PASSWORD.
+ Customize the Amazon URL, headers, and target price in main.py according to your preferences.
+ Schedule the script to run automatically:
  For instance, using a code hosting service like <a href="https://www.pythonanywhere.com/">PythonAnywhere</a>. Detailed instructions on scheduling can be found in the documentation of the hosting service.
+ Run the script manually on your IDE:
  python main.py
##
The script will check the current price on Amazon and send an email if the price is below the specified target.
The script can be 
##
Feel free to modify the code and adapt it to your specific needs! If you encounter any issues or have suggestions for improvement, please open an issue or contribute to the repository. Happy tracking! 🚀
