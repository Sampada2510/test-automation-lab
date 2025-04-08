## Welcome to My GitHub Portfolio "test-automation-lab"

## Table of Contents
- [What's in Here?](#whats-in-here)
- [About Me](#about-me)
- [Professional Highlights](#professional-highlights)
- [First Trial Project: Swag Labs (Python + Selenium + Jenkins)](#first-trial-project-swag-labs-python--selenium--jenkins)
- [File Upload Automation with Playwright and Node.js](#file-upload-automation-with-playwright-and-nodejs)
- [Download File Automation with Playwright and Node.js](#download-file-automation-with-playwright-and-nodejs)
- [Let's Connect](#lets-connect)

## What's in Here?

This repository serves as my portfolio, showcasing a collection of interesting QA automation projects using Java, Python, Selenium, Cucumber, TestNG, Playwright, javascript and CI/CD with Jenkins. It includes detailed documentation for learning and reference, demonstrating my expertise in automation, cloud-based testing, and test optimization

---

<p align="center">
<img src="https://github.com/Sampada2510/test-automation-lab/blob/main/3793102.jpg" alt="Portfolio Banner" width="400" height="400">
</p> 

## 👩‍💻 About Me

Hey there! I'm a passionate Software Quality Engineer with over six years of experience making sure software doesn’t just work—but works flawlessly. My expertise spans **test planning, test scenario design, test execution, and automation**, all crucial to maintaining software quality throughout release cycles. From functional and non-functional testing to CI/CD integrations, I thrive in **building efficient, automated workflows that minimize manual effort and maximize reliability**.

What defines my QA mindset? It’s a **strategic approach to testing**— where every decision is backed by test coverage value—ensuring we test what matters most, avoid redundancy, and maintain high confidence in releases.

- ✅ **Test planning & strategy creation** aligned with business goals  
- ✅ **Designing high-impact test cases and scenarios** that catch edge cases early  
- ✅ **Executing and managing functional, non-functional, regression, and exploratory testing cycles**  
- ✅ **Deciding what to automate and what not to—based on stability, repeatability, and cost-benefit analysis**  
- ✅ **Performance testing using tools like JMeter**, identifying bottlenecks before users do  
- ✅ **Collaborating cross-functionally** to embed quality into the entire SDLC  

## 🏢 Professional Highlights

At **Riverus Technology Solutions**, as a Quality Assurance Engineer, I led test planning, UAT, and exploratory testing for a contract lifecycle management platform, significantly reducing post-release defects. I automated UI and API tests using **Selenium, Python, and Behave**, which greatly reduced manual testing efforts and improved test execution speed. I also established validation procedures on **AWS (S3, EC2, CloudWatch)**, authored comprehensive test cases, and leveraged **SQL and debugging skills** to accelerate defect resolution. In another major initiative at Riverus, I engineered a **Selenium-Java-TestNG automation framework** that covered over 800 regression and smoke test cases—dramatically improving execution speed and test accuracy. I also piloted **API and SQL data validation strategies** to strengthen data pipeline reliability and reporting accuracy, while applying both **white-box and black-box testing techniques** to enhance product quality.

At **KPOINT Technologies**, as a Senior Software Engineer, I revamped the test automation framework for a video and audio streaming platform, mentoring junior engineers and automating over 50 high-priority test cases within the first month. I built a robust **Selenium-Ruby-Cucumber BDD framework with Page Object Model (POM)** that significantly reduced regression testing time. I enhanced CI/CD testing by integrating tools like **Jenkins, Docker, and Kibana**, leading to faster and more stable deployments. I also explored additional automation tools like **Playwright**, and actively promoted **Agile Scrum practices**, improving team collaboration and accelerating delivery cycles.

---

## What I Bring

I bring **end-to-end quality ownership**—from ideation to production, from manual validations to intelligent automation. I don’t just write scripts—I **engineer test strategies** that scale with your product and team. Currently, I’m pursuing my **Master’s in Management Information Systems at the University at Buffalo**, staying ahead of emerging tech trends while honing my ability to bridge the gap between technology and business. I’m deeply invested in **test automation, cloud testing, and CI/CD optimization**—and always eager to connect with like-minded professionals. If you’re passionate about quality engineering, let’s chat! **https://www.linkedin.com/in/sampadatelang/**

---

### 🔹 First Trial Project: Swag Labs (Python + Selenium + Jenkins)
- **Tech Stack:** Python, Selenium, Jenkins
- **Goal:** This project is a basic demonstration of using **Selenium WebDriver with Python** to automate UI testing of a web application. It performs a test on [https://www.saucedemo.com] and then runs test in a CI/CD jenkins pipeline. 

## ✅ What This Script Does

- Opens Chrome browser and navigates to SauceDemo login page
- Logs in with test credentials
- Adds a product to the cart
- Verifies that the product is successfully added
- Navigates to the cart page
- Verifies the item is in the cart
- Closes the browser

---

## 🧠 How It Works

## What is Selenium?

Selenium is an open-source tool that automates web browsers. It allows you to simulate user actions like clicks, typing, and navigation on websites.

## What is a WebDriver?

A WebDriver is a bridge between Selenium and the web browser. It sends commands from your script to the browser. For Chrome, we use **ChromeDriver**.

---

## 💻 Setup Instructions

## 1. Install Dependencies

Ensure Python is installed, then install Selenium: pip install selenium

## 2. Download ChromeDriver
Go to: https://developer.chrome.com/docs/chromedriver/downloads

Download the version that matches your Chrome browser

Add the chromedriver to your system PATH or place it in the project folder

## 🚀 CI/CD Integration with Jenkins

This project integrates with **Jenkins** using a **Pipeline-as-Code** approach. A custom `Jenkinsfile` is provided that automates the entire testing process.

### 📄 Jenkinsfile Overview

The Jenkins pipeline performs the following steps:

#### 🔧 Environment Setup (Windows)
- Adds Python and pip to the system `PATH`
- Sets variables for:
  - `SELENIUM_TEST_DIR`: Location of the test script
  - `CHROMEDRIVER_PATH`: Path to the ChromeDriver executable

#### 📦 Install Dependencies
- Echoes environment variables for debug
- Prints Python and pip versions
- Installs Selenium using `pip`

#### 🧪 Run Selenium Test
- Runs `saucedemo_sanity_tests.py` from the defined test directory
- Uses Chrome in **headless mode**
- Passes Chrome options and ChromeDriver path to the script

#### 🧹 Post Actions
- Always prints a message indicating the test has finished

---

# File Upload Automation with Playwright and Node.js

This project demonstrates **automated file upload testing** using **Playwright**. The script navigates to a sample file upload page, uploads a file, and verifies if the upload was successful.

## Project Overview

This project automates the process of uploading a file on the **"The Internet"** website ([https://the-internet.herokuapp.com/upload](https://the-internet.herokuapp.com/upload)) using Playwright, a powerful tool for browser automation.

### What the script does:
1. Launches a Chromium browser in **headed mode** (visible browser).
2. Navigates to the **upload page**.
3. Uploads a file (`testFile.txt`).
4. Submits the form and verifies the success message and the uploaded file.
5. Waits for **2 seconds** before closing the browser to allow observation of the process.

### Technologies Used:
- **Playwright** for browser automation.
- **Node.js** and **npm** for environment setup.

---

# Download File Automation with Playwright and Node.js

This project demonstrates **automated file download testing** using **Playwright**. The script navigates to a file download page, downloads a file, and verifies the download process.

## What the Script Does

1. **Launches the Chromium browser** in headed mode (visible browser).
2. **Navigates to the file download page** on [The Internet](https://the-internet.herokuapp.com/download).
3. **Listens for the download event** triggered by clicking the file link.
4. **Downloads the file** (`logback.xml`) to a specified local directory (`downloads`).
5. **Waits for 5 seconds** to ensure the download process completes.
6. **Logs the download path** to the console.
7. **Closes the browser** after the download is complete.


## Installation Instructions

To get started with this project, follow the steps below:

Install Node.js and npm

Make sure you have **Node.js** and **npm** installed. You can download them from [https://nodejs.org/](https://nodejs.org/).

To verify installation:
node -v
npm -v

If Node.js and npm are installed but you still see the error, the PATH may not be set correctly.

To install playwright: 
npm install playwright
npm install @playwright/test

To run the test: npx playwright test upload_file_test.js

## Add a Test File

Ensure that you have a file named testFile.txt in the same directory as your script or modify the path to match your file location.

## Let's Connect
Feel free to explore my projects and reach out for collaboration!

🔗 **GitHub:** https://github.com/Sampada2510/test-automation-lab  
💼 **LinkedIn:** https://www.linkedin.com/in/sampadatelang/  
📧 **Email:** telangsampada68@gmail.com

---