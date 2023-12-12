# Health Diagnosis System

Welcome to the Health Diagnosis System! This project aims to predict diseases based on user symptoms and suggests precautions based on the identified disease. The system is in its early stages of development, and a Decision Tree model is being trained to achieve accurate predictions. The dataset required for training the model is available in the 'data' folder.

## Project Overview

- **Flask Web Application:** The web application is developed using Flask by Nikesh Shrestha, a classmate involved in this project. The application provides an interface for users to input their symptoms and receive disease predictions along with recommended precautions.

- **Decision Tree Model:** The disease prediction functionality is powered by a Decision Tree model, which is currently in the training phase. The training process involves using the available dataset to enable the model to make accurate predictions based on symptoms.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Jyotsan-Hamal/ML-projects.git]
   cd Health Diagnosis System
   ```
2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
   ```
3. **Train the Decision Tree Model:**
    ```bash
    python train_model.py

   ```
4. **Run the Flask Web Application:**
       ```bash
       python app.py
         ```
The web application will be accessible at http://localhost:5000 in your web browser.

## Project Structure
- **data:** Contains the dataset used for training the Decision Tree model.
- **templates:** HTML templates for the Flask web application.
- **static:** Static files (CSS, images) for the Flask web application.
- **app.py:** The main Flask application file.
- **train_model.py:** Script for training the Decision Tree model.
