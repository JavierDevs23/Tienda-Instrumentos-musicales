const resetOption = document.getElementById('resetOption');
const emailContainer = document.getElementById('emailContainer');
const phoneContainer = document.getElementById('phoneContainer');

//Fomulario olvide contraseña
resetOption.addEventListener('change', function () {
    if (resetOption.value === 'email') {
        emailContainer.classList.remove('d-none');
        phoneContainer.classList.add('d-none');
    } else {
        emailContainer.classList.add('d-none');
        phoneContainer.classList.remove('d-none');
    }
});

//valida el formulario de contacto
function validarFormulario() {
    var nombre = document.getElementById("nombre").value;
    var email = document.getElementById("email").value;
    var asunto = document.getElementById("asunto").value;
    var mensaje = document.getElementById("mensaje").value;
    
//Validar que se ingrese nombre y tenga entre 3 y 20 caracteres
    if (nombre == "") {
      alert("Ingrese su nombre");
      return false;
    } else if (nombre.length < 3 || nombre.length > 20) {
      alert("El nombre debe tener entre 3 y 20 caracteres");
      return false;
    }
    
    // Validar que se ingrese el correo electrónico
    if (email == "") {
      alert("Ingrese su correo electrónico");
      return false;
    }
    
    //  Validar que se ingrese el asunto de mensaje
    if (asunto == "") {
      alert("Ingrese asunto de mensaje");
      return false;
    }
    
    //  Validar que se ingrese el mensaje a enviar
    if (mensaje == "") {
      alert("Ingrese su mensaje");
      return false;
    }
    
    //  Validar que el correo sea válido
    var email_regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email_regex.test(email)) {
      alert("La dirección de correo ingresada no es válida");
      return false;
    }
    
    return true;
  }
  
  //Esto queda comentado por cualquier cosa 

/*   //formulario contacto
function validar(){
    let nombre, 
        email, 
        asunto, 
        mensaje

    nombre = document.getElementById("nombre").value;
    email = document.getElementById("email").value;
    asunto = document.getElementById("asunto").value;
    mensaje = document.getElementById("mensaje").value;

    //Nombre validacion
    if (nombre.length == 0){
        document.getElementById("alerta-nombre").innerHTML = "Ingrese nombre";
    }else{
        document.getElementById("alerta-nombre").innerHTML = "";    
    }

    //Asunto validacion
    if (asunto.length == 0) {
        document.getElementById("alerta-asunto").innerHTML = "Ingrese asunto";
    } else {
        document.getElementById("alerta-asunto").innerHTML = "";
    }

    //Mensaje validacion
    if (mensaje.length == 0) {
        document.getElementById("alerta-mensaje").innerHTML = "Ingrese mensaje";
    } else {
        document.getElementById("alerta-mensaje").innerHTML = "";
    }

    //Correo validacion
    if(email === "" || email === null || email.lenght === 0) {
        document.getElementById("alerta-correo").innerHTML =  "debe llenar este campo";
        email.focus();
        return false;
    }

    else if( !(/\S+@\S+\.\S+/.test(email)) ) {
        document.getElementById("alerta-correo").innerHTML = "debe ingresar un correo valido";
        email.focus();
        return false;
    }

}
 */