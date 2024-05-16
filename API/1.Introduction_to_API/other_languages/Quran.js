var request = require('request');
var options = {
  'method': 'GET',
  'url': 'http://api.alquran.cloud/v1/surah/114',
  'headers': {
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
