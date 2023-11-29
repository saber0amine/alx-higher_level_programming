#!/usr/bin/node

module.exports = {
  addMeMaybe: function (num, func) {
    func(++num);
  }
};
