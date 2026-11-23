# Corvix Institute of Technology

A responsive website and Streamlit app for Corvix Academy in Johar Town, Lahore.

**Live Streamlit app:** https://corvix-academy-lahore.streamlit.app/

## Courses

- **Artificial Intelligence (2 months):** Python, machine learning, deep learning, agents, chatbots, LLMs, and SLMs. Instructor: Shahzad Ishaq.
- **Graphic Designing (3 months):** design foundations, image editing, social media creative, branding, and portfolio practice. Instructor: Shahzad Ishaq.
- **E-commerce (2 months):** Amazon, Etsy, Daraz, and Shopify with Shahzad Ishaq; TikTok Seller Center and eBay with Ali Abdullah.

**Founder, owner, and CEO:** Shahzad Ishaq.

## Google Sheets enrollment

Student enquiries submitted through the website or Streamlit form are saved using the configured Apps Script endpoint. The spreadsheet itself is not linked publicly.

To store form submissions, bind a Google Apps Script project to the sheet and use the file at apps-script/Code.gs. Run setup() once, then deploy the script as a web app (execute as you; access for anyone).

- Set the deployed /exec URL in config.js for the static website.
- Add GOOGLE_SHEETS_ENDPOINT in Streamlit app secrets for the Streamlit app.

The form reports success only after Apps Script confirms that an enquiry was saved.

## Run locally

Install dependencies with python -m pip install -r requirements.txt, then run streamlit run app.py from the repository root.

## Deploy

This app is deployed on Streamlit Community Cloud from this repository's main branch using app.py. Keep app secrets out of Git.
