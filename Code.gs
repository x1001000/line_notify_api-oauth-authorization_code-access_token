function doGet(e) {
  var sheet = SpreadsheetApp.getActiveSheet();
  var lastRow = sheet.getLastRow();
  var values = sheet.getRange(1, 1, lastRow).getValues()
  return ContentService.createTextOutput(values);
}

function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSheet();
  var lastRow = sheet.getLastRow();
  sheet.getRange(lastRow + 1, 1).setValue(e.parameter.access_token);
}
