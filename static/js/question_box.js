console.log('hi')

function askQuestion () {
  const question = document.querySelector('#question-button')
  question.addEventListener('click', function (event) {
    event.preventDefault()
    fetch('question/add/')
    // method: "POST",
    // body: JSON.stringify({      })
      .then(res => res.json())
      .then(json => {
        if (json.status === 'ok') {
          console.log('WORKING')
        }
      })
  })
}

document.addEventListener('DOMContentLoaded', function () {
  askQuestion()
}
)
