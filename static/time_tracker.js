import {
  clean_display_area,
  display_labels,
  get_labels,
  init,
} from "./label.js";

import { display_time_format } from "./time_format.js";

import { create_history } from "./history.js";

class TimeTracker {
  constructor(name, time) {
    this.name = name;
    this.time = time;
  }
}

function create_time_tracker(label_name, unix_time=new Date().getTime()) {
    let display_area = document.querySelector(".labels");
  const tracker = new TimeTracker(label_name, unix_time);

  add_tracker(tracker).then(() => {
  clean_display_area();
  display_area.innerHTML = '<div class="container" id="time-tracker"></div>';

  display_time_tracker(tracker);

  const trackerInterval = window.setInterval(() => {
    display_time_tracker(tracker);
  }, 1000);

  let tracker_area = document.querySelector("#time-tracker");
  tracker_area.addEventListener("click", () => {
    clearInterval(trackerInterval);
    create_history(tracker);
    display_labels(get_labels()).then(() => {
      init();
    });
  });

  });
}

function display_time_tracker(time_tracker) {
  let tracker_area = document.querySelector("#time-tracker");
  tracker_area.innerHTML = "";
  tracker_area.innerHTML +=
    "<p class='time-tracker-name'>" +
    time_tracker.name +
    " " +
    display_time_format(Math.round((Date.now()-time_tracker.time)/1000)) +
    "</p>";
}

async function check_tracker_exist() {
  let response = await fetch("http://127.0.0.1:5000/time_tracker");

  if (!response.ok) {
    throw new Error("Not ok");
  } else {
    const json = await response.json();
    const tracker_status = json["status"];
    if (tracker_status == "true") {
      return true;
    } else {
      return false;
    }
  }
}

async function get_tracker() {
  let response = await fetch("http://127.0.0.1:5000/time_tracker");

  if (!response.ok) {
    throw new Error("Not ok");
  } else {
    const json = await response.json();

    let tracker = new TimeTracker();
    tracker.time = json["unix_time"];
    tracker.name = json["label_name"];

    return tracker;
  }
}

async function add_tracker(tracker) {
  fetch("http://127.0.0.1:5000/time_tracker", {
    method: "POST",
    body: JSON.stringify({
      label_name: tracker.name,
      unix_time: new Date().getTime(),
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
}

export { TimeTracker, create_time_tracker, check_tracker_exist, get_tracker };
