var express = require('express');
var cookieParser = require('cookie-parser');
var session = require('express-session');
var path = require('path');
var routes = require('./routes');

var app = express();

app.use(express.static(path.join(__dirname, 'public')));
app.use(cookieParser());
app.use(session({
  secret: 'not really a secret so create your own',
  name: 'node_oauth_web_flow'
}));

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use('/', routes);

var server = app.listen(3000, function() {
  console.log("Listening on port %d", server.address().port);
});