/** Validation for the login page. */

// List all the form elements
const elements = find({email: null, password: null});

// Create a validator
const validator = new Validator(Object.values(elements));

// Create a check for whether the update function should be disabled
const login = document.getElementById("login");
validator.addEventListener("validate", valid => login.disabled = !valid);

// Listen to all our elements
const INPUTS = ["focus", "input"];

listen(elements.email, INPUTS, validator.check(element => /^[^@]+@[^.]+\..+$/.test(element.value)));
listen(elements.password, INPUTS, validator.check(element => element.value !== ""));
