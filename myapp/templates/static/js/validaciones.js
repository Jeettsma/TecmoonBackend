// Obtener el formulario y los campos de entrada
const formulario = document.getElementById('mi-formulario');
const usuario = document.getElementById('usuario');
const nombreCompleto = document.getElementById('nombre-completo');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');
const regiones = document.getElementById('regiones');
const comunas = document.getElementById('comunas');
const casilla = document.getElementById('casilla');

// Agregar un evento de escucha al enviar el formulario
formulario.addEventListener('submit', function(event) {
  // Detener el envío del formulario
  event.preventDefault();

  // Validar los campos
  if (validarUsuario() && validarNombreCompleto() && validarEmail() && validarContraseña() && validarConfirmacionContraseña() && validarRegiones() && validarComunas()) {
    // Enviar el formulario si todos los campos son válidos
    formulario.submit();
  }
});

// Funciones de validación para cada campo

function validarUsuario() {
  const valor = usuario.value.trim();

  if (valor === '') {
    mostrarError(usuario, 'Por favor, ingrese un nombre de usuario');
    return false;
  } else if (valor.length < 4) {
    mostrarError(usuario, 'El nombre de usuario debe tener al menos 4 caracteres');
    return false;
  } else {
    mostrarExito(usuario);
    return true;
  }
}

function validarNombreCompleto() {
  const valor = nombreCompleto.value.trim();

  if (valor === '') {
    mostrarError(nombreCompleto, 'Por favor, ingrese su nombre completo');
    return false;
  } else if (valor.length < 4) {
    mostrarError(nombreCompleto, 'El nombre completo debe tener al menos 4 caracteres');
    return false;
  } else {
    mostrarExito(nombreCompleto);
    return true;
  }
}

function validarEmail() {
  const valor = email.value.trim();
  const regex = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/i;

  if (valor === '') {
    mostrarError(email, 'Por favor, ingrese un correo electrónico');
    return false;
  } else if (!regex.test(valor)) {
    mostrarError(email, 'Por favor, ingrese un correo electrónico válido');
    return false;
  } else {
    mostrarExito(email);
    return true;
  }
}

function validarContraseña() {
  const valor = password.value.trim();
  const regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$/;

  if (valor === '') {
    mostrarError(password, 'Por favor, ingrese una contraseña');
    return false;
  } else if (!regex.test(valor)) {
    mostrarError(password, 'La contraseña debe tener al menos 6 caracteres, incluyendo al menos un número, una letra mayúscula y una letra minúscula');
    return false;
  } else {
    mostrarExito(password);
    return true;
  }
}

function validarConfirmacionContraseña() {
  const valor = password2.value.trim();

  if (valor === '') {
    mostrarError(password2, 'Por favor, confirme su contraseña');
    return false;
  } else if (valor !== password.value.trim()) {
    mostrarError(password2, 'Las contraseñas no coinciden');
    return false;
  } else {
    mostrarExito(password2);
    return true;
  }
}

function validarRegiones() {
  const valor = regiones.value;

  if (valor === '') {
    mostrarError(regiones, 'Por favor, seleccione una región');
    return false;
  } else {
    mostrarExito(regiones);
    return true;
  }
}

function validarComunas() {
  const valor = comunas.value;

  if (valor === '') {
    mostrarError(comunas, 'Por favor, seleccione una ciudad');
    return false;
  } else {
    mostrarExito(comunas);
    return true;
  }
}

// Funciones de ayuda para mostrar y ocultar mensajes de error/exito

function mostrarError(elemento, mensaje) {
  const formControl = elemento.parentElement;
  const mensajeError = formControl.querySelector('.mensaje-error');
  formControl.className = 'form-control error';
  mensajeError.innerText = mensaje;
}

function mostrarExito(elemento) {
  const formControl = elemento.parentElement;
  formControl.className = 'form-control exito';
}