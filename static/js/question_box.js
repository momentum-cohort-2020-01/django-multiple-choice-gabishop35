/* globals fetch */

const questionForm = document.querySelector('#question-form')

function askQuestion () {
  // const question = document.querySelector('#question-button')
  questionForm.addEventListener('submit', function (event) {
    event.preventDefault()
    fetch('question/add/', {
      method: 'POST',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ questionBody: document.querySelector('#body').value, questionTitle: document.querySelector('#title').value })
    })
      .then(res => res.json())
      .then(json => {
        if (json.status === 'ok') {
          console.log(json.data)
          // document.createElement
          // let
        }
      })
  })
}

function createQuestionHTML (data) {
  return '<p class='p-tag' data-question-id='${data.pk}'>${data.title}, ${data.body} </p>'
}

function showQuestion (data) {
  const questionHTML = createQuestionHTML(data)
  const questionContainer = document.querySelector('#question-container')
  questionContainer.insertAdjacentHTML('beforeend', questionHTML)
}

document.addEventListener('DOMContentLoaded', function () {
  askQuestion()
}
)
