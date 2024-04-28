import { create_time_tracker } from "./time_tracker.js";

async function display_labels() {
  let labels = await get_labels();
  let display_area = document.querySelector(".labels");
  clean_display_area();

  for (let index = 0; index < labels.length; index++) {
    display_area.innerHTML +=
      '<button class="label btn btn-light">' + labels[index] + "</button>";
  }
  display_area.innerHTML +=
    '<button class="btn btn-dark add-btn" id="add-label">Add</button>';
  display_area.innerHTML +=
    '<button class="btn btn-dark delete-btn" id="delete-label">Delete</button>';
}

async function get_labels() {
  const response = await fetch("http://127.0.0.1:5000/labels");

  if (!response.ok) {
    throw new Error("Not ok");
  } else {
    const labels = await response.json();
    return labels;
  }
}

async function create_label(name) {
  fetch("http://127.0.0.1:5000/labels", {
    method: "POST",
    body: JSON.stringify({
      label_name: name,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
}

async function delete_label(name) {
  fetch("http://127.0.0.1:5000/labels/l", {
    method: "POST",
    body: JSON.stringify({
      label_name: name,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
}

function clean_display_area() {
  document.querySelector(".labels").innerHTML = "";
}

function init_labels() {
  let labels = document.querySelectorAll(".label");

  for (let index = 0; index < labels.length; index++) {
    labels[index].addEventListener("click", () => {
      create_time_tracker(labels[index].innerText);
    });
  }
}

function init_add_label() {
  let add_label_button = document.querySelector("#add-label");

  add_label_button.addEventListener("click", () => {
    let label_name = prompt("Create a new label:");

    if (label_name != null) {
      create_label(label_name).then(() => {
        display_labels(get_labels()).then(() => {
	    init();
        });
      });
    }
  });
}

function init_delete_label() {
  let delete_label_button = document.querySelector("#delete-label");

  delete_label_button.addEventListener("click", () => {
    let label_name = prompt("Delete a label:");

    if (label_name != null) {
      delete_label(label_name).then(() => {
        display_labels(get_labels()).then(() => {
	    init();
        });
      });
    }
  });
}

function init() {
  init_labels();
  init_add_label();
  init_delete_label();
}

export { clean_display_area, get_labels, display_labels, init };
