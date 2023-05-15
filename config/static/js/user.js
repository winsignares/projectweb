function saveuser() {
    let endpoint = '/saveuser'
    const textUser = document.getElementById('nombre');
    const textemail = document.getElementById('useremail');
    
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

function MostrarUsuario() {
  //alertify.success('Hola Mundo');
  Swal.fire({
    title: 'Custom animation with Animate.css',
    showClass: {
      popup: 'animate__animated animate__fadeInDown'
    },
    hideClass: {
      popup: 'animate__animated animate__fadeOutUp'
    }
  })


  const listausuario = document.getElementById('listausuario');
  let endpoint = "/dostablas";

      axios.get(endpoint)
      .then(function (response) {
        let data = response.data;
        let Lusuario ="";
        let longitud = (Object.keys(data).length) +1 ;
        
        for (let index = 1; index < longitud; index++) {          
          
          Lusuario += `<tr>
                        <th scope="row">${index}</th>
                        <td>${data[index].Nombre}</td>
                        <td>${data[index].email}</td>
                        <td>${data[index].NombreTarea}</td>
                      </tr>`;

        }       
        
        listausuario.innerHTML = Lusuario;

      })
      .catch(function (error) {
        console.log(error);
      })
      .finally(function () {
        // always executed
      });  
}

function MostrarUser() {
  //alertify.success('Agregado correctamente');
  const listausuario2 = document.getElementById('listausuario2');
  let endpoint = "/unatabla";

      axios.get(endpoint)
      .then(function (response) {
        let data = response.data;
        let Lusuario2 ="";
        let longitud = (Object.keys(data).length) +1 ;
        
        for (let index = 1; index < longitud; index++) {          
          
          Lusuario2 += `<tr>
                        <th scope="row">${index}</th>
                        <td>${data[index].Nombre}</td>
                        <td>${data[index].email}</td>
                      </tr>`;

        }       
        
        listausuario2.innerHTML = Lusuario2;

      })
      .catch(function (error) {
        console.log(error);
      })
      .finally(function () {
        // always executed
      });  
}
