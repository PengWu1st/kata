const { JSDOM } = require("jsdom");
const { window } = new JSDOM();
global.document = window.document;
global.window = window;

let activeEffect = null;
class Dep {
  constructor() {
    this.subscribers = new Set();
  }
  depend() {
    if (activeEffect) {
      this.subscribers.add(activeEffect);
    }
  }
  notify() {
    this.subscribers.forEach((sub) => sub());
  }
}

function observe(obj) {
  Object.keys(obj).forEach((key) => {
    const dep = new Dep();
    let value = obj[key];
    Object.defineProperty(obj, key, {
      get() {
        dep.depend();
        return value;
      },
      set(newValue) {
        value = newValue;
        dep.notify();
      },
    });
  });
}

function autorun(effect) {
  function wrapper() {
    activeEffect = wrapper;
    effect();
    activeEffect = null;
  }
  wrapper();
}

test("some reactivity test", () => {
  const state = { count: 0 };
  observe(state);
  console.log = jest.fn();

  autorun(() => {
    console.log(state.count);
  });
  expect(console.log).toHaveBeenCalledWith(0);
  state.count++;
  expect(console.log).toHaveBeenCalledWith(1);
});
