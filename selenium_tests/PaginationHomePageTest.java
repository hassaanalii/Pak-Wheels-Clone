import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.util.List;

public class PaginationHomePageTest {
    public static void main(String[] args) {

        System.setProperty("webdriver.chrome.driver", "C:\Downloads\ChromeDriver");

        ChromeOptions options = new ChromeOptions();
        options.setHeadless(true); 
        WebDriver driver = new ChromeDriver(options);

        try {
            driver.get("http://127.0.0.1:8000/home");

            
            List<WebElement> paginationControl = driver.findElements(By.className("pagination-control"));
            if (paginationControl.size() > 0) {
                System.out.println("Pagination control test passed.");
            } else {
                System.out.println("Pagination control test failed.");
            }

 
        } finally {
            driver.quit();
        }
    }
}
