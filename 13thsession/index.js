const timeContainer = document.querySelector('.time'),
  nowAmpm = timeContainer.querySelector('#period'); // time container의 자손들을 담음

function getTime() {
  const now = new Date();
  const minutes = now.getMinutes();
  let hours = now.getHours();
  const seconds = now.getSeconds();

  if (hours >= 12) {
    nowAmpm.innerText = 'PM';
  }
  if (hours == 0) {
    hours = 12;
  }
  if (hours > 12) {
    hours = hours - 12;
  }

  let ids = ['#hour','#minutes', '#seconds'];
  let values = [
    hours < 10 ? `0${hours}` : hours,
    minutes < 10 ? `0${minutes}` : minutes,
    seconds < 10 ? `0${seconds}` : seconds];
  for (let i=0; i < ids.length; i++) {
    timeContainer.querySelector(ids[i]).textContent = values[i];
  }
}

function getCalender() {
  const now = new Date();
  const day = now.getDay(); // 요일
  const month = now.getMonth(); // 월
  const date = now.getDate(); // 일
  const year = now.getFullYear(); // 년

  // 배열값들을 넣어준다. //
  let week = [
    'Sunday', // index 0
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
  ];

  let mon = [
    'Janurary',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
  ];

  let ids = ['dayname', 'month', 'daynum', 'year'];
  let values = [
    week[day], mon[month],
    date < 10 ? `0${date}` : date,
    year];
  for (let i = 0; i < ids.length; i++) {
    document.getElementById(ids[i]).firstChild.nodeValue = values[i];
  };
}

function init() {
  getTime();
  setInterval(getTime, 1000);
  getCalender();
}

init();
