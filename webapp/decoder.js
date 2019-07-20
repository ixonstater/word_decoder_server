
function clearTextField(e){
    e.target.placeholder = ''
}

function restoreTextFieldValue(e){
    e.target.placeholder = 'Please enter six letters.'
}

function validateData(letters){
    let alpha = /^[A-Za-z]+$/
    if (!letters.match(alpha)){
        throw 'Submitted characters are not all alphabetic'
    } else if (letters.length != 6){
        throw 'Wrong number of letters submitted.'
    }
}

async function postWords(words){
    words = await words
    words = Object.values(words)
    let wordList = document.getElementById('word-list-start')
    while(wordList.firstChild){
        wordList.removeChild(wordList.firstChild)
    }
    for(word of words){
        let newWord = document.createElement('p')
        newWord.innerHTML = word
        wordList.appendChild(newWord)
    }
}

function submitLetters(){
    let letters = document.getElementById('word-input').value
    let words = null
    try{
        validateData(letters)
    }catch (e){
        alert(e)
        return
    }
    // words = fetch('http://localhost:8081', {method: 'POST', body: letters}).then(
    words = fetch('http://codefordays.io:8081', {method: 'POST', body: letters}).then(
        function(response){
            return response.json()
        }
    )
    postWords(words)
}

function init(){
    document.getElementById('word-input').addEventListener('focus', clearTextField)
    document.getElementById('word-input').addEventListener('blur', restoreTextFieldValue)
    document.getElementById('submit').addEventListener('click', submitLetters)
}

document.addEventListener('DOMContentLoaded', init)