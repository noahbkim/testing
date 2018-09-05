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

/** Listen for events on an element. */
function listen(element, events, callback) {
  for (let event of events)
    element.addEventListener(event, callback);
  callback({target: element}, true);
}


/** The validator keeps track of all form names that are invalid.
 *
 * The validator essential keeps a hash set of the names of the form
 * elements and provides callbacks to be bound to update events that
 * either add or remove elements from the invalid set. It also emits
 * events when it's valid or invalid.
 */
class Validator extends PolyfillEventTarget {

  /** Create a set and add all elements.
   *
   * We do the element forl oop because iterable set initialization
   * isn't supported everywhere.
   */
  constructor(elements) {
    super();
    this.invalid = new Set();
    for (let element of elements)
      this.invalid.add(element.name);
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
        this.invalid.delete(event.target.name);
      } else if (ignore !== true) {
        if (invalid) invalid(event.target);
        this.invalid.add(event.target.name);
      }
      this.emit("validate", this.invalid.size === 0);
    }
  }

}
