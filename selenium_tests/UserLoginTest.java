import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class UserLoginTest {
    public static void main(String[] args) {
     
        System.setProperty("webdriver.chrome.driver", "C:\Downloads\ChromeDriver");

        ChromeOptions options = new ChromeOptions();
        options.setHeadless(true); 
        WebDriver driver = new ChromeDriver(options);

        try {
            driver.get("http://127.0.0.1:8000/login");

            
            WebElement phoneNumber = driver.findElement(By.name("phone-number"));
            phoneNumber.sendKeys("user_phone_number");

            WebElement password = driver.findElement(By.name("password"));
            password.sendKeys("user_password");

            driver.findElement(By.id("login-button")).click();

            if (driver.getCurrentUrl().contains("home_page")) {
                System.out.println("Login test passed.");
            } else {
                System.out.println("Login test failed.");
            }

        } finally {
            driver.quit();
        }
    }
}
