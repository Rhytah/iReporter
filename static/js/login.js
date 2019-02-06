document.getElementById('login').addEventListener('submit',signinUser)

const login_url = 'https://rhytah-ireporterv2.herokuapp.com/api/v2/auth/login/';

function signinUser(event) {
    event.preventDefault()
    let username = document.getElementById('login_username')
    let password = document.getElementById('psw')
    let invalid = document.getElementById('invalid_login')

    fetch(login_url, {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username: username.value, password: password.value})
    })
    .then((response) => response.json())
        .then((data) => {
            if (data.message == "You have successfully logged in"){
                window.location.replace('./forum.htm')
                localStorage.setItem('token', data.token)
            }else{
                invalid.textContent = '' + data.message
            }
            console.log(data)
        })
        .catch((err) => console.log(err), invalid.textContent = "Invalid username or password")
}
