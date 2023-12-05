import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class ViewCarDetailsTest {
    public static void main(String[] args) {
       
        System.setProperty("webdriver.chrome.driver", "C:\Downloads\ChromeDriver");

        ChromeOptions options = new ChromeOptions();
        options.setHeadless(true);
        WebDriver driver = new ChromeDriver(options);

        try {
        
            driver.get("http://127.0.0.1:8000/car-details/1");
            WebElement carName = driver.findElement(By.id("car-name"));
            if (!carName.getText().isEmpty()) {
                System.out.println("Car details test passed.");
            } else {
                System.out.println("Car details test failed.");
            }

        } finally {
            driver.quit();
        }
    }
}
