class PolyfillEventTarget {

  constructor() {
    this.listeners = {};
  }

  addEventListener(event, callback) {
    if (this.listeners.hasOwnProperty(event))
      this.listeners[event].push(callback);
    else this.listeners[event] = [callback];
  }

  removeEventListener(event, callback) {
    if (!this.listeners.hasOwnProperty(event)) return;
    let index = this.listeners[event].indexOf(callback);
    if (index !== -1)
      this.listeners.splice(index, 1);
  }

  emit(event, data) {
    if (this.listeners.hasOwnProperty(event))
      for (let callback of this.listeners[event])
        callback(data);
  }

}
