# Corvix Institute of Technology

A responsive website and Streamlit app for Corvix Academy in Johar Town, Lahore.

## Courses

- **Artificial Intelligence (2 months):** Python, machine learning, deep learning, agents, chatbots, LLMs, and SLMs. Instructor: Shahzad Ishaq.
- **Graphic Designing (3 months):** design foundations, image editing, social media creative, branding, and portfolio practice. Instructor: Shahzad Ishaq.
- **E-commerce (2 months):** Amazon, Etsy, Daraz, and Shopify with Shahzad Ishaq; TikTok Seller Center and eBay with Ali Abdullah.

**Founder, owner, and CEO:** Shahzad Ishaq.

## Google Sheets enrollment

The supplied spreadsheet is linked from the site and app: [Open Corvix enrollment spreadsheet](https://docs.google.com/spreadsheets/d/1LpVDhrST0QoJJc2Rpsu2cFlQRUnuKgCwQRruUVX6Jwo/edit).

To store form submissions, bind a Google Apps Script project to the sheet and use the file at apps-script/Code.gs. Run setup() once, then deploy the script as a web app (execute as you; access for anyone).

- Set the deployed /exec URL in config.js for the static website.
- Add GOOGLE_SHEETS_ENDPOINT in Streamlit app secrets for the Streamlit app.

Until these endpoint settings are deployed, the forms direct students to contact Corvix instead of claiming submissions were stored.

## Run locally

Install dependencies with python -m pip install -r requirements.txt, then run streamlit run app.py from the repository root.

## Deploy

This repository is prepared for Streamlit Community Cloud. Choose this repository, branch main, and app.py as the entry point. Keep app secrets out of Git.# Corvix Institute of Technology

Practical courses in artificial intelligence, graphic design, and e-commerce in Johar Town, Lahore.
