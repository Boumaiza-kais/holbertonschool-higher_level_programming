#!/usr/bin/node
exports.callMeMoby = function (n, fun) {
  for (let i = 0; i < n; i++) {
    fun();
  }
};
