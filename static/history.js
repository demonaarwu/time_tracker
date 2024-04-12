async function create_history(time_tracker) {
  fetch("http://127.0.0.1:5000/history", {
    method: "POST",
    body: JSON.stringify({
      label_name: time_tracker.name,
      time: Math.round((Date.now() - time_tracker.time) / 1000),
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
}

export { create_history };
