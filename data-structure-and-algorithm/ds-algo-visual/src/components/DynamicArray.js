class DynamicArray {
  constructor(capacity) {
    this._array = new Array(capacity).fill(0);
    this._cap = capacity;
    this._size = 0;
  }

  get capacity() {
    return this._cap;
  }

  get size() {
    return this._size;
  }

  setItem(i, n) {
    this._array[i] = n;
  }

  getItem(i) {
    return this._array[i];
  }

  pushback(n) {
    if (this._size === this._cap) {
      this.resize();
    }
    this._array[this._size] = n;
    this._size += 1;
  }

  popback() {
    this._size -= 1;
    return this._array[this._size];
  }

  resize() {
    this._cap *= 2;
    const newArray = new Array(this._cap).fill(0);
    for (let i = 0; i < this._array.length; i++) {
      newArray[i] = this._array[i];
    }
    this._array = newArray;
  }
}

export default DynamicArray;
