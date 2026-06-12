const form = document.querySelector('.login');
const description = document.querySelector('.login-description')
const switchbtn = document.querySelector('#switchbtn');
const header = document.querySelector('#header')
const submitbtn = document.querySelector('#submitbtn');

// for the form
const username = document.querySelector('#username');
const password = document.querySelector('#password')



switchbtn.addEventListener('click', () => {
    description.classList.toggle('right');
    form.classList.toggle('register');

    username.value = '';
    password.value = '';

    if (form.classList.contains('register')) {
        switchbtn.textContent = "< Login";
        header.textContent = "Register";
        username.name = 'register-username';
        password.name = 'register-password';
        submitbtn.textContent = "Register";
    } else {
        switchbtn.textContent = "Register >";
        header.textContent = "Login";
        username.name = 'username';
        password.name = 'password';
        submitbtn.textContent = "Login";
    }
});