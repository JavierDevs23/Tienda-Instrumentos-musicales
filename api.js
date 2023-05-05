/*fetch("productos.json")
.then(function(response){
   return response.json();
})
.then(function(productos){
   let placeholder = document.querySelector("#data-output");
   let out = "";
   for(let producto of productos){
      out += `
         <tr>
            <td> <img src='${producto.imagen}'> </td>
            <td>${producto.precio}</td>
            <td>${producto.imagen}</td>
            <td>${producto.descripcion}</td>
         </tr>
      `;
   }
 
   placeholder.innerHTML = out;
});*/
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
  