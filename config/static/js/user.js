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

function MostrarUsuario() {
  //alertify.success('Hola Mundo');
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
