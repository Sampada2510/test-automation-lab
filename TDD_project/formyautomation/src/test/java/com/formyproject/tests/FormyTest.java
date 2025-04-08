package com.formyproject.tests;

import com.formyproject.pages.BasePage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.time.Duration;

public class FormyTest extends BasePage {

    WebDriverWait wait;

    @BeforeMethod
    public void setUp() {
        super.setUp();
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    @AfterMethod
    public void tearDown() {
        super.tearDown();
    }

    @Test
    public void testFormSubmission() throws InterruptedException {
        System.out.println("Navigating to form page...");
        driver.get("https://formy-project.herokuapp.com/form");

        Thread.sleep(1000); // Pause to observe page load

        System.out.println("Waiting for form elements...");
        WebElement firstNameField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("first-name")));
        WebElement lastNameField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("last-name")));
        WebElement jobTitleField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("job-title")));
        WebElement submitButton = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("a.btn")));

        System.out.println("Filling out form...");
        firstNameField.sendKeys("John");
        lastNameField.sendKeys("Doe");
        jobTitleField.sendKeys("Software Engineer");

        Thread.sleep(1000); // Pause to observe inputs

        System.out.println("Submitting form...");
        submitButton.click();

        System.out.println("Waiting for success message...");
        WebElement successMessage = wait
                .until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".alert.alert-success")));

        Assert.assertTrue(successMessage.isDisplayed(), "Form submission was not successful.");

        Thread.sleep(1500); // Observe result
    }

    @Test
    public void testAutoCompleteForm() throws InterruptedException {
        System.out.println("Navigating to autocomplete page...");
        driver.get("https://formy-project.herokuapp.com/autocomplete");

        Thread.sleep(1000);

        System.out.println("Waiting for autocomplete input...");
        WebElement addressField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("autocomplete")));

        System.out.println("Typing address...");
        addressField.sendKeys("1600 Amphitheatre Parkway");

        Thread.sleep(1000); // Let the autocomplete suggestions populate

        Thread.sleep(1000); // Allow time to observe the result

        System.out.println("Checking if address is populated...");
        Assert.assertTrue(addressField.getAttribute("value").contains("1600 Amphitheatre"),
                "Address field did not retain the input value.");
    }

    @Test
    public void testCheckbox() throws InterruptedException {
        System.out.println("Navigating to checkbox page...");
        driver.get("https://formy-project.herokuapp.com/checkbox");

        Thread.sleep(1000);

        System.out.println("Waiting for checkbox...");
        WebElement checkbox = wait.until(ExpectedConditions.elementToBeClickable(By.id("checkbox-1")));

        System.out.println("Clicking checkbox...");
        checkbox.click();

        Thread.sleep(1000);

        Assert.assertTrue(checkbox.isSelected(), "Checkbox was not checked.");
    }
}
