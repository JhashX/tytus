class RTablaDeSimbolos: 
    def __init__(self):
        ''' Reporte Tabla de Simbolos'''

    def crearReporte(self,ts_global,ts_globalIndex):
        f = open("reportes/ts.html", "w")
        f.write("<!DOCTYPE html>")
        f.write("<html lang=\"en\" class=\"no-js\">")
        f.write("")
        f.write("<head>")
        f.write("    <meta charset=\"UTF-8\" />")
        f.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">")
        f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("    <title>Tabla de Simbolos</title>")
        f.write("    <meta name=\"description\"")
        f.write("        content=\"Sticky Table Headers Revisited: Creating functional and flexible sticky table headers\" />")
        f.write("    <meta name=\"keywords\" content=\"Sticky Table Headers Revisited\" />")
        f.write("    <meta name=\"author\" content=\"Codrops\" />")
        f.write("    <link rel=\"shortcut icon\" href=\"../favicon.ico\">")
        f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/normalize.css\" />")
        f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/demo.css\" />")
        f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/component.css\" />")
        f.write("</head>")

        f.write("<body>")
        f.write("    <div class=\"container\">")
        f.write("        <!-- Top Navigation -->")
        f.write("        <header>")
        f.write("            <h1>Tabla de Simbolos</h1>")
        f.write("        </header>")
        f.write("        <div class=\"component\">")
        f.write("            <table>")
        f.write("                <thead>")
        f.write("                    <tr>")
        f.write("                        <th>No.</th>")
        f.write("                        <th>ID</th>")
        f.write("                        <th>TIPO</th>")
        f.write("                        <th>VALOR</th>")
        f.write("                        <th>AMBITO</th>")
        f.write("                    </tr>")
        f.write("                </thead>")
        f.write("                <tbody>")
        if len(ts_global.simbolos) > 0:
            i = 0
            while i < len(ts_global.simbolos):
                f.write("                    <tr>")
                f.write("                        <td class=\"text-left\">"+ str(i+1) +"</td>")
                f.write("                        <td class=\"text-left\">"+ str(ts_global.simbolos[i].val) +"</td>")
                f.write("                        <td class=\"text-left\">"+ str(ts_global.simbolos[i].tipo) +"</td>")
                f.write("                        <td class=\"text-left\">"+ str(ts_global.simbolos[i].valor) +"</td>")
                f.write("                        <td class=\"text-left\">"+ str(ts_global.simbolos[i].ambito) +"</td>")
                f.write("                    </tr>")
                i += 1
        f.write("                </tbody>")
        f.write("            </table>")
        f.write("        </div>")
        f.write("    </div><!-- /container -->")
        if len(ts_globalIndex.simbolos) > 0:
            f.write("    <div class=\"container\">")
            f.write("        <!-- Top Navigation -->")
            f.write("        <header>")
            f.write("            <h1>Tabla de Simbolos INDEX</h1>")
            f.write("        </header>")
            f.write("        <div class=\"component\">")
            f.write("            <table>")
            f.write("                <thead>")
            f.write("                    <tr>")
            f.write("                        <th>No.</th>")
            f.write("                        <th>ID</th>")
            f.write("                        <th>TIPO</th>")
            f.write("                        <th>COLUMNAS</th>")
            f.write("                        <th>RESTRICCION</th>")
            f.write("                        <th>AMBITO</th>")
            f.write("                    </tr>")
            f.write("                </thead>")
            f.write("                <tbody>")
            if len(ts_globalIndex.simbolos) > 0:
                i = 0
                while i < len(ts_globalIndex.simbolos):
                    f.write("                    <tr>")
                    f.write("                        <td class=\"text-left\">"+ str(i+1) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_globalIndex.simbolos[i].id) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_globalIndex.simbolos[i].tipo) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_globalIndex.simbolos[i].columnas) +"</td>")
                    cadena = ""
                    for sim in ts_globalIndex.simbolos[i].restriccion:
                        cadena += str(sim)+"<br>"
                    f.write("                        <td class=\"text-left\">"+ str(cadena) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_globalIndex.simbolos[i].tabla) +"</td>")
                    f.write("                    </tr>")
                    i += 1
            f.write("                </tbody>")
            f.write("            </table>")
            f.write("        </div>")
            f.write("    </div><!-- /container -->")

        f.write("    <script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js\"></script>")
        f.write("    <script src=\"http://cdnjs.cloudflare.com/ajax/libs/jquery-throttle-debounce/1.1/jquery.ba-throttle-debounce.min.js\"></script>")
        f.write("    <script src=\"js/jquery.stickyheader.js\"></script>")
        f.write("</body>")
        f.write("")
        f.write("</html>")
        f.close()

    def crearReporte1(self,ts_global,ts_globalIndex):
        f = open("reportes/dot.dot", "w")
        
        if len(ts_global.simbolos) > 0:
            f.write("<body>")
            f.write("    <div class=\"container\">")
            f.write("        <!-- Top Navigation -->")
            f.write("        <header>")
            f.write("            <h1>Tabla de Simbolos</h1>")
            f.write("        </header>")
            f.write("        <div class=\"component\">")
            f.write("            <table>")
            f.write("                <thead>")
            f.write("                    <tr>")
            f.write("                        <th>No.</th>")
            f.write("                        <th>ID</th>")
            f.write("                        <th>TIPO</th>")
            f.write("                        <th>VALOR</th>")
            f.write("                        <th>AMBITO</th>")
            f.write("                    </tr>")
            f.write("                </thead>")
            f.write("                <tbody>")
            if len(ts_global.simbolos) > 0:
                i = 0
                while i < len(ts_global.simbolos):
                    f.write("                    <tr>")
                    f.write("                        <td class=\"text-left\">"+ str(i+1) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_global.simbolos[i].val) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_global.simbolos[i].tipo) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_global.simbolos[i].valor) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_global.simbolos[i].ambito) +"</td>")
                    f.write("                    </tr>")
                    i += 1
            f.write("                </tbody>")
            f.write("            </table>")
            f.write("        </div>")
            f.write("    </div><!-- /container -->")
        if len(ts_globalIndex.simbolos) > 0:
            f.write("    <div class=\"container\">")
            f.write("        <!-- Top Navigation -->")
            f.write("        <header>")
            f.write("            <h1>Tabla de Simbolos INDEX</h1>")
            f.write("        </header>")
            f.write("        <div class=\"component\">")
            f.write("            <table>")
            f.write("                <thead>")
            f.write("                    <tr>")
            f.write("                        <th>No.</th>")
            f.write("                        <th>ID</th>")
            f.write("                        <th>TIPO</th>")
            f.write("                        <th>COLUMNAS</th>")
            f.write("                        <th>RESTRICCION</th>")
            f.write("                        <th>AMBITO</th>")
            f.write("                    </tr>")
            f.write("                </thead>")
            f.write("                <tbody>")
            if len(ts_globalIndex.simbolos) > 0:
                i = 0
                while i < len(ts_globalIndex.simbolos):
                    f.write("                    <tr>")
                    f.write("                        <td class=\"text-left\">"+ str(i+1) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_globalIndex.simbolos[i].id) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_globalIndex.simbolos[i].tipo) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_globalIndex.simbolos[i].columnas) +"</td>")
                    cadena = ""
                    for sim in ts_globalIndex.simbolos[i].restriccion:
                        cadena += str(sim)+"<br>"
                    f.write("                        <td class=\"text-left\">"+ str(cadena) +"</td>")
                    f.write("                        <td class=\"text-left\">"+ str(ts_globalIndex.simbolos[i].tabla) +"</td>")
                    f.write("                    </tr>")
                    i += 1
            f.write("                </tbody>")
            f.write("            </table>")
            f.write("        </div>")
            f.write("    </div><!-- /container -->")
        f.close()