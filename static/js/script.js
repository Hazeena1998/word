var btnconvert = document.getElementById('btt');
var input = document.getElementById('it');
var output = document.getElementById('th');



document.getElementById('btt').addEventListener("click", function(){
    document.getElementById('th').innerHTML=numberToWords.toWords(document.getElementById('it').value);

});