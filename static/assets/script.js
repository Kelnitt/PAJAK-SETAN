function ValidAprioriRules(event) {
  var support = document.getElementById("support").value;
  var confidence = document.getElementById("confidence").value;
  var supportError = document.getElementById("supportError");
  var confidenceError = document.getElementById("confidenceError");
  console.log(support)
  console.log(confidence)
  var valid = true;

  // Validate Min Support (between 0.01 and 0.1)
  if (support < 0.01 || support > 0.1) {
      supportError.textContent = "Min. Support must be between 0.01 and 0.1";
      valid = false;
  } else {
      supportError.textContent = "";
  }

  // Validate Min Confidence (between 0.1 and 1.0)
  if (confidence < 0.1 || confidence > 1.0) {
      confidenceError.textContent = "Min. Confidence must be between 0.1 and 1.0";
      valid = false;
  } else {
      confidenceError.textContent = "";
  }

  // If form is not valid, prevent submission
  if (!valid) {
      event.preventDefault();
  }
}