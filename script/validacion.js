//Formulario Registro JQuery
$(document).ready(function() {
    function validarCorreo(correo) {
      const re = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
      return re.test(correo);
    }

    function tieneDigito(password) {
      return /\d/.test(password);
    }

    $('#formulario-registrarse').on('submit', function(e) {
      e.preventDefault();

      let errores = false;

      const nombres = $('#nombres').val().trim();
      if (nombres === '') {
        $('#alerta-nombre-r').text('Debes llenar el campo con tu nombre.').css('color', 'red');
        $('#nombres').css('border-color','red');
        errores = true;
      } else {
        $('#alerta-nombre-r').text('');
        $('#nombres').css('border-color','green');
      }

      const apellidos = $('#apellidos').val().trim();
      if (apellidos === '') {
        $('#alerta-apellido-r').text('Debes llenar el campo con tus apellidos.').css('color', 'red');
        $('#apellidos').css('border-color','red');
        errores = true;
      } else {
        $('#alerta-apellido-r').text('');
        $('#apellidos').css('border-color','green');
      }

      const username = $('#username').val().trim();
      if (username === '' || username.length < 4 || username.length > 20) {
        $('#alerta-nombre-user-r').text('Debes llenar el campo con un nombre de usuario que contenga entre 4 y 20 caracteres.').css('color', 'red');
        $('#username').css('border-color','red');
        errores = true;
      } else {
        $('#alerta-nombre-user-r').text('');
        $('#username').css('border-color','green');
      }

      const email = $('#email').val().trim();
      if (email === '' || !validarCorreo(email)) {
        $('#alerta-email-r').text('Debes llenar el campo con un correo válido.').css('color', 'red');
        $('#email').css('border-color','red');
        errores = true;
      } else {
        $('#alerta-email-r').text('');
        $('#email').css('border-color','green');
      }

      const telefono = $('#telefono').val().trim();
      if (telefono === '' || telefono.length !== 9) {
        $('#alerta-telefono-r').text('Debes llenar el campo con un número de teléfono de 9 dígitos.').css('color', 'red');
        $('#telefono').css('border-color','red');
        errores = true;
      } else {
        $('#alerta-telefono-r').text('');
        $('#telefono').css('border-color','green');
      }

      const password = $('#password').val();
      if (password === '' || password.length < 4 || !tieneDigito(password)) {
        $('#alerta-contraseña-r').text('Debes llenar el campo con una contraseña de al menos 4 caracteres y que contenga al menos 1 dígito.').css('color', 'red');
        $('#nombres').background;
        $('#password').css('border-color','red');
        errores = true;
      } else {
        $('#alerta-contraseña-r').text('');
        $('#password').css('border-color','green');
      }

      const passwordConfirm = $('#passwordConfirm').val();
      if (password !== passwordConfirm) {
        $('#alerta-contraseña-c-r').text('Las contraseñas no coinciden.').css('color', 'red');
        $('#passwordConfirm').css('border-color','red');
        errores = true;
      } else {
        $('#alerta-contraseña-c-r').text('');
        $('#passwordConfirm').css('border-color','green');
      }

      const terminos = $('#terminos').is(':checked');
      if (!terminos) {
        $('#alerta-terminos-r').text('Debes aceptar los términos y condiciones.').css('color', 'red');
        $('#terminos').css('border-color','red');
        errores = true;
      } else {
        $('#alerta-terminos-r').text('');
        $('#terminos').css('border-color','green');
    }

    if (!errores) {
      console.log('Formulario enviado correctamente');
    }
  });
});