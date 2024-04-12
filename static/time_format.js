function display_time_format(seconds) {
  let hours = (seconds - (seconds % 3600)) / 3600;
  let minutes = (seconds - hours * 3600 - ((seconds - hours * 3600) % 60)) / 60;
  let secs = seconds - hours * 3600 - minutes * 60;

  let format = "";

  if (hours <= 9) {
    format += "0" + hours + ":";
  } else {
    format += hours + ":";
  }
  if (minutes <= 9) {
    format += "0" + minutes + ":";
  } else {
    format += minutes + ":";
  }
  if (secs <= 9) {
    format += "0" + secs;
  } else {
    format += secs;
  }

  return format;
}

export { display_time_format };
