package com.formyproject.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class BasePage {
    public WebDriver driver;

    public void setUp() {
        System.setProperty("webdriver.chrome.driver",
                "C:\\Users\\sampa\\Downloads\\JOBS\\Projects\\SeleniumAutomation\\TDD_project\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*"); // Important to prevent connection issues
        // options.addArguments("--headless"); // Uncomment if you want headless later

        driver = new ChromeDriver(options);
        driver.manage().window().maximize();
    }

    public void tearDown() {
        if (driver != null) {
            try {
                driver.quit();
            } catch (Exception e) {
                System.out.println("Exception during driver.quit(): " + e.getMessage());
            }
        }
    }
}
