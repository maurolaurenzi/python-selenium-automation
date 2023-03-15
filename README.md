# First Case - Memes Scraper

This is a Python script that scrapes images from the main page of the icanhas.cheezburger.com website and saves them locally. It uses the Requests and Selenium libraries.

## Dependencies

In order to run this script, the following dependencies must be installed:

- Python 3.x
- requests
- selenium
- ChromeDriver

### Python

If you do not already have Python 3.x installed, you can download it from the official website: https://www.python.org/downloads/

Pip should come pre-installed with Python 3.x, but if it does not, you can install it by following the instructions here: https://pip.pypa.io/en/stable/installing/

### Requests and Selenium

You can install Requests and Selenium using pip:

pip3 install requests
pip3 install selenium


### ChromeDriver

To install ChromeDriver, you can download it from the following link: https://sites.google.com/a/chromium.org/chromedriver/downloads

## How to Run

1. Make sure you have all the dependencies installed.
2. Clone the repository and navigate to the project directory.
3. Run the command `python memes_scraper.py`.
4. The script will scrape the first 10 images from the main page of icanhas.cheezburger.com and save them in a 'memes' folder.

## Notes

- The script will create a 'memes' folder if it doesn't already exist.
- The number of images to scrape can be changed by modifying the `num_images` variable in the script.


