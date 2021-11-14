const signupForm = document.getElementById('signup-form');

signupForm.onsubmit = (e) => handleSignup(e);

const handleSignup = (e) => {
  e.preventDefault();

  username = getUsername();

  passwords = getPasswords();

  console.log(`사용자 이름 : ${username}`);
  // python: f"사용자 이름 : {username}"

  if (validataUsername(username) && validatePassword(passwords)) {
    console.log('Valid signup form!')
  } else {
    console.log('Invalid!')
  }
}

const getUsername = () => {
  return document.querySelector('input[name=username]').value;
  // return document.getElementById('username').value;
}

const validataUsername = (username) => {
  return username !== '';
}


const getPasswords = () => {
  return [...document.querySelectorAll('input[type=password]')].map(
    (input) => input.value
  )
}

const validatePassword = (passwords) => {
  return isSamePassword(passwords);
}

const isSamePassword = ([pw1, pw2]) => {
  return pw1 === pw2;
}

// [password1.value, password2.value]
// const isSamePassword = (passwords) => {
//   return passwords[0] === passwords[1];
// }

// ==
