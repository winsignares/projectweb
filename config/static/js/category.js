function savecategoria() {
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