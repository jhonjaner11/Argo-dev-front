

   /* var columna=new Array(5);
    /*columna[0]='columnaasd';
    columna[1]=2;
    columna[2]=3;
    columna[3]=4;
    columna[4]=5;
    columna[5]=3;*/
 	var n=9
 	var x=2
    var filas=new Array(x);
   /* filas[0]='a';
    filas[1]=2;
    filas[2]=3;
    filas[3]=4;
    filas[4]=5;*/
    for (var i = 0; i < filas.length; i++) {
        
        filas[i]=new Array(n); 

        
    }

    var tabla=new Array();
    tabla[0]=columna;
    tabla[1]=filas;
    function crearTabla(){
        var tbl = document.getElementById("tabla");
        var tblBody = document.createElement("tbody");
        for (var i = 0; i < filas.length; i++) {
            var fila = document.createElement("tr");
            for (var j = 0; j < n; j++) {
                var celda = document.createElement("td");
                var textoCelda = document.createTextNode(i+'-'+j);
                celda.appendChild(textoCelda);
                fila.appendChild(celda);
            }
            tblBody.appendChild(fila);
        }
        tbl.appendChild(tblBody);
        tbl.setAttribute("border", "2");
    }

 