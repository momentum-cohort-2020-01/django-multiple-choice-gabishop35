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
        console.log(json.data)

        if (json.status === 'ok') {
          showQuestion(json.data)
          // return '<p class='p-tag' data-question-id='${data.pk}'>${data.title}, ${data.body} </p>'
        }
      })
  })
}

function createQuestionHTML (data) {
  return `<a href="'question/<int:pk>/'" class='p-tag' > ${data.title} ${data.body} </a>`
}

function showQuestion (data) {
  // console.log(data)
  const questionHTML = createQuestionHTML(data)
  const questionContainer = document.querySelector('#question-container')
  questionContainer.insertAdjacentHTML('beforeend', questionHTML)
}

function getAllQuestions () {
  return fetch('http://127.0.0.1:8000/', {
    method: 'GET'
  })
    .then(response => response.json())
}

getAllQuestions().then(showQuestion)

document.addEventListener('DOMContentLoaded', function () {
  askQuestion()
})
