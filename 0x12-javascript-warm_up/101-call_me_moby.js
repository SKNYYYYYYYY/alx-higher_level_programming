#!/usr/bin/node
exports.callMeMoby = function (a, x) {
  for (let i = 0; i < a; i++) {
    x();
  }
};
