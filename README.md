🛒 Amazon website Automation testing using Selenium

📌 Project Overview

This project is a "Selenium-based web automation script" that mimics real user behavior while shopping online.

The bot performs the following actions:

1. Opens Google
2. Searches for Amazon
3. Navigates to the Amazon website
4. Searches for a product (iPhone 17 Pro Max)
5. Scrolls through product listings
6. Randomly selects a product
7. Switches to the product tab
8. Attempts to add the item to the cart

This project is useful for:

* Learning Selenium automation
* Practicing XPath & element locating
* Understanding waits & synchronization
* Demonstrating QA automation skills

🚀 Features

* Automated Google search navigation
* Dynamic product search on Amazon
* Random product selection logic
* Page scrolling automation
* Tab switching handling
* Add-to-cart automation
* Exception handling for robustness

🛠️ Tech Stack

* Python
* Selenium WebDriver
* ChromeDriver
* XPath Selectors
* Explicit Waits

📂 Project Structure

/Testing-amazonwebsite
│
├── amazon_bot.py        # Main automation script
├── README.md            # Project documentation
└── requirements.txt     # Dependencies (optional)

⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/SachinES1606/Testing_amazonwebsite/tree/main
cd amazon-automation-testing

2️⃣ Install Dependencies
pip install selenium

3️⃣ Download ChromeDriver
* Download the version matching your Chrome browser
* Add it to PATH or project folder
  
▶️ How to Run
python testing_amazonwebsite.py
The browser will open and automatically perform all actions.

🧠 How It Works
🪜 Step-by-Step Flow

1. Launches Chrome browser
2. Opens Google homepage
3. Searches for “Amazon”
4. Clicks Amazon search result
5. Searches for product keyword
6. Scrolls product listings
7. Randomly selects a product
8. Switches to new tab
9. Clicks **Add to Cart** button

⚠️ Important Notes

* Script uses static XPaths which may break if Amazon updates UI
* Increase/decrease based on internet speed
* Use WebDriverWait for production-level automation
* Intended for **learning/testing purposes only**

 🧪 Future Improvements

* Login automation
* Price tracking
* Multiple product search
* Headless execution
* Screenshot capture
* CSV report generation

🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Submit a Pull Request

👨‍💻 Author

Sachin
Automation & Data Enthusiast⭐
