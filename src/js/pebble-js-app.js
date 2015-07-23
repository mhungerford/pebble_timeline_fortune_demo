var topic = 'fortune';

Pebble.addEventListener("ready", function(e) {
  console.log("started js app");

  Pebble.timelineSubscribe(topic, function () {
    console.log('Subscribed to ' + topic);
  }, function (error) {
    console.log('Error subscribing to topic: ' + error);
  });
});
