// window.onload=raschitat();
// --------- Сечение и толщина столбцов  -----------
var sechTolshStolbValues = {
  "60x60": ['1.5',    '1.8', '2.0', '3.0'],
  "80x80": ['2.0', '2.5', '3.0']
}

window.onload = function() {
  var sechenie = document.getElementById("sechenieStolbcov");
  var tolshina = document.getElementById("tolshinaStolbcov");

  for (var x in sechTolshStolbValues) {
    sechenie.options[sechenie.options.length] = new Option(x, x);
  }
  sechenie.onchange = function() {
    //empty tolshina- dropdowns

    tolshina.length = 1;
    //display correct values
    var z = sechTolshStolbValues[this.value];
    for (var i = 0; i < z.length; i++) {
        tolshina.options[tolshina.options.length] = new Option(z[i], z[i]);
    }
  }
}
// --------- Сечение и толщина столбцов конец   /-----------


// Pokritiye 
// $.each({% autoescape off %}{{pokritiya_as_json}}{% endautoescape %}, function (index, item) {
//     $('#tipPokritiya').append(
//             $('<option></option>').val(item.Title).html(item.Title)
//     )
// });



// calculate the price of Solbcov 
function getStolbcovPrice() {
  var sechenieStolbcov  = document.getElementById('sechenieStolbcov').value;
  var tolshinaStolbcov  = document.getElementById('tolshinaStolbcov').value;
  
  if (sechenieStolbcov == '') {
    alert("Сечение не может быть мустым")
  }

  if (tolshinaStolbcov == '') {
    alert("Сечение не может быть мустым")
  }
  var cena = 0;
  if(sechenieStolbcov == '60x60' ) {
    switch (tolshinaStolbcov) {
      // "60x60": ['1.5м',    '1.8м', '2м', '3м'],
      case '1.5м':
        cena = 490;
        break;
      case '1.8м':
        cena = 510;
        break;   
      case '2м':
        cena = 558;
        break;
      case "3м":
        cena = 770;
        break; 
    }
  }
  else if (sechenieStolbcov == '80x80') {
    // "80x80": ['2м', '2.5м', '3м']
    switch (tolshinaStolbcov) {
      case "2м":
        cena = 846;
        break;   
      case "2.5м":
        cena = 928;
        break;   
      case "3м":
        cena = 1003;
        break; 
    }
  }

  var steps = document.getElementById('shagStolbcov').value; 
  var numOfStolbcov = dlina / steps ;
  totalPriceOfStolb = numOfStolbcov * cena;
  console.log('Cena stolb: ', cena);
  console.log('steps: ', steps);
  console.log('numOfStolbcov: ', numOfStolbcov);


  return totalPriceOfStolb;
}

function raschitat() {
    visota  = document.getElementById('visota').value;
    dlina  = document.getElementById('dlina').value;
    if(visota == ""){
        alert("Вы не указали ширину");
    } else if(dlina == ""){
        alert("Вы не указали длину");
    }
    else {
        // cena = 440;
        // console.log(cena);
        cenaStolbcov = getStolbcovPrice(); // cena stolbcov 
        ploschad = parseFloat (visota)* parseFloat (dlina);
        document.getElementById('ploschad').innerHTML = "Площадь равна:  "+ ploschad +" кв. м." + '<br>'
          "стоимость столбцов: " + cenaStolbcov;
        stoimost = ploschad + cenaStolbcov;

        document.getElementById('stoimost').innerHTML = "Стоимость равна: <br> <span class='cena'>"+ stoimost +" р.</span>";
    }

}