
function saveuser() {
    let endpoint = '/saveuser'
    const textUser = document.getElementById('nombre');  
    const textemail = document.getElementById('useremail');  
   
    axios.post(endpoint, {
        'fullname': textUser.value,
        'email': textemail.value
    })
      .then(function (response) {
        console.log(response)
    })
      .catch(function (error) {
        console.log(error);
    });
}

