<!DOCTYPE html>
<html>
<body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    <script>
       /**
         * Replace "http://ib.esy.es/_php/select_comissao1.php" with a relative path.
         * 
         * In this case, it should be "/_php/select_comissao1.php"
         */
        $.getJSON("Output.json",
            function (data) {
                var tr = data.report
                for (var i = 0; i < data.length; i++) {
                    tr = $('<tr/>');
                    tr.append("<td>" + data[i].monero + "</td>");
                    tr.append("<td>" + data[i].zcash + "</td>");
                    tr.append("<td>" + data[i].litecoin + "</td>");
                    $('.table1').append(tr);
                }
            });
    </script>

    <table class="table1">
        <tr>
            <th>Monero</th>
            <th>Zcash</th>
            <th>Litecoin</th>
        </tr>
    </table>
</body>
</html>