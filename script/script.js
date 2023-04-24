//Fomulario Olvide Contraseña JavaScript

const resetOption = document.getElementById('resetOption');
const emailContainer = document.getElementById('emailContainer');
const phoneContainer = document.getElementById('phoneContainer');

resetOption.addEventListener('change', function () {
    if (resetOption.value === 'email') {
        emailContainer.classList.remove('d-none');
        phoneContainer.classList.add('d-none');
    } else {
        emailContainer.classList.add('d-none');
        phoneContainer.classList.remove('d-none');
    }
});

//Formulario Contacto JavaScript
function validar() {
    event.preventDefault();

    let nombre = document.getElementById("nombre");
    let email = document.getElementById("email");
    let asunto = document.getElementById("asunto");
    let mensaje = document.getElementById("mensaje");

    let alertaNombre = document.getElementById("alerta-nombre");
    let alertaCorreo = document.getElementById("alerta-correo");
    let alertaAsunto = document.getElementById("alerta-asunto");
    let alertaMensaje = document.getElementById("alerta-mensaje");

    let valido = true;

    // Validar nombre
    if (nombre.value.trim() === "") {
      alertaNombre.innerText = "Por favor, ingrese su nombre.";
      valido = false;
    } else {
      alertaNombre.innerText = "";
    }

    // Validar correo electrónico
    let regexEmail = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!regexEmail.test(email.value.trim())) {
      alertaCorreo.innerText = "Por favor, ingrese un correo electrónico válido.";
      valido = false;
    } else {
      alertaCorreo.innerText = "";
    }

    // Validar asunto
    if (asunto.value.trim() === "") {
      alertaAsunto.innerText = "Por favor, ingrese un asunto.";
      valido = false;
    } else {
      alertaAsunto.innerText = "";
    }

    // Validar mensaje
    if (mensaje.value.trim() === "") {
      alertaMensaje.innerText = "Por favor, ingrese un mensaje.";
      valido = false;
    } else {
      alertaMensaje.innerText = "";
    }

}

