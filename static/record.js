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
    display_todays_record(records["todays_record"]);
    display_last_weeks_record(records["last_weeks_record"]);
    display_overall_record(records["overall_record"]);
}

function display_todays_record(todays_record)
{
    let today_area = document.querySelector(".today");

    for (var label of Object.keys(todays_record))
    {
	today_area.innerHTML += '<p>' + label + ': ' + todays_record[label] + ' s</p>';
    }
}

function display_last_weeks_record(last_weeks_record)
{
    let week_area = document.querySelector(".week");

    for (var label of Object.keys(last_weeks_record))
    {
	week_area.innerHTML += '<p>' + label + ': ' + last_weeks_record[label] + ' s</p>';
    }

}

function display_overall_record(overall_record)
{
    let overall_area = document.querySelector(".all");

    for (var label of Object.keys(overall_record))
    {
	overall_area.innerHTML += '<p>' + label + ': ' + overall_record[label] + ' s</p>';
    }


}

async function main()
{
    records = await get_records();
    display_records(records);
}

main()
