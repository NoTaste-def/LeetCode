/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function () {
  if (this.length === 0) {
    console.log(-1);
    return -1;
  }
  console.log(this[this.length - 1]);
  return this[this.length - 1];
};

const arr = [1, 2, 3];
arr.last(); // 3