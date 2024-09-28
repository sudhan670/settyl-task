# Negotiation Chatbot

## Overview
This project implements a negotiation chatbot using FastAPI and the Google Generative AI library (Gemini API). The chatbot allows users to propose price offers and receive counter-offers or responses based on a defined pricing logic.

## Prerequisites
- Python 3.7+
- FastAPI
- Google Generative AI library
- Uvicorn (for running the FastAPI server)

## Installation

1. **Set Up Environment**: Ensure you have Python and pip installed. Create a virtual environment if desired.

2. **Install Required Libraries**:
   ```bash
   pip install fastapi uvicorn google-generativeai pydantic
   ```

3. **Set the API Key**: Obtain your API key from Google Cloud and set it as an environment variable:
   ```bash
   export API_KEY=<YOUR_API_KEY>
   ```

## Project Structure
```
negotiation_chatbot/
│
├── main.py                # Main FastAPI application file
└── requirements.txt       # List of dependencies
```

## Code Explanation

1. **Importing Libraries**:
   - The project imports FastAPI, Pydantic for request validation, and the Google Generative AI library for accessing the Gemini API.

2. **Configuring the Gemini API**:
   - The API key is retrieved from the environment variable and configured using the `genai.configure()` method.

3. **Defining Pricing Logic**:
   - Constants for minimum and maximum price, along with the initial offer, are defined.

4. **Request Model**:
   - A Pydantic model is defined for validating user input, specifically the user offer.

5. **Generating AI Responses**:
   - The function `get_gemini_response()` calls the Gemini API to generate responses based on the user’s input.

6. **Negotiation Logic**:
   - The `negotiate()` function handles the negotiation based on the user offer and generates a corresponding bot response.

7. **API Endpoints**:
   - Two endpoints are defined: 
     - `/start-negotiation`: Initializes the negotiation process.
     - `/negotiate`: Processes user offers and returns bot responses.

8. **Running the Server**:
   - The application runs on a specified host and port using Uvicorn.

## How to Run the Application

1. Save the code in a file named `main.py`.
2. Set your API key in the environment variable.
3. Run the application:
   ```bash
   $ uvicorn app:app
   ```
4. Access the API:
   - Start a negotiation: `GET http://localhost:8000/start-negotiation`
   - Propose an offer: `POST http://localhost:8000/negotiate` with JSON body `{"user_offer": 80}`.

## Conclusion
This README outlines the steps to integrate the Gemini API into a FastAPI application for creating a negotiation chatbot. The chatbot uses pricing logic to engage with users dynamically, offering a responsive negotiation experience. For further enhancements, consider implementing additional features such as user authentication or a more complex negotiation strategy.
