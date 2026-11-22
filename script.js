(() => {
  const menuButton = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".primary-nav");
  const form = document.querySelector("#enrollment-form");
  const status = document.querySelector("#form-status");
  const frame = document.querySelector("#submission-frame");
  const pageLoader = document.querySelector("#page-loader");
  const nonceField = document.querySelector("#submission-nonce");
  const submitButton = form.querySelector('button[type="submit"]');
  let pendingNonce = "";
  let timeoutId;

  document.querySelector("#current-year").textContent = new Date().getFullYear();

  window.addEventListener("load", () => {
    window.setTimeout(() => pageLoader.classList.add("is-hidden"), 650);
  }, { once: true });

  menuButton.addEventListener("click", () => {
    const expanded = menuButton.getAttribute("aria-expanded") === "true";
    menuButton.setAttribute("aria-expanded", String(!expanded));
    menuButton.setAttribute("aria-label", expanded ? "Open menu" : "Close menu");
    nav.classList.toggle("is-open", !expanded);
  });

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("is-open");
      menuButton.setAttribute("aria-expanded", "false");
      menuButton.setAttribute("aria-label", "Open menu");
    });
  });

  document.querySelectorAll("[data-course]").forEach((link) => {
    link.addEventListener("click", () => {
      document.querySelector("#student-course").value = link.dataset.course;
    });
  });

  window.addEventListener("message", (event) => {
    if (event.source !== frame.contentWindow || !event.data || event.data.type !== "corvix-enrollment") return;
    if (!pendingNonce || event.data.nonce !== pendingNonce) return;
    window.clearTimeout(timeoutId);
    pendingNonce = "";
    submitButton.disabled = false;
    submitButton.innerHTML = 'Send my enquiry <span aria-hidden="true">↗</span>';
    if (event.data.success) {
      status.dataset.state = "success";
      status.textContent = "Thanks! Your enquiry has been sent. We’ll be in touch soon.";
      form.reset();
    } else {
      status.dataset.state = "error";
      status.textContent = "We couldn’t send your enquiry. Please try again or contact us by phone or email.";
    }
  });

  form.addEventListener("submit", (event) => {
    const endpoint = window.CORVIX_CONFIG && window.CORVIX_CONFIG.googleSheetsEndpoint;
    if (!endpoint) {
      event.preventDefault();
      status.dataset.state = "error";
      status.textContent = "Online enrolment is not connected yet. Please call 0346 4433934 or email us directly.";
      return;
    }
    if (form.elements.website.value) {
      event.preventDefault();
      return;
    }
    try {
      const parsedEndpoint = new URL(endpoint);
      if (parsedEndpoint.protocol !== "https:" ||
          !(parsedEndpoint.hostname === "google.com" || parsedEndpoint.hostname.endsWith(".google.com"))) {
        throw new Error("The Google Sheets endpoint must be a secure Google Apps Script URL.");
      }
    } catch (error) {
      event.preventDefault();
      status.dataset.state = "error";
      status.textContent = error.message || "The enrollment form is not configured correctly. Please contact us directly.";
      return;
    }
    form.action = endpoint;
    pendingNonce = window.crypto && window.crypto.randomUUID
      ? window.crypto.randomUUID()
      : `${Date.now()}-${Math.random().toString(36).slice(2)}`;
    nonceField.value = pendingNonce;
    submitButton.disabled = true;
    submitButton.textContent = "Sending your enquiry…";
    status.dataset.state = "";
    status.textContent = "Sending securely to Corvix Academy…";
    timeoutId = window.setTimeout(() => {
      if (!pendingNonce) return;
      pendingNonce = "";
      submitButton.disabled = false;
      submitButton.innerHTML = 'Send my enquiry <span aria-hidden="true">↗</span>';
      status.dataset.state = "error";
      status.textContent = "We couldn’t verify your submission. Please try again or contact us by phone or email.";
    }, 15000);
  });
})();
