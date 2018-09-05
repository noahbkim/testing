/** Small utility for finding several elements by their IDs. */
function find(elements) {

  /* Handle a dictionary of ID: null. */
  if (elements instanceof Object) {
    for (let id of Object.keys(elements))
      if (elements.hasOwnProperty(id))
        elements[id] = document.getElementById(id);
    return elements;

  /* Handle an array of IDs. */
  } else if (elements instanceof Array) {
    const map = {};
    for (let id of elements)
      elements[id] = document.getElementById(id);
    return map;
  }

}


class Validator extends PolyfillEventTarget {

  constructor(elements) {
    super();
    this.invalid = new Set();
    for (let element of elements)
      this.invalid.add(element);
  }

  /** Generate a callback that validates an event target.
   *
   * The return is a callable which can be added as an event listener
   * directly. The condition is a callable given the target HTML
   * element and the update is a global update callable invoked after
   * changes have been made.
   */
  check(condition, valid, invalid) {

    // Add default validation behavior but allow it to be cancelled with null
    if (valid === undefined) valid = element => element.classList.remove("invalid");
    if (invalid === undefined) invalid = element => element.classList.add("invalid");

    // Generate the check function
    return (event, ignore) => {  // Use ignore flag to only do validation
      if (condition(event.target)) {
        if (valid) valid(event.target);
        this.invalid.delete(event.target);
      } else if (ignore !== true) {
        if (invalid) invalid(event.target);
        this.invalid.add(event.target);
      }
      this.emit("validate", this.invalid.size === 0);
    }
  }

  /** Listen for events on an element. */
  listen(element, events, callback) {
    for (let event of events)
      element.addEventListener(event, callback);
    callback({target: element}, true);
  }

}
