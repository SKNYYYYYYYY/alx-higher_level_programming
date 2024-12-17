#!/usr/bin/node
exports.addMeMaybe = function (num, funct) {
  const nb = num + 1;
  funct(nb);
};
