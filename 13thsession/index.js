const timeContainer = document.querySelector('.time'),
  nowHour = timeContainer.querySelector('#hour'),
  nowMin = timeContainer.querySelector('#minutes'),
  nowSec = timeContainer.querySelector('#seconds'),
  nowAmpm = timeContainer.querySelector('#period') // time container의 자손들을 담음

function getTime() {
  const now = new Date()
  const minutes = now.getMinutes()
  let hours = now.getHours()
  const seconds = now.getSeconds()

  if (hours >= 12) {
    nowAmpm.innerText = 'PM'
  }
  if (hours == 0) {
    hours = 12
  }
  if (hours > 12) {
    hours = hours - 12
  }

  nowHour.innerText = hours < 10 ? `0${hours}` : hours
  nowMin.innerText = minutes < 10 ? `0${minutes}` : minutes
  nowSec.innerText = seconds < 10 ? `0${seconds}` : seconds
  // nowHour.innerText = hours
  // nowMin.innerText = minutes
  // nowSec.innterText = seconds
}

function getCalender() {
  const now = new Date()
  const day = now.getDay() // 요일
  const month = now.getMonth() // 월
  const date = now.getDate() // 일
  const year = now.getFullYear() // 년

  // 배열값들을 넣어준다. //
  let week = [
    'Sunday', // index 0
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
  ]

  let ids = ['dayname', 'month', 'daynum', 'year']
  let values = [week[day], month, date, year]
  for (let i = 0; i < ids.length; i++) {
    document.getElementById(ids[i]).firstChild.nodeValue = values[i]
  }
}

function init() {
  getTime()
  setInterval(getTime, 1000)
  getCalender()
}

init()
