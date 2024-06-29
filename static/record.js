import { display_time_format } from './time_format.js';

async function get_records()
{
  const response = await fetch("http://127.0.0.1:5000/records");

  if (!response.ok) {
    throw new Error("Not ok");
  } else {
    const records = await response.json();
    return records;
  }
}

function display_records(records)
{
    display_record(records["todays_record"], "today");
    display_record(records["last_weeks_record"], "week");
    display_record(records["overall_record"], "all");
}

function display_record(record, record_type)
{
    let display_area;

    switch (record_type)
    {
	case "today":
	    display_area = document.querySelector(".today");
	    break;
	case "week":
	    display_area = document.querySelector(".week");
	    break;
	default:
	    display_area = document.querySelector(".all");
    }

    for (var label of Object.keys(record))
    {
	display_area.innerHTML += '<p>' + label + ': ' + display_time_format(record[label]) + '</p>';
    }
}

async function main()
{
    let records = await get_records();
    display_records(records);
}

main()
