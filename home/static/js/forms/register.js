/** Validation for the registration page. */

// List all the form elements
const elements = {
  first_name: null, last_name: null,
  email: null, year: null, month: null, date: null, male: null, female: null};

// Create a list for all currently invalid elements
const invalid = new Set();

// Populate the lists but only use remove redundancy in sex elements
for (let field of Object.keys(elements))
  invalid.add(elements[field] = document.getElementById(field));  // Trying to make this as unreadable as possible
invalid.delete(elements.female);


// Create a check for whether the update function should be disabled
const submit = document.getElementById("submit");
function update() {
  submit.disabled = (invalid.size > 0);
}


// Create a check function generator based on element value
function check(condition) {
  return function(event) {
    if (condition(event.target)) {
      event.target.classList.remove("invalid");
      invalid.delete(event.target);
    } else {
      event.target.classList.add("invalid");
      invalid.add(event.target);
    }
    update();
  }
}  // This is a pretty sick idea though


// Make a convenience wrapper for event listener for multiple events
function listen(element, events, callback) {
  for (let event of events)
    element.addEventListener(event, callback);
}


// Listen to all our elements
const INPUTS = ["focus", "input"];
const filled = check(element => element.value !== "");
const numeric = check(element => element.value !== "" && /^\d+$/.test(element.value));
listen(elements.first_name, INPUTS, filled);
listen(elements.last_name, INPUTS, filled);
listen(elements.email, INPUTS, check(element => /^[^@]+@[^.]+\..+$/.test(element.value)));
listen(elements.year, INPUTS, numeric);
listen(elements.month, INPUTS, numeric);
listen(elements.date, INPUTS, numeric);


// Do special checking for the radio selection
function checkSex() {
  if (!elements.male.checked && !elements.female.checked)  invalid.add(elements.male);
  else invalid.delete(elements.male);
  update();
}
elements.female.addEventListener("click", checkSex);
elements.male.addEventListener("click", checkSex);
