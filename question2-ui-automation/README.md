# UI Test Automation with Selenium – Pos Malaysia Rate Calculator

This automation script uses **Selenium (Python)** to verify the rate calculator on the [Pos Malaysia](https://www.pos.com.my/send/ratecalculator) website.

---

## Test Scenario

**Goal**: Verify that the calculator works when entering a valid postcode, selecting a destination country (India), and inputting weight.

### Test Steps:
1. Open the [rate calculator](https://www.pos.com.my/send/ratecalculator)
2. Leave the "From" country in the default value as 'Malaysia', then enter postcode: `35600`
3. Select country: `India` and leave the postcode empty.
4. Enter weight: `1kg`
5. Click on the **Calculate** button
6. Verify user can see multiple quotes and shipments options available.

---

## Technologies Used

- **Language**: Python
- **Framework**: Selenium WebDriver
- **Browser Driver**: ChromeDriver
- **Waiting Mechanism**: WebDriverWait + Expected Conditions

---

## Setup Instructions

### 1. Install Requirements

Make sure you have Python installed. Then install Selenium:

```bash
pip install selenium
```

### 2. Download ChromeDriver

- Visit: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
- Download the version that matches your Chrome browser
- Place `chromedriver` in your project folder or add to system PATH

### 3. Run the Script

python pos_rate_calculator_test.py

---

## File Structure

```
question2-ui-automation/
│
├── pos_rate_calculator_test.py     # Main automation script
└── README.md                       # You're reading this!
```

## Author

Evelyn Loh
[GitHub Profile](https://github.com/evelynwork-QA/pos-malaysia-assessment-test/)
