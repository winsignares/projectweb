function savecategory() {
    let endpoint = '/savecategory'
    const textname = document.getElementById('imput category');

    axios.post(endpoint, {
        'namecategory' : textname.value
      })
      .then(function (response) {
        alert(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}

function MostrarCategoria() {
  //alertify.success('Hola Mundo');
  const listacategoria = document.getElementById('listacategoria');
  let endpoint = "/todascategorias";

      axios.get(endpoint)
      .then(function (response) {
        let data = response.data;
        console.log(data)
        let Lusuario ="";
        let longitud = (Object.keys(data).length) +1 ;
        
        for (let index = 1; index < longitud; index++) {          
          
          Lusuario += `<tr>
                        <th scope="row">${index}</th>
                        <td>${data[index].ID}</td>
                        <td>${data[index].Nombre}</td>
                      </tr>`;

        }       
        
        listacategoria.innerHTML = Lusuario;

      })
      .catch(function (error) {
        console.log(error);
      })
      .finally(function () {
        // always executed
      });  
}