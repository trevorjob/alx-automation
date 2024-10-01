# ALX Project Files Automation

This Python script automates the process of fetching project details from the ALX intranet, creating necessary files and folders, and generating a README.md file with project information.

## Features

- **Login Automation**: Automates logging into the ALX intranet.
- **File and Folder Creation**: Scrapes the project page to generate the correct file and folder structure on your local machine.
- **Auto-Generated Comments**: Inserts required comments into the files based on the ALX project guidelines.
- **Auto-Generated README**: Creates a README.md file for each project with the project title and task list.
- **File Permissions**: Updates file permissions to make Python files executable.

## Requirements

To run this script, ensure you have the following installed:

- Python 3.x
- Selenium
- Chrome WebDriver
- Requests library

## Installation

Clone the repository or download the script.

Install the required dependencies using pip:

```
pip install selenium requests
```

Download and install Google Chrome WebDriver and ensure it is added to your system's PATH.

- linux (ubuntu/debian): https://github.com/password123456/setup-selenium-with-chrome-driver-on-ubuntu_debian

- windows: https://medium.com/@patrick.yoho11/installing-selenium-and-chromedriver-on-windows-e02202ac2b08

- mac: https://medium.com/@sethi.ashima/how-to-install-chromedriver-in-mac-7d8e2f980eb

### Usage

Update the script with your ALX credentials:

```
emailAdd = "your alx email address"
pwd = "your alx password"
```

Run the script by providing the project ID as a command-line argument:

```
python main.py [PROJECT_ID]
```

Replace [PROJECT_ID] with the actual ALX project

```
number, e.g., python main.py 123.
```

The script will then:

- Log in to the ALX intranet.
- Scrape the specified project page.
- Generate the appropriate folder and file structure.
- Insert the required comments into each file.
- Create a README.md file with the project title and tasks.

## Dependencies

- **Selenium**: Automates browser actions such as logging in and navigating web pages.
- **Requests**: Simplifies making HTTP requests to the project page.
- **Chrome WebDriver**: Required for Selenium to control the Chrome browser.

## Troubleshooting

- **Invalid URL**: If the project URL is incorrect, the script will print an error message.
- **Login Issues**: Ensure your ALX credentials are correct.
- **Missing WebDriver**: If Chrome WebDriver is not installed or added to PATH, the script will fail to open the browser.

## Customization

You can customize this script for other platforms by:

- Modifying the login credentials and URLs.
- Changing the file creation logic to match different project structures.

## Contributing

Feel free to open an issue or submit a pull request for any improvements or bug fixes.
