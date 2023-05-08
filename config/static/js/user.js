<<<<<<< HEAD
//var es para trabajar variables de tipo global
//let  se declara dentro de los metodos osea es de manera local
//const se utiliza en cuestion de objetos


function saveUser(){

}

//cuando se cree siempre un js el sccrip siempre se tiene que colocar en el html
=======

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

>>>>>>> 9ede7cddd4d94bc9e70eb6cedf88a2296f5b32c3
