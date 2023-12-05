import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class UserRegistrationTest {
    public static void main(String[] args) {
   
        System.setProperty("webdriver.chrome.driver", "C:\Downloads\ChromeDriver");

        ChromeOptions options = new ChromeOptions();
        options.setHeadless(true); 
        WebDriver driver = new ChromeDriver(options);

        try {
            driver.get("http://127.0.0.1:8000/register");

            WebElement username = driver.findElement(By.name("username"));
            username.sendKeys("new_user");

            WebElement password = driver.findElement(By.name("password"));
            password.sendKeys("new_password");

           
            driver.findElement(By.id("register-button")).click();

            WebElement successMessage = driver.findElement(By.id("success-message"));
            if (successMessage.getText().contains("Registration successful")) {
                System.out.println("Registration test passed.");
            } else {
                System.out.println("Registration test failed.");
            }

        } finally {
            driver.quit();
        }
    }
}
