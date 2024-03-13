#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  for (let i = list.length - 1, x = 0; i >= 0; i--, x++) {
    rev[i] = list[x];
  }
  return (rev);
};
