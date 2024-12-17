#!/usr/bin/node
exports.addMeMaybe = function (num, funct) {
    let nb = num + 1;
    funct(nb);
}
