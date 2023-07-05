function validar() {
    var nombre = document.getElementById("nombre").value;
    var email = document.getElementById("email").value;
    var asunto = document.getElementById("asunto").value;
    var mensaje = document.getElementById("mensaje").value;
  
    var regexNombre = /^[a-zA-Z\s]+$/;
    var regexEmail = /^\S+@\S+\.\S+$/;
  
    var mensajeError = "";
  
    if (!regexNombre.test(nombre)) {
      mensajeError +=