# First Case - Memes Scraper

A Python script that scrapes images from the main page of the icanhas.cheezburger.com website and saves them locally. It uses the Requests library to download and store the images and the Selenium framework to interact with the browser.

## Dependencies

In order to run this script, the following dependencies must be installed:

- Python 3.x
- pip (Python package installer)
- requests
- selenium
- ChromeDriver

### Python

If you do not already have Python 3.x installed, you can download it from the official website: https://www.python.org/downloads/

Pip should come pre-installed with Python 3.x, but if it does not, you can install it by following the instructions here: https://pip.pypa.io/en/stable/installing/

### Requests and Selenium

You can install Requests and Selenium using pip:

`pip3 install requests`

`pip3 install selenium`


### ChromeDriver

To install ChromeDriver, you can download it from the following link: https://chromedriver.chromium.org/downloads

## How to Run

1. Make sure you have all the dependencies installed.
2. Clone the repository and navigate to the project directory.
3. Run the command `python3 first_case/memes_scraper.py`.
4. The script will scrape the first 10 images from the main page of icanhas.cheezburger.com and save them in a 'memes' folder.

## Notes

- The script will create a 'memes' folder if it doesn't already exist.
- The number of images to scrape can be changed by modifying the `num_images` variable in the script.


# Second Case - Contact Form Testing

This codebase contains test cases for a website's contact form using Python and Selenium. The test suite employs the Page Object Model (POM) design pattern, organizing the test suite into two sections: the pages folder, which contains page object methods that encapsulate the functionalities and interactions of the web pages, and the tests folder, which contains test scripts that utilize these methods to conduct end-to-end testing.

## Dependencies

In order to run this code, you will need to have the following dependencies installed:

- Python 3.x
- pip (Python package installer)
- Selenium (`pip3 install selenium`)
- pytest (`pip3 install pytest`)
- ChromeDriver

The installation process for these dependencies was already described in the first case section.

## Usage

To run the test cases, navigate to the directory where the `test_contact_form.py` file is located in your terminal and run the following command:

`pytest test_contact_form.py`

This will execute the test cases and output the results in the terminal.

## Test Cases

The test cases are located in the `test_contact_form.py` file and include the following:

- Verify that all elements from contact form are displayed
- Verify that contact form cannot be submitted without name
- Verify that contact form cannot be submitted without door count
- Verify that contact form cannot be submitted without phone number

## Test data

Test data is stored in the `data/test_data.json` file, which is loaded and parsed in the test script.





