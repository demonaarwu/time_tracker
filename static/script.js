import { display_labels, init } from "./label.js";

import {
  check_tracker_exist,
  create_time_tracker,
  get_tracker,
} from "./time_tracker.js";

async function main() {
  const tracker_exist = await check_tracker_exist();
    console.log(tracker_exist);

  if (!tracker_exist) {
    display_labels().then(init);
  } else {
    const tracker = await get_tracker();
    create_time_tracker(tracker.name);
  }
}

main();
