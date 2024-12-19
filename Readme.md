# Lab 11 - Automation and Web Testing

## **Lab 11 Requirement:**

### Description:
The objective of this assignment is to automate web interactions using Selenium in Python. The task is to create a Python script that opens a website, searches for a product, extracts relevant details from the product page, and saves a screenshot of the page.

---

## **Instructions:**

### Part 1: Selenium Automation

1. **Set Up Selenium**:
   - Install the required Python libraries using:
     
     pip install selenium webdriver-manager
   

2. **Create the Python Script**:
   - Write a Python script that automates the following steps on Amazon:
     1. Open the website.
     2. Find the search bar and enter a product name (e.g., "Laptop").
     3. Wait for search results to load.
     4. Click on the first product from the search results.
     5. Extract and print:
        - The product title.
        - The product URL.
        - The product price (if available).
        - The product rating (if available).
     6. Take a screenshot of the product page and save it.
     7. Close the browser after a short delay.

3. **Required Functionalities**:
   - **Dynamic Waits**: Use WebDriverWait to ensure elements are loaded before interacting with them.
   - **Error Handling**: Implement error handling to manage situations where elements (like price or rating) are missing.
   - **Pop-up Handling**: Handle any potential pop-ups or alerts on the page.

4. **Additional Requirements**:
   - Maximize the browser window to ensure elements are visible.
   - Ensure that the product's price and rating (if present) are captured and displayed correctly.
   - Take a screenshot of the product page and save it with a meaningful name (e.g., `product_page_screenshot.png`).
   - Make sure the browser is closed after performing the necessary actions.

### Part 2: Flask Application (Backend)

1. **Flask Application**:
   - Create an in-memory list called `tasks` to store task descriptions.
   

     tasks = []
   

2. **Functions**:
   - `add_task(task)`: Adds a task to the `tasks` list.
   - `get_tasks()`: Returns the current list of tasks.

3. **Flask Routes**:
   - `/`: Displays the HTML page with:
     - A form to submit a new task.
     - A list of all current tasks.
   - `/add-task`: Accepts POST requests with a task description via form data. Adds the submitted task to the `tasks` list using `add_task()`.

### Part 3: Testing with SeleniumBase

1. **SeleniumBase Testing**:
   - Write test cases using SeleniumBase to verify the following:
     - Adding Tasks: Ensure that when a task is added, it appears in the task list.
     - Verifying Tasks: Ensure that the correct list of tasks is displayed on the page.

2. **Instructions for Testing**:
   - **Install Dependencies**:
     - Install Flask:
      
       pip install Flask
      
     - Install SeleniumBase for testing:
       
       pip install seleniumbase
       
   
   - **Create the Test File (test_app.py)**:
     - Write tests to:
       - Open the Flask application.
       - Add a task using the form.
       - Verify that the task appears in the list of tasks.

---

## **Deliverables**:

1. **Python Script**:  
   - A fully working Python script named `selenium_automation.py` that performs the tasks outlined in the instructions.
   - Screenshot: A screenshot of the product page saved as `product_page_screenshot.png`.

2. **Flask Application**:
   - Backend: `app.py`
   - Frontend: `templates/index2.html`
   - Testing: `test_app.py`

3. **Code Explanation**:  
   - A brief explanation of the script and tests, explaining:
     - How the browser is launched and configured.
     - How elements are located on the webpage.
     - How data (product title, price, rating) is extracted.
     - How the screenshot is taken and saved.
     - Any pop-ups or alerts that were handled.
