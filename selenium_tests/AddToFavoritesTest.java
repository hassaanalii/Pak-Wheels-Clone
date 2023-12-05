import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddToFavoritesTest {
    public static void main(String[] args) {
        
        System.setProperty("webdriver.chrome.driver", "C:\Downloads\ChromeDriver");

        ChromeOptions options = new ChromeOptions();
        options.setHeadless(true); 
        WebDriver driver = new ChromeDriver(options);

        try {
            
            driver.get("http://127.0.0.1:8080/favourite-specific-car/1");

            WebDriverWait wait = new WebDriverWait(driver, 10);
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("form-notes-id"))); 
         
            WebElement notes = driver.findElement(By.id("form-notes-id")); 
            notes.sendKeys("Test Note");

            WebElement rating = driver.findElement(By.id("form-rating-id")); 
            rating.sendKeys("5");

           
            driver.findElement(By.cssSelector("button[type='submit']")).click();


        } finally {
            driver.quit();
        }
    }
}
