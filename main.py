from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os
import random
# Set up environment variable for the API key
API_KEY = "YOUR_API_KEY"  # Make sure to set this in your environment
genai.configure(api_key=API_KEY)
# Initialize FastAPI app
app = FastAPI()
# Pricing logic: Minimum and maximum price
MIN_PRICE = 50
MAX_PRICE = 100
INITIAL_OFFER = 100
# Request schema for user input
class OfferInput(BaseModel):
    user_offer: int
# Function to call the Gemini API for generating chatbot responses
def get_gemini_response(prompt: str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
# Negotiation logic: Handle user offers and generate bot counter-offers
def negotiate(user_offer: int):
    # Simple negotiation logic
    if user_offer >= MAX_PRICE:
        bot_offer = f"That's too high. I can accept ${MAX_PRICE} as the maximum."
    elif user_offer >= INITIAL_OFFER:
        bot_offer = f"That's a fair offer. I'll accept your offer of ${user_offer}."
    elif user_offer >= MIN_PRICE:
        # Counter slightly above user's offer, but below initial
        counter_offer = random.randint(user_offer + 5, INITIAL_OFFER)
        bot_offer = f"How about ${counter_offer}? Can we meet halfway?"
    else:
        bot_offer = f"${user_offer} is too low. The minimum I can accept is ${MIN_PRICE}."
    # Generate a response using Gemini for dynamic conversation
    prompt = f"The customer offered ${user_offer}. How should the bot respond?"
    ai_response = get_gemini_response(prompt)
    return bot_offer, ai_response
# Endpoint to start the negotiation
@app.get("/start-negotiation")
def start_negotiation():
    bot_offer = INITIAL_OFFER
    return {
        "bot_offer": bot_offer,
        "message": f"Welcome to the negotiation! My initial offer is ${bot_offer}. What's your counteroffer?"
    }
# Endpoint to handle user offers and bot responses
@app.post("/negotiate")
def handle_negotiation(offer_input: OfferInput):
    user_offer = offer_input.user_offer
    # Ensure the user offer is valid
    if user_offer < 0:
        raise HTTPException(status_code=400, detail="Offer price must be a positive number.")
    # Negotiate based on user offer
    bot_offer, ai_response = negotiate(user_offer)
    return {
        "user_offer": user_offer,
        "bot_offer": bot_offer,
        "ai_response": ai_response
    }
# Run FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
