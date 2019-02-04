// const modal = document.querySelector(".modal");
document.getElementById('signup').addEventListener('submit',signUp)
// const signup = document.querySelector(".signup");
const url = 'http://127.0.0.1:5000/api/v2/auth/signup/';
let firstname = document.getElementById('firstname');
let lastname = document.getElementById('lastname');
let username = document.getElementById('username');
let email = document.getElementById('email');
let password = document.getElementById('password');
let phone = document.getElementById('phone');
let invalid = document.getElementById('invalid')


// modal.addEventListener("submit");
function signUp(event){
    event.preventDefault()
    let freshaccount={
        firstname:firstname.value,
        lastname:lastname.value,
        username:username.value,
        password: password.value,
        email : email.value,
        phone : phone.value
        }
    const options={
        method: 'POST',
        mode: 'cors',
        headers: {
            "content-type": "application/json",
        },
        body: JSON.stringify(freshaccount)
        }
    fetch(url,options)
    .then((response) => response.json())
        .then((data) => {
            if (data.status == "OK"){
                invalid.textContent = '' + data.message
                window.location.replace('./index.htm')
            }else{
                invalid.textContent = ''+data.message
            }
            
            console.log(data)
        })
        .catch((error) => console.log(error), invalid.textContent = "Ooops. Something went wrong");
    }