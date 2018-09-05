/** Validation for the registration page. */

// List all the form elements
const elements = find({
  first_name: null, last_name: null,
  email: null, age: null, male: null, female: null,
  password1: null, password2: null
});

// Create a validator
const validator = new Validator(Object.values(elements));

// Create a check for whether the update function should be disabled
const submit = document.getElementById("submit");
validator.addEventListener("validate", valid => submit.disabled = !valid);

// Listen to all our elements
const INPUTS = ["focus", "input"];
const filled = validator.check(element => element.value !== "");
const numeric = validator.check(element => element.value !== "" && /^\d+$/.test(element.value));
const password2 = validator.check(element => element.value === elements.password1.value && element.value !== "");

validator.listen(elements.first_name, INPUTS, filled);
validator.listen(elements.last_name, INPUTS, filled);
validator.listen(elements.email, INPUTS,
  validator.check(element => /^[^@]+@[^.]+\..+$/.test(element.value)));
validator.listen(elements.age, INPUTS, numeric);
validator.listen(elements.password1, INPUTS,
  validator.check(element => element.value.length >= 8));
validator.listen(elements.password2, INPUTS, password2);

// Update the second password validation when the first changes
elements.password1.addEventListener("input", () => password2({target: elements.password2}));

// Do special checking for the radio selection
const selected = validator.check(() => elements.male.checked || elements.female.checked, null, null);
validator.listen(elements.female, ["change"], selected);
validator.listen(elements.male, ["change"], selected);
