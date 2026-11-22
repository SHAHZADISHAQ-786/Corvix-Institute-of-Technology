from __future__ import annotations

import re
import secrets
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
import streamlit as st


ROOT = Path(__file__).resolve().parent
SPREADSHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1LpVDhrST0QoJJc2Rpsu2cFlQRUnuKgCwQRruUVX6Jwo/edit"
)
COURSES = [
    {
        "name": "Artificial Intelligence",
        "color": "ai",
        "duration": "2 months",
        "instructor": "Shahzad Ishaq",
        "summary": "Learn Python and build a foundation in machine learning, deep learning, language models, and practical AI applications.",
        "topics": [
            "Python fundamentals for AI",
            "Machine learning (ML) foundations",
            "Deep learning (DL) concepts",
            "Large and small language models (LLMs and SLMs)",
            "AI agents, workflows, and chatbots",
            "A guided AI project",
        ],
        "level": "Beginner-friendly",
    },
    {
        "name": "Graphic Designing",
        "color": "design",
        "duration": "3 months",
        "instructor": "Shahzad Ishaq",
        "summary": "Learn visual design foundations and create clear graphics for digital and print projects.",
        "topics": [
            "Color theory, typography, and visual hierarchy",
            "Composition, layouts, and design principles",
            "Image editing and digital graphics",
            "Social media creative and brand identity",
            "Guided design exercises and portfolio pieces",
        ],
        "level": "Start with the fundamentals",
    },
    {
        "name": "E-commerce",
        "color": "commerce",
        "duration": "2 months",
        "instructor": "Shahzad Ishaq and Ali Abdullah",
        "summary": "Explore six major selling platforms and practice presenting products and managing online-store basics.",
        "topics": [
            "Amazon seller and product-listing basics — Shahzad Ishaq",
            "Etsy shop and listing basics — Shahzad Ishaq",
            "Daraz seller basics — Shahzad Ishaq",
            "Shopify storefront fundamentals — Shahzad Ishaq",
            "TikTok Seller Center — Ali Abdullah",
            "eBay selling fundamentals — Ali Abdullah",
            "Product research, listings, orders, and customer service",
        ],
        "level": "Practical digital-business skills",
    },
]
CONTACT_PHONE = "0346 4433934"
CONTACT_EMAIL = "sahibzadashahzadishaq@gmail.com"

st.set_page_config(
    page_title="Corvix Academy | Skills for what's next",
    page_icon=":material/school:",
    layout="wide",
)

if not st.session_state.get("corvix_intro_shown"):
    with st.spinner("Getting Corvix Academy ready…"):
        time.sleep(0.7)
    st.session_state["corvix_intro_shown"] = True

st.html(
    """
    <style>
      .st-key-course-ai {
        border: 1px solid #cce49c;
        border-top: 6px solid #95c83d;
        border-radius: 16px;
        background: linear-gradient(145deg, #f1fbdc, #ffffff 78%);
        padding: 1.15rem;
      }
      .st-key-course-design {
        border: 1px solid #dacdf9;
        border-top: 6px solid #8a63e6;
        border-radius: 16px;
        background: linear-gradient(145deg, #f0e9ff, #ffffff 78%);
        padding: 1.15rem;
      }
      .st-key-course-commerce {
        border: 1px solid #bce7e2;
        border-top: 6px solid #26a4a0;
        border-radius: 16px;
        background: linear-gradient(145deg, #ddf7f3, #ffffff 78%);
        padding: 1.15rem;
      }
      .corvix-eyebrow {
        color: #64746a;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
      }
      .corvix-footer {
        border-top: 1px solid #e2e7df;
        color: #65716c;
        margin-top: 2rem;
        padding-top: 1rem;
      }
      @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after { scroll-behavior: auto !important; }
      }
    </style>
    """
)

brand, location = st.columns([3, 2], vertical_alignment="center")
with brand:
    st.markdown("# corvix<span style='color:#83b43d'>.</span>", unsafe_allow_html=True)
    st.caption("ACADEMY · LEARN. CREATE. GROW.")
with location:
    location_info, sheet_link = st.columns([1.2, 1], vertical_alignment="center")
    with location_info:
        st.markdown("**Johar Town, Lahore**  \nPractical skills for what's next.")
    with sheet_link:
        st.link_button(
            "Google Sheet",
            SPREADSHEET_URL,
            icon=":material/table_chart:",
            width="stretch",
        )

home_tab, courses_tab, about_tab, enroll_tab = st.tabs(
    ["Home", "Courses", "About", "Admissions"]
)

with home_tab:
    intro, portrait = st.columns([1.25, 0.75], vertical_alignment="center")
    with intro:
        st.markdown("#### Learn. Create. Grow.")
        st.title("Make your next move count.")
        st.write(
            "Build practical skills in AI, graphic design, and e-commerce. "
            "Learn the fundamentals, make things, and take your next step with confidence."
        )
        st.caption("Choose Courses above to explore each learning path.")
    with portrait:
        st.image(
            ROOT / "assets" / "corvix-portrait.png",
            alt="Portrait shared for the Corvix Academy website",
            width="stretch",
        )
    st.caption("Learn in a supportive environment in Johar Town, Lahore.")

with courses_tab:
    st.markdown("<p class='corvix-eyebrow'>Find your direction</p>", unsafe_allow_html=True)
    st.header("Skills for the real world")
    st.write("Explore the topics and hands-on practice covered in each learning path.")
    course_columns = st.columns(3)
    for column, course in zip(course_columns, COURSES):
        with column:
            with st.container(border=True, key=f"course-{course['color']}"):
                st.badge(course["level"], color={
                    "ai": "green",
                    "design": "violet",
                    "commerce": "blue",
                }[course["color"]])
                st.subheader(course["name"])
                st.badge(course["duration"], color="blue")
                st.caption(f"Instructor: {course['instructor']}")
                st.write(course["summary"])
                with st.expander("View course topics"):
                    for topic in course["topics"]:
                        st.markdown(f"- {topic}")
                st.caption("Ask us about this course in Admissions.")

with about_tab:
    left, right = st.columns([1, 1.2], vertical_alignment="center")
    with left:
        st.image(
            ROOT / "assets" / "corvix-portrait.png",
            alt="Portrait shared for the Corvix Academy website",
            width="stretch",
        )
    with right:
        st.markdown("<p class='corvix-eyebrow'>More than a class</p>", unsafe_allow_html=True)
        st.header("Learn it. Try it. Make it yours.")
        st.write(
            "At Corvix, learning is about doing—not just watching. "
            "Our courses focus on clear fundamentals, guided practice, "
            "and steady progress at your own pace."
        )
        st.markdown(
            "- **Practical from day one:** build understanding through hands-on learning.\n"
            "- **A supportive place to grow:** ask questions, explore ideas, and keep improving.\n"
            "- **Learn close to home:** join us in Johar Town, Lahore."
        )
        st.subheader("Founder, owner, and CEO")
        st.write("**Shahzad Ishaq**")
        st.caption(
            "Instructor for AI, graphic design, and the Amazon, Etsy, Daraz, and Shopify modules. "
            "TikTok Seller Center and eBay modules are taught by Ali Abdullah."
        )
        st.link_button(
            "Open the enrollment spreadsheet",
            SPREADSHEET_URL,
            icon=":material/table_chart:",
        )

with enroll_tab:
    contact, enquiry = st.columns([0.85, 1.15], vertical_alignment="top")
    with contact:
        st.markdown("<p class='corvix-eyebrow'>Your next step</p>", unsafe_allow_html=True)
        st.header("Good things start with hello.")
        st.write("Tell us what you would like to learn. We’ll get back to you about the next steps.")
        st.markdown(f"**Phone:** [{CONTACT_PHONE}](tel:+923464433934)")
        st.markdown(f"**Email:** [{CONTACT_EMAIL}](mailto:{CONTACT_EMAIL})")
        st.markdown("**Location:** Johar Town, Lahore, Pakistan")
    with enquiry:
        st.subheader("Enrollment enquiry")
        with st.form("corvix-enrollment"):
            student_name = st.text_input("Your name", max_chars=100)
            phone = st.text_input("Phone number", max_chars=30)
            email = st.text_input("Email address (optional)", max_chars=150)
            course_name = st.selectbox(
                "Course of interest",
                ["Choose a course", *[course["name"] for course in COURSES], "Other / not sure yet"],
            )
            message = st.text_area("What would you like to learn? (optional)", max_chars=1000)
            submitted = st.form_submit_button(
                "Send my enquiry",
                type="primary",
                icon=":material/send:",
                width="stretch",
            )

        if submitted:
            if not student_name.strip() or not phone.strip() or course_name == "Choose a course":
                st.error("Please add your name, phone number, and course of interest.")
            elif email.strip() and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()):
                st.error("Please enter a valid email address, or leave it blank.")
            else:
                try:
                    endpoint = st.secrets.get("GOOGLE_SHEETS_ENDPOINT", "")
                except FileNotFoundError:
                    endpoint = ""

                if not endpoint:
                    st.warning(
                        f"Online enrolment is not connected yet. Please call {CONTACT_PHONE} "
                        f"or email {CONTACT_EMAIL}."
                    )
                else:
                    parsed_endpoint = urlparse(endpoint)
                    if (
                        parsed_endpoint.scheme != "https"
                        or not (
                            parsed_endpoint.hostname == "google.com"
                            or (
                                parsed_endpoint.hostname is not None
                                and parsed_endpoint.hostname.endswith(".google.com")
                            )
                        )
                    ):
                        st.error("The enrollment form is not configured with a valid Google Apps Script URL.")
                    else:
                        try:
                            response = requests.post(
                                endpoint,
                                data={
                                    "source": "streamlit",
                                    "nonce": secrets.token_hex(24),
                                    "name": student_name.strip(),
                                    "phone": phone.strip(),
                                    "email": email.strip(),
                                    "course": course_name,
                                    "message": message.strip(),
                                },
                                timeout=20,
                            )
                            response.raise_for_status()
                            result = response.json()
                            if result.get("success"):
                                st.success("Thank you! Your enquiry has been sent to Corvix Academy.")
                            else:
                                st.error("We couldn’t save your enquiry. Please contact us by phone or email.")
                        except (requests.RequestException, ValueError) as error:
                            st.error(f"We couldn’t verify your enquiry was saved: {error}")

st.html(
    f"<div class='corvix-footer'>© {time.localtime().tm_year} Corvix Academy · "
    "Johar Town, Lahore · "
    f"<a href='mailto:{CONTACT_EMAIL}'>{CONTACT_EMAIL}</a></div>"
)
