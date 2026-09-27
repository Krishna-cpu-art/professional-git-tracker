import os
import streamlit as st
import requests

# 1. Configure the web page tab and layout
st.set_page_config(page_title="Professional Git Tracker", layout="centered")

# 2. Add the main title and description to the UI
st.title("The Professional Git Tracker")
st.write("Turn raw code changes into professional commit messages and plain-English progress reports.")

# 3. Create a text box for the user to paste their code, saving it to 'code_diff'
code_diff = st.text_area("Paste your code changes here:", height=200)

# 4. Create the button and check if it gets clicked
if st.button("Generate Commit & Report"):
    
    # 5. Check if the user actually pasted something (length > 0)
    if len(code_diff) > 0:
        st.info("Analyzing your code...")
        
        # --- START OF API LOGIC ---
        
        # 6. Set up the API Key and exact URL (Paste your real key here)
        api_key = os.environ.get("Gemini_API_Key")
        if not api_key:
            st.error("API key not found. Please set the 'Gemini_API_Key' environment variable.")
            st.stop()
        
        # Use an f-string to inject the api_key into the URL. 
        # Make sure there are no typos or spaces in this exact URL string!
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={api_key}"
        
        # 7. Define the instructions (prompt) for the AI, injecting the user's code
        prompt = f"""You are a mentor who is teaching a student how to publish a project on Git. 
        Take the input code from the user and mentor him. 
        Firstly, give him a professional technical Git commit message. 
        Then explain in plain English how the code works.
        
        Here are the code changes:
        {code_diff}
        """
        
        # 8. Structure the payload exactly as Google's API expects it
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        
        # 9. Send the POST request to the API
        response = requests.post(url, json=payload)
        
        # 10. Check if the server responded with a 200 Success code
        if response.status_code == 200:
            # Convert response to dictionary
            data = response.json()
            
            # Extract just the text from the nested dictionary structure
            ai_message = data["candidates"][0]["content"]["parts"][0]["text"]
            
            # Display success message and the AI's output on the website
            st.success("Done!")
            st.write(ai_message)
            
        else:
            # If it's not 200 (like your previous 404), print the error code to the screen
            st.error(f"API Error. Status Code: {response.status_code}")
            # Also print the raw error message from the server to help us debug
            st.error(response.text)
            
        # --- END OF API LOGIC ---
            
    else:
        # If the text box was empty when they clicked the button
        st.warning("Please paste some code changes first.")