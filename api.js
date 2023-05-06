
$(document).ready(function(){
    $("#enviar").click(function(){
      $.getJSON("productos.json", function(data){
        $.each(data, function(i, item){
          $("#categorias tbody").append(
            "<tr><td>" + (i+1) + "</td><td>" +
            item.nombre + "</td><td><img src='" + 
            item.imagen +"'></td><td>"+
            item.descripcion + "</td></tr>"
          );
        });
      });
    });
  });
  