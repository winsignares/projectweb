function saveuser() {
    let endpoint = '/pruebaaxios'
    const textUser = document.getElementById('nombre');
    const textemail = document.getElementById('email');
    
    axios.post(endpoint, {
        'fullname' : textUser.value,
        'email' : textemail.value
      })
      .then(function (response) {
        alert(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}