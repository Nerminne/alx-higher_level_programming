#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let taskNum = 0;
const info = {};
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const content = JSON.parse(body);
    let usrid = content[0].userId;
    for (const i in content) {
      if (content[i].userId === usrid) {
        if (content[i].completed) {
          taskNum++;
        }
      } else {
        info[usrid] = taskNum;
        usrid++;
        taskNum = 0;
        if (content[i].completed) {
          taskNum++;
        }
      }
    }
    console.log(info);
  } else {
    console.log(`Error Code: ${response.statusCode}`);
  }
});
