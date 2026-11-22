const SHEET_NAME = "Enrollments";
const HEADERS = ["Submitted at", "Name", "Phone", "Email", "Course", "Message"];

function setup() {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  if (!spreadsheet) throw new Error("Open this Apps Script project from the Google Sheet you want to use.");
  let sheet = spreadsheet.getSheetByName(SHEET_NAME);
  if (!sheet) sheet = spreadsheet.insertSheet(SHEET_NAME);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.setFrozenRows(1);
    sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight("bold");
  }
}

function doPost(event) {
  const parameters = event && event.parameter ? event.parameter : {};
  const nonce = String(parameters.nonce || "").replace(/[^a-zA-Z0-9-]/g, "").slice(0, 100);
  const isStreamlitRequest = parameters.source === "streamlit";
  let success = false;
  try {
    const name = cleanValue(parameters.name, 100);
    const phone = cleanValue(parameters.phone, 30);
    const email = cleanValue(parameters.email, 150);
    const course = cleanValue(parameters.course, 100);
    const message = cleanValue(parameters.message, 1000);
    const spamTrap = cleanValue(parameters.website, 200);
    if (!spamTrap && nonce && name && phone && course) {
      const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
      if (!spreadsheet) throw new Error("The script must be bound to the enrollment spreadsheet.");
      let sheet = spreadsheet.getSheetByName(SHEET_NAME);
      if (!sheet) { setup(); sheet = spreadsheet.getSheetByName(SHEET_NAME); }
      sheet.appendRow([new Date(), safeCellValue(name), safeCellValue(phone), safeCellValue(email), safeCellValue(course), safeCellValue(message)]);
      success = true;
    }
  } catch (error) {
    console.error("Enrollment submission failed: " + error.message);
  }
  if (isStreamlitRequest) return ContentService.createTextOutput(JSON.stringify({success: success, nonce: nonce})).setMimeType(ContentService.MimeType.JSON);
  return HtmlService.createHtmlOutput("<!doctype html><html><body><script>window.parent.postMessage({type:'corvix-enrollment',success:" + (success ? "true" : "false") + ",nonce:" + JSON.stringify(nonce) + "},'*');</script></body></html>").setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

function cleanValue(value, maxLength) {
  return String(value || "").trim().replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, "").slice(0, maxLength);
}

function safeCellValue(value) {
  return /^[=+\-@]/.test(value) ? "'" + value : value;
}
